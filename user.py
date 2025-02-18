import re

def valid_first_name():
    """
        Description:
                Validates the first name entered by the user. 
                The first name must start with an uppercase letter, followed by at least two more letters (uppercase or lowercase).
        Parameter:
                None. Takes user input directly.
        Return:
                bool: Returns True if the first name is valid, False otherwise.
    """
    try:
        pattern = r"^[A-Z][a-zA-Z]{2,}$"
        first_name = input("Enter first name: ").strip()
        if not first_name:
            raise ValueError("First name cannot be empty.")
        if re.match(pattern, first_name):
            print("It is a Valid First Name.")
            return True
        else:
            print("It is an Invalid First Name. It must start with a capital letter and have at least 3 characters.")
            return False

    except ValueError as ve:
        print(f"Error: {ve}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

def valid_last_name():
    """
        Description:
                Validates the last name entered by the user. 
                The last name must start with an uppercase letter, followed by at least two more letters.
        Parameter:
                None. Takes user input directly.
        Return:
                bool: Returns True if the last name is valid, False otherwise.
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
            print("It is an Invalid Last Name. It must start with a capital letter and have at least 3 characters.")
            return False

    except ValueError as ve:
        print(f"Error: {ve}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

def valid_email():
    """
        Description:
                Validates the email address entered by the user. 
                It must follow the format username@domain1.domain2 (optional .domain3).
        Parameter:
                None. Takes user input directly.
        Return:
                bool: Returns True if the email format is valid, False otherwise.
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
            print("It is an Invalid Email Address. It must follow the format username@domain1.domain2 (optional .domain3).")
            return False

    except ValueError as ve:
        print(f"Error: {ve}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

def valid_mobile():
    """
        Description:
                Validates the mobile number entered by the user. 
                It must start with a 2-digit country code, followed by a space and a 10-digit mobile number.
        Parameter:
                None. Takes user input directly.
        Return:
                bool: Returns True if the mobile number format is valid, False otherwise.
    """
    try:
        pattern = r"^[0-9]{2} [0-9]{10}$"
        mobile = input("Enter your mobile number: ").strip()
        if not mobile:
            raise ValueError("Mobile number cannot be empty.")
        if re.match(pattern, mobile):
            print("It is a Valid Mobile Number.")
            return True
        else:
            print("It is an Invalid Mobile Number. Format should be 'CC XXXXXXXXXX'.")
            return False

    except ValueError as ve:
        print(f"Error: {ve}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

def validate_password_rule1():
    """
        Description:
                Validates the password entered by the user. 
                The password must be at least 8 characters long.
        Parameter:
                None. Takes user input directly.
        Return:
                bool: Returns True if the password meets the required criteria, False otherwise.
    """
    try:
        pattern = r"^.{8,}$"
        password = input("Enter your password: ").strip()
        if not password:
            raise ValueError("Password cannot be empty.")
        if re.match(pattern, password):
            print("It is a Valid Password.")
            return True
        else:
            print("It is an Invalid Password. It must be at least 8 characters long.")
            return False

    except ValueError as ve:
        print(f"Error: {ve}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

def validate_password_rule2():
    """
        Description:
                Validates the password entered by the user.
                The password must contain atleast one uppercase letter.
                The password must be at least 8 characters long.
        Parameter:
                None. Takes user input directly.
        Return:
                bool: Returns True if the password meets the required criteria, False otherwise.
    """
    try:
        pattern = r"^(?=.*[A-Z]).{8,}$"
        password = input("Enter your password: ").strip()
        if not password:
            raise ValueError("Password cannot be empty.")
        if re.match(pattern, password):
            print("It is a Valid Password.")
            return True
        else:
            print("It is an Invalid Password. It must be at least 8 characters long and contain atleast one uppercase letter.")
            return False

    except ValueError as ve:
        print(f"Error: {ve}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

def validate_password_rule3():
    """
        Description:
                Validates the password entered by the user.
                The password must contain atleast 1 numeric number in password.
                The password must contain atleast one uppercase letter.
                The password must be at least 8 characters long.
        Parameter:
                None. Takes user input directly.
        Return:
                bool: Returns True if the password meets the required criteria, False otherwise.
    """
    try:
        pattern = r"^(?=.*[A-Z])(?=.*\d).{8,}$"
        password = input("Enter your password: ").strip()
        if not password:
            raise ValueError("Password cannot be empty.")
        if re.match(pattern, password):
            print("It is a Valid Password.")
            return True
        else:
            print("It is an Invalid Password. It must be at least 8 characters long and contain atleast one uppercase letter and one numeric number.")
            return False

    except ValueError as ve:
        print(f"Error: {ve}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False


def main():
    """
        Main function to execute validation functions in a sequence.
    """
    try:
        if valid_first_name():
            if valid_last_name():
                if valid_email():
                    if valid_mobile():
                        if validate_password_rule1():
                            if validate_password_rule2():
                                validate_password_rule3()
                                  
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()



