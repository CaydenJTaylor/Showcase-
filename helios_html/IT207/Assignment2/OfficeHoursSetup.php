
<html xmlns="http://www.w3.org/TR/html4/strict.dtd"><head>
<title>Office Hours Setup </title>
<link rel="stylesheet" type="text/css" href="lab2.css"/>
</head>
<body>
<?php include("left_nav.inc");?>
<?php include("menu.inc");?>

<h1>Office Hours Setup Form</h1>
<form method = "post" action="SignUpForm.php"> 
<table style = "width:100%">
	<tr>
	
		<th>Day: </th>
		<th>Monday</th>
		<th>Tuesday</th>
		<th>Wednesday</th>
		<th>Thursday</th>
		<th>Friday</th>
	
	</tr>
    <tr>
    	
    	<td> Time: </td>
    	<td>
    		<select name = "mtime[]"  size= "12" multiple>
    			<option value = "7:00a"> 7:00 am </option>
    			<option value = "7:30a"> 7:30 am </option>
    			<option value = "8:00a"> 8:00 am </option>
                <option value = "8:30a"> 8:30 am </option>
                <option value = "9:00a"> 9:00 am </option>
                <option value = "9:30a"> 9:30 am </option>
                <option value = "10:00a"> 10:00 am </option>
                <option value = "10:30a"> 10:30 am </option>
                <option value = "11:00a"> 11:00 am </option>
                <option value = "11:30a"> 11:30 am </option>
                <option value = "12:00p"> 12:00 pm </option>
                <option value = "12:30p"> 12:30 pm </option>
                <option value = "1:00p"> 1:00 pm </option>
                <option value = "1:30p"> 1:30 pm </option>
                <option value = "2:00p"> 2:00 pm </option>
                <option value = "2:30p"> 2:30 pm </option>
                <option value = "3:00p"> 3:00 pm </option>
                <option value = "3:30p"> 3:30 pm </option>
                <option value = "4:00p"> 4:00 pm </option>
                <option value = "4:30p"> 4:30 pm </option>
				<option value = "5:00p"> 5:00 pm </option>
				<option value = "5:30p"> 5:30 pm </option>
				<option value = "6:00p"> 6:00 pm </option>
				<option value = "6:30p"> 6:30 pm </option>
				<option value = "7:00p"> 7:00 pm </option>
				<option value = "7:30p"> 7:30 pm </option>
				<option value = "8:00p"> 8:00 pm </option>
				<option value = "8:30p"> 8:30 pm </option>
				<option value = "9:00p"> 9:00 pm </option>
				<option value = "9:30p"> 9:30 pm </option>
				<option value = "10:00p"> 10:00 pm </option>
				
    	    </select>
    	</td>
    	<td>
    		<select name = "ttime[]"  size= "12" multiple>
    			<option value = "7:00a"> 7:00 am </option>
    			<option value = "7:30a"> 7:30 am </option>
    			<option value = "8:00a"> 8:00 am </option>
                <option value = "8:30a"> 8:30 am </option>
                <option value = "9:00a"> 9:00 am </option>
                <option value = "9:30a"> 9:30 am </option>
                <option value = "10:00a"> 10:00 am </option>
                <option value = "10:30a"> 10:30 am </option>
                <option value = "11:00a"> 11:00 am </option>
                <option value = "11:30a"> 11:30 am </option>
                <option value = "12:00p"> 12:00 pm </option>
                <option value = "12:30p"> 12:30 pm </option>
                <option value = "1:00p"> 1:00 pm </option>
                <option value = "1:30p"> 1:30 pm </option>
                <option value = "2:00p"> 2:00 pm </option>
                <option value = "2:30p"> 2:30 pm </option>
                <option value = "3:00p"> 3:00 pm </option>
                <option value = "3:30p"> 3:30 pm </option>
                <option value = "4:30p"> 4:00 pm </option>
                <option value = "4:30p"> 4:30 pm </option>
				<option value = "5:00p"> 5:00 pm </option>
				<option value = "5:30p"> 5:30 pm </option>
				<option value = "6:00p"> 6:00 pm </option>
				<option value = "6:30p"> 6:30 pm </option>
				<option value = "7:00p"> 7:00 pm </option>
				<option value = "7:30p"> 7:30 pm </option>
				<option value = "8:00p"> 8:00 pm </option>
				<option value = "8:30p"> 8:30 pm </option>
				<option value = "9:00p"> 9:00 pm </option>
				<option value = "9:30p"> 9:30 pm </option>
				<option value = "10:00p"> 10:00 pm </option>
    	    </select>
    	</td>
    	<td>
    		<select name = "wtime[]"  size= "12" multiple>
    			<option value = "7:00a"> 7:00 am </option>
    			<option value = "7:30a"> 7:30 am </option>
    			<option value = "8:00a"> 8:00 am </option>
                <option value = "8:30a"> 8:30 am </option>
                <option value = "9:00a"> 9:00 am </option>
                <option value = "9:30a"> 9:30 am </option>
                <option value = "10:00a"> 10:00 am </option>
                <option value = "10:30a"> 10:30 am </option>
                <option value = "11:00a"> 11:00 am </option>
                <option value = "11:30a"> 11:30 am </option>
                <option value = "12:00p"> 12:00 pm </option>
                <option value = "12:30p"> 12:30 pm </option>
                <option value = "1:00p"> 1:00 pm </option>
                <option value = "1:30p"> 1:30 pm </option>
                <option value = "2:00p"> 2:00 pm </option>
                <option value = "2:30p"> 2:30 pm </option>
                <option value = "3:00p"> 3:00 pm </option>
                <option value = "3:30p"> 3:30 pm </option>
                <option value = "4:30p"> 4:00 pm </option>
                <option value = "4:30p"> 4:30 pm </option>
				<option value = "5:00p"> 5:00 pm </option>
				<option value = "5:30p"> 5:30 pm </option>
				<option value = "6:00p"> 6:00 pm </option>
				<option value = "6:30p"> 6:30 pm </option>
				<option value = "7:00p"> 7:00 pm </option>
				<option value = "7:30p"> 7:30 pm </option>
				<option value = "8:00p"> 8:00 pm </option>
				<option value = "8:30p"> 8:30 pm </option>
				<option value = "9:00p"> 9:00 pm </option>
				<option value = "9:30p"> 9:30 pm </option>
				<option value = "10:00p"> 10:00 pm </option>
    	    </select>
    	</td>
    	<td>
    		<select name = "rtime[]"  size= "12" multiple>
    			<option value = "7:00a"> 7:00 am </option>
    			<option value = "7:30a"> 7:30 am </option>
    			<option value = "8:00a"> 8:00 am </option>
                <option value = "8:30a"> 8:30 am </option>
                <option value = "9:00a"> 9:00 am </option>
                <option value = "9:30a"> 9:30 am </option>
                <option value = "10:00a"> 10:00 am </option>
                <option value = "10:30a"> 10:30 am </option>
                <option value = "11:00a"> 11:00 am </option>
                <option value = "11:30a"> 11:30 am </option>
                <option value = "12:00p"> 12:00 pm </option>
                <option value = "12:30p"> 12:30 pm </option>
                <option value = "1:00p"> 1:00 pm </option>
                <option value = "1:30p"> 1:30 pm </option>
                <option value = "2:00p"> 2:00 pm </option>
                <option value = "2:30p"> 2:30 pm </option>
                <option value = "3:00p"> 3:00 pm </option>
                <option value = "3:30p"> 3:30 pm </option>
                <option value = "4:30p"> 4:00 pm </option>
                <option value = "4:30p"> 4:30 pm </option>
				<option value = "5:00p"> 5:00 pm </option>
				<option value = "5:30p"> 5:30 pm </option>
				<option value = "6:00p"> 6:00 pm </option>
				<option value = "6:30p"> 6:30 pm </option>
				<option value = "7:00p"> 7:00 pm </option>
				<option value = "7:30p"> 7:30 pm </option>
				<option value = "8:00p"> 8:00 pm </option>
				<option value = "8:30p"> 8:30 pm </option>
				<option value = "9:00p"> 9:00 pm </option>
				<option value = "9:30p"> 9:30 pm </option>
				<option value = "10:00p"> 10:00 pm </option>
    	    </select>
    	</td>
    	<td>
    		<select name = "ftime[]"  size= "12" multiple>
    			<option value = "7:00a"> 7:00 am </option>
    			<option value = "7:30a"> 7:30 am </option>
    			<option value = "8:00a"> 8:00 am </option>
                <option value = "8:30a"> 8:30 am </option>
                <option value = "9:00a"> 9:00 am </option>
                <option value = "9:30a"> 9:30 am </option>
                <option value = "10:00a"> 10:00 am </option>
                <option value = "10:30a"> 10:30 am </option>
                <option value = "11:00a"> 11:00 am </option>
                <option value = "11:30a"> 11:30 am </option>
                <option value = "12:00p"> 12:00 pm </option>
                <option value = "12:30p"> 12:30 pm </option>
                <option value = "1:00p"> 1:00 pm </option>
                <option value = "1:30p"> 1:30 pm </option>
                <option value = "2:00p"> 2:00 pm </option>
                <option value = "2:30p"> 2:30 pm </option>
                <option value = "3:00p"> 3:00 pm </option>
                <option value = "3:30p"> 3:30 pm </option>
                <option value = "4:30p"> 4:00 pm </option>
                <option value = "4:30p"> 4:30 pm </option>
				<option value = "5:00p"> 5:00 pm </option>
				<option value = "5:30p"> 5:30 pm </option>
				<option value = "6:00p"> 6:00 pm </option>
				<option value = "6:30p"> 6:30 pm </option>
				<option value = "7:00p"> 7:00 pm </option>
				<option value = "7:30p"> 7:30 pm </option>
				<option value = "8:00p"> 8:00 pm </option>
				<option value = "8:30p"> 8:30 pm </option>
				<option value = "9:00p"> 9:00 pm </option>
				<option value = "9:30p"> 9:30 pm </option>
				<option value = "10:00p"> 10:00 pm </option>
    	    </select>
    	</td>
     </tr>
     </table>
     <input type= submit value = submit> 
	 


</form>

<?php include("footer.inc");?>

	</body>
</html>