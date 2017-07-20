# -*- coding: utf-8 -*-
"""
@author: rajat
"""

balance = 3926
annualInterestRate = 0.2

monthlyPayment = 10 # monthly payment is multiples of 10, so start with 10
monthlyInterestRate = annualInterestRate / 12.0

while True: # run infinite loop until, break when we reach lowest monthly payment
    unpaidBalanceEachMonth = balance
    for i in range(12): # run loop for 12 months
        monthlyUnpaidBalance = unpaidBalanceEachMonth - monthlyPayment
        unpaidBalanceEachMonth = monthlyUnpaidBalance  + monthlyInterestRate *\
                                        monthlyUnpaidBalance
    if(unpaidBalanceEachMonth <= 0):  # check if the unpaid balance has reached 
                                     #  zero at end of one year for that
                                    #   particular monthly installment rate 
        print ("Lowest Payment:", monthlyPayment)
        break
    else:
        monthlyPayment += 10 #monthly payment is multiple of 10          
