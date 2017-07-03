

(function($) {
    "use strict"; // Start of use strict

    // jQuery for page scrolling feature - requires jQuery Easing plugin
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: ($($anchor.attr('href')).offset().top - 65)
        }, 1250, 'easeInOutExpo');
        event.preventDefault();
    });

    // Highlight the top nav as scrolling occurs
    $('body').scrollspy({
        target: '.navbar-fixed-top',
        offset: 65
    })

    // Fit Text Plugin for Main Header
    $("#caption-text").fitText(
        1.4, {
            minFontSize: '5px',
            maxFontSize: '26px'
        }
    );

 // Offset for Main Navigation
    $('#mainNav').affix({
        offset: {
            top: 100
        }
    })

 // Initialize WOW.js Scrolling Animations
    new WOW().init();
