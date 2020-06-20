"""person.py: Person module of the Bank Account project."""

import sys

__author__ 	= "YOUR_NAME"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ 	= "TODAY'S DATE"

class Person:
	"""Defines the Person class."""
	def __init__(self, firstName, lastName, address):
		self.firstName = firstName
		self.lastName = lastName
		self.address = address

	def __str__(self):
		return 'FIRST NAME: {}\nLAST NAME: {}\nADDRESS: {}'.format(self.firstName,self.lastName,self.address)

	def get_first_name(self):
		return self.firstName

	def get_last_name(self):
		return self.lastName

	def get_address(self):
		return self.address

	def set_first_name(self,name):
		self.firstName = name

	def set_last_name(self,name):
		self.lastName = name

	def set_address(self,address):
		self.address = address