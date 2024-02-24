function printSelectedValue(actualData, predictedData) {
    // Get the selected value from the dropdown
    var selectedValue = document.getElementById('visualSelector').value;
    var selectedModelValue = document.getElementById('modelSelector').value;

    if (selectedModelValue === '0') {
        console.log("No model selected");
        return; 
    }

    var canvas = document.getElementById('plotCanvas');

    if (selectedValue === '0') {
        canvas.style.backgroundColor = 'red';
        console.log("value 0:", actualData);
    } else if (selectedValue === '1') {
        canvas.style.backgroundColor = 'blue';
        console.log("value 1:", predictedData);
    } else if (selectedValue === '2') {
        canvas.style.backgroundColor = 'green';
        console.log("value 2:");
    }
}
