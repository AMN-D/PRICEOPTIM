var currentChart = null;

function reloadVisualizationDisplay() {
    if (currentChart) {
        currentChart.destroy();
    }
    var canvas = document.getElementById('PlotCanvas');
    var ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function showScatterPlot(actualData, predictedData) {
    reloadVisualizationDisplay();
    var ctx = document.getElementById('PlotCanvas').getContext('2d');
    var data = {
        datasets: [{
            label: 'Scatter Plot',
            backgroundColor: 'rgba(255, 99, 132, 1)', // Adjust color as needed
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
    document.getElementById('visualization-btn').textContent = "Scatter Plot ▼";
}

function showLinePlot(actualData, predictedData) {
    reloadVisualizationDisplay();
    var ctx = document.getElementById('PlotCanvas').getContext('2d');
    var data = {
        labels: actualData.map((value, index) => index), // Assuming index as labels
        datasets: [{
            label: 'Actual Data',
            borderColor: 'rgba(255, 99, 132, 1)',
            data: actualData
        }, {
            label: 'Predicted Data',
            borderColor: 'rgba(54, 162, 235, 1)',
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
    document.getElementById('visualization-btn').textContent = "Line Plot ▼";
}

function showBarChart(actualData, predictedData) {
    reloadVisualizationDisplay();
    var ctx = document.getElementById('PlotCanvas').getContext('2d');
    var data = {
        labels: actualData.map((value, index) => index), // Assuming index as labels
        datasets: [{
            label: 'Actual Data',
            backgroundColor: 'rgba(255, 99, 132, 0.6)', // Adjust color as needed
            data: actualData
        }, {
            label: 'Predicted Data',
            backgroundColor: 'rgba(54, 162, 235, 0.6)', // Adjust color as needed
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
    document.getElementById('visualization-btn').textContent = "Bar Chart ▼";
}

let lastScrollTop = 0;
const header = document.querySelector('.base-header');
const headerHeight = header.offsetHeight; // Get the height of the header
const scrollThreshold = 100; // Adjust this value to set the scroll threshold

window.addEventListener("scroll", function() {
    let currentScroll = window.pageYOffset || document.documentElement.scrollTop;
    if (currentScroll > lastScrollTop && currentScroll > scrollThreshold) {
        // Scroll down and below the threshold, hide the header
        header.style.transform = "translateY(-100%)";
        header.style.transition = "transform 0.3s ease"; // Add animation
    } else {
        // Scroll up or not yet reached the threshold, show the header
        header.style.transform = "translateY(0)";
        header.style.transition = "transform 0.3s ease"; // Add animation
    }
    lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
}, false);


