
import re

def valid_first_name():
    """
    Validates the first name.
    - The name must start with an uppercase letter.
    - The remaining letters can be uppercase or lowercase.
    - Minimum length: 3 characters.
    Returns:
        None
    """
    try:
        pattern = r"^[A-Z][a-zA-Z]{2,}$"
        first_name = input("Enter first name: ").strip()
        if not first_name:
            raise ValueError("First name cannot be empty.")
        if re.match(pattern, first_name):
            print("It is a valid first name.")
        else:
            print("It is an invalid first name. It must start with a capital letter and have at least 3 characters.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def valid_last_name():
    """
    Validates the last name.
    - The last name must start with an uppercase letter.
    - The remaining letters can be uppercase or lowercase.
    - Minimum length: 3 characters.
    Returns:
        None
    """
    try:
        pattern = r"^[A-Z][a-zA-Z]{2,}$"
        last_name = input("Enter last name: ").strip()
        if not last_name:
            raise ValueError("Last name cannot be empty.")
        if re.match(pattern, last_name):
            print("It is a valid last name.")
        else:
            print("It is an invalid last name. It must start with a capital letter and have at least 3 characters.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    try:
        valid_first_name()
        valid_last_name()

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
