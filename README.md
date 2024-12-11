<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Informe Empresarial</title>
    <style>
        /* Estilos básicos para el encabezado */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 10px 20px;
            background-color: #f5f5f5;
            border-bottom: 2px solid #ddd;
        }
        .logo {
            max-width: 120px;
            height: auto;
        }
        .company-info {
            text-align: right; /* Alinea el texto a la derecha */
        }
        .company-name {
            font-size: 20px;
            font-weight: bold;
            color: #333;
        }
        .report-title {
            font-size: 16px;
            color: #555;
        }
        .date {
            font-size: 14px;
            color: #888;
        }
        .gradient-line {
            height: 5px;
            background: linear-gradient(to right, red, blue); /* Línea decorativa */
            margin: 0;
        }
        .center-img {
            display: block;
            margin: 0 auto; /* Centra horizontalmente */
        }
    </style>
</head>
<body>
    <header>
        <img class="logo" src="img/logo-copower-colombia-color.svg" alt="Logo Empresa">
        <div class="company-info">
            <div class="company-name">Innovación y Desarrollo</div>
            <div class="report-title">Hader Cabrera</div>
            <div class="date">29/11/2024 <span id="current-date"></span></div>
        </div>
    </header>
    <div class="gradient-line"></div> <!-- Línea decorativa -->
    <main>
        <figure>
        <figcaption class= "center-text"><i>Setteo del modo de operacion del control de la mixer.</i></figcaption>
        <img src="img/set_mode.svg" alt="diagrama de flujo del modo de operación MIXER" class="center-img" width="600">
        </figure>
    </main>
</body>
</html>
