function process_the_image(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#img').fadeOut(500);
            setTimeout(function(){
            $('#img').attr('src', e.target.result); }, 450)
            setTimeout(function(){ $('#img').fadeIn(500); },   500);
        }
        reader.readAsDataURL(input.files[0]);
        $('#diag').text('COMPUTING...');
        $('#prob').text('COMPUTING...');
        var data = new FormData($('#myreq').get(0));
        $.ajax({
            url: '/result',
            type: 'POST',
            data: data,
            contentType: 'multipart/form-data',
            processData: false,
            contentType: false,
            cache: false,
            success: function(data) {
                $('#diag').text(data[0]);
                $('#prob').text((data[1]*100).toFixed(2)+'%');
            }
        });
    }
    return false;
}