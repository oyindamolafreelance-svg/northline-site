// 3D backdrop for kayonnecreatives.com.
// One fixed WebGL canvas sits behind the page. Every element with data-scene="key"
// switches the 3D object when it reaches the middle of the screen. Loaded by motion.js
// after the page has finished loading, and never when the visitor prefers reduced motion.
import * as THREE from "./three.module.min.js";
import { RoomEnvironment } from "./RoomEnvironment.js";

const TAU = Math.PI * 2;
const params = new URLSearchParams(location.search);
const SNAP = params.get("snap");          // render one scene alone (used to make stills and video)
const MANUAL = params.has("manual");      // time is advanced by window.__stage.step()
const DUST = !SNAP || params.has("dust");  // background particles
const small = matchMedia("(max-width: 899px)").matches;

const canvas = document.createElement("canvas");
canvas.id = "stage";
canvas.setAttribute("aria-hidden", "true");
document.body.prepend(canvas);

let renderer;
try {
  renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true, preserveDrawingBuffer: !!SNAP, powerPreference: "high-performance" });
} catch (e) {
  canvas.remove();
  throw e;
}
renderer.setPixelRatio(SNAP ? 1 : Math.min(devicePixelRatio, small ? 1.5 : 2));
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.05;

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(40, 1, 0.1, 120);
camera.position.set(0, 0, 9);

const pmrem = new THREE.PMREMGenerator(renderer);
scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;

scene.add(new THREE.AmbientLight(0xffffff, 0.25));
const key = new THREE.DirectionalLight(0xffd8b8, 2.2);
key.position.set(4, 5, 6);
scene.add(key);
const warm = new THREE.PointLight(0xe4b07a, 40, 30);
const cool = new THREE.PointLight(0x5cc4b8, 30, 30);
scene.add(warm, cool);

// ---------- shared materials and helpers ----------
const M = {
  copper: new THREE.MeshStandardMaterial({ color: 0xc27a48, metalness: 1, roughness: 0.24 }),
  gold: new THREE.MeshStandardMaterial({ color: 0xe8b47c, metalness: 1, roughness: 0.16 }),
  dark: new THREE.MeshStandardMaterial({ color: 0x1d222b, metalness: 0.5, roughness: 0.35 }),
  teal: new THREE.MeshStandardMaterial({ color: 0x5cc4b8, metalness: 0.5, roughness: 0.25, emissive: 0x0b3a35 }),
  paper: new THREE.MeshStandardMaterial({ color: 0xf3ece0, metalness: 0, roughness: 0.6 }),
  glass: new THREE.MeshPhysicalMaterial({ color: 0xa8ddd5, metalness: 0, roughness: 0.05, transparent: true, opacity: 0.32, clearcoat: 1 }),
  wire: new THREE.MeshBasicMaterial({ color: 0xa8582a, wireframe: true, transparent: true, opacity: 0.35 }),
  glow: new THREE.MeshBasicMaterial({ color: 0xd9894e }),
  tealGlow: new THREE.MeshBasicMaterial({ color: 0x1f9e90 }),
  line: new THREE.LineBasicMaterial({ color: 0xa8582a, transparent: true, opacity: 0.55 }),
};

