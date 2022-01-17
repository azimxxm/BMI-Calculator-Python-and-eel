import eel

eel.init('app')


@eel.expose
def bmi_calculator(height, weight):
    if height != "":
        if weight != "":
            bmi = int(weight)/((int(height)/100)**2)
            if bmi < 18.5:
                return "Your BMI is " + format(bmi, ".1f") + "(Underweight)"
            elif bmi > 18.5 and bmi < 24.9:
                return "Your BMI is " + format(bmi, ".1f") + "(Normal)"
            elif bmi > 24.09 and bmi < 29.9:
                return "Your BMI is " + format(bmi, ".1f") + "(Overweight)"
            elif bmi > 30 and bmi < 200:
                return "Your BMI is " + format(bmi, ".1f") + "(Obesity)"
            else:
                return "Something wetn wrong!"
        else:
            return "Weight is empty!"
    else:
        return "Height is empty!"


eel.start("main.html", size=(800, 600))
