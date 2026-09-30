#Start
# Creating a class for shoes in the inventory
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost 
        self.quantity = quantity
      # Defining methods for my inventory  
    def get_cost(self):
        return self.cost
        
        
        

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"
        

#=============Shoe list===========
# A empty shoe list variable to store a list of shoe objects
shoe_list = []


#==========Functions outside the class==============

def read_shoes_data():
      try:
        #reading from inventory.txt.
        with open("inventory.txt", "r") as file:

            # Skip the first line
            file.readline()

            # Read each line in the file
            for line in file:

                # Split the data using commas
                data = line.strip().split(",")

                country = data[0]
                code = data[1]
                product = data[2]
                cost = float(data[3])
                quantity = int(data[4])

                #Creating shoe object to read our data
                shoe = Shoe(country, code, product, cost, quantity)

                #Adding the shoe to a list using append
                shoe_list.append(shoe)

      except FileNotFoundError:
          print("the inventory file could not be found in our inventory.")

      except ValueError:
          print("There is an error with the data in the inventory file. ")  


# function to capture all shoes
def capture_shoes():
    country = input("Please enter the country: ")
    code = input("Please enter the shoe code: ")
    product = input("Please enter the product name: ")
    cost = float(input("Please enter the cost: "))
    quantity = int(input("Please enter the quantity: "))

     #Creating shoe object to read our data
    shoe = Shoe(country, code, product, cost, quantity)

    # Adding the shoe to a list 

    print("The shoe has been added successfully.")


# Function to view all shoes
def view_all():
   #Going through each shoe in the shoe list
    for shoe in shoe_list:
        print(shoe)


# Function to restock missing shoes
def re_stock():
    # Checking if the shoe list is empty
    if len(shoe_list) == 0:
        print("there are no more shoes.")
        return
    
    # Start with the shoe with the lowest quantity
    low_quantity = shoe_list[0]

    # Going throught the list to find the shoe with the lowest quantity
    for shoe in shoe_list:
        if shoe.quantity < low_quantity.quantity:
            low_quantity = shoe

    print("\nThe shoe with the lowest quantity: ")
    print(low_quantity)

    # Asking for user input if they want to add stock
    choice = input("Would you like to add stock to this shoe? (yes/no):")

    if choice.lower() == "yes":
        amount = int(input("How many shoes would you like to add: "))

        #Updating the quantity
        low_quantity.quantity += amount

        #Updating the inventory file
        with open("inventory.txt", "w") as file:
           file.write("Country,Code,Product,Cost,Quantity\n")

           for shoe in shoe_list:
                file.write(
                    f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n"
                )

        print("The quantity of the shoes has been updated.")
    else:
        print("No stock has been added to the inventory.")


# Function to search for a specific shoe
def search_shoe():
    #Asking the user to input shoe code to search for a shoe
    code = input("Please enter the shoe code: ")
    #Searching through the list to find a shoe
    for shoe in shoe_list:
        if shoe.code == code:
            print("\nThe shoe has been found in the inventory: ")
            print(shoe)
            return shoe
    print("Shoe not found.")


# Function to find value per item
def value_per_item():
    #Calculating the value of every shoe in the inventory
    for shoe in shoe_list:
        #Calculating the value by multiplying cost multiplied by quantity
        value = shoe.cost * shoe.quantity
        print(shoe.product, "value", value)


# Function to find highest quantity of shoes
def highest_qty():
    # Check if the list is empty
    if len(shoe_list) == 0:
        print("There are no shoes in the list.")
        return

    # Start with the first shoe as the highest quantity
    high_quantity = shoe_list[0]

    # Finding the shoe with the highest quantity
    for shoe in shoe_list:
        if shoe.quantity > high_quantity.quantity:
            high_quantity = shoe

    print("\nThe shoe with the highest quantity is: ")
    print(high_quantity)
    print("This shoe is available for sale.")

#==========Main Menu=============


# Read the shoe data from the file
read_shoes_data()

# Create the menu for user input when accesing the directory
while True:

    print("\n----------Store shoe Inventory Menu----------")
    print("1. Capture shoe")
    print("2. View all shoes")
    print("3. Re-stock shoes")
    print("4. Search for a shoe")
    print("5. Calculate value per item")
    print("6. Find shoe with highest quantity")
    print("7. Exit")

    choice = input("Please enter your choice: ")

    if choice == "1":
        capture_shoes()

    elif choice == "2":
        view_all()

    elif choice == "3":
        re_stock()

    elif choice == "4":
        search_shoe()

    elif choice == "5":
        value_per_item()

    elif choice == "6":
        highest_qty()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

#Stop