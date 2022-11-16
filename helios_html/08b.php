<html>
 <head>
 <title>08b</title>
 </head>
 <body>
 <?php

 (int) $GPA == 3.72;
 (string) $str1 = "I have a $GPA GPA";
 (string) $str2 = "I have a 3.72 GPA";

 if(strcasecmp( $str1, $str2)> 0)
 {
 echo "the first statement is larger than the second one";
 } else {
 echo "the second statement is larger than the first one";
 }
 ?>
 </body>
</html>