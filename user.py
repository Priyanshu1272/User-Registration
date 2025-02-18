
import re


def valid_first_name():
    """
    Validates the first name.

    - Must start with an uppercase letter.
    - Remaining characters can be uppercase or lowercase.
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
            print("It is a valid name.")
        else:
            print("It is an invalid name. It should start with a capital letter and have at least 3 characters.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    valid_first_name()

if __name__ == "__main__":
    main()
