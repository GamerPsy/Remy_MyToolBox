let liste = document.querySelectorAll('div > ul > li > a');
let element = [];
let idFocus = [];
let cartes = [];

for (let i = 0; i < liste.length; ++i) {
	element.push(liste[i]);
	idFocus.push(element[i].getAttribute('href').slice(1));
}

for (let i = 0; i < liste.length; ++i) {
	cartes.push(document.getElementById(idFocus[i]));
	console.log(cartes[i]);
}

function toggle(idP) {
	for (let i = 0; i < cartes.length; ++i) {
		cartes[i].style.display = "none";
	}
	
	carte = document.getElementById(idP);
	if (carte.style.display != "none") {
		carte.style.display = "none";
	}
	else {
		carte.style.display = "block";
	}
}

for (let i = 0; i < liste.length; ++i) {
	element[i].addEventListener("click", toggle.bind(this, idFocus[i]), false);
};
