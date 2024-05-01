$(document).ready(function() {
    // Select multiple elements at once and hide them initially
    $('.header, .me, .learn, .features, .features2, .footer').hide();

    // Set staggered animation using each() and delay
    $('.header, .me, .learn, .features, .features2, .footer').each(function(index) {
        // Fade in each element with a delay based on its position
        $(this).delay(200 * index).fadeIn(1000);
    });
});
