<?php

namespace App;


class FindNumber
{
    public function find(array $numbers) :int
    {
//        for($i = $numbers[0]; $i<=$numbers[0]+count($numbers); $i++) {
//            if (!in_array($i, $numbers)) {
//                $result = $i;
//            }
//        }
        $compareNumbers = range(min($numbers), max($numbers));
        $result = array_diff($compareNumbers, $numbers);
        sort($result);
        return $result[0];
    }
}