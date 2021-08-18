# Assignment-2
Assignment-2

#### Complete the following:

#### Name: Kalyani Nikure
#### Email: kmn6bg@umkc.edu

<br/>

#### 1. Classes and objects:
Create a class Employee and then do the following:
a. Create a data member to count the number of Employees.
b. Create a constructor to initialize:
i. id, name, department, salary, balance, and isEmployed=True.

Create the following functions:
i. giveRaise: It takes in an integer, which is the percentage of a pay raise.
ii. Pay: This should pay the employee once. Their balance should increase by the amount they are paid.
iii. Fire: this should remove the employee from the payroll. It should set their payrate to 0, and isEmployed to false. (Note: Retain the records for the employee, just make sure they aren’t paid anymore.)
iv. sEmployed: a Boolean function that should return if they are employed or not.
d. Read employee data from input.txt to create instances of the Employee class:
i. File structure:
1. NEW: keyword to create a new employee following: ID, Name, Department, Salary
2. RAISE: keyword to give raise to a specific employee following: ID, raise_percentage that will change the emp. salary.
3. PAY: keyword to pay all employee once, balance should increase by the amount they are paid (salary).
4. FIRE: Keyword to remove the employee from payroll. Emp. Following is Emp. ID

e. Create a Fulltime and Parttime Employee class and it should inherit the properties of Employee class.
f. Create the instances of Fulltime and Parttime Employee class and call their member functions.

g. Create a function to average salary paid to all employees. Write the average salary paid to the end of output.txt file after printing the total number of employees.

h. Your program should output data to output.txt with the following format:
i. Emp. Name, ID ###, Department:
ii. If employed, write out their Salary in this format: Current salary: $##
iii. If NOT employed, you should write out: Not employed with the company.
iv. The employee’s balance to date: Pay earned to date: $##
v. Add a blank line between employees.
vi. ….
vii. Total number of employees: ###
viii. Average Salary paid to all employees: $###

![image](https://user-images.githubusercontent.com/30693095/122455172-bcc1be80-cf71-11eb-9b45-4d225ceac4a1.png)
The screenshot above shows the console output.
Program explaination: Created a class 'Employee' with a constructor to initialize values for id, name, dept, salary, balance, isemployed variables. I also created a emp_dict named dictionary to save the details of all employees.
I also created member functions giveRaise(), Pay(), Fire(), isEmployee() and readFromFile() to perform oprations on employee data and read the instructions from the input.txt file. Then, finally we are printing the output in the output.txt file in the format mentioned in the question.

Main() function makes a call to all the functions using the object of employee function.

![image](https://user-images.githubusercontent.com/30693095/122455297-d95df680-cf71-11eb-8bb3-8feafbbc81dd.png)
Screenshot above shows the final output in the output.txt file.


#### 2. Web scraping 
Write a simple program that parse a Wiki page mentioned below and follow the instructions: https://en.wikipedia.org/wiki/Machine_learning 
a. Print out the title of the page 
b. Find all the links in the page (‘a’ tag) 
c. Iterate over each tag(above) then return the link using attribute "href" using get
![image](https://user-images.githubusercontent.com/30693095/122308933-f8f21200-ced2-11eb-95b8-11d1755e8968.png)
I have created a class WikiScrapping to declare source_doc and soup variables. Defined functions like get_title and wiki_links to print the title of the page and get all the links from the 'href' tag.

#### 3. Numpy
1. Using NumPy create random vector of size 15 having only Integers in the range 1-20.
2. Reshape the array to 3 by 5
3. Print array shape.
4. Replace the max in each row by 0
5. Extract a diagonal from the array, and save as .npy file format.

![image](https://user-images.githubusercontent.com/30693095/122308882-e2e45180-ced2-11eb-98fb-81db232065ca.png)
The screenshot above shows the console output which contains the randomized array of size 15. I have also printed the reshaped array of 3* 5 size. 
We then replaced all the maximum valules of each row by 0 using np.where and np.max function.

Output written in .npy file
![image](https://user-images.githubusercontent.com/30693095/122309010-1c1cc180-ced3-11eb-89d0-bb7e8e46cca5.png)
I have also written the output of diagonal contents in the output.npy file.
