<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<link rel="stylesheet" type="text/css" href="style_lab4.css">
<head>
	<title>
		Comments Book
	</title>
</head>	
	<body>
	
		<table width ="100%" bgcolor="#adadad">
         <tr>
         <?php
          for($d=1;$d<=7;$d++)
          {
          	echo"<th>".date("l",mktime(0,0,0,07,$d,2021))."</th>"; 
          }
         ?>
         
         </tr> 	
         
             <tr>
         	<?php
         	 $startdate = 1;
         	function numofblanks($f)
            {
             switch($f)
             {
             	case 0:
             	{
             		$blanks = 0;
             		break;
             	}
             	case 1:
             	{
             		$blanks = 1;
             		break;
             	}
             	case 2:
             	{
             		$blanks = 2;
             		break;
             	}
             	case 3:
             	{
             		$blanks = 3;
             		break;
             	}
             	case 4:
             	{
             		$blanks = 4;
             		break;
             	}
             	case 5:
             	{
             		$blanks = 5; 
             		break;
             	}
             	case 6:
             	{
             		$blanks = 6;
             		break;
             	}
             	default:
             	 $blanks = 0;
             }
             return $blanks;
         }
            $blanks = numofblanks($f); 
            
            $remstart = (7-$blanks);
            echo "<br/>";
           
            for($i=0;$i<$blanks;$i++){
              echo "<td>&nbsp</td>";               
            }
            for($j=1;$j<=$remstart;$j++)
	</body>
</html>