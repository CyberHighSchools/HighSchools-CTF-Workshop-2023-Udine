<?php
    if(isset($_GET['path']) && is_string($_GET['path'])){
        $path = realpath($_GET['path']);
        header('Content-Type: image/jpg');
        readfile($path);
    }
