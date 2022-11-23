<?php

require __DIR__.'/../src/EvenOdd.php';

$evenOdd = new \App\EvenOdd();
echo $evenOdd->findIntruder([1,2,3]);
echo $evenOdd->findIntruder([2,4,7,8]);
echo $evenOdd->findIntruder([2,-40,7878,-1, 0]);
echo $evenOdd->findIntruderOptimized([2,-40,7878,-1, 0]);