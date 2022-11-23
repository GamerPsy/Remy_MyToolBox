<?php
/**
 * Created by PhpStorm.
 * User: sylvain
 * Date: 13/11/18
 * Time: 11:42
 */

namespace App;


class MorseTranslator
{
    const ALPHABET = [
        "-.-.--" => "!",
        "....-" => "4",
        "..--.." => "?",
        "--..--" => ",",
        ".-.-.-" => ".",
        "..---" => "2",
        "...--" => "3",
        "--..." => "7",
        "-...." => "6",
        "....." => "5",
        "---.." => "8",
        "-..." => "B",
        "----." => "9",
        ".--." => "P",
        "-----" => "0",
        "--.." => "Z",
        "-.--" => "Y",
        "-..-" => "X",
        "-.-." => "C",
        "...-" => "V",
        ".----" => "1",
        "..-." => "F",
        "...." => "H",
        ".---" => "J",
        "--.-" => "Q",
        "-..-." => "/",
        ".-.." => "L",
        "..." => "S",
        "---" => "O",
        "-.-" => "K",
        ".-." => "R",
        "..-" => "U",
        "-.." => "D",
        ".--" => "W",
        "--." => "G",
        "-." => "N",
        "--" => "M",
        ".." => "I",
        ".-" => "A",
        "-" => "T",
        "." => "E",
    ];

    public function translate(string $morse) :string
    {
        $morseWords = explode ('   ', $morse);
        foreach ($morseWords as $morseWord) {
            $word = '';
            $morseLetters = explode(' ', $morseWord);
            foreach ($morseLetters as $morseLetter) {
                $word .= self::ALPHABET[$morseLetter];
            }
            $words[] = $word;
        }

        return implode(' ', $words);
    }
}