/* DesarrollaGT — interacciones mínimas (menú móvil y medición de clics a WhatsApp) */
(function () {
  var boton = document.querySelector('.nav-toggle');
  var menu = document.getElementById('menu');
  if (boton && menu) {
    boton.addEventListener('click', function () {
      var abierto = menu.classList.toggle('open');
      boton.setAttribute('aria-expanded', abierto ? 'true' : 'false');
    });
    menu.addEventListener('click', function (e) {
      if (e.target.closest('a')) {
        menu.classList.remove('open');
        boton.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // Medición de clics a WhatsApp: funciona en cuanto se agregue Google Analytics 4 (gtag)
  // o GoatCounter. Sin ninguno de los dos, no hace nada. Ver README.md.
  document.addEventListener('click', function (e) {
    var enlace = e.target.closest('a[href*="wa.me/"]');
    if (!enlace) return;
    var origen = enlace.getAttribute('data-origen') || 'sin-origen';
    if (typeof window.gtag === 'function') {
      window.gtag('event', 'click_whatsapp', { origen: origen, pagina: location.pathname });
    }
    if (window.goatcounter && typeof window.goatcounter.count === 'function') {
      window.goatcounter.count({ path: 'whatsapp-' + origen, title: 'Clic WhatsApp', event: true });
    }
  });
})();
