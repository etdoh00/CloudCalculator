<?php
declare(strict_types=1);
use PHPUnit\Framework\TestCase;
require 'functions.inc.php';
require 'functions.sort.php';

final class Tests extends TestCase
{
    public function testMaxMinFunction():void {
      
        
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
    public function testSortFunction(): void{
        
        $mark_1 = '10';
        $mark_2 = '20';
        $mark_3 = '30';
        $mark_4 = '40';
        $mark_5 = '50';
        $module_1 = 'module_1';
        $module_2 = 'module_2';
        $module_3 = 'module_3';
        $module_4 = 'module_4';
        $module_5 = 'module_5';

        
        $modules = array($module_1,$module_2,$module_3,$module_4,$module_5);
        $marks = array($mark_1,$mark_2,$mark_3,$mark_4,$mark_5);

        $module_marks = array();
        for ($i = 0; $i < count($modules); $i++) {
          $module_marks_array = array("module"=>$modules[$i], "marks"=>$marks[$i]);
          array_push($module_marks,$module_marks_array);
        }

        $result = getSortedModules($modules,$marks);
        rsort($module_marks);  
        $expected = $module_marks;
        $this->assertEquals($expected,$result,"Testing sort function");
    }
}