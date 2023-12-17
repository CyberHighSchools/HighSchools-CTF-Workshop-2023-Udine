<?php
header("Content-Type: application/json");
$admin = new stdClass();
$admin->username = base64_encode($_ENV['ADMIN_USERNAME']);
$admin->password = base64_encode($_ENV['ADMIN_PASSWORD']);
echo json_encode([$admin]);




