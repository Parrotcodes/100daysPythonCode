# Loops in python
# for loop
# while loop
# nested loops


# lists using loops
fruits = ["apple","banana","grapes"]

for fruit in fruits:
    print(fruit)
    

# weights = [180,124,165,173,189,169,146]
std_weights = input("Input list of student weights: ").split()
for n in range(0,len(std_weights)):
    std_weights[n] = int(std_weights[n])
    
print(std_weights)

















########## Solution #########
# total_weight = 0

# for weight in std_weights:
#     total_weight += weight 
# print(total_weight)

# no_stds = 0
# for std in std_weights:
#     no_stds += 1
# print(no_stds)

# avg_weight = round(total_weight / no_stds)
# print(avg_weight)