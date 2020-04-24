$('#animate1').delay(500).fadeIn(500);

$('#animate2')
  .css('right', -500)
  .animate(
    {
      right: '0',
    },
    {
      duration: 300,
      specialEasing: {
        height: 'easeOutBounce',
      },
    }
  );

$(function () {
  var messages = [],
    index = 0;

  messages.push('One-on-One');
  messages.push('Classes');
  messages.push('Online Training');
  messages.push('Your place or mine');

  function cycle() {
    $('#advertMsg')
      .html(messages[index])
      .animate(
        {
          top: 0,
          opacity: 1,
        },
        250
      )
      .delay(1250)
      .animate(
        {
          top: -10,
          opacity: 0,
        },
        500
      );
    index++;

    if (index === messages.length) {
      index = 0;
    }

    setTimeout(cycle, 2500);
  }

  cycle();
});
