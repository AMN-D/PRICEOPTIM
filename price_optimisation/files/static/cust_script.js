document.addEventListener("DOMContentLoaded", function () {
    var selectElement = document.getElementById('selectOption');
    var containerDiv = document.querySelector('.body-your-inside-csv-container');
    var paragraph = document.createElement('p'); // Create the paragraph element

    selectElement.addEventListener('change', function () {
        if (selectElement.value === '1') {
            // Fill the table
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

                // Remove the paragraph if it exists
                if (containerDiv.contains(paragraph)) {
                    containerDiv.removeChild(paragraph);
                }
            }
        } else if (selectElement.value === '0') {
            // Clear the div
            containerDiv.innerHTML = '';

            // Add the paragraph
            paragraph.textContent = 'CSV';
            containerDiv.appendChild(paragraph);
        } else {
            console.log('Select a value');
        }
    });
});