class ErrorHandling:
    @staticmethod
    def handle_error(error_message):
        try:
            # Print the error message
            print(f"Error: {error_message}")
        except Exception as e:
            # If any unexpected error occurs during error handling, print a generic message
            print("An unexpected error occurred during error handling:", e)
