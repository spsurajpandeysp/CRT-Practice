def is_valid_email(email):

    if email.count('@') != 1:
        return False
    
  
    local_part, domain_part = email.split('@')
    

    if not local_part:
        return False
    
    
    if '.' not in domain_part:
        return False
    

    domain_name, *extensions = domain_part.split('.')
    

    if not domain_name or not all(extensions):
        return False
    

    return True


email = input("Enter your email ID: ")
if is_valid_email(email):
    print(f"{email} is a valid email.")
else:
    print(f"{email} is not a valid email.")
