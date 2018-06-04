cars = 100 # Number of cars available.
space_in_a_car = 4.0 # Number of seats per car.
drivers = 30 # Number of able drivers
passengers = 90 # Number of available passengers
cars_not_driven = cars - drivers
cars_driven = drivers # Value equal to Line 3.
carpool_capacity = cars_driven * space_in_a_car
# Able drivers times seats available.  
average_passengers_per_car = passengers / cars_driven # Available passengers divided by able drivers


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")
