import random
import string

program = int(input("enter a num to start a program (1, 2, 3, 4, 5, 6 or 7): "))

match(program):

# تمارین حلقه   
    case 1:
        sum = 0
        for i in range(1,11):
            sum +=i
        print(sum)

    case 2:
        for i in range(1,51):
            if i == 42:
                break
            if i % 5 == 0:
                continue
            if  i % 3 == 0:
                print(i)
    

 # ثمرین پسوورد جنیتور   
    case 3:
        while True:
            print("\n========== MAIN MENU ==========")
            print("1. Password Generator")
            print("2. Number Guessing Game")
            print("3. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                print("\n--- Password Generator ---")

                length = int(input("Enter password length: "))

                if length <= 0:
                    print("Invalid password length!")

                else:
                    characters = string.ascii_letters + string.digits + string.punctuation

                    password = ""

                    for i in range(length):
                        password += random.choice(characters)

                    print("Your password is:", password)
  
            elif choice == "2":
                print("\n--- Number Guessing Game ---")

                c_num = random.randint(1, 100)
                chance = 7

                for i in range(7):
                    e_num = int(input("Guess the number (1-100): "))

                    if e_num == c_num:
                        print("tabrik You won!")
                        break

                    elif e_num > c_num:
                        chance -= 1
                        print(f"bigger! {chance} chances left.")

                    else:
                        chance -= 1
                        print(f"smaller! {chance} chances left.")

                else:
                    print("bakhti pisar jan!")
                    print(f"The correct number was: {c_num}")

            elif choice == "3":
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice! Try again.")


# تمرین فکتوریل

    case 4:
        num = int(input("\nenter a num to give you the factorial of it: "))
        t_num = num
        fact = 1
        while num > 0:
            fact *= num
            num -= 1
        print(f"your factorial of {t_num} is {fact}")

# تمرین کلاسی 
    case 6:
        num = int(input("\nplease enter a num to see if its a prime number or not: "))
        count = 0
        for i in range (2,num-1):
            if num % i == 0:
                print("\nthe num you entered is not prime ")
                break
        else :
            print("\nthe num you entered is prime ")

# چالش اسلاید
    case 7:
        balance = 1_000_000
        while True:
            print("""
                1 - balance
                2 - deposite
                3 - withdraw
                4 - exit
                     """)
            
            entry = int(input("enter a option in menu: (1,2,3,4): "))

            if entry == 1:
                 
                 print(f"your account balance is {balance}")

            elif entry == 2:

                deposit_val = int(input("please enter a value for deposit: "))

                if deposit_val <= 0:
                    print("please enter a valid number!")
                else :
                    balance -= deposit_val
                    print(f"succes! your balance after deposite is {balance} ")

            elif entry == 3:

                withdraw_val = int(input("please enter a value for withdrtaw: "))

                if withdraw_val <= 0:
                    print("please enter a valid number!")
                else :
                    balance += withdraw_val
                    print(f"succes! your balance is after withdraw is {balance} ")

            elif entry == 4:
                break   