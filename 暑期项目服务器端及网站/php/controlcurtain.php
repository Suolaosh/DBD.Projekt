<?php
error_reporting(E_ALL ^ E_NOTICE);
require_once 'UpdateMysql.php';

$state = $_POST['state'];

$cbody = implode("", file('control.txt'));
$myfile = fopen("control.txt", "w");

if ($state == "1") {
	$txt = "1" . substr($cbody, 1, 2);
	fwrite($myfile, $txt) or die("error");
} else if ($state == "0") {
	$txt = "0" . substr($cbody, 1, 2);
	fwrite($myfile, $txt) or die("error");
} else {
    $txt = $cbody;
    fwrite($myfile, $txt) or die("error");
    echo "error";
}
fclose($myfile);
?>