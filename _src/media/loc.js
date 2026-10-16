const { chromium } = require('playwright-core');
const out = process.argv[2];
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell', args: ['--no-sandbox'] });
  const p = await b.newPage({ viewport: { width: 1100, height: 900 }, deviceScaleFactor: 1, reducedMotion: 'reduce' });
  await p.goto('http://localhost:8765/demo/', { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const el = p.locator('.demo');
  await el.scrollIntoViewIfNeeded();
  const bb = await el.boundingBox();
  const clip = { x: Math.max(0, bb.x - 24), y: bb.y - 24, width: Math.round((bb.width + 48) / 2) * 2, height: Math.round((bb.height + 48) / 2) * 2 };
  for (const k of ['en', 'de', 'ja', 'ar']) {
    await p.click(`button[data-k=${k}]`);
    await p.waitForTimeout(150);
    await p.screenshot({ path: `${out}/${k}.png`, clip });
  }
  console.log(clip);
  await b.close();
})();
