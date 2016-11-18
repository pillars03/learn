<?php
$dir = "D:\Game";
$handle=opendir($dir);
while (false !== ($file = readdir($handle))) {
    if ($file != "." && $file != "..") {
        echo "$file\n";
    }
}
 closedir($handle);