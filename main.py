print('Welcome to the Python Bank, where all your savings are safely kept!')
balance = 500


name = input('What is your name? ')
print('Hello, ' + name + '! How may we assist you today?')
print('1. Open a new account\n2. Deposit\n3. Withdraw\n4. Check balance\n5. Exit')
assistance = int(input('Please enter the number of your choice: '))


def new_account():
  print('Please enter the following information to create a new account:')  
  account_name = input('Full name: ')
  Date_of_birth = input('Date of birth: ')
  address = input('Address: ')
  email = input('Email: ')
  account_type = input('What type of account would you like to open?')
  print('You have successfully opened a ' + account_type + ' account.')

def deposit():
  print('Please enter the following information to deposit: ')
  account_name = input('Full name: ')
  input('Account number: ')  # Updated this line to remove assignment to account_number
  deposit_amount = input('How much would you like to deposit? ')
  print('You have successfully deposited $' + deposit_amount + ' to your account.')
  new_balance = int(deposit_amount) + int(balance)
  print('Your new balance is ' + str(new_balance) + '.')



def withdraw():
  print('Please enter the following information to withdraw: ')
  account_name = input('Full name: ')
  account_number = input('Account number: ')
  removal_amount = input('how much would you like to withdraw? ')
  print('You have successfully withdrawn $' + removal_amount + ' from your account.')
  new_balance = int(balance) - int(removal_amount)
  print('Your new balance is ' + str(new_balance) + '.')

def check_balance(): #function used to check balance
  print('Please enter the following information to check your balance: ')
  account_name = input('Full name: ')
  account_number = input('Account number: ')
  print('Your balance is ' + str(balance) + '.')
#add a user input asking the user if they want to withdraw or deposit money



#The if statements below are used to determine which function to call based on the user's input.
if assistance == 5:
  print('Thank you for using the Python Bank. Have a great day!')

if assistance == 1:
  new_account()

if assistance == 2:
  deposit()

if assistance == 3:
  withdraw()

if assistance == 4:
  check_balance()