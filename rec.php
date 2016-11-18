<?php
$a=5;
function factorial($n){
    if($n == 0){ // base case
        return 1;
    }else { // recursive call
        return ($n * factorial($n-1));
    }
}
print factorial($a);