import { defineConfig } from 'vitest/config';

// Hand-maintained -- see .openapi-generator-ignore. The generator emits no test
// config of its own.
export default defineConfig({
  test: {
    environment: 'node',
    include: ['test/**/*.test.ts'],
  },
});
