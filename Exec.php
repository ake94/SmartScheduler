
	
<?php header('Content-Type: text/plain');


$output = shell_exec("python event_scheduler.py");
$fp = fopen('data1.txt', 'w');
fwrite($fp,$output);
fclose($fp);
echo file_get_contents('eventSchedule.txt');

?>
	

