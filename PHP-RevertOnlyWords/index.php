<?php

function revertOnlyWords($sentence)
{
    $sentence = explode(" ", $sentence);
    $result = [];
    foreach ($sentence as $mot) {
        $result[] .= strrev($mot);
    }
    $result = implode(" ", $result);
    
    return $result; 
}

$test = "Hello World";
echo revertOnlyWords($test);// attendu "olleH dlroW"