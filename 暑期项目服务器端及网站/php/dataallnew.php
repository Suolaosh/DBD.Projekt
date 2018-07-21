<?php
error_reporting(E_ALL ^ E_NOTICE);
require_once 'OperateMysql.php';
$phpGetall = new OperateMysql();
$conn = $phpGetall -> Connect_Mysql();

$sql = "SELECT temp.id,temp.temp,hum.hum,intens.intens,intens.while,intens.deviceid FROM temp,hum,intens WHERE temp.id=hum.id and hum.id = intens.id ORDER BY temp.time DESC LIMIT 16";
$result = $phpGetall -> Query_Mysql($sql, $conn) or die("查询失败");
 
//定义变量json存储值
$data = "";
$array = array();
class all {
	public $time;
	public $temp;
	public $hum;
	public $intens;
	public $while;
	public $deviceid;
}

while ($row = mysql_fetch_row($result)) {
	list($time, $temp, $hum, $intens, $while, $deviceid) = $row;

	$gz = new all();
	$gz -> time = intval($time);
	$gz -> temp = floatval($temp);
	$gz -> hum = floatval($hum);
	$gz -> intens = floatval($intens);
	$gz -> while = $while;
	$gz -> deviceid = intval($deviceid);

	//数组赋值
	$array[] = $gz;
}

$data = json_encode($array);
echo $data;
mysql_close();
?>