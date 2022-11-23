<?php

namespace App;


class Decypher
{
    /**
     * @var string
     */
    private $keyword;
    private $alphabet;
    private $cypherAlphabet;

    public function __construct(string $keyword)
    {
        $this->keyword = $keyword;
        $this->alphabet = range('A', 'Z');
        $this->cypherAlphabet = $this->buildAlphabet();
    }

    private function buildAlphabet()
    {
        $splitKeyword = str_split($this->keyword);
        $alphabetMinusKeyword = array_merge($splitKeyword, array_diff($this->alphabet, $splitKeyword));
        return array_combine($alphabetMinusKeyword, $this->alphabet);
    }

    public function translate(string $cryptedPassword) : string
    {
        for($i=0; $i<strlen($cryptedPassword);$i++) {
            $letter = $cryptedPassword[$i];
            $decypherLetters[] = $this->cypherAlphabet[$letter];
        }

        return implode($decypherLetters);
    }
}