const { chromium } = require('playwright-core');
const out = process.argv[2];
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell', args: ['--no-sandbox', '--enable-unsafe-swiftshader'] });
  const p = await b.newPage({ viewport: { width: 900, height: 675 } });
  p.on('pageerror', e => console.log('ERR', e.message));
  const scenes = (process.argv[3]||'').split(',');
  for (const s of scenes) {
    await p.goto(`http://localhost:8765/_src/media/snap.html?snap=${s}&manual&w=900&h=675&t=2.2`);
    await p.waitForFunction(() => window.__ready, null, { timeout: 30000 });
    await p.evaluate(() => { for (let i = 0; i < 40; i++) window.__stage.step(1 / 30); });
    await p.locator('#stage').screenshot({ path: `${out}/${s}.png`, omitBackground: true });
    process.stdout.write(s + ' ');
  }
  await b.close();
})();
