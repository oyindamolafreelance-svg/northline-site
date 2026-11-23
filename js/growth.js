// Kayonne Growth pages: the job-value calculator and the mobile "Book a free call" bar.
// The animations are CSS only; this file adds no motion of its own.
(function () {
  var v = document.getElementById("calc-value"), j = document.getElementById("calc-jobs"), out = document.getElementById("calc-out");
  if (v && j && out) {
    var usd = new Intl.NumberFormat("en-US", { style: "currency", currency: "USD", maximumFractionDigits: 0 });
    var calc = function () {
      var a = parseFloat(v.value), b = parseFloat(j.value);
      if (!(a > 0) || !(b > 0)) { out.textContent = "Enter your numbers to see the total."; return; }
      var m = a * b;
      out.textContent = "That's " + usd.format(m) + " a month, or " + usd.format(m * 12) + " a year.";
    };
    v.addEventListener("input", calc); j.addEventListener("input", calc);
  }
  // The bar shows on phones and hides while the closing button is on screen.
  var bar = document.getElementById("book-bar"), close = document.getElementById("g-close");
  if (bar && close && "IntersectionObserver" in window) {
    new IntersectionObserver(function (es) {
      es.forEach(function (e) { bar.classList.toggle("hide", e.isIntersecting); });
    }).observe(close);
  }
})();
