
$(document).ready(function(){
  $("#comments_control").change(
    function () {
      var selected_value = $(this).val();
      switch(selected_value) {
        case 'HIDE': {
          createJsKitCommentCookie('HIDE');
          $('.js-kit-comments').hide();
        };http:
        break;
        case 'SHOW': {
          createJsKitCommentCookie('SHOW');
          $('.js-kit-comments').show();
        };
        break;
        default: {
        };
      }
    }
  );

  // js-kit comments control configuration:
  function createJsKitCommentCookie(value, days) {
    var name = 'default_comments_control_behavior';
    if (days) {
      var date = new Date();
      date.setTime(date.getTime()+(days*24*60*60*1000));
      var expires = "; expires="+date.toGMTString();
    }
    else var expires = "";
    document.cookie = name+"="+value+expires+"; path=/";
  }

  function readJsKitCommentCookie() {
    var name = 'default_comments_control_behavior';
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
      var c = ca[i];
      while (c.charAt(0)==' ') c = c.substring(1,c.length);
      if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
  }
  var config_value = readJsKitCommentCookie();
  switch (config_value) {
    case 'HIDE': {
      $("#comments_control").val('HIDE');
    };
    break;
    case 'SHOW': {
      $("#comments_control").val('SHOW');
    };
    break;
    default: {
      createJsKitCommentCookie('SHOW');
    };
  }
});

