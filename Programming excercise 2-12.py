# Named constants
COMISSION_RATE = 0.3
NUM_SHARES = 2000
PURCHASE_PRICE = 40.0
SELLING_PRICE = 42.75

#Variables
amountPaidForStock = 0.0 #Amount paid for the stock
purchaseCommission = 0.0 #Commission paid to purchase stock
totalPaid = 0.0          #Total amount Paid
stockSoldFor = 0.0       #Amount stock sold for
sellingcommission = 0.0  #Commission paid to sell stock
totalRecieved = 0.0      #Total amount recieved
profitorloss = 0.0       #Amount of profit or loss

#calculate the amount that Joe paid for the stock, not
#including the commission.
AmountPaidForStock = PURCHASE_PRICE*NUM_SHARES

#calculate the amount of commission that Joe paid his broker
#when he bought the stock.
purchasecomssion = amountPaidForStock*COMISSION_RATE

#calculate the total amount that Joe paid, which is the amount
#he paid for the stock plus the commission he paid his broker.
totalpaid = amountPaidForStock+purchaseCommission

#calculate the total amount that Joe sold the stock for.
stocksoldfor = NUM_SHARES*SELLING_PRICE

#calculate the amount of commission that Joe paid his broker
#when he sold the stock.
sellingcommission = SELLING_PRICE*COMISSION_RATE

#calculate the amount of money left over, after Joe paid
#his broker.
totalrecieved = stocksoldfor-sellingcommission

# Print the required data.
print ("Amount paid for stock: $" , format (amountPaidForStock, '.2F'))
print ("commission paid on the purchase: $, format(purchaseCommission", '.2F')
print ("Amount the stock sold for : $", format(stocksoldfor,'.2F'))
print ("commission paid on the sale: $", format(sellingcommission, '.2F'))
print ("Profit ( or loss if negative): $", format(profitorloss, '.2F'))

