// Scroll reveals only. Content below the fold fades in once; nothing is hidden for no-JS or reduced-motion visitors.
(function () {
  var calm = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var els = Array.prototype.slice.call(document.querySelectorAll(".reveal"));
  if (!els.length || calm || !("IntersectionObserver" in window)) return;
  var line = window.innerHeight * 0.92;
  els.forEach(function (el) { if (el.getBoundingClientRect().top > line) el.classList.add("pre"); });
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.remove("pre"); io.unobserve(e.target); } });
  }, { threshold: 0.15 });
  els.forEach(function (el) { io.observe(el); });
  var yr = document.getElementById("yr"); if (yr) yr.textContent = new Date().getFullYear();
})();
