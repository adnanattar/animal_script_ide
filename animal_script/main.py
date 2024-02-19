import sys
import os
from flask import Flask, render_template, request

# Add the parent directory of your package to the sys.path temporarily
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
package_dir = os.path.join(parent_dir, "animal_script")
sys.path.insert(0, parent_dir)
sys.path.insert(0, package_dir)

# Now you can use absolute imports within your package
from animal_script.conditions import Conditions
from animal_script.arithmetic import Arithmetic
from animal_script.error_handling import ErrorHandling
from animal_script.data_structures import DataStructures
from animal_script.control import Control

class AnimalScript:
    def __init__(self):
        self.variables = {}

    def evaluate_multiline(self, input_str):
        results = []
        lines = input_str.strip().split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line.startswith("Dolphin"):
                i += 1
                if i < len(lines):
                    next_line = lines[i].strip()
                    if next_line.isdigit():
                        self.variables[line.split()[1]] = int(next_line)
                        results.append(f"Variable {line.split()[1]} set to {next_line}.")
                    else:
                        results.append("Follow the Animal Rules")
                else:
                    results.append("Follow the Animal Rules")
            elif line.startswith("Monkeys"):
                tokens = line.split()
                if len(tokens) >= 4 and tokens[1].isalpha() and tokens[2].isdigit():
                    var_name = tokens[1]
                    start_value = int(tokens[2])
                    end_value = int(tokens[3])
                    for value in range(start_value, end_value + 1):
                        self.variables[var_name] = value
                        results.append(f"Variable {var_name} set to {value}.")
                else:
                    results.append("Invalid input for Monkeys. Please provide valid arguments.")
            elif line.startswith("Tiger"):
                condition = line.split("Tiger")[1].strip()
                result = self.evaluate_condition(condition)
                if result is not None:
                    results.append(result)
                else:
                    results.append("Invalid condition for Tiger.")
            else:
                result = self.evaluate(line)
                results.append(result)
            i += 1
        return '\n'.join(results)

    def evaluate_condition(self, condition):
        try:
            a, operator, b = condition.split()
            a = int(a) if a.isdigit() else self.variables.get(a, None)
            b = int(b) if b.isdigit() else self.variables.get(b, None)
            if a is not None and b is not None:
                if operator == '<':
                    return str(a < b)
                elif operator == '>':
                    return str(a > b)
                elif operator == '<=':
                    return str(a <= b)
                elif operator == '>=':
                    return str(a >= b)
                elif operator == '==':
                    return str(a == b)
                elif operator == '!=':
                    return str(a != b)
            else:
                return None
        except ValueError:
            return None

    def evaluate_dolphin(self, input_str):
        var_name = input_str
        if var_name.isdigit():
            self.variables[var_name] = int(var_name)
            return f"Variable {var_name} set to {var_name}."
        else:
            return "Invalid input for Dolphin. Please enter a number."

    def evaluate(self, input_str):
        try:
            tokens = input_str.split()
            if tokens[0] in ["Monkeys", "Tiger", "Dolphin", "Whale"]:
                return Control.evaluate_control(tokens, self)
            elif tokens[0] in ["Elephants", "Frogs", "Bees", "Lions", "Giraffes", "Kangaroos", "Rhinos", "Zebras", "Pandas", "Lemurs", "Owls"]:
                # Replace variable names with their values before evaluating arithmetic expressions
                for i, token in enumerate(tokens):
                    if token in self.variables:
                        tokens[i] = str(self.variables[token])
                return Arithmetic.perform_operation(*tokens)
            else:
                return "Unknown statement."
        except ValueError:
            return "Invalid operands. Please provide valid numbers."
        except Exception as e:
            return "Follow the Animal Rules"



app = Flask(__name__)
animal_script = AnimalScript()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_code', methods=['POST'])
def run_code():
    code = request.form['code']
    results = []
    
    for line in code.splitlines():
        result = animal_script.evaluate(line.strip())
        results.append(result)

    return '\n'.join(results)

if __name__ == "__main__":
    app.run(debug=True)
