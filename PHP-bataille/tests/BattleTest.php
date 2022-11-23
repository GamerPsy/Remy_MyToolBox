<?php

namespace Tests;


use App\Battle;
use PHPUnit\Framework\TestCase;

class BattleTest extends TestCase
{

    private $battle;

    protected function setUp() : void
    {
        $this->battle = new Battle();
    }

    public function testWinPlayer()
    {
        $this->assertEquals('P2', $this->battle->compare('A','2'));
        $this->assertEquals('P1', $this->battle->compare('2','A'));
        $this->assertEquals('P1', $this->battle->compare('R','D'));
        $this->assertEquals('P1', $this->battle->compare('R','2'));
        $this->assertEquals('P2', $this->battle->compare('D','R'));
    }

    public function testEquality()
    {
        $this->assertEquals('Bataille', $this->battle->compare('A','A'));
        $this->assertEquals('Bataille', $this->battle->compare('2','2'));
        $this->assertEquals('Bataille', $this->battle->compare('V','V'));
    }
}