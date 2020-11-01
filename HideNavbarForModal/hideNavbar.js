// masquer la navbar au clic sur modal
function hiddeNavbar() {
  let laNavbar = document.getElementById("navbar");
  laNavbar.classList.remove("showNav");
  laNavbar.classList.add("hiddeNav");
}

// remettre la navbar à la fermeture du modal
$("#exampleModal").on("hidden.bs.modal", function () {
  let laNavbar = document.getElementById("navbar");
  laNavbar.classList.remove("hiddeNav");
  laNavbar.classList.add("showNav");
});
