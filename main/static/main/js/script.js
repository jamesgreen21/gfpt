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
          opacity: 1,
        },
        150
      )
      .delay(1500)
      .animate(
        {
          top: -10,
          opacity: 0,
        },
        350,
        function () {
          $(this).css({ top: 0 });
        }
      );
    index++;

    if (index === messages.length) {
      index = 0;
    }

    setTimeout(cycle, 2000);
  }

  cycle();
});
