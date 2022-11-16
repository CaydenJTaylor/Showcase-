
<html xmlns="http://www.w3.org/TR/html4/strict.dtd"><head>
<title>06b</title>
<link rel="stylesheet" type="text/css" href="style_lab1.css">
</head>
<body>
<?php 
	$LunchChoices = array("Salad", "Sushi", "Thai", "Mexican", "Inidan");
	echo "Foreach:<br/>";
	foreach ($LunchChoices as $number => $LunchName){
		echo "Lunch $number is $LunchName<br/>";
	}
	
	echo "<br/>While:<br/>";
	$choice = 0;
	while ($choice <=4){
		echo $LunchChoices [$choice],"<br/>";
		++$choice;
	}
?>
</body>
</html>