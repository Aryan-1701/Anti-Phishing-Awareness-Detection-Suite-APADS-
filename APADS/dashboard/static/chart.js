// Simple wrapper to render a bar chart using Chart.js-like code.
// To keep dependencies minimal, we draw a very basic canvas bar chart.
function renderBarChart(canvasId, labels, values) {
  const canvas = document.getElementById(canvasId);
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  ctx.clearRect(0,0,canvas.width,canvas.height);

  const max = Math.max(...values, 1);
  const padding = 40;
  const availableWidth = canvas.width - padding * 2;
  const barWidth = availableWidth / labels.length * 0.6;
  const gap = (availableWidth / labels.length) * 0.4;
  const baseY = canvas.height - padding;

  ctx.font = "14px Arial";
  ctx.fillStyle = "#333";

  labels.forEach((label, i) => {
    const val = values[i];
    const barHeight = (val / max) * (canvas.height - padding * 2);
    const x = padding + i * (barWidth + gap) + gap/2;
    const y = baseY - barHeight;

    // draw bar
    ctx.fillStyle = "#1976d2";
    ctx.fillRect(x, y, barWidth, barHeight);

    // draw label
    ctx.fillStyle = "#000";
    ctx.fillText(label, x, baseY + 18);

    // draw value
    ctx.fillText(String(val), x + barWidth/4, y - 6);
  });
}
