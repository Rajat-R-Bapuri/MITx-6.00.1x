# -*- coding: utf-8 -*-
"""
@author: rajat
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for month in range(12):  #run loop for 12 months 
    monthlyInterestRate = annualInterestRate/12.0   
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    balance = monthlyUnpaidBalance  + monthlyInterestRate * monthlyUnpaidBalance

print("Remaining balance:", round(balance,2)) #round remaining balance to 2 decimal places
