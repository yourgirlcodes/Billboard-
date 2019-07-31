$(document).ready(function () {
    $("#ask_to_add").click(function () {
        $("#newpostform").css("display", "block");
    });

    $("#close").click(function () {
        $("#newpostform").css("display", "none");
    })

    //    $("#addpost").click(function () {
    //        $.ajax("/SocialBoard", {
    //            type: "POST",
    //            data: {
    //                "content": $("#newcontent").val(),
    //                "title": $("#newtitle").val(),
    //                "author": $("#newauthor").val()
    //            },
    //            success: function (data) {
    //                $("#posts").html(data + $("#posts").html())
    //                $("#newtext").val(""),
    //                $("#newtitle").val(""),
    //                $("#newauthor").val("");
    //            }
    //        })
    //    });




})