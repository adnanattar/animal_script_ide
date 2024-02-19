# control.py

import sys
import os

# Add the parent directory of your package to the sys.path temporarily
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
package_dir = os.path.join(parent_dir, "animal_script")
sys.path.insert(0, parent_dir)
sys.path.insert(0, package_dir)

# Now you can use absolute imports within your package
from animal_script.conditions import Conditions
from animal_script.arithmetic import Arithmetic

class Control:
    @staticmethod
    def evaluate_control(tokens, animal_script):
        try:
            if tokens[0] == "Monkeys":
                return Arithmetic.evaluate_giraffe(tokens, animal_script)
            elif tokens[0] == "Tiger":
                return Conditions.evaluate_fox(tokens, animal_script)
            elif tokens[0] == "Dolphin":
                return Control.evaluate_dolphin(tokens, animal_script)
            elif tokens[0] == "Whale":
                return Control.evaluate_whale(tokens, animal_script)
        except Exception as e:
            # Print an error message if an exception occurs
            print("Follow the Animal Rules")
            return None  # Or return any appropriate value indicating failure

    @staticmethod
    def evaluate_dolphin(tokens, animal_script):
        # Method to evaluate Dolphin statements
        var_name = tokens[1]
        user_input = input(f"Enter value for {var_name}: ")
        if user_input.startswith('"') and user_input.endswith('"'):
            # If the user input is a string, store it as is
            animal_script.variables[var_name] = user_input.strip('"')
            return f"Variable {var_name} set to {user_input}."
        else:
            # If the user input is an integer, convert it to int and store
            animal_script.variables[var_name] = int(user_input)
            return f"Variable {var_name} set to {user_input}."

    @staticmethod
    def evaluate_whale(tokens, animal_script):
        # Method to evaluate Whale statements
        if len(tokens) < 2:
            return "Invalid input. Please provide a message or variable name after 'Whale'."
        if tokens[1].startswith('"') and tokens[1].endswith('"'):
            # If the Whale statement contains a message, print it
            message = tokens[1].strip('"')
            return f"Whale says: {message}"
        else:
            # If the Whale statement refers to a variable, print its value if defined
            var_name = tokens[1]
            if var_name in animal_script.variables:
                value = animal_script.variables[var_name]
                return f"Whale says: {value}" if isinstance(value, str) else f"Variable {var_name} is set to {value}"
            else:
                return f"Variable {var_name} is not defined."
