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

  var de = doc.lang === "de";

  // Headings decode through letters from other scripts before settling into place.
  var POOL = "ÄßéøñçΩλЖБДあ中한عص日語ふअ";
  function decode(el) {
    if (!el || el.dataset.decoded || el.children.length) return;
    var final = el.textContent;
    if (!final.trim() || final.length > 90) return;
    el.dataset.decoded = "1";
    var len = final.length, start = 0, dur = 650 + len * 14, frame = 0;
    el.setAttribute("aria-label", final);
    el.style.height = el.offsetHeight + "px";
    el.classList.add("decoding");
    function step(ts) {
      if (!start) start = ts;
      var p = (ts - start) / dur;
      if (frame++ % 2 === 0) {
        var out = "";
        for (var i = 0; i < len; i++) {
          var c = final[i];
          out += c === " " || p >= (i / len) * 0.7 + 0.3 ? c : POOL[(Math.random() * POOL.length) | 0];
        }
        el.textContent = out;
      }
      if (p < 1) requestAnimationFrame(step);
      else { el.textContent = final; el.removeAttribute("aria-label"); el.style.height = ""; el.classList.remove("decoding"); }
    }
    requestAnimationFrame(step);
  }
  setTimeout(function () { decode(document.querySelector(".hero h1, .intro h1")); }, 250);
  var hio = new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { decode(e.target); hio.unobserve(e.target); } });
  }, { rootMargin: "0px 0px -15% 0px" });
  [].slice.call(document.querySelectorAll("main h2")).forEach(function (h) { hio.observe(h); });

  // The greetings marquee speeds up and leans with scroll speed.
  var marq = [].slice.call(document.querySelectorAll(".marquee"));
  if (marq.length && document.getAnimations) {
    var lastY = window.scrollY, vel = 0, ticking = false;
    function tick() {
      var y = window.scrollY, d = y - lastY; lastY = y;
      vel += (d - vel) * 0.2;
      marq.forEach(function (m) {
        var anim = m.firstElementChild.getAnimations()[0];
        if (anim) anim.playbackRate = 1 + Math.min(8, Math.abs(vel) / 6);
        m.style.transform = "skewX(" + Math.max(-12, Math.min(12, -vel * 0.25)).toFixed(2) + "deg)";
      });
      if (Math.abs(vel) > 0.05) requestAnimationFrame(tick); else ticking = false;
    }
    window.addEventListener("scroll", function () { if (!ticking) { ticking = true; requestAnimationFrame(tick); } }, { passive: true });
  }

  if (window.matchMedia("(pointer: fine)").matches) {
    // Cursor ring that grows over links and says "View" over cards.
    var ring = document.createElement("div"), dot = document.createElement("div"), label = document.createElement("span");
    ring.className = "cursor hide"; dot.className = "cursor-dot hide"; ring.appendChild(label);
    ring.setAttribute("aria-hidden", "true"); dot.setAttribute("aria-hidden", "true");
    document.body.appendChild(ring); document.body.appendChild(dot);
    var tx = -100, ty = -100, rx = -100, ry = -100, moving = false;
    window.addEventListener("pointermove", function (e) {
      tx = e.clientX; ty = e.clientY;
      dot.style.transform = "translate(" + tx + "px," + ty + "px) translate(-50%,-50%)";
      ring.classList.remove("hide"); dot.classList.remove("hide");
      if (!moving) { moving = true; requestAnimationFrame(follow); }
    }, { passive: true });
    document.addEventListener("pointerleave", function () { ring.classList.add("hide"); dot.classList.add("hide"); });
    function follow() {
      rx += (tx - rx) * 0.18; ry += (ty - ry) * 0.18;
      ring.style.transform = "translate(" + rx.toFixed(1) + "px," + ry.toFixed(1) + "px) translate(-50%,-50%)";
      if (Math.abs(tx - rx) + Math.abs(ty - ry) > 0.3) requestAnimationFrame(follow); else moving = false;
    }
    document.addEventListener("pointerover", function (e) {
      var t = e.target;
      var view = t.closest && t.closest(".img-cards a, .team, video, .link-cards a, .mega-preview");
      var link = t.closest && t.closest("a, button, summary, input, select, textarea, label");
      ring.classList.toggle("is-view", !!view);
      ring.classList.toggle("is-link", !view && !!link);
      label.textContent = view ? (view.tagName === "VIDEO" ? (de ? "Play" : "Play") : (de ? "Ansehen" : "View")) : "";
    });

    // Buttons lean toward the pointer.
    [].slice.call(document.querySelectorAll(".magnetic, .nav-actions .btn")).forEach(function (btn) {
      btn.addEventListener("pointermove", function (e) {
        var r = btn.getBoundingClientRect();
        var x = e.clientX - (r.left + r.width / 2), y = e.clientY - (r.top + r.height / 2);
        btn.style.transform = "translate(" + (x * 0.28).toFixed(1) + "px," + (y * 0.4).toFixed(1) + "px)";
      });
      btn.addEventListener("pointerleave", function () { btn.style.transform = ""; });
    });

    // Team panels light up where the pointer is.
    [].slice.call(document.querySelectorAll(".team")).forEach(function (t) {
      t.addEventListener("pointermove", function (e) {
        var r = t.getBoundingClientRect();
        t.style.setProperty("--gx", ((e.clientX - r.left) / r.width * 100).toFixed(1) + "%");
        t.style.setProperty("--gy", ((e.clientY - r.top) / r.height * 100).toFixed(1) + "%");
      });
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
