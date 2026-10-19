import time
from functools import wraps


call_counts = {}

def track_function(function):
    """Print call information and timing for the function being decorated."""
    call_counts[function.__name__] = 0

    @wraps(function)
    def wrapper(*args, **kwargs):
        call_counts[function.__name__] += 1
        call_number = call_counts[function.__name__]

        print(f"Starting function: {function.__name__}")
        start_time = time.perf_counter()

        try:
            return function(*args, **kwargs)
        except Exception as error:
            print(f"Error in {function.__name__}: {error}")
            raise 

        finally:
            elapsed_time = time.perf_counter() - start_time
            print(
                f"Function: {function.__name__} | Calls: {call_number} | "
                f"Execution time: {elapsed_time:.6f} seconds"
            )
            print(f"Finished function: {function.__name__}")

    return wrapper

@track_function
def add(a, b):
    """Return the sum of two numbers."""
    return a + b


@track_function
def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


@track_function
def calculate_average(numbers):
    """Return the average of a list of numbers."""
    return sum(numbers) / len(numbers)


@track_function
def fail_on_purpose():
    """Raise an error to demonstrate that the decorator logs and re-raises it."""
    raise ValueError("This is an intentional example error.")


def main():
    """Run examples of successful calls and an exception."""
    print("\n--- add ---")
    result = add(10, 20)
    print(f"Result: {result}\n")

    print("--- multiply ---")
    result = multiply(a=4, b=5)
    print(f"Result: {result}\n")

    print("--- calculate_average ---")
    result = calculate_average([10, 20, 30])
    print(f"Result: {result}\n")

    print("--- intentional error ---")
    try:
        fail_on_purpose()
    except ValueError as error:
        print(f"Caught in main: {error}\n")

    print("--- preserved metadata ---")
    print(f"Function name: {add.__name__}")
    print(f"Function docstring: {add.__doc__}")


if __name__ == "__main__":
    main()
