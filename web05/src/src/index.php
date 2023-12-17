<html>

<head>
    <title>Cat gallery</title>
    <link rel="stylesheet" href="css/main.css">
</head>

<body>
    <div class="title">
        <h1>Benvenuto in cat gallery!</h1>
        <p>Ecco alcuni gatti</p>
    </div>
    <div id="cats" class="cats">
        <img src="/serve_file.php?path=gallery/1.jpg">
        <img src="/serve_file.php?path=gallery/2.jpg">
        <img src="/serve_file.php?path=gallery/3.jpg">
        <img src="/serve_file.php?path=gallery/4.jpg">
        <img src="/serve_file.php?path=gallery/5.jpg">
        <img src="/serve_file.php?path=gallery/6.jpg">
        <img src="/serve_file.php?path=gallery/7.jpg">
        <img src="/serve_file.php?path=gallery/8.jpg">
        <img src="/serve_file.php?path=gallery/9.jpg">
        <img src="/serve_file.php?path=gallery/10.jpg">
    </div>
    <script>
        window.addEventListener('load', () => {
            let direction = 1;
            let step = 1;
            self.setInterval(() => {
                const flavoursContainer = document.getElementById('cats');
                const flavoursScrollWidth = flavoursContainer.scrollWidth;
                console.log({
                    direction
                }, flavoursContainer.scrollLeft, flavoursContainer.scrollWidth);
                if (direction == 1 && (flavoursContainer.scrollLeft + window.innerWidth + step) >= flavoursScrollWidth)
                    direction = -1;
                if (direction == -1 && flavoursContainer.scrollLeft - step <= 0)
                    direction = 1;
                flavoursContainer.scrollBy(step * direction, 0);
            }, 15);
        });
    </script>
</body>

</html>
