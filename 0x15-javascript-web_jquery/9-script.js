
function main () {
  const d = $('DIV#hello');
  $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    d.text(data.hello);
  });
}

$('document').ready(main);
