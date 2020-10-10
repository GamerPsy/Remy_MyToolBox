let monBouton = document.getElementById("monBouton");
let texte1 = document.getElementById("texte1");
let texte2 = document.getElementById("texte2");

monBouton.addEventListener("click", () => {
  if(getComputedStyle(texte1).display != "none"){
    texte1.style.display = "none";
    texte2.style.display = "block";
    document.getElementById("monBouton").innerHTML = "Merci de votre participation !";
    monBouton.setAttribute("disabled", "disabled");
    monBouton.className = "btn btn-success"
    monBouton.style.cursor = "auto"
  }
})
