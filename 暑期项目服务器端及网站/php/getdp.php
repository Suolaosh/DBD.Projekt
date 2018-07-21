<?php

error_reporting(E_ALL ^ E_NOTICE);
require_once 'OperateMysql.php';
$phpGetdp = new OperateMysql();
$conn = $phpGetdp -> Connect_Mysql();
$sql = "SELECT * FROM dp ";
$result = $phpGetdp -> Query_Mysql($sql, $conn) or die("查询失败");

//定义变量json存储值
$data = "";
$array = array();
class dp {
	public $dpid;
	public $shortname;
	public $pinyin;
	public $plant;
	public $lng;
	public $lat;
	public $size;
}

while ($row = mysql_fetch_row($result)) {
	list($dpid, $shortname, $pinyin, $plant, $lng, $lat, $size) = $row;

	$gz = new dp();
	$gz -> dpid = intval($dpid);
	$gz -> shortname = $shortname;
	$gz -> pinyin = $pinyin;
	$gz -> plant = $plant;
	$gz -> lng = floatval($lng);
	$gz -> lat = floatval($lat);
	$gz -> size = floatval($size);
	//数组赋值
	$array[] = $gz;
}
$data = json_encode($array);
echo $data;
mysql_close();
?>