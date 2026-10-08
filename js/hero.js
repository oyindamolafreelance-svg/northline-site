import * as THREE from "https://unpkg.com/three@0.166.1/build/three.module.js";

const canvas = document.querySelector("#ring");
if (!canvas) throw new Error("missing canvas");

const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.setSize(canvas.clientWidth, canvas.clientHeight, false);
renderer.outputColorSpace = THREE.SRGBColorSpace;

const scene = new THREE.Scene();
scene.fog = new THREE.Fog(0x07080b, 8, 18);
const camera = new THREE.PerspectiveCamera(38, canvas.clientWidth / canvas.clientHeight, 0.1, 40);
camera.position.set(0, 0.2, 7.2);

scene.add(new THREE.AmbientLight(0x8a7568, 0.35));
const key = new THREE.DirectionalLight(0xffd2b0, 2.4);
key.position.set(4, 3, 5);
scene.add(key);
const rim = new THREE.PointLight(0xc4845a, 18, 20);
rim.position.set(-3, 1, 2);
scene.add(rim);

const ring = new THREE.Mesh(
  new THREE.TorusGeometry(1.7, 0.42, 80, 180),
  new THREE.MeshPhysicalMaterial({
    color: 0xb8734a,
    metalness: 1,
    roughness: 0.22,
    clearcoat: 0.4,
    clearcoatRoughness: 0.3
  })
);
ring.rotation.x = 0.9;
ring.rotation.z = 0.25;
scene.add(ring);

const floor = new THREE.Mesh(
  new THREE.CircleGeometry(8, 64),
  new THREE.MeshStandardMaterial({ color: 0x0c0d11, metalness: 0.8, roughness: 0.35 })
);
floor.rotation.x = -Math.PI / 2;
floor.position.y = -1.8;
scene.add(floor);

function resize() {
  const w = canvas.clientWidth;
  const h = canvas.clientHeight;
  renderer.setSize(w, h, false);
  camera.aspect = w / h;
  camera.updateProjectionMatrix();
}
addEventListener("resize", resize);

let t = 0;
function frame() {
  t += 0.008;
  ring.rotation.y = t;
  ring.rotation.x = 0.85 + Math.sin(t * 0.6) * 0.08;
  renderer.render(scene, camera);
  requestAnimationFrame(frame);
}
frame();
