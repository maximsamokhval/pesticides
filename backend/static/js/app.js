function dataFormatter(value, row) {

    if (value === '0001-01-01T00:00:00') {
        return ''
    } else {
        // Создаем объект Date
        const date = new Date(value);
        const formattedDate = `${date.getFullYear()}-${(date.getMonth() + 1)
            .toString()
            .padStart(2, '0')}-${date.getDate().toString().padStart(2, '0')}`;

        return formattedDate;
    }

}

function statusFormatter(value, row) {

    if (value === 'В ожидании') {
        let color = '#757474'
        return '<div style="color: ' + color + '">' + value + '</div>'
    } else if (value === 'Дозволено') {
        let color = '#07fd07'
        return '<div style="color: ' + color + '">' + value + '</div>'

    } else if (value === 'Заборонено') {
        let color = '#f10606'
        return '<div style="color: ' + color + '">' + value + '</div>'
    } else if (value === 'Не затверджено на рівні ЄС') {
        let color = '#85c9f1'
        return '<div style="color: ' + color + '">' + value + '</div>'
    }

}

function pesticideFormatter(value, row) {
    return "<a href='" + row.URL + "'>" + row.pesticide + "</a>";
}

function monitoringFormatter(value) {
    if (value === true) {
        let color = '#000000'
        return '<div style="color: ' + color + '">' + '<i class="bi bi-eye"></i>'
        '</div>'
    } else {
        return "";
    }

}

const $table = $('#table');

$(function () {

    $table.bootstrapTable({
        data: data,
        formatNoMatches: function () {
            return 'Відсутні дані для відображення';
        }
    })

    $table.bootstrapTable('sortBy', {
        field: 'agrochemical',
        sortOrder: 'asc'
    })

})


