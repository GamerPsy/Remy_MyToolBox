<?php
/**
 * Created by PhpStorm.
 * User: sylvain
 * Date: 13/12/18
 * Time: 10:55
 */

namespace Tests;
use App\ChristmasTree;
use PHPUnit\Framework\TestCase;

class ChristmasTreeTest extends TestCase
{
    public function testOneLevel()
    {
        $christmasTree = new ChristmasTree();
        $this->assertEquals(['*'], $christmasTree->draw(1));
    }

    public function testTwoLevel()
    {
        $christmasTree = new ChristmasTree();
        $this->assertEquals([' * ', '***'], $christmasTree->draw(2));
    }

    public function testThreeLevel()
    {
        $christmasTree = new ChristmasTree();
        $this->assertEquals(['  *  ', ' *** ', '*****'], $christmasTree->draw(3));
    }
}