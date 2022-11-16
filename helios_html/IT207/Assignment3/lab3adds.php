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

<h1>New Contact Entry</h1>
<form method = "post" action = "lab3add.php"> 
First Name <input type = "text" name = "fname"> Last Name <input type = "text" name = 
"lname"></br>
Email Address <input type = "text" name = "email"></br>
Phone Number <input type = "text" name = "phone"></br>
Address <input type = "text" name = "address"> City <input type = "text" name = 
"city"></br>
State <select name = "state">
<option value = "Virginia">Virginia</option>
</select>
Zip <input type = "text" name = "zip"></br>
<input type="submit" name="Add Entry">
</form>
<hr>
<a href="lab3.php">Return to Directory</a>
<?php include("footer.inc");?>
</body>
</html>