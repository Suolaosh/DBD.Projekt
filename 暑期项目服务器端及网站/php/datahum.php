<?php
error_reporting(E_ALL ^ E_NOTICE);
require_once 'OperateMysql.php';
$phpGethum = new OperateMysql();
$conn = $phpGethum->Connect_Mysql();

$sql = "SELECT * FROM hum";
$result = $phpGethum -> Query_Mysql($sql, $conn) or die("查询失败");

//定义变量json存储值
	$data="";
	$array= array();
	class hum{
		public $id;
	    public $hum;
	    public $time;
		public $while;
		public $deviceid;
	}
while ($row = mysql_fetch_row($result))
	{ 
		list($id,$hum,$time,$while,$deviceid) = $row;   
  	
		$gz = new hum();
		$gz->id = intval($id);
		$gz->hum = floatval($hum);
		$gz->time= intval($time);
		$gz->while= $while;
		$gz->deviceid= intval($deviceid);
 
		//数组赋值
		$array[] = $gz;
	}
 
	$data = json_encode($array);
	echo $data;
mysql_close();
?>