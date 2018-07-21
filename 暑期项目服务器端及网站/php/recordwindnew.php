<?php
error_reporting(E_ALL ^ E_NOTICE);
require_once 'OperateMysql.php';
$phpGetwind = new OperateMysql();
$conn = $phpGetwind->Connect_Mysql();

$sql = "SELECT * FROM wind ORDER BY id DESC LIMIT 8";
$result = $phpGetwind -> Query_Mysql($sql, $conn) or die("查询失败");

//定义变量json存储值
	$data="";
	$array= array();
	class wind{
		public $id;
	    public $deviceid;
	    public $time;
		public $state;
		public $while;
	}
while ($row = mysql_fetch_row($result))
	{ 
		list($id,$deviceid,$time,$state,$while) = $row;   
		
		$gz = new wind();
		$gz->id = intval($id);
		$gz->deviceid = intval($deviceid);
		$gz->time= intval($time);
		$gz->state= intval($state);
		$gz->while= $while;
 
		//数组赋值
		$array[] = $gz;
	}
 
	$data = json_encode($array);
	echo $data;
mysql_close();
?>