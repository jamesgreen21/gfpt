$(document).ready(function() {
  $(function() {
    $('[data-toggle="tooltip"]').tooltip()
    $(".dropdown-trigger").dropdown();
    $('.parallax').parallax();
    $('.sidenav').sidenav();
    $('.carousel').carousel({indicators: true, numVisible: 3, dist: -200});
    $('.modal').modal();
    $('.datepicker').datepicker({'format': 'yyyy-mm-dd'});
    $('select').formSelect();
  })
});


(function() {
        let documentElem = $(document),
            nav = $('nav'),
            lastScrollTop = 0;

        documentElem.on('scroll', function(){
            var currentScrollTop = $(this).scrollTop();
            if (currentScrollTop <= lastScrollTop || currentScrollTop < 80) nav.css("top", "0");
            else nav.css("top", "-80px");
            lastScrollTop = currentScrollTop;
        })
    }) ();

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            $('#imagePreview').css('background-image', 'url('+e.target.result +')');
            $('#imagePreview').hide();
            $('#imagePreview').fadeIn(650);
        }
        reader.readAsDataURL(input.files[0]);
    }
}
$("#id_image").change(function() {
    readURL(this);
});