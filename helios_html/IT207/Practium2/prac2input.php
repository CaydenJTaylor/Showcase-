<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
<head>
	<title>
		Input birthday
	</title>
<link rel="stylesheet" type="text/css" href="cal.css"/>
</head>
<body>
Input Birthday
<?php

$monthErr = $dayErr = $yearErr ;


if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (empty($_POST["month"])) {
    $monthErr = "month is required";
  } else {
    $month = test_input($_POST["month"]);
  }

  if (empty($_POST["day"])) {
    $dayErr = "day is required";
  } else {
    $day = test_input($_POST["day"]);
  }

  


  if (empty($_POST["year"])) {
    $yearErr = "year is required";
  } else {
    $year = test_input($_POST["year"]);
  }
}
?>
<?php
if(isset($_POST['submit'])){
$month = "Month:".$_POST['month']."
";
$day = "Day:".$_POST['day']."
";
$year = "Year:".$_POST['year']."
";
$file=fopen("data.txt", "a");
fwrite($file, $month);
fwrite($file, $day);
fwrite($file, $year);
fclose($file);
}
?>

<form action="prac2cal.php" method="post">
Month: <input type="number" name="month"><br>
<span class="error">* <?php echo $monthErr;?></span>
<br><br>
Day: <input type="number" name="day"><br>
<span class="error">* <?php echo $dayErr;?></span>
<br><br>
Year: <input type="number" name="year"><br>
<span class="error">* <?php echo $yearErr;?></span>
<br><br>
<input type="submit">
</form>

              

</body>
</html>