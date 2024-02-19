# arithmetic.py

class Arithmetic:
    @staticmethod
    def perform_operation(operator, operand1, operator_symbol, operand2):
        try:
            # Convert operands to integers if they are not already
            operand1 = int(operand1)
            operand2 = int(operand2)

            if operator == "Elephants":
                if operator_symbol != "+":
                    return "Invalid operator. Elephants only trumpet for addition ('+')."
                # Perform addition operation
                return f"Trumpets {operand1 + operand2}"
            elif operator == "Frogs":
                if operator_symbol != "-":
                    return "Invalid operator. Frogs only croak for subtraction ('-')."
                # Perform subtraction operation
                return f"Croaks {operand1 - operand2}"
            elif operator == "Bees":
                if operator_symbol != "*":
                    return "Invalid operator. Bees only buzz for multiplication ('*')."
                # Perform multiplication operation
                return f"Buzzes {operand1 * operand2}"
            elif operator == "Lions":
                if operator_symbol == "/":
                    if operand2 == 0:
                        return "You tried to divide by zero? Well, that's just arranging a fight between Elephant and Ant. You can't divide by zero, it's undefined!"
                    else:
                        # Perform true division operation
                        return f"Roar {operand1 / operand2}"
                elif operator_symbol == "//":
                    if operand2 == 0:
                        return "You tried to divide by zero? Well, that's just arranging a fight between Elephant and Ant. You can't divide by zero, it's undefined!"
                    else:
                        # Perform floor division operation
                        return f"Charges {operand1 // operand2}"
                else:
                    return "Invalid operator. Lions only roar for true division ('/') and floor division ('//')."
            elif operator == "Giraffes":  # New functionality
                if operator_symbol != "**":
                    return "Invalid operator. Giraffes only perform exponentiation ('**')."
                # Perform exponentiation operation
                return f"Stretches {operand1 ** operand2}"
            elif operator == "Kangaroos":  # New functionality
                if operator_symbol != "%":
                    return "Invalid operator. Kangaroos only hop for modulus ('%')."
                # Perform modulus operation
                return f"Hops {operand1 % operand2}"
            elif operator == "Rhinos":  # New functionality
                if operator_symbol != "//":
                    return "Invalid operator. Rhinos only charge for floor division ('//')."
                # Perform floor division operation
                return f"Charges {operand1 // operand2}"
            elif operator == "Zebras":  # New functionality
                if operator_symbol != "/":
                    return "Invalid operator. Zebras only gallop for true division ('/')."
                # Perform true division operation
                return f"Gallops {operand1 / operand2}"
            elif operator == "Pandas":  # New functionality
                if operator_symbol != "^":
                    return "Invalid operator. Pandas only roll for bitwise XOR ('^')."
                # Perform bitwise XOR operation
                return f"Rolls {operand1 ^ operand2}"
            elif operator == "Lemurs":  # New functionality
                if operator_symbol != "|":
                    return "Invalid operator. Lemurs only leap for bitwise OR ('|')."
                # Perform bitwise OR operation
                return f"Leaps {operand1 | operand2}"
            elif operator == "Owls":  # New functionality
                if operator_symbol != "&":
                    return "Invalid operator. Owls only hoot for bitwise AND ('&')."
                # Perform bitwise AND operation
                return f"Hoots {operand1 & operand2}"
            else:
                return "Unknown statement."
        except Exception as e:
            return "Follow the Animal Rules"
