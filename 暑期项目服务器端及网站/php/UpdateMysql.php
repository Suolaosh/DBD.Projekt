<?php
class UpdateMysql {
	function Add($Sql) {
		require_once 'OperateMysql.php';
		$addMysql = new OperateMysql();
		$conn = $addMysql -> Connect_Mysql();
		$result = $addMysql -> Add_Mysql($Sql, $conn) or die('神tm的错误!' . mysql_error());

		if ($result) {
			//$response["success"] = 1;json_encode($response);
			echo "success";
			//插入成功
		} else {
			//插入失败
			//$response["failed"] = 0;json_encode($response);
			echo "error";
		}
		mysql_close();
	}

	function getDate() {
		$data24 = "" . date("h") + 12;
		$data = "" . date("Y-m-d") . " " . $data24 . ":" . date("i:s");
		return $date;
	}
}

?>
