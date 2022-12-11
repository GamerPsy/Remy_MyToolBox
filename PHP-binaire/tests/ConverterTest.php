<?php
namespace Tests;

use PHPUnit\Framework\TestCase;
use App\Converter;

class ConverterTest extends TestCase
{
    public function testBinToDec()
    {
        $converter = new Converter();
        $nbDecimal = $converter->binToDec('1101');
        $this->assertEquals(13, $nbDecimal);
    }

    public function testNotBin()
    {
        $this->expectException(\Exception::class);
        $converter = new Converter();
        $converter->binToDec('1AB');
    }

    public function testOneNumber()
    {
        $binary = new Converter();
        $this->assertEquals(1, $binary->convertToDecimal('1'));
        $this->assertEquals(0, $binary->convertToDecimal('0'));
    }

    public function testMultipleNumbers()
    {
        $binary = new Converter();
        $this->assertEquals(2, $binary->convertToDecimal('10'));
        $this->assertEquals(22, $binary->convertToDecimal('10110'));
        $this->assertEquals(bindec('101010101010101'), $binary->convertToDecimal('101010101010101'));
    }
}