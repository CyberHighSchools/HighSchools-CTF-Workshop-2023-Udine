<?php
$username = $_COOKIE['username'];
$password = $_COOKIE['password'];

if (!isset($username) || !isset($password) || $username !== $_ENV['ADMIN_USERNAME'] || $password !== $_ENV['ADMIN_PASSWORD']) {
    header('Location: /login.php');
} else {
    $logged = 1;
}

?>
<html>

<head>
    <title>Advanced authentication System</title>
    <link rel="stylesheet" href="static/css/main.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body>
    <div class="box">
        <?php
        echo '<p name="flag">Ho tenuto la flag al sicuro per te:';
        if ($logged == 1)
            echo $_ENV['FLAG'];
        echo "</p>";
        ?>
    </div>
</body>

</html>
