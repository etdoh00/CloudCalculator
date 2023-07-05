<?php
use PHPUnit\Framework\TestCase;

class MaxMinTest extends TestCase{
    public function testFunctions() {
        require 'functions.inc.php';
        
    $module_1 = 'module_1';
    $module_2 = 'module_2';
    $module_3 = 'module_3';
    $module_4 = 'module_4';
    $module_5 = 'module_5';
    $mark_1 = 30;
    $mark_2 = 40;
    $mark_3 = 50;
    $mark_4 = 34;
    $mark_5 = 11;

    $modules = array($module_1,$module_2,$module_3,$module_4,$module_5);
    $marks = array($mark_1,$mark_2,$mark_3,$mark_4,$mark_5);
    
    $result = getMaxMin($modules,$marks);
    $expected = ["module_3 - 50", "module_5 - 11"];
    $this->assertSame($expected,$result,"......Performing MaxMin test......");

    }
}