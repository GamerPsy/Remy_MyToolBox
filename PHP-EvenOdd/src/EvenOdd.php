<?php

namespace App;

class EvenOdd
{
    public function findIntruder(array $numbers): int
    {
        foreach ($numbers as $number) {
            if ($number % 2 === 0) {
                $evenOdd['even'][] = $number;
            } else {
                $evenOdd['odd'][] = $number;
            }
        }

        if (count($evenOdd['even']) === 1) {
            return $evenOdd['even'][0];
        } else {
            return $evenOdd['odd'][0];
        }
    }

    const EVEN = 0;
    const ODD = 1;
    public function findIntruderOptimized(array $numbers): int
    {
        foreach ($numbers as $number) {
            $evenOdd[abs($number % 2)][] = $number;
        }

        if (count($evenOdd[self::EVEN]) === 1) {
            return $evenOdd[self::EVEN][0];
        } else {
            return $evenOdd[self::ODD][0];
        }
    }

}