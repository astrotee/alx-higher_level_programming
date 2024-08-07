
const ul = $('UL#list_movies');
$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  for (const film of data.results) {
    ul.append('<li>' + film.title + '</li>');
  }
});
