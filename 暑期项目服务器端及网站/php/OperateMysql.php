<?php
error_reporting(E_ALL ^ E_NOTICE);

class OperateMysql {
	
	function Connect_Mysql() {

		$conn = mysql_connect(SAE_MYSQL_HOST_M . ':' . SAE_MYSQL_PORT, SAE_MYSQL_USER, SAE_MYSQL_PASS);
		
		$db_select = mysql_select_db(SAE_MYSQL_DB, $conn);
		if (!$db_select) {
			die('can\'t select db:' . mysql_error());
		}

		//解决中文乱码
		mysql_query("SET NAMES UTF8");
		mysql_query("SET CHARACTER SET UTF8");
		mysql_query("SET CHARACTER_SET_RESULT = UTF8");
		return $conn;
	}

	//数据库查询
	function Query_Mysql($Sql, $conn) {
		$result = mysql_query($Sql, $conn);
		//查询成功返回 查询的结果  失败则返回false
		return $result;
	}

	//数据库增加记录语句
	function Add_Mysql($Sql,$conn) {
		$result = mysql_query($Sql,$conn);
		//插入成功返回true失败返回false
		return $result;
	}

	//数据库修改记录
	function Update_Mysql($Sql, $conn) {
		$result = mysql_query($Sql, $conn);
		//修改成功返回true失败返回false
		return $result;
	}

	//数据库删除记录
	function Delete_Mysql($Sql, $conn) {
		$result = mysql_query($Sql, $conn);
		//插入成功返回true失败返回false
		return $result;
	}

}
?>
