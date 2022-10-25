<?php
//on compte les occurences de chaque lettre dans un string
//on ressort un tableau où les lettres sont dans l'ordre alphabétique en clef et l'occurence en valeur

$exemple = "balblablablabla";

function calcOccurenceLettres($mot) 
{
    $mot = str_split($mot);
    $calc = array_count_values($mot);
    ksort($calc);

    return $calc;
}

print_r(calcOccurenceLettres($exemple)); //Array ([a] => 5, [b] => 5, [l] => 5);
