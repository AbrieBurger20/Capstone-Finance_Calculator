import math

# ask user to choose between two investment options
print("=" * 80)
print("investment - to calculate the amount of interest you'll earn on your investment.")
print("bond - to calculate the amount you'll have to pay on a home loan.")
print("=" * 80)

# allow user to enter option
user_option = input("Enter which calculation you want to do: ").casefold()

# calculations based on user's choice and inputs
if user_option == "investment":
    deposit = int(input("How much money are you depositing? (R) "))
    interest_rate = float (input("Enter the interest rate (%): "))
    years_invested = int(input("For how long do you want to invest your money (years): "))
    type_interest = input("Which type of interest do you want? simple or compound: ").casefold()

    # calculations based on user's choice of interest
    simple_interest = deposit * (1+interest_rate / 100 * years_invested)
    compound_interest = deposit * math.pow((1 + interest_rate / 100), years_invested)
    
  
    if type_interest == "simple":
        print(f"The amount you will get back after the given period is R{round(simple_interest, 2)}.")

    if type_interest == "compound":
        print(f"The amount you will received after the given period is: R{round(compound_interest, 2)}")

# calculations on the event the user chooses bond as an investment option
elif user_option == "bond":
        property_value = int(input("Enter present value of the house: (R) "))
        bond_rate = float(input("Enter the interest rate (%): "))
        payback_length = int(input("Enter the number of months you plan to pay back the bond: "))

        annual_interest = bond_rate / 100
        monthly_interest = annual_interest / 12
        repayment = (monthly_interest * property_value) / (1 - ((1 + monthly_interest) ** (-payback_length)))
        print(f"The monthly repayments on your bond will be: R{round(repayment, 2)}")

# message for user does not choose either investment  or bond
else:
     print("Pick either 'investment' or 'bond'.")
        
        


        
    


