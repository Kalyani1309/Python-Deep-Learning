# Create an empty dictionary
emp_dict = {}

# function to calculate average salary
def avg_salary():
    employee_count = len(emp_dict)
    total_salary = 0
    for key in list(emp_dict.keys()):
        total_salary += emp_dict[key][2]
    return total_salary / employee_count

# Employee class
class Employee():

    # constructor to intialize id, name, dept, sal, balance, isemployed variables
    def __init__(self, id, name, dept, sal, balance, isemployed = True):
        self.id = id
        self.name = name
        self.dept = dept
        self.sal = sal
        self.balance = balance
        self.isemployed = isemployed

    # Function to give raise to employees with percentage of a pay raise provided as input
    def giveRaise(self, emp_id, payrate):
        for key in list(emp_dict):
            if key == emp_id:
                emp_dict[emp_id][2] = (emp_dict[emp_id][2] * (100 + payrate)) / 100

    # Function to pay all the employees
    def Pay(self):
        for key in list(emp_dict):
            if emp_dict[key][4]:
                emp_dict[key][3] += emp_dict[key][2]

    # Function to remove the employess from payroll
    def Fire(self, emp_id):
        for key in emp_dict.keys():
            if key == emp_id:
                emp_dict[emp_id][4] = False

    # A Boolean function that should return if they are employed or not.
    def isEmployee(self):
        return self.isemployed

    def readFromFile(self):
        # Read the input file contents
        infile = open("Input", "r")
        # Loop through each line of the file
        for line in infile:
            # Split the line into words
            words = line.strip().split(" ")
            choice = words[0]
            if choice == 'NEW':
                str1 = " "
                e = Employee(words[1], str1.join(words[2:4]), words[4], float(words[5]), 0.0)
                emp_dict.update({e.id: [e.name, e.dept, e.sal, 0.0, e.isemployed]})
            elif choice == 'RAISE':
                self.giveRaise(words[1], float(words[2]))
            elif choice == 'PAY':
                self.Pay()
            elif choice == 'FIRE':
                self.Fire(words[1])
            else:
                print("Invalid input in file")


#Created a Parttime Employee class which inherits the properties of Employee class
class PartTime(Employee):
    def __init__(self, id, name, dept, sal, balance, isEmployed=True):
        Employee.__init__(self, id, name, dept, sal, balance, isemployed=True)

    # Created a new member function
    def changeEmployeeStatus(self):
        print("\nPart Time function called")

#Created a Fulltime Employee class which inherits the properties of Employee class
class FullTime(Employee):
    def __init__(self, id, name, dept, sal, balance, isEmployed=True):
        Employee.__init__(self, id, name, dept, sal, balance, isemployed=True)

    # Changed defination of isEmployee method from Employee class
    def isEmployee(self):
        print("\nFull Time function called")
        return self.isemployed

# Main body
if __name__ == '__main__':
    infile = open("input", "r")
    line = infile.readline()
    words = line.split(' ')
    emp = Employee(words[1], words[2:4], words[4], int(words[5]), 0)

    # Call read from file function
    emp.readFromFile()
    # print the contents of the employee dictionary
    print("Final Employee details: ")
    for key in list(emp_dict.keys()):
        print(key, ":", emp_dict[key])

    # open the output file to write the output contents
    outfile = open("output", "w")
    # Iterate over dictionary to get the final values
    for key in list(emp_dict.keys()):
        if emp_dict[key][4]:
            output_str = "ID: {}, Emp. Name: {}, Department: {}, Current salary: ${}\n".format(key, emp_dict[key][0],  emp_dict[key][1], str(emp_dict[key][2]))
            outfile.write(output_str + "\n")

        else:
            output_str = "ID: {}, Emp. Name: {}, Department: {}, Not employed with the company. Pay earned to date: ${}\n".format(key, emp_dict[key][0], emp_dict[key][1], str(emp_dict[key][3]))
            outfile.write(output_str + "\n")

    # Printing the number of employees and
    outfile.write("Total number of employees: " + str(len(emp_dict)) + "\n")
    outfile.write("\nAverage Salary paid to all employees: $" + str(avg_salary()))

    # Creating instance of PartTime class and calling member functions
    pt = PartTime(15, "Kalyani", "CS", 10000.0, 40000.0)
    pt.isEmployee()
    pt.changeEmployeeStatus()

    # Creating instance of FullTime class and calling member functions
    ft = FullTime(15, "Sweety", "CS", 10000.0, 50000.0)
    ft.isEmployee()


