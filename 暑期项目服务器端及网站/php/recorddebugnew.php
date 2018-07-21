<?php
error_reporting(E_ALL ^ E_NOTICE);
require_once 'OperateMysql.php';
$phpGetdebug = new OperateMysql();
$conn = $phpGetdebug->Connect_Mysql();

$sql = "SELECT * FROM debug ORDER BY id DESC LIMIT 8";
$result = $phpGetdebug -> Query_Mysql($sql, $conn) or die("查询失败");

//定义变量json存储值
	$data="";
	$array= array();
	class debug{
		public $id;
	    public $deviceid;
	    public $power;
		public $loraactive;
		public $while;
	}
while ($row = mysql_fetch_row($result))
	{ 
		list($id,$deviceid,$power,$loraactive,$while) = $row;   
  	
		$gz = new debug();
		$gz->id = intval($id);
		$gz->deviceid = intval($deviceid);
		$gz->power= intval($power);
		$gz->loraactive= intval($loraactive);
		$gz->while = $while;
 
		//数组赋值
		$array[] = $gz;
	}
 
	$data = json_encode($array);
	echo $data;
mysql_close();
?>