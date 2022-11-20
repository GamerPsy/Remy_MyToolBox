<?php

function funkyRevert($mot)
{
    $start = $end = "";
    if (strlen($mot) % 2 == 0) {
        for ($i = strlen($mot) - 1; $i > 0; $i -= 2) {
            $start .= $mot[$i];
        }
        for ($i = 0; $i < strlen($mot); $i += 2) {
            $end .= $mot[$i];
        }
    }
    
    return $start . $end . "\n";
}


$test1 = "helloworld";
echo funkyRevert($test1); //output helloworld => drwlehlool  - 1-2-3-4-5-6-7-8-9-10 => 10-8-6-4-2 - 1-3-5-7-9

$test2 = "jump";
echo funkyRevert($test2); //output jump => pujm  - 1-2-3-4 => 4-2-1-3
