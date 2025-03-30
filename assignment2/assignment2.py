# Task 2
import csv

def read_employees():
  employees_dict = {}
  rows = []

  try: 
    with open('../csv/employees.csv', 'r') as file:
      content = csv.reader(file)

      #read the first row for headers
      headers = next(content)
      employees_dict['fields'] = headers
      # print(headers)

      #remaining rows
      for row in content:
        rows.append(row)

      employees_dict['rows'] = rows

  except Exception as e:
    print(f"An error occured: {e}")

  return employees_dict

employees = read_employees()
print(read_employees())

# Task 3
def column_index(header):
  return employees["fields"].index(header)
  

employee_id_column = column_index("employee_id")
print(column_index("employee_id"))

# Task 4

# def first_name(row_number):
#   first_name_column = column_index("first_name")
#   return employees["rows"][row_number][first_name_column]

# row_number = 2
# first_name = first_name(row_number)
# print(f"here: {row_number} and {first_name}")

# Task 5

def employee_find(employee_id):
  employee_id_col_index = column_index("employee_id")

  if employee_id_col_index is not None:
        
    def employee_match(row):
      return int(row[employee_id_column]) == employee_id
        
      # Use filter to find matching rows
    matches = list(filter(employee_match, employees["rows"]))
    return matches
    
  else:
    return []
  
employee_id_enter = 1
employees_found = employee_find(employee_id_enter)

# Task 6
def employee_find_2(employee_id):

  employee_id_column = column_index("employee_id")

  if employee_id_column is not None:
    # Use filter with a lambda function to find matching rows
      matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
      return matches
  else:
      return []

# Task 7

def sort_by_last_name():
  last_name_column_index = column_index("last_name")

  if last_name_column_index is not None:
    
    employees["rows"].sort(key=lambda row: row[last_name_column_index])
    return employees["rows"]
  else:
      return []
  
sorted_employees = sort_by_last_name()
print("Sorted by last name:")
for row in sorted_employees:
    print(row)
  

# Task 8
def employee_dict(row):
  employee_info ={}
  employee_id_column_index = column_index("employee_id")

  for index, header in enumerate (employees["fields"]):
    if index != employee_id_column_index:
      employee_info[header] = row[index]

  return employee_info

test_row = employees["rows"][0] #test here
employee_info_dict = employee_dict(test_row)
print("Employee dictionary (excluding employee_id):")
print(employee_info_dict)

# Task 9
def all_employees_dict():
  employees_dict = {}
  employee_id_column_index = column_index("employee_id")

  for row in employees["rows"]:
    employee_id = row[employee_id_column_index]
    employees_dict[employee_id] = employee_dict(row)

  return employees_dict

all_employees = all_employees_dict()
print("All employees dictionary:")
print(all_employees)

# Task 10

import os

def get_this_value():
  return os.environ.get('THISVALUE')
 
# Task 11

import custom_module

def set_that_secret(new_secret):
  custom_module.set_secret(new_secret)

set_that_secret("new_secret_value")
print(custom_module.secret)

# Task 12
import csv

def read_csv_to_dict():

  with open('../csv/minutes1.csv', 'r') as file:
    reader = csv.reader(file)
    headers = next(reader) 
    rows = [tuple(row) for row in reader]  
    return {'fields': headers, 'rows': rows}
  
  with open('../csv/minutes2.csv', 'r') as file:
    reader = csv.reader(file)
    headers = next(reader) 
    rows = [tuple(row) for row in reader]  
    return {'fields': headers, 'rows': rows}

def read_minutes():
  minutes1 = read_csv_to_dict('../csv/minutes1.csv')
  minutes2 = read_csv_to_dict('../csv/minutes2.csv')
  return minutes1, minutes2

#store the values
minutes1, minutes2 = read_minutes()

#Task 13

def create_minutes_set():

  set1 = set(minutes1['rows'])
  set2 = set(minutes2['rows'])

  combine_both_sets = set1.union(set2)

  return combine_both_sets

minutes_set = create_minutes_set

# Task 14
from datetime import datetime

def create_minutes_list():
  minutes_list = list(minutes_set)



# Task 15
def write_sorted():


