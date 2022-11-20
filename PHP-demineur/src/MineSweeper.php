<?php
/**
 * Created by PhpStorm.
 * User: wilder2
 * Date: 17/01/19
 * Time: 09:48
 */

namespace WcsDojo;

class MineSweeper
{
    private $grid;

    public function __construct(array $grid)
    {
        $this->grid = $grid;
    }

    public function tryCase(int $x, int $y)
    {
        if (!isset($this->grid[$x][$y])) {
                throw new \LogicException();
        }
        if ($this->grid[$x][$y] === 1) {
            return 'BOOM';
        } elseif ($this->grid[$x][$y] === 0) {
            $mine = 0;
            for ($i = $y - 1; $i <= $y + 1; $i++) {
                for ($j = $x - 1; $j <= $x + 1; $j++) {
                    $mine+=$this->grid[$j][$i] ?? 0;
                }

            }

            return $mine;
        }
    }
}