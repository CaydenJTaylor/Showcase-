
<html xmlns="http://www.w3.org/TR/html4/strict.dtd"><head>
<title>Practice Lab </title>
<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>

	<div class="page"> <!--Whole page-->
		<div class="navigation"> <!--Left Navigation-->
			<!--#include virtual="menu.inc"-->
				<h3>
	</h3>
	
	<h3>Assignments</h3>
	<ul>
		<li><a href="http://helios.ite.gmu.edu/~ctaylo50/IT207/Assignment1/Lab1.php">Assignment 1 </a></li>
		<li><a href="http://helios.ite.gmu.edu/~ctaylo50/IT207/Assignment2/OfficeHoursSetup.php">Assignment 2 </a></li>
		<li><a href="http://helios.ite.gmu.edu/~ctaylo50/IT207/Assignment3">Assignment 3 </a></li>
		<li><a href="http://helios.ite.gmu.edu/~ctaylo50/IT207/Assignment4">Assignment 4 </a></li>
	</ul>
	<h3>Lab Practica</h3>
	<ul>
		<li><a href="http://helios.ite.gmu.edu/~ctaylo50/IT207/Practium1">Practicum 1</a></li>
		<li><a href="http://helios.ite.gmu.edu/~ctaylo50/IT207/Practium2">Practicum 2</a></li>
	</ul>
		</div> <!--Left Navigation Closing-->
		
		<div class="allcontent"> <!--Other part other than navigation-->
			
			<div class="header"> <!--Header-->
			
				
				<!--#include virtual="header.inc"-->
								<div class="leftheader"> <!-- Left Header-->
					<p>
					</p><div class="headingfont">
					IT 207-DL3 Fall 2021 </div>
					Daniel Garrison<br>
					George Mason university
					<br>
										<p></p>
				
				</div> <!--Left Header Closing-->
				
				<div class="rightheader"> <!--Right Header-->
				
					<p>
					</p><div class="headingfont"><?php
					echo "Cayden Taylor";
					?></div>
					<a href="mailto:ctaylo50@gmu.edu">ctaylo50@gmu.edu</a><br>
					<?php
						echo date("l jS \of F Y h:i:s A");
					
					?>

					<br>
														
										<p></p>
				
				</div> <!--Right Header Closing-->
				
			</div> <!--Header closing-->
			
			<div class="maincontent"> <!--Content-->
			
				<div class="leftcontent"> <!--homepage left partition-->
				
					<div class="picture"> <!--Photo-->
					
						<img src="CaydenPic.jpg" alt="Pic of Cayden" style="width:100%;height:100%;">
						
					</div> <!--Photo close-->
					<div class="personal_academic"> <!--Summary-->
					
							<h3><?php
$LeftHeader= "Summary";
echo "<p>$LeftHeader";
?></h3>
							<ul>
							<li>Personal
								<ul>
								<li>Born in Spotsylvania, VA </li>
								<li>Lived in the United States my whole life </li>
								<li>Currently live in Fredericksburg, VA </li>
								</ul>
							</li>
							
							<li> Academic
								<ul>
									<li>Finished high School in Fredericksburg, VA at Courtland HighSchool</li>
									<li>Associates degree in General Studies at Germanna Community College</li>
									<li>Looking to gain Bachelors in IT with Security concentration from George Mason University</li>
								</ul>
							</li>
							</ul>
					
					</div> <!--Summary Closing-->
					
				</div> <!--homepage left partition Closing-->
				
				<div class="rightcontent"> <!--homepage right partition Professional and Personal Details-->
				
					
					<h3><p><?php
$RightHeader= "Professional and Personal Details";
echo "<p>$RightHeader";
?></p></h3>
					<p><?php
					echo "I am currently a Junior at George Mason University looking to gain my bachelors degree in Information Technology.I currently work at best buy part time until my IT intersnhip in the summer."
				?>
					<br>
					</p><p><?php
					echo "In my free time I like to play and watch sports with my friends and I also am big into video games. I'm also very big into fitness so, another thing I like to do in my free time is go to the gym."
				?>
					</p>
				
				</div> <!--homepage right partition closing-->
				
			</div> <!--Content Closing-->
			
			<div class="footer"> <!--Footer-->
			
				<!--#include virtual="footer.inc"-->
				<p>"This web site is entirely original work and full academic copyright is retained. This web site complies with the Mason Honor Code <a href="https://oai.gmu.edu/mason-honor-code/">GMU honor-code/</a></p>
				<p><?php
// outputs e.g. 'Last modified: March 04 1998 20:43:59.'
echo "Last modified: " . date ("F d Y H:i:s.", getlastmod());
?></p>
			</div> <!--Footer Closing-->
		</div> <!--content closing-->
		
		
	</div> <!--page closing-->

</body>
</html>