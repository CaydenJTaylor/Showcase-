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
if(!empty($_POST["fname"]) && !empty($_POST["lname"]) && !empty($_POST["email"]) && !
empty($_POST["phone"]) && !empty($_POST["address"]) && !empty($_POST["city"]) && !
empty($_POST["state"]) && !empty($_POST["zip"]))
{
$first = $_POST["fname"];
$last = $_POST["lname"];
$email = $_POST["email"];
$phone = $_POST["phone"];
$address = $_POST["address"];
$city = $_POST["city"];
$state = $_POST["state"];
$zip = $_POST["zip"];
$new = "--".$first.",".$last.",".$email.",".$phone.",".$address.",".$city.",".$state.",".$zip;
$writeFile = fopen("contacts.txt","a");
if(fwrite($writeFile, $new)==true) 
{
echo "Contact has been successfully added</br></br>";
}
else
{
echo "Contact has failed to be added</br></br>";
}
}
else
{
echo "You must enter a value in each field.</br></br>";
}
?>
<a href='lab3.php'>Return to Directory</a>;
<?php include("footer.inc");?>
</body>
</html>