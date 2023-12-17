<?php
$themes = array(
    "christmas" => (object)array("background" => "public/christmas.jpg", "color" => "green"),
    "pizza" => (object)array("background" => "public/pizza.jpg", "color" => "red"),
);
// Defaults for session
$auth = False;
$theme = $themes['christmas'];

$session_data = new stdClass();
$session_data->theme = $theme;
$session_data->auth = $auth;

// Encryption function: XOR
function enc($key, $data)
{
    $times = ceil(strlen($data) / strlen($key));
    $secret = str_repeat($key, $times); // Since the key is short
    $result = '';
    for ($i = 0; $i < strlen($data); ++$i) {
        $result = $result . ($data[$i] ^ $secret[$i]);
    }
    return $result;
}

function saveConf($data)
{
    setrawcookie('session', base64_encode(enc($_ENV['KEY'], json_encode($data))));
}
function loadConf()
{
    return json_decode(enc($_ENV['KEY'], base64_decode($_COOKIE['session'])));
}

// Load existing conf or save default if necessary
if (isset($_COOKIE['session'])) {
    $session_data = loadConf();
} else {
    saveConf($session_data);
}

// Update if necessary
if (isset($_GET['theme']) && array_key_exists($_GET['theme'], $themes)) {
    $session_data->theme = $themes[$_GET['theme']];
    saveConf($session_data);
}
?>
<html>

<head>
    <title>Challenge a tema</title>
    <style>
        body {
            background-image: url("<?php echo $session_data->theme->background; ?>");
        }

        h1 {
            color: <?php echo $session_data->theme->color; ?>;
        }

        .main {
            margin: 20vh 30vw;
            background-color: #dedede;
            text-align: center;
            border: 2px solid black;
            border-radius: 5px;
        }

        button {
            width: 200px;
            height: 50px;
            color: white;
            background-color: <?php echo $session_data->theme->color; ?>;
            border: 0px;
            border-radius: 0px;
        }
    </style>
</head>

<body>
    <div class="main">
        <h1>Bevenuto!</h1>
        <p>Scegli il tuo tema preferito</p>
        <span>
            <button onClick="document.location='/?theme=christmas';">Natale</button>
            <button onClick="document.location='/?theme=pizza';">Pizza</button>
        </span>
        <p> <!-- p as in padding -->
            <?php
            if ($session_data->auth) {
                echo "Ben fatto, ecco la flag " . $_ENV['FLAG'];
            }
            ?>
        </p>
    </div>
</body>

</html>
