<html>
<head>
<title>05b</title>
</head>
<body>

<?php
function mod_output($value1, $value2) {
	echo "First Value: ", $value1, "<br />";
	echo "Second Value: ", $value2, "<br />";
	$output1 = $value1 % $value2;
	echo "Modulus: ", $output1, "<br />";
}
mod_output(5,3);


function mod_output2($valueone, $valuetwo) {
	$output2 = $valueone % $valuetwo;
	Return $output2;
}
echo mod_output2(10, 35);
?>

</body>
</html>
	