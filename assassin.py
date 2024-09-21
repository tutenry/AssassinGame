import random
import os
import time

names = []
kill_book = {}

def new_game():
  global kill_book
  global names
  names = ["Seth", "Austin", "Mann", "Jack", "Rylan", "Conner"]
  kill_book = {}

  random.shuffle(names)
  
  for i in names:
    if names.index(i) == len(names)-1:
      kill_book[i] = names[0]
    else:
      kill_book[i] = names[names.index(i)+1]

  with open("assassinSave.txt", "w+") as saveFile:
    saveFile.write(f"{names}\n{kill_book}")

def resume_game():
  global kill_book
  global names

  with open("assassinSave.txt", "r") as saveFile:
    names_list = saveFile.readline().strip().replace("[", "").replace("]", "").replace("'", "").replace(" ", "").split(",")
    for name in names_list:
      if name == "AustinJunior":
        name = "Austin Junior"
      elif name == "AustinSenior":
        name = "Austin Senior"
      names.append(name)

    kill_book_temp = saveFile.readline().strip().replace("{", "").replace("}", "").replace("'", "").split(",")
    kill_book_list = []
    for item in kill_book_temp:
      name_duo = item.replace(" ", "").split(":")
      for name in name_duo:
        if name == "AustinSenior":
          name = "Austin Senior"
        elif name == "AustinJunior":
          name = "Austin Junior"
        kill_book_list.append(name)

    for name in kill_book_list:
      if kill_book_list.index(name) != len(kill_book_list)-1:
        kill_book[name] = kill_book_list[kill_book_list.index(name)+2]
      else:
        kill_book[name] = kill_book_list[0]
        
    
  

  
def ask_name():
  name_wanted = input("Enter name ('delete' to remove, 'print' to print kill book)\n")
  if name_wanted.lower() == "delete":
    remove_name()
  elif name_wanted.lower() == "print":
    print_book()
    end = input("\n'end' to quit\n")
  else:
    Time = time.time()
    current_time = time.time()
    print(name_wanted, "has to kill",     kill_book[name_wanted])
    while Time < current_time + 3:
      Time = time.time()
  
  os.system("cls")

def remove_name():
  delete_name = input("Enter a name to delete\n")
  if delete_name in names:    
    
    for key, value in kill_book.items():
      
      if value == delete_name:
        for key in kill_book.keys():
          if kill_book[key] == value:
            attacker_name = key
        attacker_index = names.index(attacker_name)
        if attacker_index+2 >= len(names):
          kill_book[attacker_name] = names[0]
        else:
          kill_book[attacker_name] = names[attacker_index+2]

        names.remove(value)
    del kill_book[delete_name]
    
    with open("assassinSave.txt", "w+") as saveFile:
      saveFile.write(f"{names}\n {kill_book}")
        
        
        
      
  os.system("cls")
  

def print_book():
  print(kill_book)

def start_game():
  new = input("New game?\n").lower()
  if new == "yes":
    new_game()
  else:
    resume_game()
  os.system("cls")
    

start_game()
while len(names) > 1:
  ask_name()
print(names[0], "HAS WON!!!")