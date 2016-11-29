<?php
$filename='E:/wow/res/samejson/army.json';
$army=file_get_contents($filename);
$army=json_decode($army,true);
foreach($army as $item){
    $fileArr[]=$item['json'];
}
foreach($fileArr as $file){
    $fileReName="E:/wow/res/".$file.'.json';
    if(file_exists($fileReName)){
        $donghua=file_get_contents($fileReName);
        $donghua=json_decode($donghua,true);
        if(count($donghua['Content']['Content']['UsedResources'])>2){
            var_dump($donghua['Content']['Content']['UsedResources']);
            var_dump($file);
        }
        $plist=$donghua['Content']['Content']['UsedResources'][0];
        $png=$donghua['Content']['Content']['UsedResources'][1];
        $keyName=str_replace('_','',$file);
        if($plist!='plist_'.$keyName.'.plist'){
            var_dump($plist);
            var_dump($png);
            var_dump($file);
            echo "<br>";
        }
    }
}
?>