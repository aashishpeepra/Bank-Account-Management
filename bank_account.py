"""bank_account.py: Bank account module of the Bank Account project."""

import sys

__author__ 	= "YOUR_NAME"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ 	= "TODAY'S DATE"

class Bank_Account:
	"""Defines the Bank_Account class."""
	def __init__(self, accountNumber, owner, initialBalance):
		self.accountNumber = accountNumber
		self.owner = owner
		self.initialBalance = initialBalance
		self.bank_card = None

	def __str__(self):
		return 'ACCOUNT No: {}\nBALANCE: ${:,.2f}\nCARD INFO:\n{}'.format(self.accountNumber,self.initialBalance,self.bank_card)

	def get_account_number(self):
		return self.accountNumber

	def get_owner(self):
		return self.owner 

	def get_balance(self):
		return self.initialBalance

	def deposit(self, amount):
		self.initialBalance += amount

	def transfer(self,bank,amount):
		if amount>self.initialBalance:
			return None
		bank.initialBalance += amount
		self.deposit(-amount)
		return amount



