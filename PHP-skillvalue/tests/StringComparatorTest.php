<?php

namespace Tests;


use App\StringComparator;
use PHPUnit\Framework\TestCase;

class StringComparatorTest extends TestCase
{
    public function testFindString()
    {
        $stringComparator = new StringComparator();
        $this->assertEquals('comp', $stringComparator->find(['comparateur', 'compas', 'decomposer']));
        $this->assertEquals('a', $stringComparator->find(['aaa', 'bab', 'ca']));
    }
}

