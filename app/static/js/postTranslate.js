// TODO: переделать на нативный js
// Перевод постов 
function translate(sourceElem, destElem, sourceLang, destLang) {
  $(destElem).html('<img src="{{ url_for('static', filename='img/loading.gif') }}">');
  $.post('/translate', {
    text: $(sourceElem).text(),
    source_language: sourceLang,
    dest_language: destLang
  }).done((response) => {
    $(destElem).text(response['text'])
  }).fail(() => {
    $(destElem).text("{{ _('Error: Could not contact server.') }}");
  });
}