



# Assignment 7

## Pickling files and Structured Error Handling

### Introduction
This assignment covered pickling data into a binary file (.dat) and using structured error handling to display messages to the user and keep the program running to a voluntary completion. I decided to model the code after the work we had done in Assignment06, hoping to create a basic structure for collecting, storing, and loading dimensional data that I could use in my work as an estimator for a commercial glass and door installer. My intent was to store and load data in a format such that I can later add additional code to perform calculations on the individual data entries and thus produce the quantities of framing component stock lengths used for each location.

### Writing the code:
_Note: Since we covered function creation and implementation in the previous assignment, this section will focus on the assigned tasks of demonstrating pickling and structured error handling rather than walking throught the entire code._

**1. Create function to pickle data and write to binary file**  
I decided that I wanted to store dictionaries in the binary file rather than lists, because I intend to collect a third piece of data in the future that will determine whether certain calculations are performed to the first two items associated with that new piece of data. In Chapter 7 of Python Programming for the Absolute Beginner, I learned that in order to store data in dictionary format, I need to use a module called “shelve”, which builds on the pickle module.  I invoke that module below for the write function: 
```
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
```
_Figure 1 – Writing a list of dictionaries into a binary file using the shelve module_


**2. Create a function to load shelf data from the binary file back into the program**    
This step proved too difficult for me. I wanted to load all of the data in the file back into the program as a list of rows, but I was only able to come up with code that loads the last piece of information in the file for each of the keys “Width” and “Height”. I searched online for a solution but was unable to solve this, so I am hoping to receive feedback to this assignment that will show me how to do this properly. Here is the code I was able to come up with:
```
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
```
_Figure 2 – Reads data from binary file into a dictionary, but only captures the final data entry in the file_


**3. Demonstrate structured error handling**  
This part of the code makes sure that the program can keep running even if the user enters data in the wrong format or if some other unforeseen error were to occur.
```
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
```
_Figure 3 – Structured error handling_

### Testing the code: 
After preparing the code, I needed to test it to make sure it was working as expected. First I opened the program in the command console to test. Here I see that I am able to log dimensions and view that data:
![image of command conole showing data collection](https://user-images.githubusercontent.com/88747068/131229924-51ee5784-6c15-4699-abe3-22ad26ce65f7.png)  
_Figure 4 – Command console test_  

Then I tested it in PyCharm as well and found I was also able to save the file as intended.

![image of PyCharm interface showing successful save message](https://user-images.githubusercontent.com/88747068/131229927-09a8327a-64b0-43fb-afe7-811e2de1a08a.png)  
_Figure 5 – PyCharm test: data saves successfully_  


I can confirm too, that the file has populated in my folder along with some other files that support it:

![image of open window containing StorefrontTakeoff.dat file and others](https://user-images.githubusercontent.com/88747068/131229898-6f61f6ba-0146-4442-b2dc-4964e244c359.png)  
_Figure 6 — Files saved in folder_  


Unfortunately when I stop and restart the program, I find that I have only loaded the final data entry:

![image of PyCharm interface resulting only one pair of width and height measurements](https://user-images.githubusercontent.com/88747068/131229920-d1b355dc-f83e-4be8-a336-a7c73bdb0e8f.png)  
_Figure 7 – PyCharm test: only partial data load_  

### Summary:
In this coding exercise I was able to write binary data to a file using the shelve module, which is a way to pickle dictionaries. I was also able to load some of that data back to the file, although was not successful in fully reconstructing the dictionary list. I also used structured error handling to help ensure that the program would run smoothly and not quit unexpectedly.
