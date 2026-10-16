const { chromium } = require('playwright-core');
const out = process.argv[2];
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell', args: ['--no-sandbox', '--enable-unsafe-swiftshader'] });
  const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
  p.on('pageerror', e => console.log('ERR', e.message));
  await p.goto('http://localhost:8765/_src/media/reel.html?snap=hero&manual&dust&w=1280&h=720&t=0');
  await p.waitForFunction(() => window.__ready, null, { timeout: 30000 });
  const seq = ['hero', 'windows', 'globe', 'seal', 'film', 'helix', 'gears', 'network', 'cubes', 'plane', 'hero'];
  const fps = 30, per = 1.6; let f = 0;
  for (let k = 0; k < seq.length; k++) {
    if (k > 0) await p.evaluate(s => window.__stage.show(s), seq[k]);
    const frames = Math.round(per * fps) * (k === seq.length - 1 ? 0.5 : 1);
    for (let i = 0; i < frames; i++) {
      await p.evaluate(() => window.__stage.step(1 / 30));
      await p.screenshot({ path: `${out}/f${String(f++).padStart(4, '0')}.png` });
    }
  }
  console.log('frames', f);
  await b.close();
})();
