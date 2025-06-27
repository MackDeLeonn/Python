import re

def password_strength_analyzer(password):
    feedback = []

#Check Length
    if len(password) < 8:
        feedback.append("Too short: Password should be at least 8 characters.")
        strength = "Weak"
    #If the password is less than 8 characters
    elif len(password) < 12:
        feedback.append("Medium length: Consider using 12+ characters for better security.")
        strength = "Medium"
    #If the password is less than 12 characters
    else:
        feedback.append("Good length: Password is long enough.") 
        strength = "Strong"
#If the password is equal to or more than 12 characters

#Checks Variety
    has_upper = bool(re.search(r"[A-Z]", password))
    #Checks for uppercase letters
    has_lower = bool(re.search(r"[a-z]", password))
    #Checks for lowercase letters
    has_digit = bool(re.search(r"\d", password))
    #Checks for numbers
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    #Checks for special characters

    variety_issues = 0
#Starts with a score 0, which is good
    
    if not has_upper:
        feedback.append("Missing uppercase letters.")
        variety_issues += 1
    if not has_lower:
        feedback.append("Missing lowercase letters.")
        variety_issues += 1
    if not has_digit:
        feedback.append("Missing numbers.")
        variety_issues += 1
    if not has_special:
        feedback.append("Missing special characters (e.g. !, @, #, etc.).")
        variety_issues += 1
    #Adds to the variety score if characters were missing, which will include feedback depending on what you're missing

    if variety_issues == 0:
        feedback.append("Good variety of character types.")
    #Will let you know if you have a good variety in your password

# Check for patterns
    sequential_pattern = bool(re.search(r"(123|234|345|456|567|678|789|890|abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)", password, re.IGNORECASE))
    repeated_chars = bool(re.search(r"(.)\1{2,}", password))
    #Detects sequential patterns, ignoring case sensitivity, and checks for repeated characters

#Feedback from patterns
    if sequential_pattern:
        feedback.append("Avoid common patterns like '123' or 'abc'.")
        strength = "Weak"
    if repeated_chars:
        feedback.append("Avoid repeated characters like 'aaa'.")
        strength = "Weak"
    if not sequential_pattern and not repeated_chars:
        feedback.append("No common patterns detected.")
    #If there are sequential patterns or repeated characters, the password is weak

#Final results and feedback
    if strength == "Strong" and variety_issues == 0:
        feedback.append("\nOverall Strength: **Strong** – Great job!")
    elif strength == "Medium" or variety_issues <= 1:
        feedback.append("\nOverall Strength: **Medium** – Some improvements needed.")
    else:
        feedback.append("\nOverall Strength: **Weak** – Please improve your password.")
    #Determines the password's strength through the variety score and patterns

#Return all the feedback
    return "\n".join(feedback)

#Enter the password
user_password = input("Enter your password: ")
print(password_strength_analyzer(user_password))
