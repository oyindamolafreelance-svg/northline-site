# Making the scene images and videos

These scripts render the 3D scenes in `js/scene.js` to still images and video.
They need Node with `playwright-core`, a Chromium headless shell, ffmpeg and Python with Pillow.

1. From the repo root, serve the site: `python3 -m http.server 8765`
2. Stills: `node _src/media/snap.js OUTDIR hero,windows,globe` writes one transparent PNG per scene.
   Convert them to `img/scenes/<scene>.webp`.
3. Showreel: `node _src/media/reel.js OUTDIR` writes numbered frames. Encode with
   `ffmpeg -framerate 30 -i OUTDIR/f%04d.png -c:v libx264 -crf 26 -pix_fmt yuv420p -movflags +faststart media/showreel.mp4`
4. Localisation video: `node _src/media/loc.js OUTDIR` writes one frame per language, joined with ffmpeg `xfade`.
5. Work page screenshots: `node _src/media/work.js OUTDIR`.

Set the browser path in each script (`executablePath`) to wherever Chromium is installed.
For the Japanese, Korean, Chinese and Arabic letters to render, the machine needs Noto fonts for those scripts.
