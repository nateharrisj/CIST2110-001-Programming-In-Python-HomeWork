# Project 2
# Name: Nate Harris
# Project 2 will test on topics learned in class so far. You will be creating a contact list program with an external csv file that will store the contacts. The program will have the following features:
# 1. Add contact
# 2. View contacts
# 3. Delete contact
# 4. Save contacts to csv file
# 5. Next Birthday
# 0. Quit

# Import the csv module, datetime module
import csv
import datetime as dt
import tabulate
import os
from typing import Dict


# There is also a contact.csv file that will be used to store the contacts. The csv file will have the following format:
# Name,Phone,Email,Birthday
# The program will be menu driven and will display the menu as shown above. The program will run until the user selects option 0 to quit. The program will be implemented in a file called Project2.py. The program will use the following functions:
# import_csv - This function will import the contacts from the csv file. The function will return a dictionary of contacts. The key will be the name of the contact and the value will be a dictionary containing the phone number, email address, and birthday. The function will take one parameter, the name of the csv file. The function will display an error message if the file does not exist. The function will display a message if the file exists and the contacts were imported successfully.
# Hint1: Use the csv module to read the csv file. Use the csv.reader function. IE. reader = csv.reader(file)
# Hint2: You will need to skip the first line of the csv file since it contains the column headers. You can do that with the next function. IE. next(reader)
# Hint3: You will need to create a dictionary of contacts. You can do that by looping through the reader object. IE. for row in reader:
# Hint4: You will need to convert the birthday to a datetime object. You can do that by using the strptime function. IE. dt.datetime.strptime(row[3], '%m/%d/%Y')
# Hint5: You will need to create a dictionary of the phone number, email address, and birthday. You can do that by creating a dictionary and adding the values to the dictionary. IE. contact[row[0]] = {'Phone': row[1], 'Email': row[2], 'Birthday': dt.datetime.strptime(row[3], '%m/%d/%Y')}
# Hint6: Use the FileNotFoundError exception to catch if the file does not exist.

# Declare the 'contact' dictionary
contact = {}
def import_csv(filename):

    if os.path.exists(filename):
        with open("contacts.csv", "r+", encoding="utf-8") as file:
            next(file)
            reader = csv.reader(file)
            for row in reader:
                contact[row[0]] = {
                    "Phone": row[1],
                    "Email": row[2],
                    "Birthday": dt.datetime.strptime(row[3], "%m/%d/%Y"),
                }
        print("Contacts imported successfully")
    else:
        raise FileNotFoundError("File does not exist")


# add_contact(name, phone, email, birthday) - This function will add a contact to the dictionary. The function will take four parameters, the name, phone number, email address, and birthday. The function will return True if the contact was added and False if the contact was not added. The function will display an error message if the contact already exists.
# Hint 1: You will need to convert the birthday to a datetime object. You can do that by using the strptime function. IE. dt.datetime.strptime(birthday, '%m/%d/%Y')
# Hint 2: To add a contact to the dictionary, you need to use the key as the name and the values as a dictionary that contains the phone number, email address, and birthday. To reference the specific key you can use contact[name]
    

def add_contact(name, phone, email, birthday):
    if name in contact:
        print("Contact already exists")
        return False
    else:
        contact[name] = {
            "Phone": phone,
            "Email": email,
            "Birthday": dt.datetime.strptime(birthday, "%m/%d/%Y"),
        }
        return True

# view_contacts() - This function will display the contacts in the dictionary. The function will take no parameters. The function will return nothing. The function will display a message if there are no contacts in the dictionary. Use string formatting to display the contacts in a table format. The table should have a header row and each contact should be on a separate row. The table should have the following columns: Name, Phone, Email, Birthday. The birthday should be formatted as mm/dd/yyyy. The table should be sorted by name.
# Hint 1: You will need to loop through the dictionary to display the contacts. IE. for key, value in contact.items():

    
def view_contacts():
    if not contact:
        print("No contacts available")

    header = "{:<22}{:<20}{:<40}{:<20}".format("Name", "Phone", "Email", "Birthday")
    print(header)

    for key in sorted (contact.keys()):
        value = contact[key]
        print(
            "{:<22}{:<20}{:<40}{:<20}".format(
                key,
                value["Phone"],
                value["Email"],
                value["Birthday"].strftime("%m/%d/%Y"),
            )
        )

