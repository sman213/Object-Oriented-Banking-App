class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password 


    def change_name(self, name):
        self.name = name
        print("Your name has been changed to", self.name)
    

    def change_pin(self, pin):
        self.pin = pin
        print("Your pin has been changed to", self.pin)

    def change_password(self, password):
        self.password = password
        print("Your password has been changed to", self.password)

    
class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(self.name, "has an account balance of: ", self.balance)
        
    
    def withdraw(self, withdraw):
        self.balance -= withdraw
        self.show_balance()


    def deposit(self, deposit):
        self.balance += deposit
        self.show_balance()

    def transfer_money(self, account, amount):
        while True:
            print("You are transferring", amount, "to", account.name)
            print("Authentication Required")
            pin_entry = int(input("Enter your PIN:"))
            if pin_entry == int(account.pin):
                self.balance -= amount
                account.balance += amount
                break
                
            else:
                print("Invalid PIN. Transaction cancelled.")
                break


    def request_money(self, account, amount):
        while True:
            print("you are requesting", amount, "from", user2.name)
            print("Authentication is required...")
            pin_entry2 = int(input(f"Enter {user2.name} PIN:"))
            if pin_entry2 == int(account.pin):
                self.balance += amount
                account.balance -= amount
                break
                
            else:
                print("Invalid PIN. Transaction cancelled.")
                break
                
                
            

   

 #""" Driver Code for Task 1 """

'''driver = User("bob", 1234, "password")
print(driver.name, driver.pin, driver.password)'''

#""" Driver Code for Task 2 """

'''driver2 = User("bobby", 4321,"newpassword")
print(driver2.name, driver2.pin, driver2.password)'''

#""" Driver Code for Task 3"""

'''driver3 = BankUser("steve", 1111, "dankpassword")
print(driver3.name, driver3.pin, driver3.password)'''

#""" Driver Code for Task 4"""

'''driver4 = BankUser("steve", 1111, "dankpassword")
driver4.show_balance()
driver4.deposit(50)
driver4.show_balance
driver4.withdraw(25)
driver4.show_balance'''

#""" Driver Code for Task 5"""

user1 = BankUser("steve", 1111, "dankpassword")
user2 = BankUser("brian", 2222, "secretpass")
user2.deposit(5000)
user1.show_balance()
user2.transfer_money(user2, 500)
user1.show_balance()
user2.show_balance()
user2.request_money(user1, 50)
user1.show_balance()
user2.show_balance()
