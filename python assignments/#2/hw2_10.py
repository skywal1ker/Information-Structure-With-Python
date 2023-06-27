#10 Task


"""45. The world record in the 100-meter dash is 9.58 seconds, set by Usain Bolt. Write a
program that prompts for a runner’s time in the 100 meter dash. Given that there are
approximately 3.28 feet in a meter and 5280 feet in a mile, calculate and print the runner’s
average speed in miles per hour."""

distance = 100
time = 9.58
hours = 3600
meters = 1000
miles_per_hour = (distance / time) * (hours / meters) / 1.609


print(miles_per_hour)