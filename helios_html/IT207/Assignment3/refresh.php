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
if(!empty($_POST["new_first"]) && !empty($_POST["new_last"]) && !
empty($_POST["new_email"]) && !empty($_POST["new_phone"]) && !
empty($_POST["new_address"]) && !empty($_POST["new_city"]) && !
empty($_POST["new_state"]) && !empty($_POST["new_zip"]))
{
$new = "--" . $_POST['new_first'] . "," . $_POST['new_last'] . "," . $_POST['new_email'] . 
"," . $_POST['new_phone'] . "," . $_POST['new_address'] . "," . $_POST['new_city'] . "," . 
$_POST['new_state'] . "," . $_POST['new_zip'];
$file = file_get_contents("contacts.txt"); 
$contacts = explode("--",$file);
$count = count($contacts); 
for($x=0;$x<$count;$x++){
$contact = explode(",",$contacts[$x]); 
if(strcasecmp($contact[0],$_POST["new_first"])==0 && strcasecmp($contact[1],
$_POST["new_last"])==0){
$contacts[$x] = $new;
$writeFile = fopen("contacts.txt","w");
if(fwrite($writeFile, $contacts[$x])>0)
echo "Edit was Successful";
else
echo "Edit failed";
}
}
}
else
{
echo "You must enter a value in each field. Click your browser's Back button to return to 
the form.</br></br>";
}
?>
<hr>
<a href = "lab3.php" >Return to Directory</a>
<?php include("footer.inc");?>
</body>
</html>
