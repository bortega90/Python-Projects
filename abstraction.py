from __future__ import division


from abc import ABC, abstractmethod


class house(ABC):
    def downPayment(self, amount):
        print('Your down payment amount is: ', amount)

#pass b/c we are inputting amount when we call the function
    def cost(self, amount):
        print('The house costs {}'.format(amount))

class mortage(house):
    #this will give us the montly amount... i wanted to input more variables
    #and simple formula to get the monthly amount but had a hard time trying
    #to divide values with variables so i gave up and just input amounts
    def payment(self, amount):
        print('Your monthly payment will be ${}'.format(amount))


obj = mortage()
obj.cost("260,000")
obj.downPayment("20,000")
obj.payment("611.11")
