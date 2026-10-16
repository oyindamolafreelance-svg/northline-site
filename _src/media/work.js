const { chromium } = require('playwright-core');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell', args: ['--no-sandbox', '--enable-unsafe-swiftshader'] });
  const errs = [];
  const d = await b.newPage({ viewport: { width: 1280, height: 800 } });
  d.on('pageerror', e => errs.push(e.message)); d.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  await d.goto('http://localhost:8765/', { waitUntil: 'networkidle' });
  await d.waitForFunction(() => document.documentElement.classList.contains('has3d'), null, { timeout: 30000 });
  await d.waitForTimeout(2500);
  await d.screenshot({ path: process.argv[2] + '/site-desktop.png' });
  const m = await b.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 1 });
  m.on('pageerror', e => errs.push(e.message));
  await m.goto('http://localhost:8765/de/', { waitUntil: 'networkidle' });
  await m.waitForFunction(() => document.documentElement.classList.contains('has3d'), null, { timeout: 30000 });
  await m.waitForTimeout(2500);
  await m.screenshot({ path: process.argv[2] + '/site-phone-de.png' });
  console.log('errors:', errs.length ? errs : 'none');
  await b.close();
})();
