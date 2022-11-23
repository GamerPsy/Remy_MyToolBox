<?php
/**
 * Created by PhpStorm.
 * User: sylvain
 * Date: 24/10/18
 * Time: 22:55
 */

namespace App;


class Battle
{
    const CARDS = ['A' => 1, '2' => 2, '3' => 3, '4' => 4, '5' => 5,
                   '6' => 6, '7' => 7, '8' => 8, '9' => 9, '10' => 10,
                   'V' => 11, 'D' => 12, 'R' => 13,
    ];

    const WINNERS = [1 => 'P1', 0 => 'Bataille', -1 =>'P2'];

    public function compare(string $card1, string $card2): string
    {
        // if (self::CARDS[$card1] > self::CARDS[$card2]) {
//            $winner = 'P1';
//        } elseif (self::CARDS[$card1] < self::CARDS[$card2]) {
//            $winner = 'P2';
//        } else {
//            $winner = 'Bataille';
//        }

        return self::WINNERS[self::CARDS[$card1] <=> self::CARDS[$card2]];
    }
}