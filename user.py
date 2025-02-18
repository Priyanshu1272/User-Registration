
import re


def valid_first_name():
    """
    Validates the first name.
    - The name must start with an uppercase letter.
    - The remaining letters can be uppercase or lowercase.
    - Minimum length: 3 characters.
    Returns:
        bool: True if valid, False otherwise.
    """
    try:
        pattern = r"^[A-Z][a-zA-Z]{2,}$"
        first_name = input("Enter first name: ").strip()

        if not first_name:
            raise ValueError("First name cannot be empty.")
        if re.match(pattern, first_name):
            print("It is a valid First Name.")
            return True
        else:
            print("It is an invalid First Name. It must start with a capital letter and have at least 3 characters.")
            return False

    except ValueError as ve:
        print(f"Error: {ve}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

def valid_last_name():
    """
    Validates the last name.
    - The last name must start with an uppercase letter.
    - The remaining letters can be uppercase or lowercase.
    - Minimum length: 3 characters.
    Returns:
        bool: True if valid, False otherwise.
    """
    try:
        pattern = r"^[A-Z][a-zA-Z]{2,}$"
        last_name = input("Enter last name: ").strip()

        if not last_name:
            raise ValueError("Last name cannot be empty.")

        if re.match(pattern, last_name):
            print("It is a Valid Last Name.")
            return True
        else:
            print("It is an invalid Last Name. It must start with a capital letter and have at least 3 characters.")
            return False

    except ValueError as ve:
        print(f"Error: {ve}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

def valid_email():
    """
    Validates the email address.
    - The email must follow the pattern username.domain1@domain2.domain3.
    - username, domain1, domain2 are mandatory, while domain3 is optional.
    Returns:
        bool: True if valid, False otherwise.
    """
    try:
        pattern = r"^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*@[a-zA-Z0-9]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$"
        email = input("Enter your email address: ").strip()
        if not email:
            raise ValueError("Email cannot be empty.")
        if re.match(pattern, email):
            print("It is a Valid Email Address.")
            return True
        else:
            print("It is an invalid Email Address. It must follow the format username@domain1.domain2 (with optional .domain3).")
            return False

    except ValueError as ve:
        print(f"Error: {ve}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

def main():
    try:
        # Validate First Name
        if valid_first_name():
            # Validate Last Name
            if valid_last_name():
                # Validate Email
                valid_email()

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

