<?php
/**
 * Created by PhpStorm.
 * User: sylvain
 * Date: 13/12/18
 * Time: 10:57
 */

namespace App;


class ChristmasTree
{
    public function draw(int $level) :array
    {
        for($i=0; $i<$level; $i++) {
            $spaces = str_repeat(' ', $level-$i-1);
            $stars = str_repeat('*', 2*$i+1);
            $tree[] = $spaces.$stars.$spaces;
        }

        return $tree;
    }
}






















