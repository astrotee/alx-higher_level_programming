
function getHello () {
  const d = $('DIV#hello');
  const lang = $('INPUT#language_code');
  $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=' + lang.val(), function (data) {
    d.html(data.hello);
  });
}
function main () {
  const b = $('INPUT#btn_translate');
  b.on('click', getHello);
}

$('document').ready(main);
