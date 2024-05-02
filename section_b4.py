
def employeeBonusCalculation():
    while True:
        salary = int(input('Enter your salary amount:'))
        yearOfService = int(input('Enter your years of service:'))

        if yearOfService > 4:
            netBonusAmount = int((8/100) * salary)
        else:
            netBonusAmount = 0
        
        print(f'Your net bonus amount is: {netBonusAmount}')
        run = int(input('Press 1 to continue or any other number to quit: '))

        if run != 1:
            break
employeeBonusCalculation()


def saccoTransaction():
    accountbalance = 0
    run = 1
    while run == 1:
        print('\nWelcome to WITU Sacco.')
        print('1. Deposit Money')
        print('2. Withdraw Money')
        print('3. Check Balance')
        
        studentChoice = int(input('Enter your selection (1, 2, or 3): '))

        if studentChoice == 1:
            print('\nProcessing a deposit transaction.')
            depositAmount = int(input('Enter amount to be deposited: '))
            
            if depositAmount < 1000:
                print('Minimum deposit is 1000.')
            else:
                accountbalance += depositAmount
                print(f'Dear student, you have deposited {depositAmount:,}, and your new account balance is {accountbalance}.')

        elif studentChoice == 2:
            print('\nProcessing a withdraw transaction.')
            withdrawAmount = int(input('Enter amount to be withdrawn: '))
            
            if accountbalance == 0:
                print('Your balance is 0.')
            elif withdrawAmount < 500:
                print('Minimum withdraw amount is 500.')
            elif withdrawAmount > accountbalance:
                print('Withdraw failed, insufficient funds.')
            else:
                accountbalance -= withdrawAmount
                print(f'Dear student, you have withdrawn {withdrawAmount:,}, and your new account balance is {accountbalance}.')
        
        elif studentChoice == 3:
            print(f'Your account balance is {accountbalance:.2f}.')
        
        else:
            print('You entered a wrong choice! Please select 1, 2, or 3.\n')
        
        run = int(input('Enter 1 to continue or any other number to exit: '))
        if run != 1:
            print('Thanks for using WITU Sacco.')
            break

saccoTransaction()


