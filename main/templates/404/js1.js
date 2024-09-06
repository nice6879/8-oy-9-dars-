document.addEventListener('mousemove', (event) => {
  const pageX = document.documentElement.clientWidth;
  const pageY = document.documentElement.clientHeight;
  const mouseY = event.pageY;
  const mouseX = event.pageX;

  // Calculate the movement of the eyes
  const yAxis = (pageY / 2 - mouseY) / pageY * 300;
  const xAxis = -mouseX / pageX * 100 - 100;

  // Apply the transformation
  document.querySelector('.box__ghost-eyes').style.transform = `translate(${xAxis}%, -${yAxis}%)`;
});

