<?php
error_reporting(E_ALL ^ E_NOTICE);
require_once 'OperateMysql.php';
$phpGetpumpnew = new OperateMysql();
$conn = $phpGetpumpnew->Connect_Mysql();

$sql = "SELECT * FROM pump ORDER BY id DESC LIMIT 8";

$result = $phpGetpumpnew -> Query_Mysql($sql, $conn) or die("查询失败");

//定义变量json存储值
	$data="";
	$array= array();
	class pump{
		public $id;
	    public $deviceid;
        public $time;
        public $state;
	    
		public $while;
	}
while ($row = mysql_fetch_row($result))
	{ 
		list($id,$deviceid,$time,$state,$while) = $row;   
  	
		$gz = new pump();
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