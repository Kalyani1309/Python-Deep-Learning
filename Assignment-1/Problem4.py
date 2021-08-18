# problem 4 using Loops
WeightInLbs = []                                                # Create empty lists for weights in lbs and kgs
WeightInKgs = []

N = int(input("Enter number of Students: "))                    # Read number of students from the user input
print("Enter the weights for each student: ")

for i in range(0, N):                                           # Take weights for N students in a list
    WeightInLbs.append(float(input()))

for j in range(N):                                              # Append the converted weights in the WeightInKgs List
    WeightInKgs.append(WeightInLbs[j] * 0.454)

print("\nOriginal weights in lbs.: {}".format(WeightInLbs))     # Print outputs
print("Converted weights in kgs.: {}".format(WeightInKgs))

# ======================================================================================================================
# Problem 4 using List comprehensions
WeightInLbs = []                                                # Create empty lists for weights in lbs and kgs
WeightInKgs = []

N = int(input("\nEnter number of Students: "))                  # Read number of students from the user input
print("Enter the weights for each student: ")

for i in range(0, N):                                           # Take weights for N students in a list
    WeightInLbs.append(float(input()))

WeightInKgs = [weight * 0.454 for weight in WeightInLbs]        # Create WeightInKgs List using list comprehensions

print("\nOriginal weights in lbs.: {}".format(WeightInLbs))     # Print outputs
print("Converted weights in kgs.: {}".format(WeightInKgs))
