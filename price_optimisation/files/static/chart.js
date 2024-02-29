var currentChart = null;

function reloadVisualizationDisplay() {
    if (currentChart) {
        currentChart.destroy();
    }
    var canvas = document.getElementById('plotCanvas');
    var ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function pltBarChart(actualData, predictedData, parentContainerClass) {

    actualData = JSON.parse(actualData);
    predictedData = JSON.parse(predictedData);

    var canvas = document.getElementById('plotCanvas');
    var parentContainer = document.querySelector('.' + parentContainerClass);

    canvas.width = parentContainer.offsetWidth;
    canvas.height = parentContainer.offsetHeight;

    var ctx = canvas.getContext('2d');

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

function pltLineplot(actualData, predictedData, parentContainerClass) {

    actualData = JSON.parse(actualData);
    predictedData = JSON.parse(predictedData);

    var canvas = document.getElementById('plotCanvas');
    var parentContainer = document.querySelector('.' + parentContainerClass);

    canvas.width = parentContainer.offsetWidth;
    canvas.height = parentContainer.offsetHeight;
    
    var ctx = canvas.getContext('2d');

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

function pltScatterplot(actualData, predictedData, parentContainerClass) {
    // Parse actual and predicted data from string to array
    actualData = JSON.parse(actualData);
    predictedData = JSON.parse(predictedData);

    // Get canvas element
    var canvas = document.getElementById('plotCanvas');
    var parentContainer = document.querySelector('.' + parentContainerClass);

    canvas.width = parentContainer.offsetWidth;
    canvas.height = parentContainer.offsetHeight;

    var ctx = canvas.getContext('2d');
    
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
                pltScatterplot(actualData, predictedData, 'body-main-anal-canvas');
                break;
            case '2':
                pltLineplot(actualData, predictedData, 'body-main-anal-canvas');
                break;
            case '3':
                pltBarChart(actualData, predictedData, 'body-main-anal-canvas');
                break;
            default:
                console.log("Invalid value");
        }
    }
}

