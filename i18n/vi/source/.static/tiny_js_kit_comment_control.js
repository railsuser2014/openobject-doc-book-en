
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
  function createJsKitCommentCookie(value) {
    var name = 'default_comments_control_behavior';
    var date = new Date(2038, 0, 1);
    date.setTime(date.getTime());
    var expires = "; expires="+date.toGMTString();
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
      $("#comments_control").val('HIDE').change();
    };
    break;
    case 'SHOW': {
      $("#comments_control").val('SHOW').change();
    };
    break;
    default: {
      createJsKitCommentCookie('SHOW');
    };
  }
});

