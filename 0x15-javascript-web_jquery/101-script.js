
function main () {
  const ul = $('UL.my_list');
  const add = $('DIV#add_item');
  const rmv = $('DIV#remove_item');
  const clr = $('DIV#clear_list');
  add.on('click', function () {
    ul.append('<li>Item</li>');
  });
  rmv.on('click', function () {
    ul.children('li').last().remove();
  });
  clr.on('click', function () {
    ul.empty();
  });
}

$('document').ready(main);
