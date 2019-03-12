// from data.js
var tableData = data;

// YOUR CODE HERE!

$('#ufo-table').DataTable( {
    data: tableData,
    columns: [
        { data: 'datetime' },
        { data: 'city' },
        { data: 'state' },
        { data: 'country' },
        { data: 'shape' },
        { data: 'durationMinutes' },
        { data: 'comments' }
    ]
} );

