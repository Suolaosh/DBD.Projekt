<?php
error_reporting(E_ALL ^ E_NOTICE);
require_once 'OperateMysql.php';
$phpGettemp = new OperateMysql();
$conn = $phpGettemp->Connect_Mysql();

$sql = "SELECT * FROM temp ORDER BY id DESC LIMIT 8";
$result = $phpGettemp -> Query_Mysql($sql, $conn) or die("查询失败");

//定义变量json存储值
	$data="";
	$array= array();
	class temp{
		public $id;
	    public $temp;
	    public $time;
		public $while;
		public $deviceid;
	}
while ($row = mysql_fetch_row($result))
	{ 
		list($id,$temp,$time,$while,$deviceid) = $row;   
  	
		$gz = new temp();
		$gz->id = intval($id);
		$gz->temp = floatval($temp);
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