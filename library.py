import random
from datetime import datetime

#step 0 (From previous step)
number = random.randint(10, 10000)
card_number = [1, 2, 3, 4, 5, 6, 7, 8, 0, 9,] 
book_titles = ["A Moveable Feast", "A Room of One’s Own", "A Tale of Two Cities", "G"]



#step 1:
print("Option 1: Borrow a book ")
print("Option 2: Return a book ")
print("Option 3: Replace a book ")

#step 2:
choice = input("Enter the number of your choice (1, 2 or 3): ")

if choice == "1":
    book_name = input("What's the name of the book you want to borrow: ") 
 
    if book_name not in book_titles:
        print("We do not have this book in store.")
    else:
        print("We have this book in store.")
        
        # library card
        lib_card = input("Do you have a library card? (yes/no): ").strip().lower() 

        if lib_card == "no":
            card = input("Sorry, we can only allow card holders to borrow books. Would you like a library card? (yes/no): ").strip().lower()
            
            if card == "no":
                print("We cannot let you borrow this book.")
            elif card == "yes":
                name = input("Enter your first name: ")
                if len(name) > 20:
                    name = input("Name is too long, please enter a shorter name: ")
                elif len(name) < 2:
                    name = input("Name is too short, please enter a longer name: ")
                
                surname = input("Enter your surname: ")
                if len(surname) > 20:
                    surname = input("Surname is too long, please enter a shorter surname: ")
                elif len(surname) < 2:
                    surname = input("Surname is too short, please enter a longer surname: ")
                  
                age = int(input("Enter your age: "))
                if age >= 16:
                    print(f"Welcome to Lesley's Library, you are an official card member. Your card number is {number}")
                elif age < 16:
                    children_acc = input("You are too young for our adult accounts. Would you like a children's Acc instead? You will need your parent's details (yes/no): ").strip().lower()
                    if children_acc == "yes": 
                        parent_name = input("Enter parent's first name: ")
                        if len(parent_name) > 20:
                            parent_name = input("Name is too long, please enter a shorter name: ")
                        elif len(parent_name) < 2:
                            parent_name = input("Name is too short, please enter a longer name: ")
                        
                        parent_surname = input("Enter parent's surname: ")
                        if len(parent_surname) > 20:
                            parent_surname = input("Surname is too long, please enter a shorter surname: ")
                        elif len(parent_surname) < 2:
                            parent_surname = input("Surname is too short, please enter a longer surname: ")
                        
                        print(f"Welcome to Lesley's Library, you are an official card member. Your card number is {number}") 

        if lib_card == "yes":
            card_num = int(input("Enter your card number please: ")) 
            if card_num != number and card_num not in card_number:
                print("Invalid number.")
            else:
                print("You can take the book, be sure to bring it back in 21 days / 3 weeks.")
                borrow_date = input("Enter today's date (DD/MM/YYYY): ")

elif choice == "2":
    book_name = input("What's the name of the book you want to return: ")
    card_num = int(input("Enter your card number please: ")) 
     
    date_taken_str = input("Enter the date you borrowed the book (DD/MM/YYYY): ")
    date_returned_str = input("Enter the date you are returning the book today (DD/MM/YYYY): ")
    
    # Convert text inputs into actual date objects to do the math
    date_taken = datetime.strptime(date_taken_str, "%d/%m/%m%Y" if len(date_taken_str) > 10 else "%d/%m/%Y")
    date_returned = datetime.strptime(date_returned_str, "%d/%m/%Y")
    
    difference = (date_returned - date_taken).days
    
    # Check if the return is older than the allowed 21 days
    if difference > 21:
        days_overdue = difference - 21
        amount_due = days_overdue * 0.50
        print(f"You have been overdue for {days_overdue} days. Due to this, you will be charged £0.50 for every day overdue. This brings your total fine to: £{amount_due:.2f}")
    else:
        print("Thank you for returning your book on time!")
    print("Good day!")

elif choice == "3":
    while True:
        book = input("What's the name of the book you would like to replace (or type 'exit' to quit): ")
        if book.lower() == 'exit':
            break
        print("Thank you for replacing the book titled", book)