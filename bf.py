from bf_parser import *

def main():
    # just for fun 
    c_interpreter = bf_interpreter() 

    l_interpreter_input = str(input(">: "))
    
    c_interpreter.parse_interpret_input(l_interpreter_input)

if __name__ == "__main__":
    main()