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

<li><a href="http://helios.ite.gmu.edu/~ctaylo50/IT207/">Home </a></li>
<h1>Online Contacts Directory</h1>
<h2>Search for a Contact</h2>
<form method = "post" action = "">
First Name <input type = "text" name = "fname"></br></br>
Last Name <input type = "text" name = "lname"></br></br>
<input type="submit" name="Search">
</form>
<hr>
<a href = "lab3add.html" >Add New Contact</a> 
<?php include("footer.inc");?>
</body>
</html>
