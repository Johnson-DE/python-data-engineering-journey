import logging

logging.basicConfig (
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
try:
    logging.info("Program Started")
    a = int(input("Enter a Number: "))
    b = int(input("Enter a Another Number: "))
    op = input("Enter Operation("+", "-", "*", "/") :")

    if op=="+":
        logging.info(a+b)
        print(a+b)
    elif op=="-":
        logging.info(a-b)
        print(a-b)
    elif op=="*":
        logging.info(a*b)
        print(a*b)
    elif op=="/":
        logging.info(a/b)
        print(a/b)


except ValueError:
    logging.error("Invalid Input Provided")
    print("Invalid Input")

except ZeroDivisionError:
    logging.error("Division by Zero Attempted")
    print("Divide by Zero")
finally:
    logging.info("program ended")