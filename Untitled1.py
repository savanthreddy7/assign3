#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Employee:
    # Class variable to count the number of employees
    employee_count = 0

    def __init__(self, name, family, salary, department):
        # Instance variables
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department

        # Increment the employee count
        Employee.employee_count += 1

    def average_salary(self, *salaries):
        total_salary = sum(salaries) + self.salary
        average = total_salary / (len(salaries) + 1)  # +1 to include the current instance's salary
        return average


class FulltimeEmployee(Employee):
    def __init__(self, name, family, salary, department, bonus):
        # Call the constructor of the base class (Employee)
        super().__init__(name, family, salary, department)

        # Instance variable specific to FulltimeEmployee
        self.bonus = bonus


# Create instances of Employee and FulltimeEmployee
employee1 = Employee("John Doe", "Doe Family", 50000, "HR")
employee2 = Employee("Jane Smith", "Smith Family", 60000, "IT")
fulltime_employee = FulltimeEmployee("Alice Johnson", "Johnson Family", 80000, "Marketing", 10000)

# Call member functions
average_salary_result = employee1.average_salary(employee2.salary)
print(f"Average Salary for {employee1.name} and {employee2.name}: {average_salary_result}")

average_salary_result_fulltime = fulltime_employee.average_salary()
print(f"Average Salary for {fulltime_employee.name}: {average_salary_result_fulltime}")

# Print the total number of employees
print(f"Total number of employees: {Employee.employee_count}")


# In[2]:


import numpy as np

# Create a random vector of size 20 with float values in the range 1-20
random_vector = np.random.uniform(1, 20, size=20)

# Reshape the array to a 4 by 5 matrix
reshaped_array = random_vector.reshape(4, 5)

# Replace the max in each row with 0 (along axis=1)
reshaped_array[np.arange(reshaped_array.shape[0]), np.argmax(reshaped_array, axis=1)] = 0

# Print the original array, reshaped array, and the result after replacement
print("Original Vector:")
print(random_vector)
print("\nReshaped Array (4 by 5):")
print(reshaped_array)
+++


# In[3]:


import numpy as np

# Create a random vector of size 20 with float values in the range 1-20
random_vector = np.random.uniform(1, 20, size=20)

# Reshape the array to a 4 by 5 matrix
reshaped_array = random_vector.reshape(4, 5)

# Replace the max in each row with 0 (along axis=1)
reshaped_array[np.arange(reshaped_array.shape[0]), np.argmax(reshaped_array, axis=1)] = 0

# Print the original array, reshaped array, and the result after replacement
print("Original Vector:")
print(random_vector)
print("\nReshaped Array (4 by 5):")
print(reshaped_array)


# In[ ]:




