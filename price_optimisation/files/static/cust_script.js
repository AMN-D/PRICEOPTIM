document.addEventListener("DOMContentLoaded", function () {
    var selectElement = document.getElementById('selectOption');

    selectElement.addEventListener('change', function () {
        if (selectElement.value === '1') {
            var containerDiv = document.querySelector('.body-your-inside-csv-container');
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
            }
        } else {
            console.log('Select a value');
        }
    });
});