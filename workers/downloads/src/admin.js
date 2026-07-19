// Admin dashboard for /admin — a single self-contained HTML page.
// The page itself is public; every data call requires the ADMIN_KEY.
// NOTE: inner script deliberately avoids backticks/${} so this file can
// wrap it in one template literal.

export const ADMIN_HTML = `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Orders — Build Your House</title>
<style>
  :root {
    --bg: #f6f4f0; --card: #ffffff; --ink: #1f2933; --muted: #6b7280;
    --line: #e5e1da; --accent: #b45309; --good: #15803d; --bad: #b91c1c; --warn: #a16207;
  }
  * { box-sizing: border-box; }
  body { margin: 0; font: 15px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background: var(--bg); color: var(--ink); }
  .wrap { max-width: 1180px; margin: 0 auto; padding: 24px 16px 64px; }
  h1 { font-size: 22px; margin: 0 0 4px; }
  .sub { color: var(--muted); margin: 0 0 20px; font-size: 13px; }
  .card { background: var(--card); border: 1px solid var(--line); border-radius: 10px; padding: 16px; margin-bottom: 16px; }
  .keyrow { display: flex; gap: 8px; flex-wrap: wrap; align-items: center; }
  input[type=password] { flex: 1; min-width: 220px; padding: 8px 10px; border: 1px solid var(--line); border-radius: 8px; font-size: 14px; }
  button { padding: 8px 14px; border: 1px solid var(--line); border-radius: 8px; background: var(--ink); color: #fff; font-size: 14px; cursor: pointer; }
  button.ghost { background: #fff; color: var(--ink); }
  button:disabled { opacity: .5; cursor: default; }
  .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 10px; margin-bottom: 16px; }
  .stat { background: var(--card); border: 1px solid var(--line); border-radius: 10px; padding: 12px 14px; }
  .stat b { display: block; font-size: 22px; }
  .stat span { color: var(--muted); font-size: 12px; }
  .diag { display: flex; flex-direction: column; gap: 6px; font-size: 14px; }
  .diag .ok { color: var(--good); }
  .diag .fail { color: var(--bad); font-weight: 600; }
  .tablewrap { overflow-x: auto; }
  table { border-collapse: collapse; width: 100%; font-size: 13.5px; background: var(--card); border: 1px solid var(--line); border-radius: 10px; }
  th, td { text-align: left; padding: 9px 10px; border-bottom: 1px solid var(--line); white-space: nowrap; }
  th { background: #faf8f5; font-size: 12px; text-transform: uppercase; letter-spacing: .04em; color: var(--muted); }
  tr:last-child td { border-bottom: 0; }
  .badge { display: inline-block; padding: 1px 8px; border-radius: 999px; font-size: 12px; font-weight: 600; }
  .b-paid { background: #dcfce7; color: var(--good); }
  .b-unpaid { background: #f3f4f6; color: var(--muted); }
  .b-refunded { background: #fef9c3; color: var(--warn); }
  .b-disputed { background: #fee2e2; color: var(--bad); }
  .b-discount { background: #e0e7ff; color: #3730a3; }
  td.actions button { padding: 3px 9px; font-size: 12px; margin-right: 4px; }
  a { color: var(--accent); }
  #msg { margin: 10px 0; font-size: 14px; color: var(--bad); }
  .mono { font-family: ui-monospace, Menlo, monospace; font-size: 12px; color: var(--muted); }
</style>
</head>
<body>
<div class="wrap">
  <h1>Orders — Owner-Builder Job Site Binder</h1>
  <p class="sub">Live data from Stripe + download logs. Nothing on this page is cached.</p>

  <div class="card keyrow">
    <input id="key" type="password" placeholder="Admin key" autocomplete="current-password">
    <button id="load">Load orders</button>
    <button id="forget" class="ghost">Forget key</button>
  </div>

  <div id="msg"></div>
  <div class="stats" id="stats" hidden></div>
  <div class="card diag" id="diag" hidden></div>
  <div class="tablewrap"><table id="tbl" hidden>
    <thead><tr>
      <th>Date</th><th>Customer</th><th>Amount</th><th>Status</th>
      <th>Downloads</th><th>Last download</th><th>Actions</th>
    </tr></thead>
    <tbody id="rows"></tbody>
  </table></div>
</div>

<script>
(function () {
  var keyInput = document.getElementById('key');
  var msg = document.getElementById('msg');
  keyInput.value = localStorage.getItem('byh_admin_key') || '';

  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function money(cents, cur) {
    return (cents / 100).toLocaleString('en-US', { style: 'currency', currency: (cur || 'usd').toUpperCase() });
  }
  function fmtDate(v) {
    var d = typeof v === 'number' ? new Date(v * 1000) : new Date(v);
    return d.toLocaleString('en-US', { month: 'short', day: 'numeric', year: 'numeric', hour: 'numeric', minute: '2-digit' });
  }
  function api(path, opts) {
    opts = opts || {};
    opts.headers = { 'Authorization': 'Bearer ' + keyInput.value };
    return fetch(path, opts).then(function (r) {
      if (r.status === 401) throw new Error('Wrong admin key.');
      if (!r.ok) throw new Error('Request failed (' + r.status + ')');
      return r.json();
    });
  }
  function copy(text, btn) {
    navigator.clipboard.writeText(text).then(function () {
      var old = btn.textContent;
      btn.textContent = 'Copied!';
      setTimeout(function () { btn.textContent = old; }, 1200);
    });
  }

  function renderDiag(d) {
    var el = document.getElementById('diag');
    var pl = d.payment_link || {};
    var lines = [];
    lines.push(d.r2 && d.r2.ok
      ? '<span class="ok">&#10003; Product file in R2 (' + (d.r2.size / 1048576).toFixed(1) + ' MB)</span>'
      : '<span class="fail">&#10007; PRODUCT FILE MISSING FROM R2 — customers cannot download!</span>');
    lines.push(d.d1 && d.d1.ok
      ? '<span class="ok">&#10003; Download log DB reachable (' + d.d1.total_downloads + ' downloads logged)</span>'
      : '<span class="fail">&#10007; Download log DB unreachable</span>');
    if (!pl.found) {
      lines.push('<span class="fail">&#10007; Payment link not found in Stripe</span>');
    } else {
      lines.push(pl.redirect_ok
        ? '<span class="ok">&#10003; Payment link redirects to the download page</span>'
        : '<span class="fail">&#10007; Payment link does NOT redirect to the download page — buyers never see their file!</span>');
      lines.push(pl.allow_promotion_codes
        ? '<span class="ok">&#10003; Promotion codes enabled at checkout</span>'
        : '<span class="fail">&#10007; Promotion codes disabled</span>');
      if (!pl.redirect_ok || !pl.allow_promotion_codes) {
        lines.push('<button id="fixlink">Fix payment link now</button>');
      }
    }
    el.innerHTML = lines.join('');
    el.hidden = false;
    var fix = document.getElementById('fixlink');
    if (fix) fix.onclick = function () {
      fix.disabled = true;
      api('/admin/api/fix-payment-link', { method: 'POST' })
        .then(function () { return load(); })
        .catch(function (e) { msg.textContent = e.message; fix.disabled = false; });
    };
  }

  function renderOrders(orders) {
    var paid = orders.filter(function (o) { return o.payment_status === 'paid'; });
    var revenue = 0, downloads = 0, refunded = 0, disputed = 0;
    paid.forEach(function (o) {
      revenue += (o.amount_total || 0) - (o.amount_refunded || 0);
      downloads += o.downloads;
      if (o.refunded) refunded++;
      if (o.disputed) disputed++;
    });
    var stats = document.getElementById('stats');
    stats.innerHTML =
      '<div class="stat"><b>' + paid.length + '</b><span>paid orders</span></div>' +
      '<div class="stat"><b>' + money(revenue, 'usd') + '</b><span>net revenue</span></div>' +
      '<div class="stat"><b>' + downloads + '</b><span>downloads logged</span></div>' +
      '<div class="stat"><b>' + refunded + '</b><span>refunded</span></div>' +
      '<div class="stat"><b>' + disputed + '</b><span>disputed</span></div>';
    stats.hidden = false;

    var rows = document.getElementById('rows');
    rows.innerHTML = '';
    orders.forEach(function (o) {
      var badges = [];
      if (o.disputed) badges.push('<span class="badge b-disputed">disputed</span>');
      if (o.refunded) badges.push('<span class="badge b-refunded">refunded</span>');
      badges.push(o.payment_status === 'paid'
        ? '<span class="badge b-paid">paid</span>'
        : '<span class="badge b-unpaid">' + esc(o.payment_status) + '</span>');
      if (o.discount > 0) badges.push('<span class="badge b-discount">-' + money(o.discount, o.currency) + ' promo</span>');

      var tr = document.createElement('tr');
      tr.innerHTML =
        '<td>' + fmtDate(o.created) + '</td>' +
        '<td>' + esc(o.email || '—') + (o.name ? '<br><span class="mono">' + esc(o.name) + '</span>' : '') + '</td>' +
        '<td>' + money(o.amount_total || 0, o.currency) + '</td>' +
        '<td>' + badges.join(' ') + '</td>' +
        '<td>' + o.downloads + '</td>' +
        '<td>' + (o.last_download ? fmtDate(o.last_download) : '—') + '</td>' +
        '<td class="actions"></td>';

      var actions = tr.querySelector('.actions');
      if (o.payment_status === 'paid') {
        var b1 = document.createElement('button');
        b1.textContent = 'Copy download page link';
        b1.className = 'ghost';
        b1.onclick = function () { copy(o.success_url, b1); };
        actions.appendChild(b1);
      }
      if (o.payment_intent_id) {
        var a = document.createElement('a');
        a.href = 'https://dashboard.stripe.com/payments/' + o.payment_intent_id;
        a.target = '_blank';
        a.rel = 'noopener';
        a.textContent = 'Stripe';
        actions.appendChild(a);
      }
      rows.appendChild(tr);
    });
    document.getElementById('tbl').hidden = false;
  }

  function load() {
    msg.textContent = '';
    if (!keyInput.value) { msg.textContent = 'Enter the admin key.'; return; }
    localStorage.setItem('byh_admin_key', keyInput.value);
    document.getElementById('load').disabled = true;
    return Promise.all([api('/admin/api/orders'), api('/admin/api/diagnostics')])
      .then(function (res) {
        renderOrders(res[0].orders);
        renderDiag(res[1]);
      })
      .catch(function (e) { msg.textContent = e.message; })
      .then(function () { document.getElementById('load').disabled = false; });
  }

  document.getElementById('load').onclick = load;
  document.getElementById('forget').onclick = function () {
    localStorage.removeItem('byh_admin_key');
    keyInput.value = '';
  };
  keyInput.addEventListener('keydown', function (e) { if (e.key === 'Enter') load(); });
  if (keyInput.value) load();
})();
</script>
</body>
</html>`;
