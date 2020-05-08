
class Calculator():
    """
    Calculator based on the Harris-Benedict Calculator
    """

    def __init__(self, user_form):
        WEIGHT_ADJUST = 0.453592 if user_form.get('weight_unit') == 'pound' else 1
        HEIGHT_ADJUST = 30.48 if user_form.get('height_unit') == 'feet' else 1

        self.weight = float(user_form.get('weight')) * WEIGHT_ADJUST
        self.height = float(user_form.get('height')) * HEIGHT_ADJUST
        self.age = int(user_form.get('age'))
        self.gender = 'f' if user_form.get('gender', 'm')[0] == 'f' else 'm'
        self.pal = int(user_form.get('pal', 0))
        self.goal = int(user_form.get('goal', 0))
    
    def results(self):
        palArray = [1.2, 1.375, 1.55, 1.725, 1.9]
        goalArray = [-500, 0, 500]
        bmr = int((self.weight * 10 + self.height * 6.25 - self.age * 5) + (5 if self.gender == 'm' else -161))
        daily_target = int(bmr * palArray[self.pal] + goalArray[self.goal])
        protein = int((daily_target * 0.30) / 4)
        return {'bmr': bmr, 'protein': protein, 'daily_target': daily_target}
