<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
 "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns = "http://www.w3.org/1999/xhtml" >
<head>
 <title> Online Contacts Directory </title>
 <link rel = "stylesheet" type = "text/css" href = "lab3.css" />
</head>
<body>
<?php include("left_nav.inc");?>
<?php include("menu.inc");?>

<?php
if(!empty($_POST["fname"]) && !empty($_POST["lname"])) //ensures that first and last names 
are not empty 
{
if(file_exists("contacts.txt"))
{

$first = $_POST["fname"];
$last = $_POST["lname"];
$found = 0;
$file = file_get_contents("contacts.txt"); 
$contacts = explode("--",$file); 
$count = count($contacts); 
for($x=0;$x<$count;$x++){
$contact = explode(",",$contacts[$x]); 
contact
if(strcasecmp($contact[0],$first)==0 && strcasecmp($contact[1],$last)==0)
{
$found = 1;
}
if($found == 0)
echo "Contact not found"; 
}
}
else
{
echo "You must enter a value in each field.";
}
?>
<hr>
<a href = "lab3.php" >Return to Directory</a>
<?php include("footer.inc");?> 

</body>
</html>
