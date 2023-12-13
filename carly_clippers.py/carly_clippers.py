# List of hairstyle names
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]  

# List of haircut prices
prices = [30, 25, 40, 20, 20, 35, 50, 35]  

# Number of customers for each haircut last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]  

# Calculate total price
total_price = 0
for i in prices:
    total_price += i  
print(total_price)  

# Calculate average price  
average_price = total_price / len(prices)
rounded_average_price = round(average_price, 2)
print("Average Haircut Price: " + str(rounded_average_price))

# List comprehension to apply $5 discount 
new_prices = [item -5 for item in prices] 
print(new_prices)

# Print all hairstyles
for i in range(len(hairstyles)):
    print(hairstyles[i])
    
# Calculate total revenue
total_revenue = [prices[i] * last_week[i] for i in range(len(hairstyles))]  
print(total_revenue)

# Calculate average daily revenue
average_daily_revenue = sum(total_revenue) / 7
print(round(average_daily_revenue))

# List cuts under $30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)