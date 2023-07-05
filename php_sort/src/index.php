<?php
header("Access-Control-Allow-Origin: *");
header("Content-type: application/json");
require('functions.inc.php');

$output = array(
	"error" => false,
  "modules" => "",
	"marks" => 0,
	"sorted_modules" => ""
);

$module_1 = $_REQUEST['module_1'];
$module_2 = $_REQUEST['module_2'];
$module_3 = $_REQUEST['module_3'];
$module_4 = $_REQUEST['module_4'];
$module_5 = $_REQUEST['module_5'];
$mark_1 = $_REQUEST['mark_1'];
$mark_2 = $_REQUEST['mark_2'];
$mark_3 = $_REQUEST['mark_3'];
$mark_4 = $_REQUEST['mark_4'];
$mark_5 = $_REQUEST['mark_5'];


if (!$mark_1)  {
    echo("Error mark 1 is missing");
    return http_response_code(400);
    }
if (!$mark_2)  {
    echo("Error mark 2 is missing");
    return http_response_code(400);
}

if (!$mark_3)  {
    echo("Error mark 3 is missing");
    return http_response_code(400);
}

if (!$mark_4)  {
    echo("Error mark 4 is missing");
    return http_response_code(400);
}
            
if (!$mark_5)  {
    echo("Error mark 5 is missing");
    return http_response_code(400);
}

if (!$module_1)  {
    echo("Error module 1 is missing");
    return http_response_code(400);
}

if (!$module_2)  {
    echo("Error module 2 is missing");
    return http_response_code(400);
}

if (!$module_3)  {
    echo("Error module 3 is missing");
    return http_response_code(400);
}

if (!$module_4)  {
    echo("Error module 4 is missing");
    return http_response_code(400);
}

if (!$module_5)  {
    echo("Error module 5 is missing");
    return http_response_code(400);
}

if(!is_numeric($mark_1)) { 
    echo("Mark 1 is not an integer");
    return http_response_code(400);
}

if(!is_numeric($mark_2)) { 
    echo("Mark 2 is not an integer");
    return http_response_code(400);
}

if(!is_numeric($mark_3)) { 
    echo("Mark 3 is not an integer");
    return http_response_code(400);
}

if(!is_numeric($mark_4)) { 
    echo("Mark 4 is not an integer");
    return http_response_code(400);
}

if(!is_numeric($mark_5)) { 
    echo("Mark 5 is not an integer");
    return http_response_code(400);
}

$modules = array($module_1,$module_2,$module_3,$module_4,$module_5);
$marks = array($mark_1,$mark_2,$mark_3,$mark_4,$mark_5);

for ($k=0; $k < count($marks); $k++){
    if ($marks[$k] < 0 or $marks[$k] >100){ 
        echo "Invalid module mark. Mark must not be below 0 or exceed 100!";
        return http_response_code(400);
    }
}
$sorted_modules=getSortedModules($modules, $marks);

$output['modules']=$modules;
$output['marks']=$marks;
$output['sorted_modules']=$sorted_modules;

echo json_encode($output);
exit();
