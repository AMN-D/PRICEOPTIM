var currentChart = null;

function reloadVisualizationDisplay() {
    if (currentChart) {
        currentChart.destroy();
    }
    var canvas = document.getElementById('plotCanvas');
    var ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function pltBarChart(actualData, predictedData) {

    actualData = JSON.parse(actualData);
    predictedData = JSON.parse(predictedData);

    var canvas = document.getElementById('plotCanvas');
    var ctx = canvas.getContext('2d');

    var canvasWidth = 700;
    var canvasHeight = 600;
    canvas.width = canvasWidth;
    canvas.height = canvasHeight;

    var data = {
        labels: actualData.map((value, index) => index), // Assuming index as labels
        datasets: [{
            label: 'Actual Data',
            backgroundColor: 'rgba(207, 170, 1, 0.8)', // Adjust color as needed
            data: actualData
        }, {
            label: 'Predicted Data',
            backgroundColor: 'rgba(226, 226, 226, 0.8)', // Adjust color as needed
            data: predictedData
        }]
    };
    var options = {
        scales: {
            x: {
                type: 'linear',
                position: 'bottom'
            },
            y: {
                type: 'linear',
                position: 'left'
            }
        }
    };

    currentChart = new Chart(ctx, {
        type: 'bar',
        data: data,
        options: options
    });

}

function pltLineplot(actualData, predictedData) {

    actualData = JSON.parse(actualData);
    predictedData = JSON.parse(predictedData);

    var canvas = document.getElementById('plotCanvas');
    var ctx = canvas.getContext('2d');

    var canvasWidth = 700;
    var canvasHeight = 600;
    canvas.width = canvasWidth;
    canvas.height = canvasHeight;

    var data = {
        labels: actualData.map((value, index) => index), 
        datasets: [{
            label: 'Actual Data',
            borderColor: 'rgba(207, 170, 1, 0.8)',
            data: actualData
        }, {
            label: 'Predicted Data',
            borderColor: 'rgba(54, 162, 235, 0.8)',
            data: predictedData
        }]
    };

    var options = {
        scales: {
            x: {
                type: 'linear',
                position: 'bottom'
            },
            y: {
                type: 'linear',
                position: 'left'
            }
        }
    };

    currentChart = new Chart(ctx, {
        type: 'line',
        data: data,
        options: options
    });

}

function pltScatterplot(actualData, predictedData) {
    // Parse actual and predicted data from string to array
    actualData = JSON.parse(actualData);
    predictedData = JSON.parse(predictedData);

    // Get canvas element
    var canvas = document.getElementById('plotCanvas');
    var ctx = canvas.getContext('2d');
    
    var canvasWidth = 700;
    var canvasHeight = 600;
    canvas.width = canvasWidth;
    canvas.height = canvasHeight;
    
    var data = {
        datasets: [{
            label: 'SCATTERPLOT',
            backgroundColor: 'rgba(207, 170, 1, 0.8)',
            data: actualData.map((value, index) => ({ x: value, y: predictedData[index] }))
        }]
    };

    var options = {
        scales: {
            x: {
                type: 'linear',
                position: 'bottom'
            },
            y: {
                type: 'linear',
                position: 'left'
            }
        }
    };

    currentChart = new Chart(ctx, {
        type: 'scatter',
        data: data,
        options: options
    });

}



function printSelectedValue(actualData, predictedData) {
    var selectedValue = document.getElementById('visualSelector').value;
    var selectedModelValue = document.getElementById('modelSelector').value;
    
    reloadVisualizationDisplay();

    if (selectedModelValue === '0') {
        reloadVisualizationDisplay();
        // Trigger a change event on the "visualSelector" element
        const visualSelector = document.getElementById('visualSelector');
        visualSelector.value = '0';
        visualSelector.dispatchEvent(new Event('change'));
    } else {
        switch(selectedValue) {
            case '0':
                console.log("value 0:");
                reloadVisualizationDisplay();
                break;
            case '1':
                pltScatterplot(actualData, predictedData);
                break;
            case '2':
                pltLineplot(actualData, predictedData);
                break;
            case '3':
                pltBarChart(actualData, predictedData);
                break;
            default:
                console.log("Invalid value");
        }
    }
}

