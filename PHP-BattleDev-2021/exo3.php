<?php
include('tetris.php');

#Créer tableau pour chaque ligne afin de savoir si ligne prête ou non pour validation
$plateau = implode(",", $input);
$plateauOuiNon = [];
for($i=0;$i<20;$i++){
    if(substr_count($input[$i],"#")== 9 ){
        $plateauOuiNon[] = "Oui";
    } else{
        $plateauOuiNon[] = "Non";
    };
};

#Trouver les blocs de 4 lignes d'affilé
$ligne4Plus = $indiceFinBloc = [];
$compteur = 0;
$precedent = "";
for($i=0;$i<count($plateauOuiNon);$i++){
    if($plateauOuiNon[$i]=="Oui"){
        $compteur++;
        if($input[$i]!==$precedent){
            $precedent = $input[$i];
        } 
    }; 
    if($compteur >= 4){
        $ligne4Plus[] = $input[$i];
        $indiceFinBloc[] = $i;
        $compteur = 0;
    };
};

if(empty($ligne4Plus)){
    $reponse = "NOPE";
}
else {
    $firstLigne = $ligne4Plus[0];
    #je trouve la position de la colonne à traverser pour valider les 4 lignes
    $colonne = $compteur = 0;
    for($i=0;$i<strlen($firstLigne);$i++){
        $compteur++;
        if($firstLigne[$i]== "."){
            $colonne=$compteur;
        }
    };
    
    $reponse ="BOOM " . $colonne;
    #vérification avant la première ligne
    for($i=0;$i<=$indiceFinBloc[0];$i++){
        $test = $input[$i];
        if($test[$colonne-1] == "#"){
            $reponse = "NOPE";
        }
    };
    $ind = $indiceFinBloc[0];
    $test2 = $ind[$colonne-1];
    #vérification aprés la dernière ligne
    if($test2 == "."){
        $reponse = "NOPE";
    };
};

echo $reponse . '<br/>';
echo '<pre>';
echo var_dump($plateauOuiNon);
echo '</pre>';

?>