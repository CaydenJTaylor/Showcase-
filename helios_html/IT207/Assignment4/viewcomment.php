<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
<link rel="stylesheet" type="text/css" href="style_lab4.css">
<head>
	<title> Comments Book</title>
</head>
<body>
<?php include("left_nav.inc");?>
<?php include("menu.inc");?>
	<h1>  Comments Book </h1>
	

<?php

 if(!empty($_POST['delete']))
 {

   if(file_exists("comments.txt"))
   {
   	$Fields = file("comments.txt");
   	$count = count($Fields);
    $deleteField = $_POST['delete']-1;
    unset($Fields[$deleteField]);
    array_values($Fields);
    $updateFile = fopen("comments.txt","w");
    fwrite($updateFile,implode($Fields));
  }
  else
    {
     	echo "<p> You don't have any comments to delete</p>";
     	echo "<a href = 'assign4.html'>Return back to index page</a>";
    }
   
 }

?>

<?php
 if(!file_exists("comments.txt"))
 {
 	echo "<p> No comments are present</p>";
 	echo "<a href= 'assign4.html'>Add New comment</a>";
 }
 else
 {
 	$FileRead = file("comments.txt");
 	$count = count($FileRead);
 	if($count==0)
 	{
 		echo"<p>No comments present</p>";
 	}
 	else
 	{
 		$index=1;
 		for($i = 0;$i<$count;$i++)
 		{
           $Field = explode(",",$FileRead[$i]);
           echo "<p> $index. ";
           echo " Name: <a href ='mailto:$Field[1]'>$Field[0] </a><br/>";
           echo "Comments: $Field[2] </p>";	
           echo "--------------------------------------------";
           $index++;
 		}
 	}
 	echo "<p><a href ='index.html'>Add New Comment</a></p>";
 	echo "<p><a href = 'ascend.php'>Sort in Ascending Order</a></p>";
 	echo "<p><a href = 'descend.php'>Sort in Descending Order</a></p>";

 }

 ?>

 <form action = "viewcomment.php" method = "post">
 Delete Comment number <input type = "text" name = "delete"/>
 <input type = "submit" value = "Delete Comment"/>
</form>
<?php include("footer.inc");?>


</body>
</html>