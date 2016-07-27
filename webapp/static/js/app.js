$(document).ready(function() {
  $('#tag').bind('keyup', function() {
    $.getJSON('/api/0.1/get_tags', {
      tags: $('input[name="tags"]').val(),
      tag: $('input[name="tag"]').val()
    }, function(data) {
      var output = "";
      for (var i = 0; i < data.tags.length; i++) {
        output += "<a class='btn btn-info taglink' role='button'>" + data.tags[i] + "</a> ";
      }
      $("#result").html(output);
    });
    return false;
  });
  $(document).on('click', "td.tagslink", function() {
    var childs = this.children;
    var url = "/?";
    for (var i = 0; i < childs.length; i++) {
      url = url + "tag=" + childs[i].text + "&";
    }
    location.href = url;
    return false;
  });

  $(document).on('click', "a.taglink", function() {
    var url = window.location.href;
    if (url.indexOf(encodeURI(this.text)) == -1) {
      if (url.indexOf("?") == -1)
        url += "?";
      else
        url += "&";
      location.href = url + "tag=" + this.text;
    }
    return false;
  });

  var valueClass = {
    //English
    yes: 'success',
    no: 'danger',
    //German
    ja: 'success',
    freigegeben: 'success',
    nein: 'danger'
  };
  $('td').each(function() {
    if (this.innerText in valueClass)
      $(this).addClass(valueClass[this.innerText]);
  });

  $('#btndelete').click(function() {
    location.href = "/delete?id=" + $('#dataid').val();
    return false;
  });

  $('.removetag').click(function() {
    var url = window.location.href;
    url = url.replace(encodeURI("tag=" + this.innerText), '');
    url = url.replace("&&", '&');
    location.href = url;
  });
});
