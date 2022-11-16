<!DOCTYPE html PUBLIC
"-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<link rel="stylesheet" type="text/css" href="pracstyle.css" />
<?php
define('BUS_CAPACITY', 30);
define('CAR_CAPACITY', 4);

$passengers = @$_POST['passengers'];

function display_option($number) {
    $string = "";
    for ($i = 0; $i < $number; $i++) {
        $string .= "o ";
    }
    return $string;
}
?>
<form action='./passengers.php' method='post'>
    <div class="labp1-outer-box">
       
            <?php echo $passengers ? "Passenger Distribution" : "Passenger Distribution Results"; ?>
        <div class="labp1-inner-box">
            <div class="labp1-inner-box-content">
                <br />
                <?php if ($passengers) {
                    echo "<p>$passengers passengers need transportation:</p>";
                    $bus_ontake = round($passengers/BUS_CAPACITY, 2) % 10;
                    $left_over = $passengers % BUS_CAPACITY;
                    $car_ontake = round($left_over/CAR_CAPACITY, 2) % 10;
                    $left_over = $left_over % CAR_CAPACITY;
                    echo "<p>$bus_ontake Busses Needed</p>";
                    echo display_option($bus_ontake);
                    echo "<p>$car_ontake Cars Needed</p>";
                    echo display_option($car_ontake);
                    echo "<p>$left_over Passengers left over</p>";
                    echo display_option($left_over);
                } else { ?>
                    <span>Total Number of Passengers:</span>
                    <input type="text" name="passengers" />
                    <br />
                <?php } ?>
                <br />
            </div>
        </div>
        <?php
        if ($passengers) {
            echo "<p>Legend: Passengers per Bus = 30 | per Car = 4</p>";
        }
        else {
            echo "<input type='submit' />";
        }
        ?>
    </div>
</form>
<br />
<br />
<?php
if ($passengers) {
    echo "<p>", date("H:i M d, Y T", getlastmod()), " | <a href='./passengers.php'>Return to form page</a></p>";
}
else {
    echo "<p><a href='./prac.php'>Proceed to part 1</a></p>";
}
?>
</body>
	</html>