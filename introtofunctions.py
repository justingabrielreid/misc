#!/usr/bin/python

#introductions to functions in py
#functions are useful for code that is used multiple times

""" Functions are defined with three components: 
header: def functioname(parameters)


"""

def main():
    meal_cost = float(input('Enter the cost of your bill: '))
    meal_cost_with_tax = tax(meal_cost)
    meal_cost_with_tip = tip(meal_cost)
    meal_cost_with_both = tip(tax(meal_cost))
    print "With tax: %.2f" % meal_cost_with_tax
    print "With tip: %.2f" % meal_cost_with_tip
    print "With tax and tip: %.2f" % meal_cost_with_both
  
def tax(bill):
	#adds 8% tax to a restauraunt bill
	bill = bill*1.08
	#print "With tax: %f" % bill 
	return bill

def tip(bill):
	#adds a 15% tip to a restaurant bill
	bill = bill*1.15
	#print "With tip: %f" % bill 
	return bill 

if __name__ == '__main__':
    main()