# Extra Credit: The data is a dictionary of dictionaries. You can unpack the dictionary into a list of dictionaries. Like in Lab 10 and then use the tabulate library to display the contacts in a table format. This is optional and not required. You can use string formatting to display the contacts in a table format.
        
# def view_contacts():
#     if not contact:
#         print("No contacts available")
#     else:
#         print(
#             tabulate.tabulate(
#                 contact.items(),
#                 headers=["Name", "Phone", "Email", "Birthday"],
#                 tablefmt="fancy_grid",
#             )
#         )

# delete_contact(id) - This function will delete a contact from the dictionary. The function will take one parameter, the name of the contact to delete. The function will return True if the contact was deleted and False if the contact was not deleted. The function will display an error message if the contact does not exist.


def delete_contact(name):
    if name in contact:
        del contact[name]
        return True
    else:
        return False


# next_birthday() - This function will display the next birthday. The function will take no parameters. The function will return nothing. The function will display a message if there are no contacts in the dictionary. The function will display a message if there are no birthdays in the next 30 days. The function will display the next birthday and name if there is a birthday in the next 30 days. Use string formatting to display the next birthday. The next birthday should be sorted by the next birthday. The next birthday should be formatted as mm/dd/yyyy.
# Hint: We dont care about the year, only the month and day. There are many ways to solve this issue. 1st you could replace all the years with the current year.2nd you could use the month and day attributes of the datetime object to compare the month and day of the birthday to the current month and day.


def next_birthday():
    today = dt.datetime.today()
    nxt_birthday = dt.datetime(2024, 12, 31)
    for key, value in contact.items():
        if (
            value["Birthday"].month == today.month
            and value["Birthday"].day == today.day
        ):
            print(f"{key}'s birthday is today!")
        elif (
            value["Birthday"].month == today.month and value["Birthday"].day > today.day
        ):
            if value["Birthday"] < nxt_birthday:
                nxt_birthday = value["Birthday"]
                next_birthday_name = key
    if nxt_birthday > (dt.datetime.today() + (dt.timedelta(days=30))):
        print("There are no birthdays in the next 30 days")
    else:
        print(
            f'The next birthday is {next_birthday_name} on {nxt_birthday.strftime("%m/%d/%Y")}'
        )


# save_csv(filename) - This function will save the contacts to the csv file. Prompt the user to enter a filename to save the contacts to. If the file exists, overwrite the file. If the file does not exist, create the file. The function will return True if the contacts were saved and False if the contacts were not saved.
# Hint1: Use the csv module to write the csv file. Use the csv.writer function. IE. writer = csv.writer(file)

def save_csv(filename):
    if os.path.exists(filename):
        with open("contacts.csv", "w+", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone", "Email", "Birthday"])
            for key, value in contact.items():
                writer.writerow(
                    [
                        key,
                        value["Phone"],
                        value["Email"],
                        value["Birthday"].strftime("%m/%d/%Y"),
                    ]
                )
        print("Contacts saved successfully")
        return True
    else:
        return False
    
def menu():
    print(
        """
    1. Add contact
    2. View contacts
    3. Delete contact
    4. Save contacts to csv file
    5. Next Birthday
    0. Quit
    """
    )
    choice = int(input("Enter your choice: "))
    return choice

# The main function will be used to run the program. The main function will use a while loop to display the menu and get the user's choice. The main funtion will call the appropriate function based on the user's choice. The main function will also call the save_csv function to save the contacts to the csv file before the program ends.0

def main():
    import_csv("contacts.csv")
    while True:
        try:
            choice = menu()
            if choice < 0 or choice > 5:
                print("\nInvalid choice\n")
                continue
        except ValueError:
            print("\nInvalid choice\n")
            continue
        if choice == 1:
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")
            birthday = input("Enter contact birthday (mm/dd/yyyy): ")
            add_contact(name, phone, email, birthday)
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            name = input("Enter contact name: ")
            delete_contact(name)
        elif choice == 4:
            save_csv("contacts.csv")
        elif choice == 5:
            next_birthday()
        elif choice == 0:
            save_csv("contacts.csv")
            break

    # After you are done with the program, answer the following questions using code (show your code and output):
    # How many names start with the letter A?

    # How many emails are yahoo emails?

    # How many .org emails are there?

    # How many contacts have a birthday in January?

    # Fix: Add an indented block inside the main() function

if __name__ == "__main__":
    main()
