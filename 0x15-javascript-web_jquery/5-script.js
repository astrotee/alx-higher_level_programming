
const ul = $('UL.my_list');
const d = $('DIV#add_item');
d.on('click', function () {
  ul.append('<li>Item</li>');
});
