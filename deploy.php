<?php
// Este script executa o git pull automaticamente
// Você deve configurar isso no Webhook do seu GitHub
$output = shell_exec('git pull origin main 2>&1');
echo "<pre>$output</pre>";
?>