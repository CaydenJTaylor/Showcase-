<html>
 <head>
 <title>08a</title>
 </head>
 <body>
 <?php
$string = "Hello my name is Cayden";

if(isset($_POST["modify_str"])){

$form = false;

extract($_POST);
// if user has entered some value, then replace it in the string using the str_replace function and print the string after modification
if (!$form){
$string = str_replace($string_search, $string_replace, $string);
echo "String after replacement: <br>";
echo $string;
}
}
else
{
$form = true;
}
if($form)
{
?>
search for and replace for the example string: <br>
<?php echo $string; ?>
<br> <br>
<form action="" method="post">
<label for="string_search"> String to search for: </label>
<input type="text" name="string_search" id="string_search" required="required" /> <br> <br>
<label for="string_replace"> Replacement string: </label>
<input type="text" name="string_replace" id="string_replace" required="required" /> <br> <br>
<input type="submit" id="modify_str" name="modify_str" value="Replace"/>
</form>
<?php
}
?>
 </body>
</html>