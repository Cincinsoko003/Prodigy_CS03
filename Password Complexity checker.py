import re

def check_password_complexity(password):
    # Criteria for password complexity
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[@$!%*?&#]', password) is not None

    # Check all criteria
    if all([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria]):
        return "Strong password"
    elif length_criteria and (uppercase_criteria or lowercase_criteria) and (digit_criteria or special_char_criteria):
        return "Moderate password"
    else:
        return "Weak password"

# Example usage
password = input("Enter a password to check its complexity: ")
print(check_password_complexity(password))
