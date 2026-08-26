# MIG-2317 — Fix sync workflow push failing on a stale sync branch

[Linear ticket](https://linear.app/ddx/issue/MIG-2317/fix-sync-workflow-push-failing-on-a-stale-sync-branch)

## Background

The hourly spec sync has failed on every run since at least 2026-08-13 13:47. `sync-spec.yml` names its branch after the upstream spec commit (`sync/mercury-18d7d69`) and pushes with `--force-with-lease`. That branch is still on origin, orphaned by closed PRs #7, #8, #11, and #12. The workflow's checkout never fetches it, so git has no remote-tracking ref to compare against and the lease fails safe:

```
! [rejected] sync/mercury-18d7d69 -> sync/mercury-18d7d69 (stale info)
```

Nothing can be synced until this is fixed, so it blocks the rest of Milestone 5.

## Implementation Steps

- [x] Fetch the sync branch explicitly before pushing, so a remote-tracking ref exists.
- [x] Name the expected value on the push rather than using the bare `--force-with-lease`.
- [x] Correct the comment at `sync-spec.yml:234-237`, which claims a pre-existing branch is "handled by the `--force-with-lease` push later". That assumption is what hid this bug.
- [ ] Verify with a manual `workflow_dispatch` run: it should succeed and open a sync PR.
- [ ] Confirm the next scheduled run also succeeds.
- [ ] Optional cleanup: delete the orphaned `sync/mercury-18d7d69` branch from origin. No longer required, since the fix overwrites it.

## Notes

### The fix

```bash
git fetch --depth=1 origin \
  "+refs/heads/$BRANCH:refs/remotes/origin/$BRANCH" || true

expected=$(git rev-parse --verify -q "refs/remotes/origin/$BRANCH" || true)

git push --force-with-lease="$BRANCH:$expected" origin "$BRANCH"
```

### Why the obvious fix doesn't work

Adding a fetch alone is not enough. Reproducing the workflow's conditions in a shallow clone shows the push still rejected as "stale info" even with a correct remote-tracking ref present, at full depth as well as shallow.

Two separate things defeat the bare `--force-with-lease`:

1. `actions/checkout` narrows `remote.origin.fetch` to the single branch it checks out, so a bare `git fetch origin "$BRANCH"` writes no tracking ref at all. The refspec has to be spelled out.
2. `git checkout -B "$BRANCH"` leaves the branch with no upstream configured, so even once the tracking ref exists, git has nothing to resolve the implicit lease against.

Naming the expected value sidesteps both. An empty `$expected` is not a degenerate case: `--force-with-lease=<ref>:` leases on the branch not existing, which is the correct guarantee for the first sync of a given spec commit.

### Verification performed

Both paths dry-run against the real remote from a clone matching the workflow's checkout, with no writes:

- Existing stale branch `sync/mercury-18d7d69` → `af69c78...c238262 (forced update)`
- Fresh branch name → `* [new branch]`

The pre-fix behaviour reproduced exactly: `! [rejected] ... (stale info)`.

### Follow-up worth considering

Sync branches accumulate whenever a PR is closed rather than merged. A workflow deleting `sync/*` branches on PR close would stop the collision arising at all. Out of scope here.

### Do not let MIG-2312 mask this

That ticket adds `info.contact` to `mercury.json` upstream, which changes the spec commit SHA, which changes the sync branch name. A fresh name has no orphaned counterpart, so the sync would start passing on its own with the bug still present.

**Do not let MIG-2312 mask this.** That ticket adds `info.contact` to `mercury.json` upstream, which changes the spec commit SHA, which changes the sync branch name. A fresh branch name has no stale remote counterpart, so the sync would start passing on its own. The bug would still be there, waiting for the next sync PR that gets closed without its branch deleted.

Worth considering as a follow-up rather than here: sync branches accumulate whenever a PR is closed rather than merged. A cleanup workflow that deletes `sync/*` branches on PR close would stop the collision arising at all. Out of scope for this fix.
