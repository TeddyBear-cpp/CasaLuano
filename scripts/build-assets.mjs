import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import * as esbuild from 'esbuild';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const dist = path.join(root, 'dist');
const media = JSON.parse(await fs.readFile(path.join(root, 'media-manifest.json'), 'utf8'));

await Promise.all([
  esbuild.build({
    entryPoints: [path.join(root, 'src/site.js')],
    outfile: path.join(dist, 'site.js'),
    bundle: true,
    minify: true,
    format: 'iife',
    platform: 'browser',
    target: ['chrome100', 'firefox100', 'safari15'],
    legalComments: 'eof',
  }),
  esbuild.build({
    entryPoints: [path.join(root, 'src/styles.css')],
    outfile: path.join(dist, 'styles.css'),
    bundle: true,
    minify: true,
    target: ['chrome100', 'firefox100', 'safari15'],
    legalComments: 'eof',
  }),
]);

for (const name of (await fs.readdir(dist)).filter(name => name.endsWith('.html'))) {
  const file = path.join(dist, name);
  let html = await fs.readFile(file, 'utf8');
  html = html.replace(/assets\/([a-z0-9-]+)\.jpg/gi, (match, stem) =>
    media[`${stem}.webp`] ? `assets/${stem}.webp` : match);
  html = html.replace(/<img\b[^>]*>/g, tag => {
    if (/\bwidth=|\bheight=/.test(tag)) return tag;
    const asset = tag.match(/\bsrc="assets\/([^"]+)"/)?.[1];
    if (!asset) return tag;
    const size = media[asset];
    if (!size) throw new Error(`Missing dimensions for ${asset} in ${name}`);
    return tag.replace(/>$/, ` width="${size.width}" height="${size.height}">`);
  });
  await fs.writeFile(file, html);
}

console.log('Bundled Lenis and site assets; updated responsive media markup.');
