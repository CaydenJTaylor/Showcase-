
<html xmlns="http://www.w3.org/TR/html4/strict.dtd"><head>
<title>Lab 1 </title>
<link rel="stylesheet" type="text/css" href="style_lab1.css">
</head>
<body>
<?php include("left_nav.inc");?>
<?php include("menu.inc");?>

<!--<form action="finalgrade.php" method="post">-->
<form action="FinalGrade.php" method="post">
			<h3>Participation</h3>
			Earned: <input type="text" name="earnedParticipation" />
			Max: <input type="text" name="maxParticipation" />
			Weight (percentage): <input type="text" name="weightParticipation" />
			<h3>Quizzes</h3>
			Earned: <input type="text" name="earnedQuiz" />
			Max: <input type="text" name="maxQuiz" />
			Weight (percentage): <input type="text" name="weightQuiz" />
			<h3>Lab Assignments</h3>
			Earned: <input type="text" name="earnedLab" />
			Max: <input type="text" name="maxLab" />
			Weight (percentage): <input type="text" name="weightLab" />
			<h3>Practica</h3>
			Earned: <input type="text" name="earnedPracticum" />
			Max: <input type="text" name="maxPracticum" />
			Weight (percentage): <input type="text" name="weightPracticum" />
			<br /><br />
			<input type="submit" />
		</form>
		
<?php
if (isset($_POST['PEarned']))
{
include('FinalGrade.php');
}
?>

<?php include("footer.inc");?>

	</body>
</html>