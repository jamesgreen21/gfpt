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

