<?php

if (isset($_POST['submit'])){

$name = $_FILES['fileToUpload']['name'];
$allowed_file_types = array('.csv','.xlsx');
$file_basename = substr($name,0,strripos($name,'.'));
$file_ext = substr($name,strripos($name,'.'));
$filesize = $_FILES["fileToUpload"]["size"];
$tmp_name =$_FILES["fileToUpload"]["tmp_name"];

$random =  rand();
$strinrand = strval($random) ;

mkdir($strinrand);





if(in_array($file_ext,$allowed_file_types))
{
#	$newfilename = md5($file_basename).$file_ext;
	$location = "C:/xampp/htdocs/PHP/".strval($random)."/";
#	if (file_exists("C:/xampp/htdocs/PHP/" . $name))
#		{
#			// file already exists error
#			echo "You have already uploaded this file.";
#		}

#	else{
if(move_uploaded_file($tmp_name,$location.$file_basename.".csv")){
	

		echo "File successfully uploaded";}
	
	}
	elseif (empty($file_basename))
	{	
		echo "Please select a file to upload.";
	} 
	
#	else
#	{
		
#		echo "Only these file typs are allowed for upload: " . implode(', ',$allowed_file_types);
#		unlink($_FILES["fileToUpload"]["tmp_name"]);
#	}
 $commandline = "C:/Python27/python.exe C:/xampp/htdocs/PHP/readfile.py ";
 $commandline = $commandline.$random;
 $command = exec ( $commandline );
#$command = exec("C:/Users/desai_s/AppData/Local/Programs/Python/Python35-32/python.exe C:/xampp/htdocs/PHP/readfile.py .$random");
 $url = "Location: /PHP/Plot.php?dirname=";
 $url = $url.$random;
 header($url);
#echo $command;
#$output = shell_exec($command.$random);
#echo $output;
#}
#if (isset($_POST['submit1'])){
#header("Content-disposition: attachment; filename = C:/xampp/htdocs/PHP/Download/.png");
#header("Content-type: application/png");
#readfile("C:/xampp/htdocs/PHP/Download/.png");
#header("C:/xampp/htdocs/PHP/Download/.png");
}
?>
<!DOCTYPE html>
<html>
<body>

<form action="newfile.php" method="POST" enctype="multipart/form-data">
    <input type="file" name="fileToUpload" id="fileToUpload">
    <input type="submit" value="Upload File" name="submit"><br/>

	
    <!--<a href="http://localhost/PHP/pictures.php">pictures</a><br/> -->
  	<!--<a href="newfile.php" download>download</a> -->
</form>

</body>
</html>