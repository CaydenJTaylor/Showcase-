
<html xmlns="http://www.w3.org/TR/html4/strict.dtd"><head>
<title>06a </title>
<link rel="stylesheet" type="text/css" href="style_lab1.css">
</head>
<body>
<?php 
	date_default_timezone_set('America/New_York');
	$current_minute = date("i");
	$current_second = date("s");
	$current_time =date("h:i:s");
	
	echo "The current time is:",$current_time,"<br />";
	if (($current_minute and $current_second)>=0 and $current_minute <=14 and $current_second <=59){
		echo "We are currently in the first quater if the hour";
	}
	else if ($current_minute >=15 and $current_minute <=29){
		echo "<br /> We are currently in the second quater of the hour";
	}
	else if ($current_minute >=30 and $current_minute <=44){
		echo "<br /> We are currently in the third quater of the hour";
	}
	else{
		echo "<br /> We are currnetly in the forth quater of the hour";
	}
	
?>
</body>
</html>