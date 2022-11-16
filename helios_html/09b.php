<html>
 <head>
 <title>09b</title>
 </head>
 <body>
 <?php

$row = 1;
if (($reader = fopen("09b.csv", "r")) !== FALSE) {
while (($content = fgetcsv($reader, 1000, ",")) !== FALSE) {
$num = count($content);
echo "<p> $num elements in row $row: <br /></p>\n";
$row++;
for ($i=0; $i < $num; $i++) {
echo $content[$i] . "<br />\n";
}
}
fclose($reader);
}

?>
 </body>
</html>