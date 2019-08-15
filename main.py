#!/usr/bin/env python3
"""
Module Docstring
"""
from nsetools import Nse
from tabulate import tabulate

__author__ = "Rwik"
__version__ = "0.1.0"
__license__ = "MIT"


def print_menu():       
	print (10 * "-" , "MENU" , 10 * "-")
	print ("1. Get Quote")
	print ("2. Get top gainers")
	print ("3. Get top loosers")
	print ("4. To be implimented")
	print ("5. Exit")
	print (70 * "-")    

loop=True      

while loop:          
	print_menu()    
	
	try:   
		nse = Nse()
		choice = int(input("Enter your choice [1-5]: "))
		if choice==1:   
			q = input("Enter stock symbol : ") 			
			q_obj = nse.get_quote(q)
			print(q_obj['averagePrice']) 
		elif choice==2:
			top_gainers = nse.get_top_gainers()
			print(tabulate(top_gainers))			
		elif choice==3:
			top_losers = nse.get_top_losers()
			print(tabulate(top_losers))
		elif choice==4:
			print("Menu 4 has been selected")
		elif choice==5:
			print("Menu 5 has been selected")
			loop=False # This will make the while loop to end as not value of loop is set to False
		else:
			print("Wrong option selection. Enter any key to try again..")
			
	except ValueError:
		print("Wrong option selection. Enter any key to try again..")





