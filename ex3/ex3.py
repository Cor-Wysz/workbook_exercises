print("I will now count my chickens:") # An overview of PEMDAS

print("Hens", 25 + 30 / 6) # First; 30 / 6 = 5, then 25 + 5 = 30.0
print("Roosters", 100 - 25 * 3 % 4) # First; 25 * 3 = 75, then 75 % 4 = 3. Finally, 100 - 3 = 97. 

# print(75 % 4) % is a module. The left integer is  divided by the right. The value is equal to the remainder.

print("Now I will count the eggs:")

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6) # First 1 / 4 = 0.25. Next, 4 % 2 = 0, becuase 4 / 2 has no remainder. Then 3 + 2 + 1 - 5 + (0) - 0.25 + 6 = 6.75

print("Is it true 3 + 2 < 5 - 7?") # 5 is not < -2, so line 12 is False. 

print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2) # A question, an operation with addition.
print("What is 5-7?", 5 - 7) # A question, an operation with subtraction.

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > -2) # 5 is greater than -2, so line 23 is True.
print("Is it greater or equal?", 5>= -2) # 5 is greater than or equal to -2, so line 24 is True.

print("Is it less or equal?", 5<= -2) # 5 is NOT less than or qual to -2, so line 26 is False. 
