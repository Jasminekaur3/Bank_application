import sys

class Bank():
	total_customers = 0

	def __init__(self, acc_balance, name):
		self.acc_balance = acc_balance
		self.name = name
		Bank.total_customers += 1

	def process_customer_request(self):
		self.greet()
		self.show_options()
		self.process_choices()

	def greet(self):
		print("Welcome!!")

	def show_options(self):
		print(''' 1.Check the balance\n 2.Deposit\n 3.Withdraw \n 4.Exit''')

	def process_choices(self):
		user_choice = int(input("Enter choices:"))
		if user_choice == 1:
			print(f"Your account baance is: {self.acc_balance}")

		elif user_choice == 2:
			deposit_amount = int(input("Enter amount to be deposited: "))
			self.acc_balance += deposit_amount
			print(f"Your account baance is: {self.acc_balance}")

		elif user_choice == 3:
			withdraw_amount = int(input("Enter the amount to withdraw: "))
			self.acc_balance -= withdraw_amount
			print(f"Your account baance is: {self.acc_balance}")

		elif user_choice == 4:
				print("Thank you. Visit again!")
				sys.exit()

		else:
			print("Wrong choice. Please enter one of the below options: ")
			print("1 2 3 4")
			sys.exit()

ram = Bank(1000, "Ram")
ram.process_customer_request()
