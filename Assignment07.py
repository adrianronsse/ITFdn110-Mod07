# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Collects dimensions for storefront frames
#              Demonstrates structured error handling
#              Demonstrates pickling using shelve module
# ChangeLog (Who,When,What):
# ARonsse, 8.25.2021, created file
# ARonsse, 8.27.2021, updated code with shelve module
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "StorefrontTakeoff"  # The name of the data file
objFile = None   # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Width, Height}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
add_height = ""  # Captures the user item data
add_width = ""  # Captures the user cost data
tup_row = "" # Captures function output in a tuple

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing items """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :type list_of_rows: list
        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        shelf = shelve.open(file_name)
        new_row = {}
        try:
            new_row['Width'] = shelf['Width']
            new_row['Height'] = shelf['Height']
            list_of_rows.append(new_row)
        finally:
            shelf.close()
        return list_of_rows

    @staticmethod
    def add_data_to_list(width, height, list_of_rows):
        """ Adds To Do items to dictionary row and adds the row to a list

        :param width: (int) with width of glass:
        :param height: (int) with height of glass:
        :param list_of_rows: (list) to fill with glass dimension data:
        :return: (list) of dictionary rows
        """

        new_row = {'Width': width, 'Height': height}
        list_of_rows.append(new_row)
        return list_of_rows

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data from a list of dictionary rows into a shelf

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want to write to file:
        :return: (list) of dictionary rows
        """
        shelf = shelve.open(file_name, 'n')
        for row in list_of_rows:
            shelf['Width'] = row['Width']
            shelf['Height'] = row['Height']
        shelf.close()
        return list_of_rows


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output items """

    @staticmethod
    def print_welcome():
        """  Display welcome message to user and description of program intent

        :return: nothing
        """
        print('''
        Welcome to the storefront calculator program. Please enter the width and height of each continuous
        storefront section. Measure along the top of the storefront section such that doors frames are 
        included in the width measurement.
        ''')

    @staticmethod
    def input_frame_dims():
        """  Collect frame dimensions from user

        :return: width, height
        """
        width = None
        height = None
        while width or height is None:
            try:
                width = int(input("Enter width in inches (use whole numbers only): ").strip())
                height = int(input("Enter height in inches (use whole numbers only): ").strip())
                return width, height
            except(ValueError):
                print("Dimensions must be entered in whole numbers only. Please try again.\n")
            except:
                print("Unknown error occurred. No data captured. Please try again.\n")

    @staticmethod
    def print_menu():
        """  Display menu for user navigation

        :return: nothing
        """
        print('''
        MENU
        1) Enter new frame dimensions
        2) Save data to file
        3) View current data
        4) Exit
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice


    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def print_current_data(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current frame dimensions are: *******")
        for row in list_of_rows:
            print(str(row['Width']) + '" x ' + str(row['Height']) + '"')

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, import shelve module
import shelve

# Step 2 - Load data from StorefrontTakeoff.txt
try:
    lstTable = Processor.read_data_from_file(strFileName, lstTable)  # read file data
    print(lstTable)
except(KeyError, FileNotFoundError, EOFError):
    input("Starting program with no current entries. Press enter to continue.")


# Step 3 - Welcome user to program
IO.print_welcome()

# Step 4 - Display menu
while True:
    IO.print_menu()   #print menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 5 - process menu choice
    if strChoice.strip() == '1':  # Add new frame dimensions
        tup_row = IO.input_frame_dims()
        add_width, add_height = tup_row  # Unpack the tuple
        Processor.add_data_to_list(add_width, add_height, lstTable)  # Pass arguments into function parameters
        IO.input_press_to_continue("\nFrame dimensions added!")
        continue  # to show the menu

    elif strChoice.strip() == '2':   # Save data to file
        Processor.write_data_to_file(strFileName, lstTable)
        IO.input_press_to_continue("\nData saved!")
        continue

    elif strChoice.strip() == '3': #display current data
        IO.print_current_data(lstTable)  # Show current data in the list/table
        IO.input_press_to_continue()

    elif strChoice.strip() == '4': #exit program
        print("Goodbye!")
        break   # and Exit