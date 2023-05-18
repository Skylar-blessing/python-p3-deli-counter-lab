
# lib/deli_counter.py

def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        line_message = "The line is currently:"
        for i, customer in enumerate(katz_deli, start=1):
            line_message += f" {i}. {customer}"
        print(line_message)

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        serving_customer = katz_deli.pop(0)
        print(f"Currently serving {serving_customer}.")

katz_deli = []

take_a_number(katz_deli, "Ada")  
take_a_number(katz_deli, "Grace") 
take_a_number(katz_deli, "Kent")  
line(katz_deli) 

now_serving(katz_deli) 
line(katz_deli)

take_a_number(katz_deli, "Matz") 
line(katz_deli) 

now_serving(katz_deli) 

line(katz_deli) 

    
