# conditions.py

class Conditions:
    @staticmethod
    def evaluate_condition(condition):
        try:
            # Evaluate the condition and return the result message
            if condition:
                return "Roar Condition is True."
            else:
                return "Roar Condition is False."
        except Exception as e:
            # Handle any exceptions and return a generic error message
            return "Follow the Animal Rules"
