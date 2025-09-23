document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");
  const btn = document.getElementById("btn-submit");
  const btnText = document.getElementById("btn-text");
  const progressBar = document.getElementById("progress-bar");
  const progressFill = document.getElementById("progress-fill");

  form.addEventListener("submit", function () {
    btn.disabled = true;
    btnText.textContent = "Carregando...";
    progressBar.style.display = "block";

    let width = 0;
    const interval = setInterval(() => {
      if (width >= 100) {
        clearInterval(interval);
      } else {
        width += 1;
        progressFill.style.width = width + "%";
      }
    }, 20); // velocidade da barra
  });
});

