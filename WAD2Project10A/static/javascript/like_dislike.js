$(document).ready(function() {
    $('[like-form]').submit(function(event){
        event.preventDefault();
        let submitter_btn = $(event.originalEvent.submitter);
        var data = new FormData(event.target);
        var picture_uuid = $('input[name=picture_uuid]').val()

        if (submitter_btn.attr("name") == "likeButton") {
            data.append("likeButton", true);
        }
        else if (submitter_btn.attr("name") == "dislikeButton") {
            data.append("dislikeButton", true);
        }

        $.ajax({
            type: 'POST',
            url: '/onlypics/like_picture',
            enctype: 'multipart/form-data',
            cache: false,
            processData: false,
            contentType: false,
            data: data,
            success: function (response) {
                event.target.reset();
                like_dislike = response["like_result"];
                var pic_uuid = response["uuid"];
                console.log(pic_uuid);
                if ("error" in response) {
                    if (like_dislike) {
                        $("#haveVoted-"+pic_uuid).text(response["error"] + "liked this picture!");
                    }
                    else {
                        $("#haveVoted-"+pic_uuid).text(response["error"] + "disliked this picture!");
                    }
                }
                else {
                    submitter_btn.css({'color':'#fff',
                            'background-color' :'#6c757d',
                            'border-color':'#6c757d'});
                }

            },
            error: function (response) {
                // alert the error if any error occured
                alert("An error occured!");
            }
        });
        return false;
    });
});

