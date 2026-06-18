def calculate_cart_total(Base_price,tax_rate=0.05):
    tax_amt=Base_price*tax_rate
    final_price=Base_price+tax_amt
    return final_price
def calculate_loyalty_points(amount_spent):
    points = amount_spent * 0.1
    # print(points)# it will not retutn anything 
    return points

def apply_bonus(points):
    return points+50
def Create_user_profile(user_name:str,email:str=None,role:str="customer"):
    return {
        "user_name": user_name,
        "email": email,
        "role": role
    }



userTot= calculate_cart_total(200)    
print(f"user owe ${userTot}")   
user_points = calculate_loyalty_points(500)
final_points = apply_bonus(user_points) 
print(final_points)
print(Create_user_profile("aum patro"))