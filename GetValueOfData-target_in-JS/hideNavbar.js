// masquer la navbar au clic sur modal
function hiddeNavbar() {
  let laNavbar = document.getElementById("navbar");
  laNavbar.classList.remove("showNav");
  laNavbar.classList.add("hiddeNav");
}

let nodes = document.getElementsByClassName("modal");
let ajout = "";

for (let i = 0; i < nodes.length; i++) {
  ajout = "#" + nodes[i].getAttribute("id");
  // remettre la navbar à la fermeture du modal
  $(ajout).on("hidden.bs.modal", function () {
    let laNavbar = document.getElementById("navbar");
    laNavbar.classList.remove("hiddeNav");
    laNavbar.classList.add("showNav");
  });
}
