# Consider a file containing temperature data one reading per line
# a) Load the file into a list as float numbers.
# b) Do this through comprehension
# c) Filter the contents of the file based on a condition without having an interim list (all values > 25)
# Try to use filter and lambda where possible.

# Load the file into a list of float numbers and do it through comprehension
with open("temperature.txt","r")as f:
    temps = [float(line.strip()) for line in f]
print(temps)

# Filter the contents of the file based on a condition without having an interim list (all values > 25)
# Try to use filter and lambda where possible.
with open("temperature.txt", "r") as f:
    filtered_temps = filter(
        lambda x: x > 25,
        map(lambda line: float(line.strip()), filter(lambda line: line.strip(), f))
    )
    filtered_list = list(filtered_temps) # convert result to a list if used multiple times
print(filtered_list)