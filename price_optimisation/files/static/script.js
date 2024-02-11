var ctx, data, options;

function reloadVisualizationDisplay() {
    var visualizationDisplay = document.querySelector('.visualization-display');
    visualizationDisplay.innerHTML = ''; // Clear the content
    document.getElementById('visualization-btn').textContent = "Stand by ▼";
}

function data(actualData, predictedData) {
    data = {
        datasets: [{
            label: 'Plot',
            backgroundColor: 'rgba(255, 99, 132, 0.5)', // Adjust color as needed
            data: actualData.map((value, index) => ({ x: value, y: predictedData[index] }))
        }]
    };
    options = {
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
}

function showScatterPlot(actualData, predictedData) {
    data(actualData, predictedData); // Call data() to populate the data variable
    ctx = document.getElementById('PlotCanvas').getContext('2d');
    var scatterPlot = new Chart(ctx, {
        type: 'scatter',
        data: data,
        options: options
    });
    document.getElementById('visualization-btn').textContent = "Scatter Plot ▼";
}

function showLinePlot(actualData, predictedData) {
    data()
    var linePlot = new Chart(ctx, {
        type: 'line',
        data: data,
        options: options
    });
    document.getElementById('visualization-btn').textContent = "Line Plot ▼";
}

