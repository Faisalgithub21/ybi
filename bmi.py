def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI).
    
    :param weight: Weight in kilograms
    :param height: Height in meters
    :return: Calculated BMI
    """
    return round(weight / (height ** 2), 2)

def classify_bmi(bmi):
    """
    Classify BMI based on WHO standards.
    
    :param bmi: Body Mass Index
    :return: Classification as a string
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def get_health_tips(bmi_category):
    """
    Provide health tips based on BMI classification.
    
    :param bmi_category: BMI classification
    :return: Health tips as a string
    """
    tips = {
        "Underweight": "Consider a balanced diet with more calories and consult a nutritionist if needed.",
        "Normal weight": "Maintain your healthy lifestyle with a balanced diet and regular exercise.",
        "Overweight": "Focus on regular physical activity and monitor your calorie intake.",
        "Obesity": "Consult a healthcare provider for a personalized plan to manage your weight effectively."
    }
    return tips.get(bmi_category, "No tips available.")

def main():
    """
    Main function to calculate and classify BMI.
    """
    print("Welcome to the BMI Calculator!")
    try:
        # User input
        weight = float(input("Enter your weight in kilograms (e.g., 70): "))
        height = float(input("Enter your height in meters (e.g., 1.75): "))
        
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive values.")
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        bmi_category = classify_bmi(bmi)
        
        # Display results
        print("\n--- BMI Results ---")
        print(f"Your BMI: {bmi}")
        print(f"Classification: {bmi_category}")
        print(f"Health Tips: {get_health_tips(bmi_category)}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
