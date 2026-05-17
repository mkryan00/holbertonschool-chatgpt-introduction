#!/usr/bin/python3
class Checkbook:
    """
    Class description:
        A simple Checkbook system that manages a user's balance and allows
        deposits, withdrawals, and balance inquiries.
    """

    def __init__(self):
        """
        Function description:
            Initializes a new Checkbook instance with a starting balance of 0.0.

        Parameters:
            None

        Returns:
            None
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function description:
            Adds a specified amount to the current balance and displays
            the updated balance.

        Parameters:
            amount (float): The amount of money to deposit.

        Returns:
            None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function description:
            Withdraws a specified amount from the balance if sufficient funds exist.
            If not enough funds are available, an error message is displayed.

        Parameters:
            amount (float): The amount of money to withdraw.

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Function description:
            Displays the current account balance.

        Parameters:
            None

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Function description:
        Runs an interactive command-line interface for the Checkbook system,
        allowing the user to deposit, withdraw, check balance, or exit.
        Includes error handling to prevent crashes from invalid input.

    Parameters:
        None

    Returns:
        None
    """
    cb = Checkbook()

    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")

        if action.lower() == 'exit':
            break

        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")

        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")

        elif action.lower() == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
