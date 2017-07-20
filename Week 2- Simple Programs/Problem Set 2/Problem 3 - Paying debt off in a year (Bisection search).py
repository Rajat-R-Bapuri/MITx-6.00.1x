# -*- coding: utf-8 -*-
"""
@author: rajat
"""

balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12

'''
reasonable lower bound for this payment would be - 
If there was no interest, the debt can be paid off 
by monthly payments of one-twelfth of the original balance
'''
lowerBound = balance / 12

'''
reasonable upper bound for this payment would be -
Imagine that instead of paying monthly, we paid off the entire balance 
at the end of the year. What we ultimately pay must be greater than what 
we would've paid in monthly installments, because the interest was compounded 
on the balance we didn't pay off each month. So a good upper bound for the 
monthly payment would be one-twelfth of the balance, after having its interest 
compounded monthly for an entire year.
'''
upperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0

while True: # run loop until lowest payment rate is reached
    unpaidBalanceEachMonth = balance
    monthlyPayment = (lowerBound + upperBound) / 2
    for i in range(12): # run loop for 12 months
        monthlyUnpaidBalance = unpaidBalanceEachMonth - monthlyPayment
        unpaidBalanceEachMonth = monthlyUnpaidBalance  + monthlyInterestRate *\
                                        monthlyUnpaidBalance
    #watching the bisection search video in the course, we need consider a
    #epsilon value which is close enough to zero, so that we reach reasonable accuracy
    # here we consider epsilon to be 0.05
    if unpaidBalanceEachMonth > 0.05 : # check if unpaid balance at end of 
                                       # one year is close enough to zero
        lowerBound = monthlyPayment
    elif unpaidBalanceEachMonth < -0.05 :
        upperBound = monthlyPayment
    else:
        break
print("Lowest Payment:", round(monthlyPayment, 2))
