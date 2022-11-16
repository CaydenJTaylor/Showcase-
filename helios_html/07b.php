<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Excercise07b</title>
</head>
<body>
<?php
	$To = "To: <" . $_GET["to"] . ">";
	$Cc = "Cc: <" . $_GET["cc"] . ">";
	$Subject = $_GET["subject"];
	$Message = $_GET["message"];
	if (empty($To) || empty($Subject) || empty($Message)) {
		echo "To, Subject, and Message must be provided";
	} else {
		$response = mail($To, $Cc, $Subject, $Message, "From: <ctaylo50@gmu.edu>");
		if ($response == 1) {
			echo "An email was sent email successful!";
		} else {
			echo "An email was sent email unsuccessful!";
		}
}
?>
</body>
</html>
