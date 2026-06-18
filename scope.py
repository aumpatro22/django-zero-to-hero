# # GLOBAL SCOPE (Lobby Billboard)
# # Everyone can see this app configuration
# MIN_PASSWORD_LENGTH = 8 
# TAX_RATE=0.18
# def register_user(username, password):
#     # LOCAL SCOPE (Inside Room 404)
#     # This variable only exists while this specific registration runs
#     password_len = len(password) 
    
#     if password_len >= MIN_PASSWORD_LENGTH:
#         status = "Account Created"
#     else:
#         status = "Password Too Short"
        
#     return status
   
# def calculate_invoice(subtotal:float):
#     tax_amt: float = TAX_RATE * subtotal
#     return {
#         "Total_amt": tax_amt + subtotal
#     }


# # Testing our scope
# print(register_user("alex_dev", "super_secure_123"))
# print("the user final amount is :",calculate_invoice(20000))
logged_in_user = "Guest"

def login_user(username):
    global logged_in_user  # Declares that we are modifying the global tracking variable
    logged_in_user = username 
    print(f"Internal function check: User is {logged_in_user}")

# Simulating a login request
login_user("hacker_btech_2026")

# Correctly referencing the global state variable directly
print(f"Global application state: User is {logged_in_user}")