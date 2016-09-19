prices = {
    "banana" : 4,
    "apple" : 2,
    "orange" : 1.5,
    "pear" : 3
    }
##print (price)

##for key in prices:
##    print (key, ":", prices [key])

stock = {
    "banana" : 5,
    "apple" : 0,
    "orange" : 6,
    "pear" : 8
    }
##print ( "In Chip's Store have:" )
##for key in stock:
##    print (key, ":", stock [key])
##print ( "All the price is:" )
##for key in prices:
##    print (key, ":", prices [key])
    

print ("In Chip's Store:")
print ()
def compute_bill ( fruit ):
    print ( fruit )
    print ( "price", ":", prices [fruit])
    print ( "stock", ":", stock [fruit])
total = 0
for key in prices:
    compute_bill(key)
    print ()
    total = total + stock[key]*prices[key]
print ("If we sold all of them, we can earn totally is: ", total)
    
