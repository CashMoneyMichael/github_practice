print("Welcome to the space travel calculator.")

distance = float(input("Enter the distance to your destination (in light-years) "))

speed = float(input("Enter the speed of your spaceship (as a fraction of the speed of light) "))

time = distance / speed

print("It will take", time, "years to reach your destination.")