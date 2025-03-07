<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Welcome Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        .container {
            text-align: center;
        }
        h1 {
            color: #333;
        }
        p {
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>It works!</h1>
        <p>
            <?php
                $version = phpversion();
                $major_minor_version = implode('.', array_slice(explode('.', $version), 0, 2));
                echo "PHP Version: " . $major_minor_version;
            ?>
        </p>
    </div>
</body>
</html>
