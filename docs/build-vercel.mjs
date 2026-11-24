import { cp, lstat, mkdir, readdir, rm } from 'node:fs/promises';
import { extname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const source = fileURLToPath(new URL('.', import.meta.url));
const output = join(source, 'dist');
const assetTypes = new Set(['.css', '.js', '.csv', '.jpg', '.jpeg', '.png', '.webp']);

await rm(output, { recursive: true, force: true });
await mkdir(output);

for (const entry of await readdir(source, { withFileTypes: true })) {
  if (entry.isFile() && extname(entry.name) === '.html') {
    await cp(join(source, entry.name), join(output, entry.name));
  }
  if (entry.isDirectory() && ['assets', 'data', 'img'].includes(entry.name)) {
    await cp(join(source, entry.name), join(output, entry.name), {
      recursive: true,
      filter: async path => {
        const stat = await lstat(path);
        return stat.isDirectory() || (stat.isFile() && assetTypes.has(extname(path).toLowerCase()));
      },
    });
  }
}
