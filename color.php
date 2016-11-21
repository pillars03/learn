<!DOCTYPE HTML>
<html>

<head>
  <meta charset="utf-8">
  <title>查看颜色</title>
</head>
<?php
$color='';
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if(stripos($_POST['color'],'#')!==false){
    $color=$_POST['color'];
  }else{
    $color='#'.$_POST['color'];
  }
}
?>
  <body style='background-color:<?php echo "$color"?>'>
  <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
    <input type="text" name="color" value="<?php echo $color;?>">
    <input type="submit" name="submit" value="Submit">
    </form>
  </body>

</html>