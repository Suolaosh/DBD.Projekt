<?php
require_once 'UpdateMysql.php';
$add  = new UpdateMysql();

$deviceid = "01";
$hum = $_POST['hum'];
$temp = $_POST['temp'];
$intens = $_POST['intens'];
$time = $_POST['time'];
$data24 = "" . date("h") + 12;
$while = "" . date("Y-m-d") . " " . $data24 . ":" . date("i:s");
$Sqltemp = "INSERT INTO temp VALUES (NULL,'$temp','$time','$while','$deviceid')";
$Sqlhum = "INSERT INTO hum VALUES (NULL,'$hum','$time','$while','$deviceid')";
$Sqlintens = "INSERT INTO intens VALUES (NULL,'$intens','$time','$while','$deviceid')";

$add -> Add($Sqltemp);
$add -> Add($Sqlhum);
$add -> Add($Sqlintens);
?>