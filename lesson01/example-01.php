<html>
<head></head>
<body>
<?php
//the location of the remote data
$url = "http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol=goog";

//Use server-side scripting to get data from a remote server using cURL
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 5);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);//danger
$data = curl_exec($ch); //opens the remote url and loads the response into $data


$result = array();
if ($data === FALSE) {
    //curl failed
} else {
    //the data is in JSON format, call json_decode to convert the data into an array of values
    $result = json_decode($data);
}
?>
<h1>This will do a one time load</h1>
<div><?php echo "$result->Name"; ?></div>
<div><?php echo "$result->LastPrice"; ?></div>
</body>
