let tmpAnimation = 0;

$(".profile-photo").click(function(){

    let element = $(".profile-photo");

    tmpAnimation = tmpAnimation + 90;

    $({degrees: tmpAnimation - 90}).animate({degrees: tmpAnimation}, {

        duration: 1000,

        step: function(now) {

            element.css({

                transform: 'rotate(' + now + 'deg)'

            });

        }

    });

});