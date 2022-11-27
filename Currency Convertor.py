currency={"USD":81,"EUR":84,"INR":1,"CAD":61,"GBP":98,"CNH":11,"RUB":1.3,"VND":0.0033,"NZD":51,"PKR":0.36} # Add more currency here
def convert(c1,a,c2): 
    if(c2=="INR"):
        print("The Currency After Converting into %s is"%c2,(amount*currency[c1]))
    elif(c1=="INR"):
        print("The Currency After Converting into %s is"%c2,(amount/currency[c2]))
    else:    
        print("The Currency After Converting into %s is"%c2,(amount/currency[c1])*currency[c2])

print(" ---------------------- ")
print("|  Currency Converter  |")
print(" ---------------------- ")
for i in currency.keys():
    print(i)
c1=input("Enter The Currency: ") #The Currency given
amount=eval(input("Enter The Amount: ")) # The amount in the given currency
c2=input("Enter The Currency you want to convert to: ") # The currency you want to covert the amountUSD
convert(c1,amount,c2)