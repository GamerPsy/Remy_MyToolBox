<?php
function fizzBuzz(int $input):string
{
    $result = '';
    if ($input % 3 == 0) {
        $result .= 'Fizz';
    }
    if ($input % 5 == 0) {
        $result .= 'Buzz';
    }
    return $input . ':' . $result . '<br/>';
}

echo fizzBuzz(3)."\n";
echo fizzBuzz(5)."\n";
echo fizzBuzz(15)."\n";
echo fizzBuzz(8)."\n";

