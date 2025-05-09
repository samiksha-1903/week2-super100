import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None
print(is_valid_email("user@domain.com"))  
print(is_valid_email("user@domain"))      
print(is_valid_email("user@.com"))        
