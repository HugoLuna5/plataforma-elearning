/**

 $(document).ready(function() {
            $.ajax({
                 type:"POST",
                 url:"/edit_favorites/",
                 data: {
                        'video': $('#test').val() // from form
                        },
                 success: function(){
                     alert('Contact Form Submitted!');
                 }
            });


});

*