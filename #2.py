def bmi(weight, height):
    """
    Calculate the Body Mass Index (BMI) for a given weight and height.

    Args:
        weight (float): The weight of the person in kilograms.
        height (float): The height of the person in meters.

    Returns:
        str: A string indicating the BMI category for the person.
             Possible values are "Underweight", "Normal", "Overweight", or "Obese".
    """
    bmi = weight / (height ** 2)

    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    else:
        return "Obese"