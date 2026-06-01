#!/usr/bin/env node
import { createRequire } from "node:module";
import { execFileSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, "..");
const iconDir = path.join(root, "G_Picture", "G_bmplib");
const workDir = process.env.IHM_ICON_WORKDIR || "/tmp/ihm-material-icons";
const nodeModules = path.join(workDir, "node_modules");
const requireFromWork = createRequire(path.join(workDir, "package.json"));

const specs = [
  { file: "ecoEdit", icon: "energy_savings_leaf", width: 94, height: 94, accent: "#22c55e", ppm: 3780, size: 58 },
  { file: "temp1", icon: "device_thermostat", width: 96, height: 96, accent: "#ef4444", ppm: 3780, size: 60 },
  { file: "esteiraIcon", icon: "conveyor_belt", width: 96, height: 96, accent: "#0ea5e9", ppm: 3780, size: 63 },
  { file: "recipe", icon: "menu_book", width: 60, height: 60, accent: "#f59e0b", ppm: 4724, size: 37 },
  { file: "hourIcon1", icon: "schedule", width: 240, height: 240, accent: "#6366f1", ppm: 3780, size: 152 },
  { file: "resetIcon2", icon: "restart_alt", width: 240, height: 240, accent: "#94a3b8", ppm: 3780, size: 152 },
  { file: "img9", icon: "home", width: 64, height: 64, accent: "#0ea5e9", ppm: 3780, size: 46, mode: "glyph" },
  { file: "menu", icon: "menu", width: 64, height: 64, accent: "#0ea5e9", ppm: 3780, size: 46, mode: "glyph" },
  { file: "return1", icon: "arrow_back", width: 48, height: 48, accent: "#cbd5e1", ppm: 3780, size: 34, mode: "glyph" },
  { file: "save1", icon: "save", width: 48, height: 48, accent: "#22c55e", ppm: 3780, size: 34, mode: "glyph" },
  { file: "edit2", icon: "edit", width: 48, height: 48, accent: "#f59e0b", ppm: 3780, size: 34, mode: "glyph" },
  { file: "ir", icon: "space_bar", width: 48, height: 48, accent: "#64748b", ppm: 3780, size: 34, mode: "glyph" },
  { file: "del1", icon: "backspace", width: 100, height: 100, accent: "#94a3b8", ppm: 3780, size: 70, mode: "glyph" },
  { file: "excluir1", icon: "delete", width: 48, height: 48, accent: "#ef4444", ppm: 3780, size: 34, mode: "glyph" },
  { file: "warning", icon: "warning", width: 80, height: 80, accent: "#ffffff", ppm: 3780, size: 58, mode: "glyph" },
  { file: "eco_icon.MID0", icon: "energy_savings_leaf", width: 128, height: 128, accent: "#94a3b8", ppm: 3780, size: 76 },
  { file: "eco_icon.MID1", icon: "energy_savings_leaf", width: 128, height: 128, accent: "#22c55e", ppm: 3780, size: 76 },
  { file: "timer1", icon: "timer", width: 96, height: 96, accent: "#6366f1", ppm: 3780, size: 60 },
];

function ensureDependencies() {
  const materialDir = path.join(nodeModules, "@material-symbols", "svg-500", "rounded");
  const sharpDir = path.join(nodeModules, "sharp");
  if (fs.existsSync(materialDir) && fs.existsSync(sharpDir)) {
    return;
  }

  fs.mkdirSync(workDir, { recursive: true });
  if (!fs.existsSync(path.join(workDir, "package.json"))) {
    execFileSync("npm", ["init", "-y"], { cwd: workDir, stdio: "ignore" });
  }
  execFileSync("npm", ["install", "sharp", "@material-symbols/svg-500"], {
    cwd: workDir,
    stdio: "inherit",
  });
}

function materialIconBody(iconRoot, name, fill = "#fff") {
  const source = fs.readFileSync(path.join(iconRoot, `${name}.svg`), "utf8");
  return source
    .replace(/^[\s\S]*?<svg[^>]*>/, "")
    .replace(/<\/svg>\s*$/, "")
    .replace(/<path/g, `<path fill="${fill}"`);
}

