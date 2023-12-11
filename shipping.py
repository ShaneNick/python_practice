# Weight of the package
weight = 41

# Premium shipping cost (a fixed cost)
premisumShipping = 125

# Ground Shipping

# Calculate ground shipping cost based on weight
ground_shipping_cost = 0  # Initialize the cost variable

if weight <= 2:
    ground_shipping_cost = weight * 1.50 + 20
elif 2 < weight <= 6:
    ground_shipping_cost = weight * 3.00 + 20
elif 6 < weight <= 10:
    ground_shipping_cost = weight * 4.00 + 20
elif weight > 10:
    ground_shipping_cost = weight * 4.75 + 20

# Display ground shipping cost
print("Your Total for ground shipping will be:")
print(ground_shipping_cost)

# Drone Shipping

# Calculate drone shipping cost based on weight
drone_shipping_cost = 0  # Initialize the cost variable

if weight <= 2:
    drone_shipping_cost = round(weight * 4.50)
elif 2 < weight <= 6:
    drone_shipping_cost = round(weight * 9.00)
elif 6 < weight <= 10:
    drone_shipping_cost = round(weight * 12.00)
elif weight > 10:
    drone_shipping_cost = round(weight * 14.25)

# Display drone shipping cost
print("Your Total for drone shipping will be:")
print(drone_shipping_cost)

# Display Premium Shipping cost
print("If you wanted to use premium shipping it costs " + str(premisumShipping))
