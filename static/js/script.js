var button = $('button');
var bgRAW = $('.background_RAW');
var bgFiltered = $('.background_Filtered');
var phone = $('img');

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


//anime ({
//	targets: ['.first', '.last'],
//	width: '0px',
//	delay: function(el) {
//		if (el.classList.contains('first')) {
//			return 0;
//		} else {
//			return 1500;
//		}
//	},
//	duration: 1500,
//	loop: false,
//	easing: 'easeInOutQuad'
//});
