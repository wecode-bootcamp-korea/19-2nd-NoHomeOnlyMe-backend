import re
import bcrypt

def validate_data(**kwargs):
    
    MIN_PW_LEN = 8
    PN_LEN = 10
    
    if not kwargs.get("email", None):
        return "KeyError"
        
    email_name, domain_name = kwargs["email"].rsplit("@", 1)
        
    if "@" in email_name or not '.' in domain_name:
        return "Invalid email form"
        
    kwargs["email"] = email_name + "@" + domain_name.lower()
    
    
    if not kwargs.get("name", None):
        return "KeyError"
        
    if not re.match(re.compile("^[가-힣]+"), kwargs["name"]):
        return "Invalid name"
        
    
    if not kwargs.get("password", None):
        return "KeyError"
        
    if len(kwargs["password"]) < MIN_PW_LEN or not re.search(re.compile("[~!@#$%^&*()_/,.<>{}]+"), kwargs["password"]):
        return "Invalid password"
    
    if not kwargs.get("phone_number", None):
        return "KeyError"
        
    if "-" in kwargs["phone_number"] or len(phone_number_body := kwargs["phone_number"].split("0", 1)[1]) != PN_LEN:
        return "Invalid phone number"
    kwargs["phone_number"] = int(phone_number_body)
    
    return kwargs