$(document).ready(function () {

    $('#create_form').submit(function (e) { 
        e.preventDefault();        
        $('#msg').fadeIn();

        url = $(this).attr("action");
        form_data = $(this).serialize();
        $.post(url, form_data,
            function (data, textStatus, jqXHR) {
                $('#msg').addClass('alert');
                backend_status=data['status']
                console.log(backend_status)
                if (backend_status === 'uploaded') {
                    $('#msg').addClass('mb-2');

                        $('#msg').text("Added to the database");
                        $('#msg').addClass("bg-success");
                        $('#msg').removeClass('bg-warning bg-danger');

                }else if (backend_status === 'failed') {
                    $('#msg').addClass('mb-2');

                        $('#msg').text("Something is seriously wrong somewhere");
                        $('#msg').addClass("bg-danger");
                        $('#msg').removeClass('bg-success bg warning');

                }else if (backend_status === 'exist') {
                    $('#msg').addClass('mb-2');

                        $('#msg').text("User already Exist fam!");
                        $('#msg').addClass("bg-warning");
                        $('#msg').removeClass('bg-success bg-danger');

                }
                setTimeout(() => {
                    $('#msg').fadeOut();
                }, 5000);
            }
        );
    });
});



