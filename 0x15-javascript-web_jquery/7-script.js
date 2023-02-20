$(function () {
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  $.get(url, function (data) {
    const content = data.name;
    $('div#character').text(content);
  });
});
