<?php

use PHPUnit\Framework\TestCase;

class SortTest extends TestCase {

    public function testFunctions(){
        require 'functions.sort.php';
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
        $this->assertEquals($expected,$result);
    }
}

?>