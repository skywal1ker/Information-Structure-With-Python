
#8 TASK





"""40. Body Mass Index (BMI) is a number calculated from a person’s weight and height. According
to the Centers for Disease Control, the BMI is a fairly reliable indicator of
body fatness for most people. BMI does not measure body fat directly, but research has
shown that BMI correlates to direct measures of body fat, such as underwater weighing
and dual energy X-ray absorptiometry. The formula for BMI is:
weight /height **2
where weight is in kilograms and height is in meters.
(a) Write a program that prompts for metric weight and height and outputs the BMI.
(b) Write a program that prompts for weight in pounds and height in inches, converts
the values to metric, and then calculates the BMI."""


height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / (height/100)**2

BMI = weight / (height/100)**2

print(f"You BMI in meters is {BMI}")

print(f"You BMI in inches is {BMI / 0.0254}")