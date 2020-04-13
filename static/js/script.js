$(document).ready(function() {
  $(function() {
    $('[data-toggle="tooltip"]').tooltip()
    $(".dropdown-trigger").dropdown();
    $('.parallax').parallax();
    $('.sidenav').sidenav();
    $('.carousel').carousel();
    $('.modal').modal();
    $('.carousel.carousel-slider').carousel({indicators: true});
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
            if(currentScrollTop > lastScrollTop) nav.css("top", "-80px");
            else nav.css("top", "0");
            lastScrollTop = currentScrollTop;
        })
    }) ();
