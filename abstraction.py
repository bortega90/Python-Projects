from __future__ import division


from abc import ABC, abstractmethod


class house(ABC):
   
    def downPayment(self, amount):
        pass

    @abstractmethod
    def cost(self, amount):
        pass

class mortage(house):
    #this will give us the montly amount... i wanted to input more variables
    #and simple formula to get the monthly amount but had a hard time trying
    #to divide values with variables so i gave up and just input amounts
    def cost(self, amount):
        print('Your monthly payment will be ${}'.format(amount))


obj = mortage()
obj.cost("611.11")
obj.downPayment("20,000")

