import traceback

with open("diary.txt","a")as file:

  try: 
    prompt_answer = ""

    what_question = input("What happened today?\n")
    file.write(what_question + "\n")

    done = "done for now"

    while prompt_answer != done:
      prompt_answer = input("What else?\n" )
      file.write(prompt_answer + "\n")
      if prompt_answer == done:
        break
  
  # except Exception as e:
  #   print("An exception occured", e)
  except Exception as e:
   trace_back = traceback.extract_tb(e.__traceback__)
   stack_trace = list()
   for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
   print(f"Exception type: {type(e).__name__}")
   message = str(e)
   if message:
      print(f"Exception message: {message}")
   print(f"Stack trace: {stack_trace}")

    









