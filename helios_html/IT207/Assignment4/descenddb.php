<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
<link rel="stylesheet" type="text/css" href="style_lab4.css">
<head>
	 <title> Descending Order </title>
</head>
<body>
<?php include("left_nav.inc");?>
<?php include("menu.inc");?>
<h2> Comments Book </h2> 
<?php

define("DB_SERVER", "localhost:3307");
define("DB_USER", "root");
define("DB_PASSWORD", "");
$conn = mysqli_connect(DB_SERVER , DB_USER, DB_PASSWORD);
if($conn) 
{
 mysqli_query($conn,"USE IT207");
 $sql = "SELECT id,name,email,comments FROM comments ORDER BY NAME DESC";
 $result = mysqli_query($conn,$sql);
 $rows = mysqli_num_rows($result);
 for($i = 0;$i<$rows;$i++)
 {
 	mysqli_data_seek($result,$i);
 	$row = mysqli_fetch_row($result);
 	echo "<p> $row[0] ";
    echo "Name :<a href ='mailto:$row[2]'>$row[1]</a><br/>";
    echo "Comments : $row[3]</p><br/>";	
    echo "--------------------------------------------";
 }
}
?>
<br/>
<a href = "viewCommentdb.php">Comments Book</a>
<?php include("footer.inc");?>
</body>
</html>