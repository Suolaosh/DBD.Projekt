<?php
error_reporting(E_ALL ^ E_NOTICE);
require_once 'OperateMysql.php';
$phpGetintens = new OperateMysql();
$conn = $phpGetintens->Connect_Mysql();

$sql = "SELECT * FROM intens";
$result = $phpGetintens -> Query_Mysql($sql, $conn) or die("查询失败");

//定义变量json存储值
	$data="";
	$array= array();
	class intens{
		public $id;
	    public $intens;
	    public $time;
		public $while;
		public $deviceid;
	}
while ($row = mysql_fetch_row($result))
	{ 
		list($id,$intens,$time,$while,$deviceid) = $row;   
  	
		$gz = new intens();
		$gz->id = intval($id);
		$gz->intens = floatval($intens);
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