from backend.calculator import Calculator
from backend.logger import Logger
from utils.validator import validate_number

logger = Logger()
calc = Calculator()

def run_demo():
    try:
        a = 10
        b = 0  # Demo crash case
        validate_number(a)
        validate_number(b)
        result = calc.divide(a, b)
        print(f"Result: {result}")
    except Exception as e:
        logger.log(str(e))
        print("An error occurred:", e)

if __name__ == "__main__":
    run_demo()