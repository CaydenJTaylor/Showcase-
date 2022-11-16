			<div class="footer"> <!--Footer-->
			
				<!--#include virtual="footer.inc"-->
				<p>"This web site is entirely original work and full academic copyright is retained. This web site complies with the Mason Honor Code <a href="https://oai.gmu.edu/mason-honor-code/">GMU honor-code/</a></p>
				<p><?php
date_default_timezone_set('EST');
date_default_timezone_set('America/New_York');
// outputs e.g. 'Last modified: March 04 1998 20:43:59.'
echo "Last modified: " . date ("F d Y h:m:s A", getlastmod());
?></p>
			</div> <!--Footer Closing-->