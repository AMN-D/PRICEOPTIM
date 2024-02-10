
function generateRandomGradientColor() {
    console.log("Function called!")
    // Generate random color values for red, green, and blue components
    var r1 = Math.floor(Math.random() * 256);
    var g1 = Math.floor(Math.random() * 256);
    var b1 = Math.floor(Math.random() * 256);
    var r2 = Math.floor(Math.random() * 256);
    var g2 = Math.floor(Math.random() * 256);
    var b2 = Math.floor(Math.random() * 256);

    // Generate CSS gradient string
    var gradientColor = "linear-gradient(to right, rgb(" + r1 + "," + g1 + "," + b1 + "), rgb(" + r2 + "," + g2 + "," + b2 + "))";

    // Apply the gradient color to the .color-box element
    document.querySelector('.color-box').style.background = gradientColor;
}

// Call the function to generate a random gradient color
generateRandomGradientColor();