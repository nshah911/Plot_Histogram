<!DOCTYPE html>
<html>
<body>

<?php
$dir = "C:/xampp/htdocs/PHP/" . $_GET['dirname'] ."/";
$reldir = "/PHP/" . $_GET['dirname'] ."";

$image = glob($reldir. "*.png");
#$dir = $dir. $_GET['dirpath'] . "/";


if($opendir = opendir($dir)){
	while(($file = readdir($opendir))!== FALSE)
	{
		if($file!="."&&$file!=".." && strstr($file,".png")){
//			$reldir = $reldir . $file;
			echo "<img src = $reldir/$file><br>";
		}
	}
}
?>
</body>
</html>