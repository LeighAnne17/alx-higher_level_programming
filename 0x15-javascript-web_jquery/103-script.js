$(document).ready(function() {
  function fetchTranslation() {
    const langCode = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`, function(data) {
      $('#hello').text(data.hello);
    }).fail(function() {
      $('#hello').text('Error: Unable to fetch translation.');
    });
  }

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress(function(event) {
    if (event.which === 13) {  // 13 is the Enter key code
      fetchTranslation();
    }
  });
});

