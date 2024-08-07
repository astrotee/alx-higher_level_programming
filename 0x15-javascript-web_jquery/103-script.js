
function getHello (event) {
  if (event.type === 'keyup' && event.which !== 13) return;
  const d = $('DIV#hello');
  const lang = $('INPUT#language_code');
  $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=' + lang.val(), function (data) {
    d.html(data.hello);
  });
}
function main () {
  const b = $('INPUT#btn_translate');
  const lang = $('INPUT#language_code');
  b.on('click', getHello);
  lang.on('keyup', getHello);
}

$('document').ready(main);
