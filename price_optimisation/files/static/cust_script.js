document.addEventListener("DOMContentLoaded", function () {
    var selectElement = document.getElementById('selectOption');
    var containerDiv = document.querySelector('.body-your-inside-csv-container');
    var paragraph = document.createElement('p'); 
    var features = {{ features|safe }};

    // Function to generate input fields
    function generateInputFields(features) {
        var container = document.getElementById('feature-input-container');

        features.forEach(function(feature) {
            var input = document.createElement('input');
            input.type = 'text';
            input.placeholder = feature.toUpperCase().replace('_', ' '); // Assuming features are in snake_case

            container.appendChild(input);
        });
    }

    selectElement.addEventListener('change', function () {
        if (selectElement.value === '1') {
            // Generate input fields
            generateInputFields(features);

            if (containerDiv) {
                var jsonData = JSON.parse('{{ json_data|escapejs }}');
                var table = '<table border="1">';
                table += '<tr>';
                for (var key in jsonData[0]) {
                    table += '<th>' + key + '</th>';
                }
                table += '</tr>';
                for (var i = 0; i < jsonData.length; i++) {
                    table += '<tr>';
                    for (var key in jsonData[i]) {
                        table += '<td>' + jsonData[i][key] + '</td>';
                    }
                    table += '</tr>';
                }
                table += '</table>';
                containerDiv.innerHTML = table;

                if (containerDiv.contains(paragraph)) {
                    containerDiv.removeChild(paragraph);
                }
            }
        } else if (selectElement.value === '0') {
            containerDiv.innerHTML = '';
            paragraph.textContent = 'CSV';
            containerDiv.appendChild(paragraph);
        } else {
            console.log('Select a value');
        }
    });
});