function changeClass()
{
    const textA = "Premier texte blablablablablablablablablablablablablablablablablablablablabla.";
    const textB = "Deuxième texte blablablablablablablablablablablablablablablablablablablablabla.";
    var x = setTimeout("document.getElementById('texteToMove').className = 'card-text'", 1500);

    if (document.getElementById('texteToMove').innerHTML == textA) {
        document.getElementById('texteToMove').className += ' animated slideOutRight';
        setTimeout(function () {
            document.getElementById('texteToMove').className = 'card-text';
            document.getElementById('texteToMove').innerHTML = textB;
            }, 1500);
    } else {
        document.getElementById('texteToMove').className += ' animated slideOutRight';
        setTimeout(function () {
            document.getElementById('texteToMove').className = 'card-text';
            document.getElementById('texteToMove').innerHTML = textA;
            }, 1500);
    }
}

window.onload = function()
{
    document.getElementById('bouton').addEventListener("click" , changeClass);
}