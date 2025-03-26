# Task 1

def hello():
  return "Hello!"


# Task 2

def greet(name):
  return f"Hello, {name}!"

# Task 3

def calc(x, y, z="multiply"):
  try:
    if z == "multiply":
      return x * y
    elif z == "add":
      return x + y
    elif z == "subtract":
      return x - y
    elif z == "divide":
      return x / y
    elif z == "modulo":
      return x % y
    elif z == "int_divide":
      return x // y
    elif z == "power":
      return pow(x,y)
    else:
      return "Error!"
  except ZeroDivisionError:
      return "You can't divide by 0!"
  except TypeError:
      return "You can't multiply those values!"

# Task 4

def data_type_conversion(value,y):
  try:
    if y == "float":
      return float(value)
    elif y == "str":
      return str(value)
    elif y == "int":
      return int(value)
  except Exception:
      return f"You can't convert {value} into a {y}."
  
# Task 5

def grade(*args):      
  try: 
    average = sum(args)/len(args)
    return "A" if average >= 90 else "B" if average >= 80 else "C" if average >= 70 else "D" if average >= 60 else "F"
  except:
      return "Invalid data was provided."

# Task 6

def repeat (x, count):
  result = ""

  for _ in range (count):
    result += x

  return result

# Task 7
# positional parameter either best or mean. best then the name with the highest score, if mean the average score is returned
#kwargs is a dict (key/value pair) and you can iterate through it as follows

def student_scores(method, **kwargs):
  if method == "mean":
    return sum(kwargs.values())/len(kwargs)
  else:
    return max(kwargs, key = kwargs.get)
  
# Task 8

def titleize(string):

  little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]

  words = words.split()

  # for letter in words:
  #   letter.capitalize()
  
  for i in range(len(words)):
    words[i] = words[i].method()

  return words

# Task 9

def hangman(secret, guess):
  result = ""

  for i in list(secret):
    if i in guess:
      result += i
    else: result += "_"
  return result

# Task 10

def pig_latin(stri):
  result = ""
  for st in stri.split(" "):
    if st[0] in "aeiou":
      result += st + "ay"
    elif st[0:2] == "qu":
      result += st[2:] + "quay"
    else:
      i=0
      while (st[i] not in "aeiou"):
        i += 1
      if st [i-1 : i+1] == "qu":
        result += st[i+1:] + st [:i+1] + "ay"
      else:
        result += st[i:] + st [:i] + "ay"
    result += " "
  return result [:-1]

print (pig_latin("the quick brown fox"))



