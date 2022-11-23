<?php

namespace App;


class StringComparator
{
    public function find(array $words) :string
    {
        foreach($words as $word) {
            $stringLength[strlen($word)] = $word;
        }
        ksort($stringLength);
        $minLengthWord = reset($stringLength);

        for($start=0; $start<=strlen($minLengthWord)-1; $start++) {
            for($length = strlen($minLengthWord) - $start; $length>=1; $length--) {
                $substr = substr($minLengthWord, $start, $length);
                $match =0;
                foreach($words as $word) {
                    if (preg_match("/$substr/", $word)) {
                        $match++;
                    }
                }
                if ($match === count($words)) {
                    $matchString[strlen($substr)] = $substr;
                }
            }
        }

        krsort($matchString);
        return reset($matchString);
    }
}