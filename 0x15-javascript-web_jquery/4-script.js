
const h = $('header');
const d = $('DIV#toggle_header');
d.on('click', function () {
  if (h.hasClass('red')) {
    h.removeClass('red');
    h.addClass('green');
  } else if (h.hasClass('green')) {
    h.removeClass('green');
    h.addClass('red');
  }
});
