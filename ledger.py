import sqlite3
import dbcontrol

class Account(object):

    def __init__(self,name = "",balance = 0):
        self.name = name
        self.balance = balance

    def getBalance():
        return self.balance

    def deposit(amount):
        self.balance += amount

    def withdrawl(amount):
        self.balance -= amount

    def loadAccount(name):
        pass


class Transactions(Account):

    def __init__(self,date,memo,amount):
        self.date = date
        self.memo = memo
        self.amount = float(amount)

    def saveTransaction(account):
        pass

    def pullTransactions(paramater):
        pass










def main():
    print "Welcome to your ledger\n"
    print "Please select from the following options\n"
    print "1: Create new account"
    print "2: Open exsisting account"
    print "3: Exit"
    selection = 0
    while selection < 1 or selection > 3:
        selection = int(input())
        if selection == 1:
            print "Please enter a name for the account"
            name = raw_input("Name")
            print "Please enter the starting balance of the account"
            balance = raw_input("Balance")
        elif selection == 2:
            pass
        elif selection == 3:
            print "Thank you for using your ledger"
            exit
        else:
            print"Incorrect input please try again"

if __name__ == '__main__':
    main()
