<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<title>
		Office Hours Sign Up
	</title>
<link rel="stylesheet" type="text/css" href="lab2.css"/>
</head>
	<body>
	<?php include("left_nav.inc");?>
<?php include("menu.inc");?>
		<h1> Office Hours Signup Form</h1>
		<?php
         date_default_timezone_set('America/New_York');           
         $d = mktime(0,0,0,date("m"),1,date("Y"));   
         $f= date("w",$d);                       
         echo "<br/>";
         $n = date("t");                          
         ?>
		  <form method = "post" action = "SignUpForm.php">
			<input type = "text" name = "name" center>Student name
			<input type = "text" name = "email" center>Email 
			<br/><br/>
			<input type = "submit" value = "submit">
		 
		 <br/>
        <?php
        function artime($dow){
        switch($dow)
                 	{
                      case 1:
                         $officetime = "mtime"; 
                         break;
                      case 2:
                        $officetime = "ttime"; 
                         break;
                      case 3:
                        $officetime = "wtime"; 
                         break;
                      case 4:
                        $officetime = "rtime"; 
                         break;
                      case 5:
                       $officetime = "ftime"; 
                         break;
                      default:
                        $officetime = " ";                
                    }
                    return $officetime;
                }

        ?>
	    <?php
	        if(!empty($_POST['time']))
	        	$time = $_POST['time'];
	        if(!empty($_POST['name']))
	        	$name = $_POST['name'];
		    if (!empty($_POST['email']))
		    $email = "Email successfully sent from " . $_POST['email'];
		    if (!empty($email))
			echo $email;
		    echo "<h1><b>" .date("F",$d)."&nbsp".date("Y",$d)."</h1></b>" ; 
			mail('dgarriso@gmu.edu','Office Hours',$officetime,$name );
	    ?>
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
            {
                                      
                 $dow= date("w",mktime(0,0,0,date("m"),$startdate,date("Y"))); 
                
                 echo "<td valign = top >".($startdate)."<br/>"; 
                 $officetime = artime($dow);       

                if (!empty($_POST["$officetime"]))
                {
                foreach ($_POST["$officetime"]  as $x)
                {
                  
                
                if (isset($time) && ("$startdate".$x == $time))
                    {
                    echo "$x --". $name. "<br />";}
                  else
   
                    {echo '<input type= radio multiple name = time value= "'."$startdate".$x.'" />'. $x. '<br />'; }
                  echo "<input type= hidden name=  $officetime"."[]"." value= $x />";

                 }
               }
               
               echo "</td>";
               $startdate++;
            }  
            ?> 
             </tr>

    
             <?php
             for($row=1;$row<=6;$row++)
            {
              echo "<tr>";

              for($col=1;$col<=7;$col++)
              {
              	 $dow= date("w",mktime(0,0,0,date("m"),$startdate,date("Y")));
               echo "<td valign = top>".($startdate)."<br/>";
               $officetime = artime($dow);
                if (!empty($_POST["$officetime"]))
                {
                foreach ($_POST["$officetime"]  as $x){
                  if (isset($time) &&("$startdate".$x == $time) )
                    echo "$x --".$name."<br />";
                  else
                    echo '<input type= radio multiple name = time value= "'."$startdate".$x.'" />'. $x. '<br />';
                 }
               }

               echo"</td>";
               $startdate++;
               if($startdate==$n)
              	break;
              }
              echo "</tr>";
              if($startdate==$n)
              	break;
            }
         	?>
         
	    </table> 
         </form>
		 <?php include("footer.inc");?>
	</body>

</html>