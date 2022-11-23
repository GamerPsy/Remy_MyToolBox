<?php

namespace Tests;


use App\FindNumber;
use PHPUnit\Framework\TestCase;

class FindNumberTest extends TestCase
{
    public function testFindNumber()
    {
        $missingNumberFinder = new FindNumber();
        $this->assertEquals(2, $missingNumberFinder->find([1,3]));
        $this->assertEquals(100, $missingNumberFinder->find([98,99,101,102]));
    }
}
