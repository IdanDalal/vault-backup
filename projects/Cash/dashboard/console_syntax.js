// Syntax check for every inline script in Cash-Console.html without a DOM: compile each block with new Function. Run: node console_syntax.js
const fs = require('fs'), path = require('path');
const html = fs.readFileSync(path.join(__dirname, 'Cash-Console.html'), 'utf8');
const re = /<script id="([a-z]+)"(?: type="([^"]+)")?>([\s\S]*?)<\/script>/g;
let m, n = 0;
while ((m = re.exec(html))) {
  const [, id, type, src] = m;
  if (type === 'application/json') { JSON.parse(src.replace(/<\\\//g, '</')); console.log('ok json', id, Math.round(src.length / 1024) + ' KB'); n++; continue; }
  try { new Function(src); console.log('ok script', id, Math.round(src.length / 1024) + ' KB'); n++; }
  catch (e) { console.error('SYNTAX', id, e.message); process.exit(1); }
}
console.log(n, 'blocks compiled');
