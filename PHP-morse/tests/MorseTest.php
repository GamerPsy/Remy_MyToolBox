<?php
/**
 * Created by PhpStorm.
 * User: sylvain
 * Date: 13/11/18
 * Time: 11:36
 */

namespace Tests;

use App\MorseTranslator;
use PHPUnit\Framework\TestCase;

class MorseTest extends TestCase
{
    public function testOneLetter()
    {
        $morseTranslator = new MorseTranslator();
        $this->assertEquals('W', $morseTranslator->translate('.--'));
        $this->assertEquals('I', $morseTranslator->translate('..'));
    }
    public function testOneWord() {
        $morseTranslator = new MorseTranslator();
        $this->assertEquals('WILD', $morseTranslator->translate('.-- .. .-.. -..'));
    }

    public function testMultipleWords()
    {
        $morseTranslator = new MorseTranslator();
        $this->assertEquals('WILD CODE', $morseTranslator->translate('.-- .. .-.. -..   -.-. --- -.. .' ));
    }
}