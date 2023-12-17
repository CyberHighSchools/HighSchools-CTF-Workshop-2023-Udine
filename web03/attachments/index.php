<?php
$themes = array(
    "christmas" => (object)array("background" => "public/christmas.jpg", "color" => "red"),
    "pizza" => (object)array("background" => "public/pizza.jpg", "color" => "green"),
);

// Valori di default per la sessione
$auth = False;
$theme = $themes['christmas'];

$session_data = new stdClass();
$session_data->theme = $theme;
$session_data->auth = $auth;

// Funzione di cifratura
function enc($key, $data)
{
    $times = ceil(strlen($data) / strlen($key));
    $secret = str_repeat($key, $times); // Ripeti la chiave per tutti i dati
    $result = '';
    for ($i = 0; $i < strlen($data); ++$i) {
        $result = $result . ($data[$i] ^ $secret[$i]);
    }
    return $result;
}

function saveConf($data)
{
    setCookie('session', base64_encode(enc($_ENV['KEY'], json_encode($data))));
}
function loadConf()
{
    return json_decode(enc($_ENV['KEY'], base64_decode($_COOKIE['session'])));
}

// Carica la configurazione o salvala se non esiste
if (isset($_COOKIE['session'])) {
    $session_data = loadConf();
} else {
    saveConf($session_data);
}

// Aggiorna la configurazione se necessario
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
        <p>
            <?php
            if ($session_data->auth) {
                echo "Ben fatto, ecco la flag " . $_ENV['FLAG'];
            }
            ?>
        </p>
    </div>
</body>

</html>
