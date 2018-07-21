<?php
//for($i=0;$i<count($cbody);$i++){ //count函数就是获取数组的长度的，长度为3 因为一行被识别为一个数组 有三行
//echo $cbody[$i];//最后是循环输出每个数组，在每个数组输出完毕后 ，输出一个换行，这样就可以达到换行效果
//}
$file = fopen("control.txt","r");
echo(fread($file,"10"));
fclose($file);
?>
