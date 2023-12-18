def is_empty(stk):
    if stk == []:
        return True 
    else:
        return False
    
def push(stk, item):
    stk.append(item)
    top = len(stk)-1

def pop(stk):
    if is_empty(main_stack) != True:
        value = stk.pop()
        if len(stk)==0: top = None
        else: top = len(stk)-1
        return value
    else:
        return "Stack Underflow"
    
def peek(stk):
    if is_empty(main_stack) != True: 
        top = len(stk)-1
        return stk[top]
    else: 
        return "Stack Underflow"

def display(stk):
    if is_empty(main_stack) != True:
        top = len(stk)-1
        for i in range(top,-1,-1):
            if i == top :
                print(f"Highest Value--> {stk[i]}")
            elif i == 0 :   
                print(f"Lowest  Value--> {stk[i]}")
            else:
                print(f"                 {stk[i]}")
        print(f"\nstack length is {len(stk)}")
    else:
        print("Stack underflow , stack is empty!!")

def take_input():
    try:
        while True:
            user_choice = int(input("""
---------STACK OPERATOR MAIN CONTROL PANEL---------
          1.PUSH
          2.POP
          3.PEEK
          4.DISPLAY STACK
          5.EXIT 
          
          
ENTER YOUR CHOICE(1-5) :"""))
            if 1 <= user_choice <=5:
                return user_choice
            else:
                print("     >>>>The Value is out of range, try again!<<<<")
    except:
        print("     >>>>please Enter a valid value<<<<")
    return 

''' Stack  Main  Prog  Starts here .....'''


main_stack = []
top = None


while True:
    
    user_choice = take_input()
    if user_choice == 1:
        item = int(input("Please enter your item"))
        push(main_stack, item)
    if user_choice == 2:
        item = pop(main_stack)
        if item == "Stack Underflow":
            print("Stack Underflow , stack is empty!!!1")
        else :
            print(item)

    if user_choice == 3:
        item = peek(main_stack)
        if item == "Stack Underflow":
            print("Stack Underflow, the stack is empty!!!")
        else:
            print(f"the highest value is {item} ")
    if user_choice == 4:
        display(main_stack)
    if user_choice == 5:
        exit()        




    