function rng(seed) {
  return () => {
    seed |= 0; seed = (seed + 0x6d2b79f5) | 0;
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function tex(w, h, draw) {
  const c = document.createElement("canvas");
  c.width = w; c.height = h;
  draw(c.getContext("2d"), w, h);
  const t = new THREE.CanvasTexture(c);
  t.colorSpace = THREE.SRGBColorSpace;
  t.anisotropy = 4;
  return t;
}

const glyphCache = {};
function glyph(ch, color = "#a8582a") {
  const k = ch + color;
  if (!glyphCache[k]) {
    glyphCache[k] = new THREE.SpriteMaterial({
      map: tex(128, 128, (g) => {
        g.fillStyle = color;
        g.font = '500 92px Fraunces, "Noto Serif CJK JP", "Noto Sans Arabic", serif';
        g.textAlign = "center"; g.textBaseline = "middle";
        g.fillText(ch, 64, 70);
      }),
      transparent: true, depthWrite: false,
    });
  }
  const s = new THREE.Sprite(glyphCache[k]);
  s.scale.setScalar(0.5);
  return s;
}

const GLYPHS = Array.from("äあ中éø한ßعñ字ç日Ωж");

function uiTexture(seed, accent = "#e4b07a") {
  const r = rng(seed);
  return tex(512, 336, (g, w, h) => {
    g.fillStyle = "#151a22"; g.fillRect(0, 0, w, h);
    g.fillStyle = "#232a35"; g.fillRect(0, 0, w, 34);
    ["#e86a5c", "#e4b07a", "#5cc4b8"].forEach((c, i) => { g.fillStyle = c; g.beginPath(); g.arc(20 + i * 20, 17, 6, 0, TAU); g.fill(); });
    g.fillStyle = accent; g.fillRect(28, 62, 220, 22);
    g.fillStyle = "#3a4250";
    for (let i = 0; i < 5; i++) g.fillRect(28, 100 + i * 18, 160 + r() * 200, 8);
    g.fillStyle = "#2c6f68"; g.fillRect(300, 60, 184, 120);
    g.fillStyle = accent; g.fillRect(28, 210, 110, 34);
    for (let i = 0; i < 3; i++) { g.fillStyle = "#1f2530"; g.fillRect(28 + i * 158, 262, 146, 56); }
  });
}

function textPage(seed, title = true) {
  const r = rng(seed);
  return tex(256, 352, (g, w, h) => {
    g.fillStyle = "#f6f0e6"; g.fillRect(0, 0, w, h);
    if (title) { g.fillStyle = "#b8743f"; g.fillRect(24, 26, 120, 12); }
    g.fillStyle = "#9b958c";
    for (let y = 58; y < h - 24; y += 13) g.fillRect(24, y, (w - 48) * (0.55 + r() * 0.45), 5);
  });
}

function boxWithFace(w, h, d, faceTex, side = M.dark) {
  const face = new THREE.MeshStandardMaterial({ map: faceTex, metalness: 0.1, roughness: 0.45, emissive: 0xffffff, emissiveMap: faceTex, emissiveIntensity: 0.35 });
  return new THREE.Mesh(new THREE.BoxGeometry(w, h, d), [side, side, side, side, face, side]);
}

function fib(n, r) {
  const pts = [];
  const g = Math.PI * (3 - Math.sqrt(5));
  for (let i = 0; i < n; i++) {
    const y = 1 - (i / (n - 1)) * 2;
    const rad = Math.sqrt(1 - y * y);
    pts.push(new THREE.Vector3(Math.cos(g * i) * rad * r, y * r, Math.sin(g * i) * rad * r));
  }
  return pts;
}

// ---------- scenes ----------
// Each maker returns a Group whose userData.update(t, dt, energy) animates it.
// energy goes up when the visitor scrolls fast, so every scene reacts to scrolling.
const makers = {
  hero() {
    const g = new THREE.Group();
    const ring = new THREE.Mesh(new THREE.TorusGeometry(1.6, 0.36, 64, 200), M.copper);
    const inner = new THREE.Mesh(new THREE.TorusGeometry(1.05, 0.05, 16, 160), M.gold);
    g.add(ring, inner);
    const r = rng(1), shards = [], sprites = [];
    for (let i = 0; i < 30; i++) {
      const m = new THREE.Mesh(new THREE.OctahedronGeometry(0.07 + (i % 4) * 0.04), i % 3 ? M.copper : M.teal);
      m.userData = { r: 2.3 + (i % 5) * 0.32, a: (i / 30) * TAU, y: (r() - 0.5) * 2.4, sp: 0.15 + r() * 0.45 };
      shards.push(m); g.add(m);
    }
    GLYPHS.slice(0, 9).forEach((ch, i) => {
      const s = glyph(ch); s.userData = { a: (i / 9) * TAU, y: Math.sin(i * 2.1) * 1.3 };
      sprites.push(s); g.add(s);
    });
    g.userData.update = (t, dt, e) => {
      ring.rotation.set(1.1 + Math.sin(t * 0.5) * 0.25, Math.sin(t * 0.4) * 0.4, t * 0.4);
      inner.rotation.set(1.1, 0, -t * 0.9);
      for (const m of shards) {
        const u = m.userData, rr = u.r + e * 1.8, a = u.a + t * u.sp;
        m.position.set(Math.cos(a) * rr, u.y + Math.sin(t + u.a) * 0.25, Math.sin(a) * rr);
        m.rotation.set(t * 2 + u.a, t * 1.4, 0);
      }
      for (const s of sprites) {
        const a = s.userData.a - t * 0.25;
        s.position.set(Math.cos(a) * (2.9 + e), s.userData.y, Math.sin(a) * (2.9 + e));
      }
    };
    return g;
  },

  windows() {
    const g = new THREE.Group(), wins = [];
    for (let i = 0; i < 5; i++) {
      const w = boxWithFace(2.6, 1.7, 0.06, uiTexture(i + 3, i % 2 ? "#5cc4b8" : "#e4b07a"));
      wins.push(w); g.add(w);
    }
    g.userData.update = (t, dt, e) => {
      wins.forEach((w, i) => {
        const k = i - 2, spread = 1 + e * 1.5 + Math.sin(t * 0.8) * 0.15;
        w.position.set(k * 0.42 * spread, k * 0.3 * spread + Math.sin(t * 1.2 + i) * 0.08, -i * 0.55 * spread);
        w.rotation.set(-0.12 + Math.sin(t * 0.6 + i) * 0.05, -0.55 + Math.sin(t * 0.5) * 0.25, 0.04);
      });
    };
    return g;
  },

  cubes() {
    const n = 6, count = n * n * n;
    const mesh = new THREE.InstancedMesh(new THREE.BoxGeometry(0.26, 0.26, 0.26), M.copper, count);
    const o = new THREE.Object3D();
    const g = new THREE.Group(); g.add(mesh);
    g.userData.update = (t, dt, e) => {
      let i = 0;
      for (let x = 0; x < n; x++) for (let y = 0; y < n; y++) for (let z = 0; z < n; z++) {
        const px = (x - 2.5) * 0.42, py = (y - 2.5) * 0.42, pz = (z - 2.5) * 0.42;
        const d = Math.hypot(px, py, pz);
        const s = 0.35 + 0.75 * (0.5 + 0.5 * Math.sin(t * 2.2 - d * 2.4));
        const push = 1 + e * 0.6 + 0.08 * Math.sin(t * 2.2 - d * 2.4);
        o.position.set(px * push, py * push, pz * push);
        o.rotation.set(t + d, t * 0.7, 0);
        o.scale.setScalar(s);
        o.updateMatrix(); mesh.setMatrixAt(i++, o.matrix);
      }
      mesh.instanceMatrix.needsUpdate = true;
      g.rotation.set(0.5, t * 0.3, 0);
    };
    return g;
  },

  phone() {
    const g = new THREE.Group(), phones = [];
    for (let i = 0; i < 3; i++) {
      const p = boxWithFace(1.05, 2.1, 0.1, tex(256, 512, (c, w, h) => {
        const r = rng(i + 9);
        c.fillStyle = "#12161d"; c.fillRect(0, 0, w, h);
        c.fillStyle = i === 1 ? "#5cc4b8" : "#e4b07a"; c.fillRect(20, 40, 216, 140);
        c.fillStyle = "#2a313d";
        for (let k = 0; k < 6; k++) c.fillRect(20, 205 + k * 40, 120 + r() * 96, 22);
        c.fillStyle = "#e4b07a"; c.beginPath(); c.arc(128, 470, 22, 0, TAU); c.fill();
      }), M.copper);
      phones.push(p); g.add(p);
    }
    g.userData.update = (t, dt, e) => {
      phones.forEach((p, i) => {
        const a = (i - 1) * 0.7 + Math.sin(t * 0.5) * 0.3;
        const r = 1.6 + e;
        p.position.set(Math.sin(a) * r, Math.sin(t * 1.3 + i * 2) * 0.15, Math.cos(a) * r - 1.4);
        p.rotation.set(Math.sin(t + i) * 0.08, a, Math.sin(t * 0.7 + i) * 0.06);
      });
    };
    return g;
  },

  network() {
    const g = new THREE.Group();
    const pts = fib(22, 2);
    const nodes = pts.map((p, i) => {
      const m = new THREE.Mesh(new THREE.SphereGeometry(i % 5 ? 0.08 : 0.14, 20, 16), i % 5 ? M.gold : M.teal);
      m.position.copy(p); g.add(m); return m;
    });
    const edges = [];
    pts.forEach((p, i) => {
      pts.map((q, j) => [j, p.distanceTo(q)]).sort((a, b) => a[1] - b[1]).slice(1, 4)
        .forEach(([j]) => { if (i < j) edges.push([i, j]); });
    });
    const pos = [];
    edges.forEach(([a, b]) => pos.push(...pts[a].toArray(), ...pts[b].toArray()));
    const lg = new THREE.BufferGeometry();
    lg.setAttribute("position", new THREE.Float32BufferAttribute(pos, 3));
    g.add(new THREE.LineSegments(lg, M.line));
    const at = glyph("@", "#a8582a"); at.scale.setScalar(1.1); g.add(at);
    const pulses = [];
    for (let i = 0; i < 14; i++) {
      const m = new THREE.Mesh(new THREE.SphereGeometry(0.05, 10, 8), i % 2 ? M.glow : M.tealGlow);
      m.userData = { e: edges[(i * 7) % edges.length], o: i / 14 };
      pulses.push(m); g.add(m);
    }
    g.userData.update = (t, dt, e) => {
      g.rotation.set(0.3, t * 0.25, 0);
      for (const m of pulses) {
        const k = (t * (0.5 + e) + m.userData.o) % 1;
        m.position.lerpVectors(pts[m.userData.e[0]], pts[m.userData.e[1]], k);
      }
      nodes.forEach((n, i) => n.scale.setScalar(1 + 0.35 * Math.max(0, Math.sin(t * 3 + i))));
    };
    return g;
  },

  bars() {
    const n = 7, count = n * n;
    const mesh = new THREE.InstancedMesh(new THREE.BoxGeometry(0.3, 1, 0.3).translate(0, 0.5, 0), M.copper, count);
    const o = new THREE.Object3D();
    const g = new THREE.Group(); g.add(mesh);
    const arrow = new THREE.Mesh(new THREE.ConeGeometry(0.25, 0.5, 4), M.teal);
    g.add(arrow);
    g.userData.update = (t, dt, e) => {
      let i = 0, top = 0;
      for (let x = 0; x < n; x++) for (let z = 0; z < n; z++) {
        const h = 0.2 + (x + z) * 0.16 * (0.75 + 0.25 * Math.sin(t * 2 - x * 0.6 - z * 0.4)) * (1 + e * 0.5);
        o.position.set((x - 3) * 0.4, -1.2, (z - 3) * 0.4);
        o.scale.set(1, h, 1); o.rotation.set(0, 0, 0);
        o.updateMatrix(); mesh.setMatrixAt(i++, o.matrix);
        top = Math.max(top, h);
      }
      mesh.instanceMatrix.needsUpdate = true;
      arrow.position.set(1.2, -1.2 + top + 0.45 + Math.sin(t * 3) * 0.1, 1.2);
      arrow.rotation.y = t * 2;
      g.rotation.set(0.45, -0.7 + Math.sin(t * 0.4) * 0.3, 0);
    };
    return g;
  },

  tunnel() {
    const g = new THREE.Group(), count = 260, r = rng(4);
    const mesh = new THREE.InstancedMesh(new THREE.BoxGeometry(0.025, 0.025, 1.4), M.glow, count);
    const data = [], o = new THREE.Object3D();
    for (let i = 0; i < count; i++) data.push({ a: r() * TAU, rad: 0.6 + r() * 2.4, z: -r() * 30, s: 0.6 + r() });
    g.add(mesh);
    const gates = [];
    for (let i = 0; i < 6; i++) {
      const ring = new THREE.Mesh(new THREE.TorusGeometry(2.2, 0.04, 8, 90), i % 2 ? M.teal : M.copper);
      ring.userData.z = -i * 5; gates.push(ring); g.add(ring);
    }
    g.userData.update = (t, dt, e) => {
      const v = (8 + e * 40) * dt;
      data.forEach((d, i) => {
        d.z += v * d.s;
        if (d.z > 6) d.z -= 32;
        o.position.set(Math.cos(d.a + t * 0.2) * d.rad, Math.sin(d.a + t * 0.2) * d.rad, d.z);
        o.scale.set(1, 1, 1 + e * 3);
        o.rotation.set(0, 0, 0);
        o.updateMatrix(); mesh.setMatrixAt(i, o.matrix);
      });
      mesh.instanceMatrix.needsUpdate = true;
      for (const ring of gates) {
        ring.userData.z += v * 0.6;
        if (ring.userData.z > 6) ring.userData.z -= 30;
        ring.position.z = ring.userData.z;
        ring.rotation.z = t * 0.5;
      }
    };
    return g;
  },

  shield() {
    const g = new THREE.Group();
    const knot = new THREE.Mesh(new THREE.TorusKnotGeometry(0.95, 0.3, 220, 28, 2, 3), M.copper);
    const shell = new THREE.Mesh(new THREE.IcosahedronGeometry(2.1, 1), M.wire);
    const core = new THREE.Mesh(new THREE.SphereGeometry(0.25, 24, 16), M.tealGlow);
    g.add(knot, shell, core);
    g.userData.update = (t, dt, e) => {
      knot.rotation.set(t * 0.4, t * 0.6, 0);
      shell.rotation.set(-t * 0.2, -t * 0.3, 0);
      shell.scale.setScalar(1 + e * 0.4 + Math.sin(t * 2) * 0.03);
      core.scale.setScalar(1 + Math.sin(t * 4) * 0.25);
    };
    return g;
  },

  seal() {
    const g = new THREE.Group();
    const face = tex(512, 512, (c, w) => {
      c.fillStyle = "#c98b52"; c.fillRect(0, 0, w, w);
      const grd = c.createRadialGradient(w / 2, w / 2, 40, w / 2, w / 2, w / 2);
      grd.addColorStop(0, "#f2c58e"); grd.addColorStop(1, "#a9662f");
      c.fillStyle = grd; c.beginPath(); c.arc(w / 2, w / 2, w / 2, 0, TAU); c.fill();
      c.strokeStyle = "#7d4620"; c.lineWidth = 6;
      [230, 170].forEach((rr) => { c.beginPath(); c.arc(w / 2, w / 2, rr, 0, TAU); c.stroke(); });
      c.fillStyle = "#6b3a17"; c.font = "600 34px Outfit, Arial, sans-serif"; c.textAlign = "center";
      const text = "CERTIFIED TRANSLATION · KAYONNE CREATIVES · ";
      Array.from(text).forEach((ch, i) => {
        c.save(); c.translate(w / 2, w / 2); c.rotate((i / text.length) * TAU); c.fillText(ch, 0, -186); c.restore();
      });
      c.strokeStyle = "#6b3a17"; c.lineWidth = 22; c.lineCap = "round"; c.lineJoin = "round";
      c.beginPath(); c.moveTo(190, 262); c.lineTo(240, 312); c.lineTo(330, 210); c.stroke();
    });
    face.center.set(0.5, 0.5); face.rotation = Math.PI / 2;
    const topMat = new THREE.MeshStandardMaterial({ map: face, metalness: 0.8, roughness: 0.3 });
    const coin = new THREE.Mesh(new THREE.CylinderGeometry(1.5, 1.5, 0.22, 96), [M.gold, topMat, M.copper]);
    coin.rotation.x = Math.PI / 2;
    const holder = new THREE.Group(); holder.add(coin); g.add(holder);
    const beads = new THREE.InstancedMesh(new THREE.SphereGeometry(0.09, 12, 10), M.gold, 48);
    const o = new THREE.Object3D();
    for (let i = 0; i < 48; i++) {
      o.position.set(Math.cos((i / 48) * TAU) * 1.62, Math.sin((i / 48) * TAU) * 1.62, 0);
      o.updateMatrix(); beads.setMatrixAt(i, o.matrix);
    }
    holder.add(beads);
    const ribbons = [-0.5, 0.5].map((x) => {
      const rb = new THREE.Mesh(new THREE.BoxGeometry(0.5, 1.6, 0.04), M.teal);
      rb.position.set(x, -1.9, -0.15); rb.rotation.z = x * 0.5; holder.add(rb); return rb;
    });
    g.userData.update = (t, dt, e) => {
      holder.rotation.set(Math.sin(t * 0.7) * 0.25, Math.sin(t * 0.5) * 0.6 + e * 3, Math.sin(t * 0.3) * 0.1);
      ribbons.forEach((rb, i) => (rb.rotation.x = Math.sin(t * 2 + i) * 0.2));
    };
    return g;
  },

  sheets() {
    const g = new THREE.Group(), pages = [];
    for (let i = 0; i < 7; i++) {
      const geo = new THREE.PlaneGeometry(1.7, 2.3).translate(0.85, 0, 0);
      const mat = new THREE.MeshStandardMaterial({ map: textPage(i + 20), side: THREE.DoubleSide, roughness: 0.7 });
      const p = new THREE.Mesh(geo, mat);
      p.position.set(-0.85, 0, -i * 0.012);
      pages.push(p); g.add(p);
    }
    const spine = new THREE.Mesh(new THREE.CylinderGeometry(0.05, 0.05, 2.4, 12), M.copper);
    spine.position.x = -0.85; g.add(spine);
    g.userData.update = (t, dt, e) => {
      pages.forEach((p, i) => {
        const k = 0.5 + 0.5 * Math.sin(t * (0.9 + e) - i * 0.55);
        p.rotation.y = -k * Math.PI * 0.92;
      });
      g.rotation.set(-0.35 + Math.sin(t * 0.4) * 0.1, 0.5 + Math.sin(t * 0.3) * 0.2, 0.08);
    };
    return g;
  },

  globe() {
    const g = new THREE.Group();
    const core = new THREE.Mesh(new THREE.SphereGeometry(1.72, 48, 32), M.dark);
    const net = new THREE.Mesh(new THREE.SphereGeometry(1.8, 28, 18), M.wire);
    g.add(core, net);
    const dots = new THREE.BufferGeometry().setFromPoints(fib(420, 1.78));
    g.add(new THREE.Points(dots, new THREE.PointsMaterial({ color: 0xa8582a, size: 0.045 })));
    const pts = fib(9, 1.8), arcs = [];
    for (let i = 0; i < 8; i++) {
      const a = pts[i], b = pts[(i * 4 + 3) % 9];
      const mid = a.clone().add(b).normalize().multiplyScalar(2.9);
      const curve = new THREE.QuadraticBezierCurve3(a, mid, b);
      g.add(new THREE.Mesh(new THREE.TubeGeometry(curve, 48, 0.012, 6), i % 2 ? M.teal : M.gold));
      const bead = new THREE.Mesh(new THREE.SphereGeometry(0.06, 12, 8), i % 2 ? M.tealGlow : M.glow);
      bead.userData = { curve, o: i / 8 }; arcs.push(bead); g.add(bead);
    }
    const sprites = GLYPHS.map((ch, i) => {
      const s = glyph(ch); s.userData = { a: (i / GLYPHS.length) * TAU, tilt: Math.sin(i * 1.7) * 0.9 };
      g.add(s); return s;
    });
    g.userData.update = (t, dt, e) => {
      core.rotation.y = net.rotation.y = t * 0.15;
      g.children[2].rotation.y = t * 0.15;
      for (const b of arcs) b.position.copy(b.userData.curve.getPoint((t * 0.35 + b.userData.o) % 1));
      for (const s of sprites) {
        const a = s.userData.a + t * 0.3, r = 2.7 + e * 1.2;
        s.position.set(Math.cos(a) * r, s.userData.tilt + Math.sin(a * 2) * 0.2, Math.sin(a) * r);
      }
      g.rotation.x = 0.25;
    };
    return g;
  },

  dice() {
    const g = new THREE.Group();
    const geos = [new THREE.IcosahedronGeometry(0.75), new THREE.BoxGeometry(0.9, 0.9, 0.9), new THREE.DodecahedronGeometry(0.65), new THREE.OctahedronGeometry(0.7), new THREE.TetrahedronGeometry(0.8)];
    const mats = [M.copper, M.teal, M.gold, M.copper, M.teal];
    const dice = geos.map((geo, i) => {
      const m = new THREE.Mesh(geo, mats[i]); m.userData.a = (i / geos.length) * TAU; g.add(m); return m;
    });
    const floor = new THREE.Mesh(new THREE.RingGeometry(1.8, 1.85, 80), M.glow);
    floor.rotation.x = -Math.PI / 2; floor.position.y = -1.3; g.add(floor);
    g.userData.update = (t, dt, e) => {
      dice.forEach((d, i) => {
        const a = d.userData.a + t * 0.4;
        d.position.set(Math.cos(a) * 1.8, -0.9 + Math.abs(Math.sin(t * 2.2 + i * 1.3)) * (1.6 + e * 2), Math.sin(a) * 1.8);
        d.rotation.set(t * (1 + i * 0.2), t * 1.3, t * 0.4 * i);
      });
      g.rotation.x = 0.25;
    };
    return g;
  },

  helix() {
    const g = new THREE.Group(), n = 34, sph = new THREE.SphereGeometry(0.11, 16, 12);
    for (let i = 0; i < n; i++) {
      const y = (i - n / 2) * 0.15, a = i * 0.42;
      const p1 = new THREE.Vector3(Math.cos(a) * 1, y, Math.sin(a) * 1);
      const p2 = new THREE.Vector3(Math.cos(a + Math.PI) * 1, y, Math.sin(a + Math.PI) * 1);
      const s1 = new THREE.Mesh(sph, M.copper); s1.position.copy(p1);
      const s2 = new THREE.Mesh(sph, M.teal); s2.position.copy(p2);
      const rung = new THREE.Mesh(new THREE.CylinderGeometry(0.025, 0.025, 2, 6), i % 2 ? M.gold : M.glass);
      rung.position.set(0, y, 0); rung.rotation.set(0, -a, Math.PI / 2);
      g.add(s1, s2, rung);
    }
    g.userData.update = (t, dt, e) => {
      g.rotation.set(0.35, t * (0.6 + e * 3), 0.25);
      g.scale.y = 1 + Math.sin(t * 1.5) * 0.05;
    };
    return g;
  },

  gears() {
    function gear(R, teeth, depth) {
      const s = new THREE.Shape(), steps = teeth * 4, r = R - depth;
      for (let i = 0; i <= steps; i++) {
        const a = (i / steps) * TAU, rr = i % 4 < 2 ? R : r;
        i ? s.lineTo(Math.cos(a) * rr, Math.sin(a) * rr) : s.moveTo(Math.cos(a) * rr, Math.sin(a) * rr);
      }
      const hole = new THREE.Path(); hole.absarc(0, 0, R * 0.32, 0, TAU, true); s.holes.push(hole);
      return new THREE.ExtrudeGeometry(s, { depth: 0.28, bevelEnabled: true, bevelThickness: 0.04, bevelSize: 0.03, bevelSegments: 2, curveSegments: 6 }).center();
    }
    const g = new THREE.Group();
    const a = new THREE.Mesh(gear(1.25, 16, 0.18), M.copper);
    const b = new THREE.Mesh(gear(0.8, 10, 0.18), M.gold);
    const c = new THREE.Mesh(gear(0.55, 7, 0.16), M.teal);
    a.position.set(-0.7, 0.2, 0); b.position.set(1.22, 0.55, 0); c.position.set(0.55, -1.1, 0.05);
    g.add(a, b, c);
    g.userData.update = (t, dt, e) => {
      const w = t * (0.6 + e * 4);
      a.rotation.z = w; b.rotation.z = -w * 1.6 + 0.16; c.rotation.z = -w * 2.29;
      g.rotation.set(-0.35 + Math.sin(t * 0.5) * 0.15, -0.45 + Math.sin(t * 0.35) * 0.25, 0);
    };
    return g;
  },

  scales() {
    const g = new THREE.Group();
    const post = new THREE.Mesh(new THREE.CylinderGeometry(0.07, 0.1, 2.6, 24), M.copper); post.position.y = -0.2;
    const base = new THREE.Mesh(new THREE.CylinderGeometry(0.8, 0.95, 0.15, 48), M.dark); base.position.y = -1.5;
    const pivot = new THREE.Group(); pivot.position.y = 1.1;
    const beam = new THREE.Mesh(new THREE.BoxGeometry(3.2, 0.08, 0.08), M.gold); pivot.add(beam);
    const top = new THREE.Mesh(new THREE.SphereGeometry(0.14, 20, 14), M.gold); top.position.y = 1.15;
    g.add(post, base, pivot, top);
    const pans = [-1.5, 1.5].map((x) => {
      const pan = new THREE.Group();
      const dish = new THREE.Mesh(new THREE.SphereGeometry(0.55, 32, 12, 0, TAU, Math.PI * 0.6, Math.PI * 0.4), M.copper);
      dish.position.y = -0.4 + 0.55; dish.scale.y = 0.6;
      const pts = [];
      for (let k = 0; k < 3; k++) { const a = (k / 3) * TAU; pts.push(0, 0, 0, Math.cos(a) * 0.45, -0.95, Math.sin(a) * 0.45); }
      const lg = new THREE.BufferGeometry(); lg.setAttribute("position", new THREE.Float32BufferAttribute(pts, 3));
      pan.add(new THREE.LineSegments(lg, M.line));
      const d = new THREE.Group(); d.add(dish); d.position.y = -1.05; pan.add(d);
      pan.userData.x = x; g.add(pan); return pan;
    });
    g.userData.update = (t, dt, e) => {
      const tilt = Math.sin(t * 1.1) * 0.22 + Math.sin(t * 7) * e * 0.2;
      pivot.rotation.z = tilt;
      pans.forEach((p) => { const x = p.userData.x; p.position.set(Math.cos(tilt) * x, 1.1 + Math.sin(tilt) * x, 0); });
      g.rotation.y = Math.sin(t * 0.4) * 0.5;
    };
    return g;
  },

  film() {
    const g = new THREE.Group(), frames = [], n = 12;
    const lines = ["Hello", "Hallo", "こんにちは", "Bonjour", "Hola", "你好", "Ciao", "안녕하세요", "Olá", "Hej", "Merhaba", "مرحبا"];
    for (let i = 0; i < n; i++) {
      const tx = tex(320, 240, (c, w, h) => {
        c.fillStyle = "#0d0f13"; c.fillRect(0, 0, w, h);
        for (let k = 0; k < 8; k++) { c.fillStyle = "#e9dfcf"; c.fillRect(10 + k * 40, 6, 20, 14); c.fillRect(10 + k * 40, h - 20, 20, 14); }
        const grd = c.createLinearGradient(0, 30, w, h - 30);
        grd.addColorStop(0, i % 2 ? "#1f5f58" : "#6d3f1f"); grd.addColorStop(1, "#151a22");
        c.fillStyle = grd; c.fillRect(14, 30, w - 28, h - 60);
        c.fillStyle = "#ffffff"; c.font = '600 30px Outfit, "Noto Sans CJK JP", "Noto Sans Arabic", sans-serif'; c.textAlign = "center";
        c.fillStyle = "rgba(0,0,0,.55)"; c.fillRect(60, h - 82, w - 120, 40);
        c.fillStyle = "#fff6e6"; c.fillText(lines[i], w / 2, h - 52);
      });
      const f = new THREE.Mesh(new THREE.PlaneGeometry(1.3, 0.98), new THREE.MeshBasicMaterial({ map: tx, side: THREE.DoubleSide }));
      f.userData.a = (i / n) * TAU; frames.push(f); g.add(f);
    }
    const reel = new THREE.Mesh(new THREE.TorusGeometry(0.6, 0.12, 16, 60), M.copper); g.add(reel);
    g.userData.update = (t, dt, e) => {
      frames.forEach((f) => {
        const a = f.userData.a + t * (0.3 + e * 2);
        f.position.set(Math.sin(a) * 2.3, Math.sin(a * 2 + t) * 0.15, Math.cos(a) * 2.3);
        f.rotation.y = a;
      });
      reel.rotation.set(Math.PI / 2, 0, t * 2);
      g.rotation.x = 0.18;
    };
    return g;
  },

  lens() {
    const g = new THREE.Group();
    const sheet = new THREE.Mesh(new THREE.PlaneGeometry(2.6, 3.4), new THREE.MeshStandardMaterial({ map: textPage(77), roughness: 0.7 }));
    sheet.rotation.set(-0.55, 0.25, 0.05); sheet.position.z = -0.6; g.add(sheet);
    const lens = new THREE.Group();
    const rim = new THREE.Mesh(new THREE.TorusGeometry(0.62, 0.08, 20, 80), M.gold);
    const glassD = new THREE.Mesh(new THREE.CylinderGeometry(0.6, 0.6, 0.04, 64), M.glass); glassD.rotation.x = Math.PI / 2;
    const handle = new THREE.Mesh(new THREE.CylinderGeometry(0.08, 0.1, 1.3, 20), M.copper);
    handle.position.set(0.75, -0.75, 0); handle.rotation.z = Math.PI / 4;
    const mark = new THREE.Mesh(new THREE.TorusGeometry(0.22, 0.035, 10, 40, Math.PI * 1.6), M.tealGlow);
    lens.add(rim, glassD, handle);
    g.add(lens, mark);
    g.userData.update = (t, dt, e) => {
      const s = t * (0.7 + e * 2);
      lens.position.set(Math.sin(s) * 0.9, Math.sin(s * 2) * 0.6, 0.4);
      lens.rotation.set(-0.3, 0.25, Math.sin(s) * 0.2);
      mark.position.set(Math.sin(s - 0.4) * 0.9, Math.sin((s - 0.4) * 2) * 0.6, -0.2);
      mark.rotation.z = t * 3;
    };
    return g;
  },

  check() {
    const g = new THREE.Group();
    const rings = [1.9, 1.55, 1.2].map((r, i) => {
      const m = new THREE.Mesh(new THREE.TorusGeometry(r, 0.05, 12, 120), [M.copper, M.gold, M.teal][i]); g.add(m); return m;
    });
    const path = new THREE.CatmullRomCurve3([new THREE.Vector3(-0.55, 0.05, 0), new THREE.Vector3(-0.15, -0.4, 0), new THREE.Vector3(0.65, 0.5, 0)], false, "catmullrom", 0.1);
    const tick = new THREE.Mesh(new THREE.TubeGeometry(path, 40, 0.11, 16), M.teal);
    g.add(tick);
    g.userData.update = (t, dt, e) => {
      rings[0].rotation.set(t * 0.7, t * 0.3, 0);
      rings[1].rotation.set(-t * 0.5, 0, t * 0.6);
      rings[2].rotation.set(0, t * 0.9 + e * 4, t * 0.2);
      tick.rotation.y = Math.sin(t * 0.8) * 0.5;
      tick.scale.setScalar(1 + Math.sin(t * 3) * 0.06);
    };
    return g;
  },

  path() {
    const g = new THREE.Group();
    const track = new THREE.Mesh(new THREE.TorusGeometry(2.1, 0.02, 8, 160), M.glow);
    const tilt = new THREE.Group(); tilt.rotation.x = 1.15; tilt.add(track); g.add(tilt);
    const nodes = [0, 1, 2, 3].map((i) => {
      const n = new THREE.Mesh(new THREE.IcosahedronGeometry(0.28, 1), i % 2 ? M.teal : M.copper);
      const a = (i / 4) * TAU; n.position.set(Math.cos(a) * 2.1, Math.sin(a) * 2.1, 0); n.userData.a = a;
      tilt.add(n); return n;
    });
    const runner = new THREE.Mesh(new THREE.SphereGeometry(0.11, 16, 12), M.glow); tilt.add(runner);
    const trail = [];
    for (let i = 0; i < 16; i++) { const m = new THREE.Mesh(new THREE.SphereGeometry(0.07 * (1 - i / 16), 8, 6), M.glow); trail.push(m); tilt.add(m); }
    g.userData.update = (t, dt, e) => {
      const a = (t * (0.9 + e * 3)) % TAU;
      runner.position.set(Math.cos(a) * 2.1, Math.sin(a) * 2.1, 0);
      trail.forEach((m, i) => { const b = a - (i + 1) * 0.06; m.position.set(Math.cos(b) * 2.1, Math.sin(b) * 2.1, 0); });
      nodes.forEach((n) => {
        const d = Math.abs(Math.atan2(Math.sin(a - n.userData.a), Math.cos(a - n.userData.a)));
        n.scale.setScalar(1 + Math.max(0, 1 - d * 3) * 0.7);
        n.rotation.set(t, t * 1.3, 0);
      });
      g.rotation.y = Math.sin(t * 0.3) * 0.3;
    };
    return g;
  },

  orbit() {
    const g = new THREE.Group();
    const rings = [2, 1.6, 1.2].map((r, i) => {
      const m = new THREE.Mesh(new THREE.TorusGeometry(r, 0.07, 16, 120), [M.gold, M.copper, M.teal][i]); g.add(m); return m;
    });
    const core = new THREE.Mesh(new THREE.SphereGeometry(0.5, 48, 32), M.gold); g.add(core);
    g.userData.update = (t, dt, e) => {
      const k = 1 + e * 3;
      rings[0].rotation.set(t * 0.5 * k, 0, 0);
      rings[1].rotation.set(0, t * 0.7 * k, t * 0.2);
      rings[2].rotation.set(t * 0.9 * k, t * 0.4, 0);
      core.scale.setScalar(1 + Math.sin(t * 2) * 0.05);
    };
    return g;
  },

  tiles() {
    const g = new THREE.Group(), tiles = [];
    for (let row = 0; row < 4; row++) for (let col = 0; col < 6; col++) {
      const i = row * 6 + col;
      const m = new THREE.Mesh(new THREE.BoxGeometry(0.62, 0.42, 0.05), [M.dark, M.dark, M.dark, M.dark, i % 5 === 0 ? M.teal : i % 3 ? M.copper : M.gold, M.dark]);
      m.userData = { row, col }; tiles.push(m); g.add(m);
    }
    g.userData.update = (t, dt, e) => {
      for (const m of tiles) {
        const { row, col } = m.userData, a = (col - 2.5) * 0.28;
        const wave = Math.sin(t * 2 - col * 0.6 - row * 0.4);
        m.position.set(Math.sin(a) * 3, (row - 1.5) * 0.55, Math.cos(a) * 3 - 3 + wave * (0.2 + e));
        m.rotation.set(wave * 0.25, a, 0);
      }
      g.rotation.y = Math.sin(t * 0.3) * 0.3;
    };
    return g;
  },

  shards() {
    const g = new THREE.Group(), r = rng(12), list = [];
    const geos = [new THREE.OctahedronGeometry(0.16), new THREE.TetrahedronGeometry(0.2), new THREE.IcosahedronGeometry(0.13)];
    for (let i = 0; i < 70; i++) {
      const m = new THREE.Mesh(geos[i % 3], [M.copper, M.teal, M.gold][i % 3]);
      m.userData = { r: 0.4 + r() * 2.1, a: r() * TAU, y: (r() - 0.5) * 2.6, sp: 0.2 + r() * 0.8 };
      list.push(m); g.add(m);
    }
    g.userData.update = (t, dt, e) => {
      for (const m of list) {
        const u = m.userData, a = u.a + t * u.sp, rr = u.r * (1 + e * 1.3);
        m.position.set(Math.cos(a) * rr, u.y + Math.sin(t * 1.5 + u.a) * 0.15, Math.sin(a) * rr);
        m.rotation.set(t * 2 * u.sp, t * u.sp, 0);
      }
    };
    return g;
  },

  ico() {
    const g = new THREE.Group();
    const solid = new THREE.Mesh(new THREE.IcosahedronGeometry(1.25, 0), new THREE.MeshStandardMaterial({ color: 0xc27a48, metalness: 1, roughness: 0.2, flatShading: true }));
    const cage = new THREE.Mesh(new THREE.IcosahedronGeometry(1.95, 1), M.wire);
    const q = glyph("?", "#127569"); q.scale.setScalar(0.9); q.position.z = 1.4;
    g.add(solid, cage, q);
    g.userData.update = (t, dt, e) => {
      solid.rotation.set(t * 0.5, t * 0.7, 0);
      cage.rotation.set(-t * 0.25, -t * 0.35, 0);
      const p = 1 + Math.sin(t * 2.4) * 0.06 + e * 0.5;
      solid.scale.setScalar(p);
      q.position.set(Math.sin(t) * 1.4, Math.cos(t * 1.3) * 0.4, Math.cos(t) * 1.4);
    };
    return g;
  },

  ring() {
    const g = new THREE.Group();
    const big = new THREE.Mesh(new THREE.TorusGeometry(1.4, 0.32, 48, 160), M.copper);
    const smalls = [0, 1, 2].map((i) => { const m = new THREE.Mesh(new THREE.TorusGeometry(0.32, 0.07, 16, 60), i === 1 ? M.teal : M.gold); g.add(m); return m; });
    g.add(big);
    g.userData.update = (t, dt, e) => {
      big.rotation.set(0.9 + Math.sin(t) * 0.2, t * (1 + e * 4), 0);
      smalls.forEach((m, i) => {
        const a = t * 1.4 + (i / 3) * TAU;
        m.position.set(Math.cos(a) * 2.2, Math.sin(a * 1.5) * 0.6, Math.sin(a) * 2.2);
        m.rotation.set(t * 2, t, 0);
      });
    };
    return g;
  },

  plane() {
    const g = new THREE.Group();
    const geo = new THREE.BufferGeometry();
    const v = [0, 0, 1.2, -0.9, 0, -0.6, 0, -0.08, -0.4, 0, 0, 1.2, 0, -0.08, -0.4, 0.9, 0, -0.6, 0, 0, 1.2, 0, -0.08, -0.4, 0, -0.35, -0.5];
    geo.setAttribute("position", new THREE.Float32BufferAttribute(v, 3));
    geo.computeVertexNormals();
    const plane = new THREE.Mesh(geo, new THREE.MeshStandardMaterial({ color: 0xf6efe4, roughness: 0.55, side: THREE.DoubleSide }));
    plane.geometry.scale(1.7, 1.7, 1.7);
    g.add(plane);
    const trail = [];
    for (let i = 0; i < 40; i++) { const m = new THREE.Mesh(new THREE.SphereGeometry(0.05, 6, 5), i % 2 ? M.glow : M.tealGlow); trail.push(m); g.add(m); }
    const pos = (s) => new THREE.Vector3(Math.sin(s) * 1.6, Math.sin(s * 2) * 0.7, Math.cos(s) * 1.1);
    g.userData.update = (t, dt, e) => {
      const s = t * (0.8 + e * 2);
      const p = pos(s), n = pos(s + 0.05);
      plane.position.copy(p); plane.lookAt(n);
      plane.rotateZ(Math.sin(s) * 0.6);
      trail.forEach((m, i) => { m.position.copy(pos(s - (i + 1) * 0.05)); m.scale.setScalar(1 - i / 40); });
    };
    return g;
  },

  default() {
    const g = new THREE.Group();
    const k = new THREE.Mesh(new THREE.TorusKnotGeometry(1.1, 0.28, 220, 24, 3, 4), M.copper);
    g.add(k);
    g.userData.update = (t, dt, e) => k.rotation.set(t * 0.4, t * (0.6 + e * 3), 0);
    return g;
  },
};

// ---------- particles that react to scrolling ----------
const P = small ? 500 : 1400, pr = rng(99);
const pPos = new Float32Array(P * 3);
for (let i = 0; i < P; i++) { pPos[i * 3] = (pr() - 0.5) * 40; pPos[i * 3 + 1] = (pr() - 0.5) * 26; pPos[i * 3 + 2] = -pr() * 30 + 4; }
const pGeo = new THREE.BufferGeometry();
pGeo.setAttribute("position", new THREE.BufferAttribute(pPos, 3));
const dust = new THREE.Points(pGeo, new THREE.PointsMaterial({ color: 0xb06a3a, size: 0.05, transparent: true, opacity: 0.5, depthWrite: false }));
if (DUST) scene.add(dust);

// ---------- scene switching with a springy pop ----------
const anchor = new THREE.Group();
scene.add(anchor);
const cache = {};
let current = null;

function get(name) {
  const k = makers[name] ? name : "default";
  if (!cache[k]) {
    const g = makers[k]();
    g.userData.s = 0; g.userData.v = 0; g.visible = false;
    const holder = new THREE.Group(); holder.add(g); holder.userData = g.userData; holder.visible = false;
    holder.userData.inner = g;
    anchor.add(holder); cache[k] = holder;
  }
  return cache[k];
}

function show(name) {
  const h = get(name);
  if (current === h) return;
  current = h;
  h.visible = true; h.userData.inner.visible = true;
}

function layout() {
  const w = SNAP ? +(params.get("w") || 1200) : innerWidth;
  const h = SNAP ? +(params.get("h") || 900) : innerHeight;
  renderer.setSize(w, h, !SNAP);
  if (SNAP) { canvas.style.width = w + "px"; canvas.style.height = h + "px"; }
  camera.aspect = w / h;
  camera.updateProjectionMatrix();
  const halfW = Math.tan((camera.fov / 2) * (Math.PI / 180)) * camera.position.z * camera.aspect;
  const side = !SNAP && camera.aspect > 1.15;
  anchor.position.x = side ? halfW * 0.58 : 0;
  anchor.scale.setScalar(SNAP ? 1 : side ? Math.min(0.95, (halfW * 0.4) / 2.6) : 0.8);
}
layout();
addEventListener("resize", layout);

// ---------- input: pointer and scroll speed ----------
let mx = 0, my = 0, lastY = scrollY, energy = 0;
addEventListener("pointermove", (e) => { mx = e.clientX / innerWidth - 0.5; my = e.clientY / innerHeight - 0.5; }, { passive: true });

if (!SNAP) {
  const tagged = [...document.querySelectorAll("[data-scene]")];
  const io = new IntersectionObserver((entries) => {
    entries.forEach((en) => { if (en.isIntersecting) show(en.target.dataset.scene); });
  }, { rootMargin: "-45% 0px -45% 0px" });
  tagged.forEach((el) => io.observe(el));
  show(tagged[0] ? tagged[0].dataset.scene : "default");
} else {
  show(SNAP);
  const h = cache[makers[SNAP] ? SNAP : "default"];
  h.userData.s = 1; h.userData.v = 0;
}

// ---------- frame loop ----------
let t = +(params.get("t") || 0), last = performance.now();

function frame(dt) {
  t += dt;
  const y = scrollY, dy = Math.abs(y - lastY); lastY = y;
  energy += (Math.min(1.2, dy / 60) - energy) * Math.min(1, dt * (dy > 0 ? 6 : 2.5));

  for (const k in cache) {
    const h = cache[k], u = h.userData;
    if (!h.visible) continue;
    const target = h === current ? 1 : 0;
    u.v += (target - u.s) * 90 * dt;            // spring
    u.v *= Math.pow(0.0015, dt);                 // damping
    u.s += u.v * dt;
    const s = Math.max(0.0001, u.s);
    h.scale.setScalar(s);
    h.rotation.y = (1 - Math.min(1, s)) * (target ? -2.5 : 2.5);
    h.rotation.z = (1 - Math.min(1, s)) * 0.6;
    u.inner.userData.update(t, dt, energy);
    if (!target && u.s < 0.02 && Math.abs(u.v) < 0.05) h.visible = false;
  }

  if (DUST) {
    const arr = pGeo.attributes.position.array, push = (0.4 + energy * 26) * dt;
    for (let i = 2; i < arr.length; i += 3) { arr[i] += push; if (arr[i] > 8) arr[i] -= 34; }
    pGeo.attributes.position.needsUpdate = true;
    dust.rotation.z = t * 0.02 + y * 0.0004;
    dust.material.size = 0.05 + energy * 0.08;
  }

  warm.position.set(Math.cos(t * 0.6) * 5, 3, Math.sin(t * 0.6) * 5 + 2);
  cool.position.set(Math.cos(t * 0.45 + 2) * -5, -2, Math.sin(t * 0.45 + 2) * 5 + 2);
  camera.position.x += (mx * 1.2 - camera.position.x) * 0.05;
  camera.position.y += (-my * 0.8 - camera.position.y) * 0.05;
  camera.lookAt(anchor.position.x * 0.35, 0, 0);
  renderer.render(scene, camera);
}

function loop(now) {
  const dt = Math.min(0.05, (now - last) / 1000);
  last = now;
  frame(dt);
  requestAnimationFrame(loop);
}

window.__stage = { step: frame, show, scenes: Object.keys(makers) };
if (!MANUAL) requestAnimationFrame((n) => { last = n; requestAnimationFrame(loop); });
else frame(0);