function composeSvg(spec, iconRoot) {
  if (spec.mode === "glyph") {
    const scale = spec.size / 960;
    const tx = (spec.width - spec.size) / 2;
    const ty = (spec.height - spec.size) / 2 + spec.size;

    return `<svg xmlns="http://www.w3.org/2000/svg" width="${spec.width}" height="${spec.height}" viewBox="0 0 ${spec.width} ${spec.height}">
  <rect width="100%" height="100%" fill="#000"/>
  <g transform="translate(${tx} ${ty}) scale(${scale})">
    ${materialIconBody(iconRoot, spec.icon, spec.accent)}
  </g>
</svg>`;
  }

  const pad = Math.max(5, Math.round(Math.min(spec.width, spec.height) * 0.085));
  const radius = Math.round(Math.min(spec.width, spec.height) * 0.2);
  const scale = spec.size / 960;
  const tx = (spec.width - spec.size) / 2;
  const ty = (spec.height - spec.size) / 2 + spec.size;

  return `<svg xmlns="http://www.w3.org/2000/svg" width="${spec.width}" height="${spec.height}" viewBox="0 0 ${spec.width} ${spec.height}">
  <rect width="100%" height="100%" fill="#fff"/>
  <rect x="${pad}" y="${pad}" width="${spec.width - pad * 2}" height="${spec.height - pad * 2}" rx="${radius}" ry="${radius}" fill="${spec.accent}"/>
  <g transform="translate(${tx} ${ty}) scale(${scale})">
    ${materialIconBody(iconRoot, spec.icon)}
  </g>
</svg>`;
}

function writeBmp(file, width, height, rgb, ppm) {
  const rowStride = Math.ceil((width * 3) / 4) * 4;
  const pixelSize = rowStride * height;
  const header = Buffer.alloc(54);

  header.write("BM", 0, 2, "ascii");
  header.writeUInt32LE(54 + pixelSize, 2);
  header.writeUInt32LE(54, 10);
  header.writeUInt32LE(40, 14);
  header.writeInt32LE(width, 18);
  header.writeInt32LE(height, 22);
  header.writeUInt16LE(1, 26);
  header.writeUInt16LE(24, 28);
  header.writeUInt32LE(0, 30);
  header.writeUInt32LE(pixelSize, 34);
  header.writeInt32LE(ppm, 38);
  header.writeInt32LE(ppm, 42);

  const body = Buffer.alloc(pixelSize);
  for (let y = 0; y < height; y += 1) {
    for (let x = 0; x < width; x += 1) {
      const source = (y * width + x) * 3;
      const target = (height - 1 - y) * rowStride + x * 3;
      body[target] = rgb[source + 2];
      body[target + 1] = rgb[source + 1];
      body[target + 2] = rgb[source];
    }
  }

  fs.writeFileSync(file, Buffer.concat([header, body]));
}

function roundedRectPath(x, y, width, height, radius) {
  const r = Math.min(radius, width / 2, height / 2);
  return [
    `M ${x + r} ${y}`,
    `H ${x + width - r}`,
    `Q ${x + width} ${y} ${x + width} ${y + r}`,
    `V ${y + height - r}`,
    `Q ${x + width} ${y + height} ${x + width - r} ${y + height}`,
    `H ${x + r}`,
    `Q ${x} ${y + height} ${x} ${y + height - r}`,
    `V ${y + r}`,
    `Q ${x} ${y} ${x + r} ${y}`,
    "Z",
  ].join(" ");
}

function recipeRowSvg(row, status) {
  const selected = row === status;
  const fill = selected ? "#fff7ed" : "#ffffff";
  const border = selected ? "#f59e0b" : "#d7dee8";
  const text = selected ? "#92400e" : "#64748b";
  const accent = selected ? "#f59e0b" : "#cbd5e1";

  return `<svg xmlns="http://www.w3.org/2000/svg" width="430" height="64" viewBox="0 0 430 64">
  <rect width="430" height="64" fill="#ffffff"/>
  <path d="${roundedRectPath(0.5, 0.5, 429, 63, 6)}" fill="${fill}" stroke="${border}"/>
  <rect x="0" y="0" width="6" height="64" fill="${accent}"/>
  <circle cx="32" cy="32" r="15" fill="${selected ? "#f59e0b" : "#eef2f7"}"/>
  <text x="32" y="38" text-anchor="middle" font-family="Arial, sans-serif" font-size="18" font-weight="700" fill="${selected ? "#ffffff" : text}">${row}</text>
</svg>`;
}

async function main() {
  ensureDependencies();

  const sharp = requireFromWork("sharp");
  const iconRoot = path.join(nodeModules, "@material-symbols", "svg-500", "rounded");

  for (const spec of specs) {
    const svg = composeSvg(spec, iconRoot);
    const rgb = await sharp(Buffer.from(svg))
      .resize(spec.width, spec.height)
      .removeAlpha()
      .raw()
      .toBuffer();

    writeBmp(path.join(iconDir, spec.file), spec.width, spec.height, rgb, spec.ppm);
    console.log(`wrote ${spec.file} from ${spec.icon}`);
  }

  for (let row = 1; row <= 6; row += 1) {
    for (let status = 0; status <= 6; status += 1) {
      const svg = recipeRowSvg(row, status);
      const rgb = await sharp(Buffer.from(svg))
        .resize(430, 64)
        .removeAlpha()
        .raw()
        .toBuffer();
      writeBmp(path.join(iconDir, `radio${row}.MID${status}`), 430, 64, rgb, 3780);
    }
    console.log(`wrote recipe row radio${row}`);
  }
}

await main();
