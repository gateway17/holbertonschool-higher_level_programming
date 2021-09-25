$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {

    data = data.results;
    $.each(data, function (index) {
        $('UL#list_movies').append('<li>' + data[index].title + '</li>');

    })                                 
})