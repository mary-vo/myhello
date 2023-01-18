print("Hello World!")

def print_hello(): 
    print("Hello World!")

def main(): 
    print_hello()

print("Special Hello World!")

def print_msg(msg_txt): 
    print(f"{msg_txt}") 
    return 0

mymsg = "Hello World!"

return_code = print_msg(mymsg)

if __name__ == '__main__': 
    main()