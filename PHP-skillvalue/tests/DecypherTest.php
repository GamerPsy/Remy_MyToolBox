<?php

namespace Tests;


use App\Decypher;
use PHPUnit\Framework\TestCase;

class DecypherTest extends TestCase
{
    public function testDecypherPassword()
    {
        $decypher = new Decypher('KEYWORD');
        $this->assertEquals('PYTHON', $decypher->translate('LXQAJI'));
    }
}
