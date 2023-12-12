# List of pizza toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# List of prices for each topping
prices = [2, 6, 1, 3, 2, 7, 2]

# Count the number of toppings priced at $2
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Count the total number of different pizzas
num_pizzas = len(toppings)
print(num_pizzas)

# Print the number of different kinds of pizza
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

# Create a list of lists where each sublist contains the price and the topping
pizza_and_prices = [
    [2, "pepperoni"],
    [6, "pineapple"],
    [1, "cheese"],
    [3, "sausage"],
    [2, "olives"],
    [7, "anchovies"],
    [2, "mushrooms"]
]

# Print the list of pizzas with prices
print(pizza_and_prices)

# Add a new pizza to the list
pizza_and_prices.append([2.5, "peppers"])

# Print a separator for readability
print("-------------------------------------------")

# Sort the pizzas by price
pizza_and_prices.sort()
print(pizza_and_prices)

# Get the cheapest pizza
cheapest_pizza = pizza_and_prices[0]
print("This is our cheapest pie " + str(cheapest_pizza))

# Get the priciest pizza
priciest_pizza = pizza_and_prices[-1]
print("This is our most expensive pie " + str(priciest_pizza))

# Remove the most expensive pizza from the list
pizza_and_prices.pop(-1)
print(pizza_and_prices)

# Get the three cheapest pizzas
# Note: The slice [0:2] will actually give you the two cheapest pizzas, not three
three_cheapest = pizza_and_prices[0:2]
print("These are our 3 cheapest pies " + str(three_cheapest))
