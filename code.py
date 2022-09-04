#  BMI = 194 / (67 * 67) * 703

def get_bmi(weight, height):
    bmi = round(weight / (height * height) * 703, 1)
    return bmi

result = get_bmi(194, 67)

print("the BMI is {}!".format(result))
