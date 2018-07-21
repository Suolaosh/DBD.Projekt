<?php
require_once 'UpdateMysql.php';
$add = new UpdateMysql();
$deviceid = "01";
$time = $_POST['time'];
$state = $_POST['state'];
$data24 = "" . date("h") + 12;
$while = "" . date("Y-m-d") . " " . $data24 . ":" . date("i:s");
$Sql = "INSERT INTO curtain VALUES (NULL,'$deviceid','$time','$state','$while')";

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

$add -> Add($Sql);
?>