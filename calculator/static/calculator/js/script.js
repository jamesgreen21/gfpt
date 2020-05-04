class CaloriesCalculator {
  constructor(weight, height, age, gender = 'm', pal, goal) {
    this.weight = weight;
    this.height = height;
    this.age = age;
    this.gender = gender;
    this.pal = pal;
    this.goal = goal;
  }
  bmr() {
    let genderConv = this.gender.toLowerCase() === 'm' ? 5 : -161;
    let rawBmr = this.weight * 10 + this.height * 6.25 - this.age * 5;
    return rawBmr + genderConv;
  }
  daily_energy() {
    var palArray = [1.2, 1.375, 1.55, 1.725, 1.9];
    return this.bmr() * palArray[this.pal];
  }
  daily_target() {
    var goalArray = [-500, 0, 500];
    return Math.round(this.daily_energy() + goalArray[this.goal]);
  }
}

document
  .getElementById('calorieCalculator')
  .addEventListener('change', (event) => {
    // Set input values
    var weight = document.getElementById('weight').value;
    var height = document.getElementById('height').value;
    var age = document.getElementById('age').value;
    var gender = document.getElementById('gender').checked === true ? 'f' : 'm';
    var pal = document.getElementById('pal').value;
    var goal = document.getElementById('goal').value;

    // Calculate results
    var newUser = new CaloriesCalculator(weight, height, age, gender, pal, goal);
    var result = newUser.daily_target();
    var targetEl = document.getElementById('calorieOutput')

    if (!result) {
        targetEl.innerHTML = 'Awaiting Inputs';
        targetEl.classList.remove("green", "red");
        targetEl.classList.add("blue");
    } else if (result <= 0) {
      targetEl.innerHTML = 'Check Inputs!';
      targetEl.classList.remove("green", "blue");
      targetEl.classList.add("red");
  } else {
        targetEl.innerHTML = result + ' Calories';
        targetEl.classList.remove("blue", "red");
        targetEl.classList.add("green");
    }
  });
