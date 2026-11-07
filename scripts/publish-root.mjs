import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const dist = path.join(root, 'dist');
const files = (await fs.readdir(dist)).filter(name =>
  name.endsWith('.html') || name === 'styles.css' || name === 'site.js' || name === 'favicon.svg');

for (const name of files) {
  await fs.copyFile(path.join(dist, name), path.join(root, name));
}
await fs.cp(path.join(dist, 'assets'), path.join(root, 'assets'), { recursive: true });
await fs.writeFile(path.join(root, '.nojekyll'), '');

console.log('Copied generated site to the GitHub Pages repository root.');
