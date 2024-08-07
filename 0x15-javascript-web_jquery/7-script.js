
const d = $('DIV#character');
$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
  d.text(data.name);
});
