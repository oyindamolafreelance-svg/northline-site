import * as THREE from "https://unpkg.com/three@0.166.1/build/three.module.js";

const canvas = document.querySelector("#stage");
const kind = document.body.dataset.scene || "home";
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 1.6));
renderer.setSize(innerWidth, innerHeight);
renderer.outputColorSpace = THREE.SRGBColorSpace;

const scene = new THREE.Scene();
scene.fog = new THREE.Fog(0x07080b, 8, 22);
const camera = new THREE.PerspectiveCamera(42, innerWidth / innerHeight, 0.1, 40);
camera.position.set(0, 0.2, 8);

scene.add(new THREE.AmbientLight(0x8a7568, 0.45));
const key = new THREE.DirectionalLight(0xffd2b0, 2.2);
key.position.set(4, 3, 5);
scene.add(key);
const rim = new THREE.PointLight(0xc4845a, 16, 24);
rim.position.set(-3, 1, 2);
scene.add(rim);

const copper = new THREE.MeshPhysicalMaterial({ color: 0xb8734a, metalness: 1, roughness: 0.24, clearcoat: 0.35 });
const glass = new THREE.MeshPhysicalMaterial({ color: 0x7daba3, metalness: 0.2, roughness: 0.08, transmission: 0.86, thickness: 0.6, transparent: true });
const wire = new THREE.MeshBasicMaterial({ color: 0xe0b08a, wireframe: true });

const group = new THREE.Group();
scene.add(group);

if (kind === "home") {
  const ring = new THREE.Mesh(new THREE.TorusGeometry(1.8, 0.38, 64, 160), copper);
  ring.rotation.x = 0.9;
  group.add(ring);
  for (let i = 0; i < 18; i++) {
    const shard = new THREE.Mesh(new THREE.OctahedronGeometry(0.12 + (i % 3) * 0.04), i % 2 ? glass : copper);
    shard.position.set(Math.cos(i) * 3.2, Math.sin(i * 1.7) * 1.4, Math.sin(i) * 2);
    group.add(shard);
  }
} else if (kind === "build") {
  for (let i = 0; i < 5; i++) {
    const plane = new THREE.Mesh(new THREE.BoxGeometry(2.4, 0.08, 1.5), i % 2 ? glass : copper);
    plane.position.y = i * 0.38 - 0.8;
    plane.rotation.y = i * 0.18;
    group.add(plane);
  }
} else if (kind === "localize") {
  group.add(new THREE.Mesh(new THREE.SphereGeometry(1.8, 32, 20), wire));
  for (let i = 0; i < 8; i++) {
    const mark = new THREE.Mesh(new THREE.SphereGeometry(0.08, 16, 16), copper);
    mark.position.set(Math.cos(i) * 1.8, Math.sin(i * 1.4) * 1.2, Math.sin(i) * 1.8);
    group.add(mark);
  }
} else if (kind === "work") {
  for (let i = 0; i < 4; i++) {
    const frame = new THREE.Mesh(new THREE.PlaneGeometry(1.6, 1.05), i % 2 ? glass : copper);
    frame.position.set((i - 1.5) * 0.45, i * 0.18, -i * 0.35);
    frame.rotation.y = -0.4 + i * 0.15;
    group.add(frame);
  }
} else if (kind === "process") {
  const orbit = new THREE.Mesh(new THREE.TorusGeometry(2.1, 0.03, 12, 80), wire);
  orbit.rotation.x = Math.PI / 2.4;
  group.add(orbit);
  for (let i = 0; i < 4; i++) {
    const node = new THREE.Mesh(new THREE.SphereGeometry(0.18, 24, 24), copper);
    node.position.set(Math.cos(i * 1.57) * 2.1, 0.2, Math.sin(i * 1.57) * 2.1);
    group.add(node);
  }
} else {
  group.add(new THREE.Mesh(new THREE.IcosahedronGeometry(1.7, 1), kind === "contact" ? copper : glass));
}

const floor = new THREE.Mesh(
  new THREE.CircleGeometry(9, 64),
  new THREE.MeshStandardMaterial({ color: 0x0c0d11, metalness: 0.7, roughness: 0.4 })
);
floor.rotation.x = -Math.PI / 2;
floor.position.y = -2.1;
scene.add(floor);

let mx = 0, my = 0, t = 0;
addEventListener("pointermove", (e) => {
  mx = (e.clientX / innerWidth - 0.5) * 0.6;
  my = (e.clientY / innerHeight - 0.5) * 0.4;
});
addEventListener("resize", () => {
  camera.aspect = innerWidth / innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(innerWidth, innerHeight);
});
function frame() {
  t += 0.007;
  group.rotation.y = t * 0.35 + mx;
  group.rotation.x = my * 0.4;
  group.position.y = Math.sin(t) * 0.12;
  renderer.render(scene, camera);
  requestAnimationFrame(frame);
}
frame();
