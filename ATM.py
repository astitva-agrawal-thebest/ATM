from card import card

def print_menu():
    print("Please choose from one of the following options...")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. Exit")

def deposit(card):
    try:
        deposit = float(input("How much ₹₹ would you like to deposit: "))
        card.set_balance(card.get_balance() + deposit)
        print("Your New Balance is: ", str(card.get_balance()))
    except:
        print("Invalid Input")
    
def withdraw(card):
    try:
        withdraw = float(input("How much ₹₹ would you like to withdraw: "))
        if(card.get_balance() < withdraw):
            print("You trying to being funny, huh YOU THINK YOU ARE FUNNY WELL FACE THE TRUTH THAT YOU ARE NOT!!! Kiddo")
        else:
            card.set_balance(card.get_balance() - withdraw)
            print("Your New Balance is: ", str(card.get_balance()))
    except:
        print("Invalid Input")

def check_balance(card):
    print("Your current balance is: ", card.get_balance())

if __name__ == "__main__":
    current_user = card("","","","","")

    list_of_card = []
    list_of_card.append(card("9890557855", 3615, "Astitva", "Agrawal", 9883997465))
    list_of_card.append(card("1366098872", 8643, "Siddhant", "Jain", 3129491845))
    list_of_card.append(card("5733013255", 2700, "Madhav", "Dhand", 2711806216))
    list_of_card.append(card("8807934799", 1142, "Kartik", "Chauhan", 4089547396))
    list_of_card.append(card("9005589677", 7629, "Kristna", "Bansel", 8511161196))
    list_of_card.append(card("6768168957", 9131, "Ansh", "Gupta", 8407782744))

    while True:
        try:
            debitcardNum = input("Please insert yours Debit Card Number:")
            debitMatch = [holder for holder in list_of_card if holder.cardNum == debitcardNum]
            if(len(debitMatch) > 0):
                current_user = debitMatch[0]
                break
            else:
                 print("You entered the wrong Debit Card Number, Try again")                
        except:
            print("What you trying to do scam us, You know what we are calling 112 on you now run for your life, YOU B*****D")
        
    while True:
        try:
            userPin = int(input("Please enter your pin: ").strip())
            if(current_user.get_pin() == userPin):
                break
            else:
                print("Invalid PIN. Please try again.")
        except:
            print("What you trying to do scam us, You know what we are calling 112 on you now run for your life, YOU B*****D")

    print("Welcome", current_user.get_firstname(), " :)") 
    option = 0 
    while True:
        print_menu() 
        try:
            option = int(input()) 
        except:
            print("Invalid input. Please try again.") 

        if(option == 1):
            deposit(current_user)
        elif(option == 2):
            withdraw(current_user)
        elif(option == 3):
            check_balance(current_user)
        elif(option == 4):
            break
        else:
            option = 0
        
    print("Thank you. Have a nice day :)")