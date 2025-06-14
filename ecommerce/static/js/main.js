let btns = document.querySelectorAll(".price");

btns.forEach((btn) => {
  btn.addEventListener("click", () => {
    let childSpan = btn.querySelector("span");
    childSpan.textContent = +childSpan.textContent + 100;
  });
});
