# Import all modules here import is a keyword
import addition
import subtraction
import multiplication
import division
import modulusdivision
import power
import squareroot
import factorial

operations = (
    "1. Addition\n",
    "2. Subtraction\n",
    "3. Multiplication\n",
    "4. Division\n",
    "5. Modulus Division\n",
    "6.power \n",
    "7.Square Root \n"
    "8. Factorial \n",
    "9.exit "

)

# Main function
if __name__ == "__main__":
    print("Welcome to Simple Calculator. It will only do two-number operations.")
    while True:  #until condition is true 
        print(*operations)   #here we used to print all opertions 
        choice = int(input("Please select your operation: "))
        if choice == 1:
            num1 = int(input("Enter number_1: "))
            num2 = int(input("Enter number_2: "))
            print(f"Addition of {num1} and {num2} is :", addition.add(a=num1, b=num2))  #here a=num1 menas we are using keyword arguments 

        elif choice == 2:
            num1 = int(input("Enter number_1: "))
            num2 = int(input("Enter number_2: "))
            print(f"Subtraction of {num1} and {num2} :", subtraction.sub(a=num1, b=num2))

        elif choice == 3:
            num1 = int(input("Enter number_1: "))
            num2 = int(input("Enter number_2: "))
            print(f"multiplication of {num1}and {num2} is ", multiplication.mul(a=num1, b=num2))

        elif choice == 4:
            num1 = int(input("Enter number_1: "))
            num2 = int(input("Enter number_2: "))
            print(f"Division of {num1} and {num2} is :", division.div(a=num1, b=num2))

        elif choice == 5:
            num1 = int(input("Enter number_1: "))
            num2 = int(input("Enter number_2: "))
            print(f"MOdulus Division of {num1} and {num2} is :", modulusdivision.modulus(a=num1, b=num2))
        elif choice==6:
            num1 = int(input("Enter number_1: "))
            num2 = int(input("Enter number_2: "))
            print(f"Power of {num1} and {num2} is :", power.po(a=num1, b=num2))
        elif choice==7:
            num1 = int(input("Enter number: "))
            print(f"Square root of {num1} is :", squareroot.seq(a=num1))
        elif choice==8:
            num1=(int(input("Enter a number : ")))
            print(f"Factorial of {num1} is :",factorial.fact(a=num1))
        
        elif choice == 9:
          print("Exiting from Calculator...")
          break #used to stop the execution
        else:
            print("Please select a valid operation between 1 to 9.")
