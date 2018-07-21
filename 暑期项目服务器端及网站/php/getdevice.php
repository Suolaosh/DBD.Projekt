<?php
error_reporting(E_ALL ^ E_NOTICE);
require_once 'OperateMysql.php';
$phpGetdevice = new OperateMysql();
$conn = $phpGetdevice -> Connect_Mysql();
$sql = "SELECT * FROM device ";
$result = $phpGetdevice -> Query_Mysql($sql, $conn) or die("查询失败");

//定义变量json存储值
$data = "";
$array = array();
class device {
	public $id;
	public $deviceid;
	public $dpid;
}

while ($row = mysql_fetch_row($result)) {
	list($id, $deviceid, $dpid) = $row;

	$gz = new device();
	$gz -> id = intval($id);
	$gz -> deviceid = intval($deviceid);
	$gz -> dpid = intval($dpid);

	//数组赋值
	$array[] = $gz;
}

$data = json_encode($array);
echo $data;
mysql_close();
?>