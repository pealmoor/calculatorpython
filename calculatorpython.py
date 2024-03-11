def calculator():
     while True:
         print("\nSelect the operation you want to perform:")
         print("1. Sum")
         print("2. Subtraction")
         print("3. Multiplication")
         print("4. Division")
         print("5. Exit")

         option = input("\nEnter the number of the desired operation: ")

         if option == '5':
             print("Exiting calculator...")
             break

calculator()


