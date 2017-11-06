$(document).ready( function() {

  //  *********************************************
  //  FOOTER - MAKE IT STICK ON TOP OF THE PAGE
  //  *********************************************

  //  toggle is-sticky class to element on click

  $(function(){
      $(window).scroll(function() {
          if ($(this).scrollTop() >= 10) {
              $('.map').fadeOut(200);
              $('.filter-options').hide();
              $('nav.main-nav').addClass('stickytop');
              $('#the-map').removeClass('not-showing');
              $('#support').removeClass('not-showing');
              $('#privacy').removeClass('not-showing');
          }
          else {
              $('stickytop').fadeOut('slow');
              $('nav.main-nav').removeClass('stickytop');
              $('.map').fadeIn(200);
              $('.filter-options').fadeIn('fast');
              $('#the-map').addClass('not-showing');
              $('#support').addClass('not-showing');
              $('#privacy').addClass('not-showing');

          }
      });
  });


      //  *********************************************
      //  SIGN UP - LOGIN DIALOGS
      //  *********************************************

});
