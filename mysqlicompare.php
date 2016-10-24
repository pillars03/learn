<?php

$host       = '';
$user       = '';
$password   = '';
$database   = '';
 
/**
 * 期望得到额结果
 * array(
 *  1 => int,
 *  2 => int,
 *  3 => int
 * )
 */
//平常顺序执行的时间
$time_start=microtime(true);
$result = array('1'=>0,'1'=>0,'1'=>0);
foreach ($result as $key=>$value) {
    $link = new mysqli($host, $user, $password, $database);
    $sql_result = $link->query("SELECT COUNT(*) AS `total` FROM `gm_user` WHERE `game`='{$key}'");
    if (is_object($sql_result)) {
        $sql_result_array = $sql_result->fetch_array(MYSQLI_ASSOC);
        $sql_result->free();
        var_dump($sql_result_array);
        // $result[$key] = $sql_result_array['total'];
    } else {
        echo "error.\n";
    }
}
// var_dump($result);
echo microtime(true)-$time_start;