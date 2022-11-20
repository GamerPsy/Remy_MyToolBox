<?php

function isAnagramme(String $mot1, String $mot2): bool
{
    if (strlen($mot1) > strlen($mot2)) {
        return false;
    }
    if (strlen($mot1) === strlen($mot2)) {
        $tableauMot1 = str_split($mot1);
        $tableauMot2 = str_split($mot2);
        sort($tableauMot1);
        sort($tableauMot2);
        $isItAnagramm = $tableauMot1 === $tableauMot2 ? true : false;
        return $isItAnagramm;
    }
    return false;
}

/////////////////TEST///////////////////////////////////////////////////////////////////////////////////////////
$wordOriginal = "algorithm";
$wordToCompare = "algorithm";
//$wordToCompare = "algorithmics";
$reponse = isAnagramme($wordOriginal, $wordToCompare) === true ? "Il y a anagramme" : "Il n'y a pas anagramme";
echo $reponse;
