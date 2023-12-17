<!DOCTYPE html>
<html>

<head>
    <title>Sistema di autenticazione avanzato</title>
    <script src="static/js/main.js"></script>
    <link rel="stylesheet" href="static/css/main.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body>
    <div class="box">
        <p>Effettua l'accesso per avere la flag.</p>
        <form class="login-form" action="javascript:submit();">
            <span class="login-form-item">
                <label for="username">Nome utente</label>
                <input id="username" type="text" name="username" placeholder="Username" />
            </span>
            <span class="login-form-item">
                <label for="password">Password</label>
                <input id="password" type="password" name="password" placeholder="********" />
            </span>
            <input class="login-form-item" type="submit" value="Accedi" />
        </form>
    </div>
</body>

</html>
