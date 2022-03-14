''' an interpreter version of brainfuck '''
import string

class bf_interpreter:
    def create_initial_byte_array(self) -> list:
        l_initial_byte_array = []
        for i in range(1000):
            l_initial_byte_array.append(0)

        return l_initial_byte_array


    # this function will be funky. Essentially, we'll need to take the user's input from the interpreter
    # and parse it into how bf would handle it, make the changes and push those changes onto the correct
    # index of the list, then return that list as it would be with the changes
    def parse_interpret_input(self, a_interpreter_input:str) -> None:
        # this acts as a hint, have at it
        
        
        l_alphabet = string.ascii_letters


        l_byte_array = self.create_initial_byte_array() # initial 1000 byte array

        l_move_pointer_right = ">" # greater than
        l_move_pointer_left = "<" # less than
        l_increment_memory_cell = "+" # plus
        l_decrement_memory_cell = "-" # minus
        l_output_current_cell_value = "." # period
        l_input_value_at_current_cell = "," # comma
        # the lexicon of bf is only 8 commands, so we need to give rules to them ..
        # <, >, +, -, [, ], and ,.
        
        # then, we'll just decode the hex value and boom, done
        l_current_index = 0
        l_current_command_length = 0
        for command in a_interpreter_input:
            l_current_command_length += 1 # could use enumerate too!
            if command == l_move_pointer_right:
                l_current_index += 1
            elif command == l_move_pointer_left:
                l_current_index -= 1
            elif command == l_increment_memory_cell:
                l_byte_array[l_current_index] += 1
            elif command == l_decrement_memory_cell:
                l_byte_array[l_current_index] -= 1
            elif command == l_output_current_cell_value:
                print(l_byte_array[l_current_index])
            elif command == l_input_value_at_current_cell:
                l_next_command = a_interpreter_input[l_current_command_length: l_current_command_length+1]
                l_byte_array.insert(l_current_index, l_next_command)



            # map to the alphabet

            for number in l_byte_array:
                if number > 0:
                    print(l_alphabet[number: number+1], end='')




        
                    
        



        
        






    
    
    
    
