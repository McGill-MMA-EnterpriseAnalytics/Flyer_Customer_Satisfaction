
$(document).ready(function () {
    $('#dataTable').DataTable({
        "paging": true // false to disable pagination (or any other option)
    });
    $('.dataTables_length').addClass('bs-select');
});