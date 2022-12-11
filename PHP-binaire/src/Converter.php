<?php

namespace App;

class Converter
{
    const BIN=['0','1'];

    public function binToDec(string $binary) :int
    {
        $binary = strrev($binary);
        $bits = str_split($binary);
        $res = 0;

        $uniqueCars = array_unique($bits);
        foreach ($uniqueCars as $car) {
            if (!in_array($car, self::BIN)) {
                throw new \Exception();
            }
        }

        foreach ($bits as $key => $value) {
            $value = $value * 2 ** $key;
            $res += $value;

        }
        return $res;
    }

    public function convertToDecimal(string $binary): int
    {
        $result = 0;
        for ($i = 0; $i < strlen($binary); $i++) {
            $power = strlen($binary) - $i - 1;
            $result += $binary[$i] * 2 ** $power;
        }

        return $result;
    }

    
}