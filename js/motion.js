// Page motion: section reveals, card tilt, videos that play only while visible,
// and the 3D backdrop (scene.js), which loads after the page is ready.
// Visitors who ask for reduced motion get a still page with the images instead.
(function () {
  var doc = document.documentElement;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var saveData = navigator.connection && navigator.connection.saveData;
  var base = document.currentScript ? document.currentScript.src : "/js/motion.js";

  // Videos: play while on screen, pause when scrolled away. Never autoplay for reduced motion.
  var vids = [].slice.call(document.querySelectorAll("video[data-autoplay]"));
  if (!reduce && "IntersectionObserver" in window) {
    var vio = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        var v = e.target;
        if (e.isIntersecting) { var p = v.play(); if (p && p.catch) p.catch(function () {}); } else v.pause();
      });
    }, { threshold: 0.25 });
    vids.forEach(function (v) { v.muted = true; vio.observe(v); });
  }

  if (reduce || !("IntersectionObserver" in window)) return;

  // Sections fold up into place in 3D as they enter the screen.
  doc.classList.add("motion");
  var targets = [].slice.call(document.querySelectorAll("main.page > section, main.page > header, main.page > article, footer .foot"));
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
  }, { rootMargin: "0px 0px -10% 0px" });
  targets.forEach(function (el) {
    [].slice.call(el.querySelectorAll(".link-cards > li, .steps > li, .stack > details, .lang-wall > li, .creds > li, .ticks > li"))
      .forEach(function (c, i) { c.style.setProperty("--n", Math.min(i, 24)); });
    if (el.getBoundingClientRect().top < window.innerHeight * 0.9) el.classList.add("in");
    else { el.classList.add("rv"); io.observe(el); }
  });

  // Cards lean toward the pointer.
  if (window.matchMedia("(pointer: fine)").matches) {
    [].slice.call(document.querySelectorAll(".link-cards .card, .steps > li, .creds > li, .plain-cards .card")).forEach(function (card) {
      card.classList.add("tilt");
      card.addEventListener("pointermove", function (e) {
        var r = card.getBoundingClientRect(), x = (e.clientX - r.left) / r.width, y = (e.clientY - r.top) / r.height;
        card.style.transform = "perspective(700px) rotateX(" + ((0.5 - y) * 12).toFixed(2) + "deg) rotateY(" + ((x - 0.5) * 14).toFixed(2) + "deg) translateZ(12px)";
        card.style.setProperty("--gx", (x * 100).toFixed(1) + "%");
        card.style.setProperty("--gy", (y * 100).toFixed(1) + "%");
      });
      card.addEventListener("pointerleave", function () { card.style.transform = ""; });
    });
  }

  // 3D backdrop, after everything else has loaded.
  if (saveData) return;
  function start() {
    import(new URL("scene.js", base).href).then(function () { doc.classList.add("has3d"); }).catch(function () {});
  }
  function idle() { (window.requestIdleCallback || function (f) { setTimeout(f, 200); })(start, { timeout: 1500 }); }
  if (document.readyState === "complete") idle(); else window.addEventListener("load", idle);
})();
