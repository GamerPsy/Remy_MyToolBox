<?php
/**
 * Created by PhpStorm.
 * User: wilder2
 * Date: 17/01/19
 * Time: 09:42
 */

namespace Test;

use PHPUnit\Framework\TestCase;
use WcsDojo\MineSweeper;


class MineSweeperTest extends TestCase
{
    public function setUp()
    {
        $grid = [
            [0, 0, 0, 1],
            [0, 1, 0, 1],
            [1, 0, 0, 0],
        ];
        $this->demineur = new MineSweeper($grid);
    }
    
    public function testTryBoom()
    {
        
        $this->assertEquals('BOOM', $this->demineur->tryCase(0, 3));
        $this->assertEquals('BOOM', $this->demineur->tryCase(1, 1));
    }
    public function testTrySuccess() {
        $this->assertEquals(1, $this->demineur->tryCase(0, 0));
        $this->assertEquals(1, $this->demineur->tryCase(2, 3));
        $this->assertEquals(2, $this->demineur->tryCase(1, 0));
        $this->assertEquals(2, $this->demineur->tryCase(2, 2));
        $this->assertEquals(2, $this->demineur->tryCase(2, 1));
        $this->assertEquals(3, $this->demineur->tryCase(1, 2));
    }
    public function testException()
    {
        $this->expectException(\LogicException::class);
        $this->demineur->tryCase(12,9);
    }
}