<?php
// https://stackoverflow.com/questions/15699101/get-the-client-ip-address-using-php
function get_client_ip()
{
    $ipaddress = '';
    if (isset($_SERVER['HTTP_CLIENT_IP']))
        $ipaddress = $_SERVER['HTTP_CLIENT_IP'];
    else if (isset($_SERVER['HTTP_X_FORWARDED_FOR']))
        $ipaddress = $_SERVER['HTTP_X_FORWARDED_FOR'];
    else if (isset($_SERVER['HTTP_X_FORWARDED']))
        $ipaddress = $_SERVER['HTTP_X_FORWARDED'];
    else if (isset($_SERVER['HTTP_FORWARDED_FOR']))
        $ipaddress = $_SERVER['HTTP_FORWARDED_FOR'];
    else if (isset($_SERVER['HTTP_FORWARDED']))
        $ipaddress = $_SERVER['HTTP_FORWARDED'];
    else if (isset($_SERVER['REMOTE_ADDR']))
        $ipaddress = $_SERVER['REMOTE_ADDR'];
    else
        $ipaddress = 'UNKNOWN';
    return $ipaddress;
}

?>
<html>

<head></head>

<body>
    <?php
    $ip = get_client_ip();
    if (!str_starts_with($ip, '127.') && $ip !== '0.0.0.0' && $ip !== '::1') {
    ?>
        <h1>Questa pagina è abilitata solo agli utenti locali. Non è accessibile da remoto.</h1>
        <p>Il tuo ip potrebbe essere <?php echo $ip; ?>.</p>
    <?php
    } else {
        echo "<p>Ben fatto! La flag è " . $_ENV['FLAG'] . "</p>";
    }
    ?>
</body>

</html>
