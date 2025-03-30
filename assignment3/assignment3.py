import pandas as pd
import numpy as np

# Task 1

dict = {
  "Name": ["Alice","Bob", "Charlie"],
  "Age": [25, 30, 35],
  "City": ["New York", "Los Angeles", "Chicago"]
}

task1_data_frame = pd.DataFrame(dict)
# print("Dataframe Task 1:")
print(task1_data_frame)

# Add new column
task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000, 80000, 90000]
print(task1_with_salary)

# Modify an existing column
task1_older = task1_with_salary.copy()
task1_older['Age'] += 1
print(task1_older)

# Save the DF as a CSV File
task1_older.to_csv("employees.csv", index=False)
print("DataFrame saved to employees.csv")

# Task 2
task2_employees = pd.read_csv("employees.csv")
print(task2_employees)

# Read data from a JSON file
import json

dict2 = {
  "Name": ["Eve","Frank"],
  "Age": [28, 40],
  "City": ["Miami", "Seattle"],
  "Salary": [60000, 95000]
}

json_object = json.dumps(dict2)

with open("additional_employees.json", "w") as outfile:
  outfile.write(json_object) 

json_employees = pd.read_json("additional_employees.json")
print(json_employees)

# combine data from JSON file into the df from the CSV file

more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)

#Task 3 Data Inspection
first_three = more_employees.head(3)
print(first_three)

last_two = more_employees.tail(2)
print(last_two)

employee_shape = more_employees.shape
print(employee_shape)

print(more_employees.info())

#Task 4 Data Cleaning

dirty_data = pd.read_csv('dirty_data.csv')
print(dirty_data)

clean_data = dirty_data.copy()
print(clean_data)

#remove dups
clean_data = clean_data.drop_duplicates()

#convert age to numeric and hanlde missing values
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')

#convert salary to numeric and replace known placeholders(unknown, n/a) with NaN
clean_data['Salary'] = clean_data['Salary'].replace("unknown", "n/a").fillna("NaN")
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')

#Fill Age with the mean and Salary with the median
mean_age = clean_data['Age'].mean()
clean_data['Age'] = clean_data['Age'].fillna(mean_age)

median_salary = clean_data['Salary'].median()
clean_data['Salary'] = clean_data['Salary'].fillna(median_salary)

#Convert Hire Date to datetime
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors="coerce") 

#Strip extra whitespace and standardize Name and Department as uppercase

clean_data["Name"] = clean_data["Name"].str.strip()
clean_data["Department"] = clean_data["Department"].str.strip()
clean_data["Name"] = clean_data["Name"].str.upper()
clean_data["Department"] = clean_data["Department"].str.upper()
print(clean_data)