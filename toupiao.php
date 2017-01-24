<!DOCTYPE HTML>
<html>

<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>点菜投票</title>
  <style>
  div
{
display: flex;
justify-content: space-around;
}
  </style>
</head>
<?php
$name='';
$prize='';
$link = new mysqli('localhost', 'root', '', 'gamemana');
$link->query('set names utf8');
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name=$_POST['name'];
    $prize=$_POST['prize'];
    $ip=$_SERVER['REMOTE_ADDR'];
    $sql="INSERT INTO diancan (name,prize,ip) VALUES ('{$name}','{$prize}','{$ip}')";
    $sql_result = $link->query($sql);
    $link->close();
    header("Location: {$_SERVER['REQUEST_URI']}");
}
$caidan=$link->query("select * from diancan");
$link->close();
?>
  <body>
    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" style="align-content: center;width: 100%;height: 100%">
      <span style='margin: auto;display: block;width: 280px;height: 50px'>
      菜名
      <input type="text" name="name"style='width:195px;height: 30px'>
      </span>
      <span style='margin: auto;display: block;width: 280px;height: 50px'>
      价格
      <input type="text" name="prize" style='width:195px;height: 30px'>
      </span>
      <input type="submit" name="submit" value="Submit" style="margin-left:auto;margin-right:auto;margin-bottom:40px;display: block;width: 200px;height: 30px">
      </form>
      <div>
      <table border="1">
        <thead>
          <tr>
            <th width=100px>菜名</th>
            <th width=100px>价格</th>
          </tr>
        </thead>
        <?php
        $sum=0;
          foreach ($caidan as $key => $value) {
            echo "<tr>"."<td>{$value['name']}</td>"."<td>{$value['prize']}</td>"."</tr>";
            $sum+=$value['prize'];
          }
          echo "<tr>"."<td style='color:blue'>总计</td>"."<td style='color:blue'>{$sum}</td>"."</tr>";
          $caidan->free();
        ?>
      </table>
    </div>
  </body>
</html>