document.addEventListener('DOMContentLoaded', () => {
  const run = document.getElementById('run');
  run.addEventListener('click', async () => {
    const script = document.getElementById('script').value;
    const res = await fetch('/api/compare', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ script })
    });
    if (!res.ok) {
      alert('Request failed');
      return;
    }
    const data = await res.json();
    document.getElementById('static').textContent = JSON.stringify(data.static, null, 2);
    document.getElementById('dynamic').textContent = JSON.stringify(data.dynamic, null, 2);
  });
});
