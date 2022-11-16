<html xmlns="http://www.w3.org/TR/html4/strict.dtd"><head>
<title>Final Grade</title>
<link rel="stylesheet" type="text/css" href="style_lab1.css">
</head>
<body>
<?php include("left_nav.inc");?>
<?php include("menu.inc");?>

<?php
if (isset($_POST['PEarned']))
 {if ( !empty($_POST['PEarned']))
 {if ( !empty($_POST['PMax']))
 {if ( !empty($_POST['PWeight']))
 {if ( !
empty($_POST['quizEarned']))
 {if ( !
empty($_POST['quizMax']))
 {if ( !
empty($_POST['quizWeight']))
 {if ( !
empty($_POST['pracEarned']))
 {if ( !
empty($_POST['pracMax']))
 {if ( !
empty($_POST['pracWeight']))
 {

$earn[] = $_POST['PEarned'];
$max[] = $_POST['PMax'];
$weight[] = $_POST['PWeight'];

$earn[] = $_POST['quizEarned'];
$max[] = $_POST['quizMax'];
$weight[] = $_POST['quizWeight'];

$earn[] = $_POST['pracEarned'];
$max[] = $_POST['pracMax'];
$weight[] = $_POST['pracWeight'];

function calculateGradeEarned($earned, $gradeMax){
	$result = $earned/$gradeMax;
	$gradeEarned = $result *100;
	return $gradeEarned;
}
function weightCalculation($grade, $gradeWeight){
	$resultofWeight = (($grade*$gradeWeight)/100);
	return $resultofWeight;
}
for ($x = 0; $x < 4; $x++){
	$gradeCalculation[$x] = calculateGradeEarned($earned[$x],$max[$x]);
}
for ($x = 0; $x < 4; $x++){
	$weightValue[] = weightCalculation($gradeCalculation[$x],$weight[$x]);
}
for($x = 0; $x < 4; $x++){
	echo "<p> You earned a ",round($gradeCalculation[$x],2),"%","for the",$AssignmentNames[$x],",with a weighted value of",$weightedValue[$x],"%.</p>";
}
$TheFinalGrade = 0;
for($x = 0; $x < 4; $x++){
	$TheFinalGrade += $weightedValue[$x];
}
echo "<br>Your Final Grade is a ", round($TheFinalGrade,2),"%,which is a";
echo $TheGrade = ((
($TheFinalGrade >= 97)? 'n A+.':
(($TheFinalGrade >=93 and $TheFinalGrade < 97)? ' A.':
(($TheFinalGrade >=90 and $TheFinalGrade < 93)? ' A-.':
(($TheFinalGrade >=87 and $TheFinalGrade < 90)? ' B+.':
(($TheFinalGrade >=83 and $TheFinalGrade < 87)? ' B.':
(($TheFinalGrade >=80 and $TheFinalGrade < 83)? ' B-.':
(($TheFinalGrade >=77 and $TheFinalGrade < 80)? ' C+.':
(($TheFinalGrade >=73 and $TheFinalGrade < 77)? ' C.':
(($TheFinalGrade >=70 and $TheFinalGrade < 73)? ' C-.':
(($TheFinalGrade >=60 and $TheFinalGrade < 70)? ' D.':
(($TheFinalGrade >=0 and $TheFinalGrade < 60)? ' F.':
?>								


<?php include("footer.inc");?>

</body>
</html>