<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
<link rel="stylesheet" type="text/css" href="style_lab4.css">

<head>
	<title> Ascending Order Comments</title>
</head>
<body>
<?php include("left_nav.inc");?>
<?php include("menu.inc");?>

<?php

$asc = file("comments.txt");
sort($asc);
print_r($asc);
$count = count($asc);
for($i = 0;$i<$count;$i++)
 		{
 		   $index =1;	
           $Field = explode(",",$asc[$i]);
           echo "<p> $index. ";
           echo " Name: <a href ='mailto:$Field[1]'>$Field[0] </a><br/>";
           echo "Comments: $Field[2] </p>";	
           echo "------------";
           $index++;
 		}
?>
<br/>
<a href = "comment.php"> Back to Comments Book </a><br/>
<a href = "index.html">Add comment </a>
<?php include("footer.inc");?>
</body>
</html
