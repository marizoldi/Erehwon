$(document).ready( function() {

  //  *********************************************
  //  FOOTER - MAKE IT STICK ON TOP OF THE PAGE
  //  *********************************************

  //  toggle is-sticky class to element on click

  $(function(){
      $(window).scroll(function() {
          if ($(this).scrollTop() >= 50) {
              $('.map').hide();
              $('.filter-options').hide();
              $('nav.main-nav').addClass('stickytop');
              $('#the-map').removeClass('not-showing');
              $('#support').removeClass('not-showing');
              $('#privacy').removeClass('not-showing');
          }
          else {
              $('nav.main-nav').removeClass('stickytop');
              $('.map').show();
              $('.filter-options').show();
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
