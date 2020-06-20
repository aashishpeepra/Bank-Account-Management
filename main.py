"""main.py: Main module of the Bank Account project."""

import sys
from person import Person
from bank_account import Bank_Account

__author__ 	= "YOUR_NAME"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ 	= "TODAY'S DATE"

def person_test_cases():
	"""Runs test cases against Person class.
	Returns:
        int: Error code after execution (0 if OK).
	"""
	
	"""The following code introduces you to writing simple test cases
		to test your code. When implementing and using complex classes,
		it is important to continuously test your code as, sometimes,
		even a minor change may inadvertently break some parts of
		your program. Here, the basic getter and setter methods are
		being tested to make sure they operate as intended. As soon as
		a single test fails, an appropriate message is printed out to
		console and the program terminates with an error code. Note
		that it is very important to properly identify your test cases.
		If all tests pass, an appropriate success message is printed
		to console, and the program terminates with code 0.
	"""
	# Test PERSON_TEST_1: Tests the constructor method.
	try:
		person_1 = Person('Jane', 'Doe', '123 Fake St., Fakeville, FA 12345, USA')
		person_2 = Person('Rupert', 'Smith', '1337 Noob Ave., Fake City, FA 54321, USA')
	except Exception as e:
		print(str(e))
		print('FAILED PERSON_TEST_1')
		return 1
	
	# Test PERSON_TEST_2: Tests the string method.
	if str(person_1) != 'FIRST NAME: Jane\nLAST NAME: Doe\nADDRESS: 123 Fake St., Fakeville, FA 12345, USA':
		print('FAILED PERSON_TEST_2')
		return 2
	
	# Test PERSON_TEST_3: Tests get_first_name method.
	if person_1.get_first_name() != 'Jane':
		print('FAILED PERSON_TEST_3')
		return 3
	
	# Test PERSON_TEST_4: Tests get_last_name method.
	if person_1.get_last_name() != 'Doe':
		print('FAILED PERSON_TEST_4')
		return 4
	
	# Test PERSON_TEST_5: Tests get_address method.
	if person_1.get_address() != '123 Fake St., Fakeville, FA 12345, USA':
		print('FAILED PERSON_TEST_5')
		return 5
	
	# Test PERSON_TEST_6: Tests set_first_name method.
	person_2.set_first_name('John')
	if person_2.get_first_name() != 'John':
		print('FAILED PERSON_TEST_6')
		return 6
	
	# Test PERSON_TEST_7: Tests set_last_name method.
	person_1.set_last_name('Smith')
	if person_1.get_last_name() != 'Smith':
		print('FAILED PERSON_TEST_7')
		return 7
	
	# Test PERSON_TEST_8: Tests set_address method.
	person_1.set_address('1337 Noob Ave., Fake City, FA 54321, USA')
	if person_1.get_address() != '1337 Noob Ave., Fake City, FA 54321, USA':
		print('FAILED PERSON_TEST_8')
		return 8
	
	print('PASSED ALL PERSON TESTS')
	return 0

def bank_account_test_cases():
	"""Runs test cases against Bank_Account class.
	Returns:
        int: Error code after execution (0 if OK).
	"""
	
	"""The following code introduces you to writing simple test cases
		to test your code. When implementing and using complex classes,
		it is important to continuously test your code as, sometimes,
		even a minor change may inadvertently break some parts of
		your program. Here, the basic getter and setter methods are
		being tested to make sure they operate as intended. As soon as
		a single test fails, an appropriate message is printed out to
		console and the program terminates with an error code. Note
		that it is very important to properly identify your test cases.
		If all tests pass, an appropriate success message is printed
		to console, and the program terminates with code 0.
	"""
	person_1 = Person('Jane', 'Doe', '123 Fake St., Fakeville, FA 12345, USA')
	person_2 = Person('Rupert', 'Smith', '1337 Noob Ave., Fake City, FA 54321, USA')
	# Test BANK_ACCOUNT_TEST_1: Tests the constructor method.
	try:
		account_1 = Bank_Account(123, person_1, 45.50)
		account_2 = Bank_Account(456, person_2, 30.0)
	except Exception as e:
		print(str(e))
		print('FAILED BANK_ACCOUNT_TEST_1')
		return 1
	
	# Test BANK_ACCOUNT_TEST_2: Tests the string method.
	if str(account_1) != 'ACCOUNT No: 123\nBALANCE: $45.50\nCARD INFO:\nNone':
		print('FAILED BANK_ACCOUNT_TEST_2')
		return 2
	
	# Test BANK_ACCOUNT_TEST_3: Tests get_account_number method.
	if account_1.get_account_number() != 123:
		print('FAILED BANK_ACCOUNT_TEST_3')
		return 3
	
	# Test BANK_ACCOUNT_TEST_4: Tests get_owner method.
	if account_1.get_owner() != person_1:
		print('FAILED BANK_ACCOUNT_TEST_4')
		return 4
	
	# Test BANK_ACCOUNT_TEST_5: Tests get_balance method.
	if account_1.get_balance() != 45.5:
		print('FAILED BANK_ACCOUNT_TEST_5')
		return 5
	
	# Test BANK_ACCOUNT_TEST_6: Tests deposit method.
	account_1.deposit(15.15)
	if account_1.get_balance() != 60.65:
		print('FAILED BANK_ACCOUNT_TEST_6')
		return 6
	
	# Test BANK_ACCOUNT_TEST_7: Tests transfer method for success.
	amount_transferred = account_1.transfer(account_2, 20.0)
	if account_1.get_balance() != 40.65 or account_2.get_balance() != 50.0 or amount_transferred != 20.0:
		print('FAILED BANK_ACCOUNT_TEST_7')
		return 7
	
	# Test BANK_ACCOUNT_TEST_8: Tests transfer method for failure.
	amount_transferred = account_1.transfer(account_2, 50.0)
	if account_1.get_balance() != 40.65 or account_2.get_balance() != 50.0 or amount_transferred is not None:
		print('FAILED BANK_ACCOUNT_TEST_8')
		return 8
	
	print('PASSED ALL BANK ACCOUNT TESTS')
	return 0

def main(argv):
	"""Main function of the script.
	Args:
		argv (list): Contains command-line arguments passed to the script.
	Returns:
        int: Error code after execution (0 if OK).
	"""
	error_code = 0
	
	error_code = person_test_cases()
	error_code = bank_account_test_cases()
	
	return error_code

if __name__ == '__main__':
	error_code = main(sys.argv[1:])
	print('[+] Terminated with code: ' + str(error_code))
	sys.exit(error_code)