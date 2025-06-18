# /bmi_calculator.py
def get_positive_float_input(prompt_message: str) -> float:
    """
    Prompts the user for a positive floating-point number and validates the input.

    Args:
        prompt_message: The message to display to the user.

    Returns:
        A positive float entered by the user.
    """
    while True:
        try:
            value_str = input(prompt_message)
            value_float = float(value_str)
            if value_float > 0:
                return value_float
            else:
                print("Input must be a positive number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value (e.g., 70.5 or 175).")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    """
    Calculates the Body Mass Index (BMI).

    Args:
        weight_kg: Weight in kilograms.
        height_cm: Height in centimeters.

    Returns:
        The calculated BMI value.
        Returns 0.0 if height is 0 to prevent division by zero,
        though get_positive_float_input should prevent this.
    """
    if height_cm <= 0: # Should be caught by input validation, but as a safeguard
        print("Error: Height must be greater than zero.")
        return 0.0 
    
    height_m = height_cm / 100  # Convert height from cm to meters
    bmi = weight_kg / (height_m ** 2)
    return bmi

def get_bmi_category(bmi: float) -> str:
    """
    Classifies the BMI into categories.

    Args:
        bmi: The Body Mass Index value.

    Returns:
        The BMI category as a string.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 24.9 <= bmi < 29.9:
        return "Overweight"
    elif bmi >= 29.9: 
        return "Obesity"
    else:
        return "Could not determine category" 

def main():
    """
    Main function to run the BMI calculator.
    """
    print("Welcome to the Command-Line BMI Calculator!")
    print("------------------------------------------")

    # Get user input for weight
    weight_kg = get_positive_float_input("Enter your weight in kilograms: ")

    # Get user input for height
    height_cm = get_positive_float_input("Enter your height in centimeters: ")

    # Calculate BMI
    bmi_value = calculate_bmi(weight_kg, height_cm)

    if bmi_value > 0: # Ensure BMI calculation was successful
        # Get BMI category
        bmi_category = get_bmi_category(bmi_value)

        # Display the results
        print("\n--- BMI Result ---")
        print(f"Your BMI is: {bmi_value:.2f}") # Display BMI rounded to two decimal places
        print(f"Category: {bmi_category}")
        print("--------------------")
        
if __name__ == "__main__":
    main()
