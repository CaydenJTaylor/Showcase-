<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>05a</title>
</head>
<body>
<?php
$days=cal_days_in_month(CAL_GREGORIAN,9,2021);
echo "There are $days days in September 2021";

$leap_month= 29;

$days == $leap_month ? $output = "The month is a leap month" : $output = "The month is a normal month.";
echo "<br>";
echo $output;




?>

</body>
</html>
	