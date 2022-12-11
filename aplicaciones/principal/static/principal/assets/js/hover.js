/* Demo purposes only */
$(".hover").mouseleave(
  function () {
    $(this).removeClass("hover");
  }
);

offset    = $('#code').offset().top
$window.scroll(function() {
    if($window.scrollTop() > offset) {
     $top_link.fadeIn();
    } else {
     $top_link.fadeOut();
    }
   }).scroll();