# HW8.py
# Author: Nate Harris

# This homework will exapnd upon the code for Lab9.py. If you did not complete Lab9.py, you should do so before attempting this homework.

# Copy the code from Lab9.py into this file. I'll add some comments to help you out.

# Import statements (activate venv and install streamlit if you haven't already)

import datetime as dt
import streamlit as sl


# Streamlit title, subtitle.

sl.title("Days till Counter")
sl.subheader("Enter dates and We'll tell you how many days until then")

#Streamlit date input and button combos for birthday, end of semester, and New Years Day.

bdate = sl.date_input("Use calander to get days until your Birthday: ", format="MM/DD/YYYY")
bday = sl.button("Days until Birthday")

sdate = sl.date_input("Use calander and select the date the semester ends: ", format="MM/DD/YYYY")
SemesterButton = sl.button("Days until the end of the semester")

nydate = sl.date_input("Use calander to select New Years day: ", format="MM/DD/YYYY")
NewYearsButton = sl.button("Days until New Year's Day")

#bday = sl.button("Days until Birthday")
#SemesterButton = sl.button("Days until the end of the semester")
#NewYearsButton = sl.button("Days until New Year's Day")

# The calculate_days function from Lab9.py

# def calculate_days(date) -> int:
#     """Calculate the number of days until the date entered by the user.

#     Args:
#         date (datetime.date): The date entered by the user.

#     Returns: 
#         int: The number of days until the date entered by the user.
#     """
#     current_date = dt.datetime.now().date()
#     days_diff = date - current_date
#     if days_diff.days < 0:
#         raise ValueError("The date entered is in the past") 
#     return days_diff.days


# START OF HOMEWORK Questions

# 1. Create a function calculate_days_until_birthday that will calculate how many days from now until the user's birthday. The function should take in the user's birthday as a parameter and return the number of days until their birthday. The function should also display the number of days until their birthday in the Streamlit app. The function should be called in the app function.

def days_until_birthday(bdate) -> int:
    """Calculate the number of days until the date entered by the user.

    Args:
        date (datetime.date): The date entered by the user.

    Returns: 
        int: The number of days until the date entered by the user.
    """
    current_date = dt.datetime.now().date()
    days_diff = bdate - current_date
    if days_diff.days < 0:
        raise ValueError("The date entered is in the past") 
    return days_diff.days
# birthday = dt.date(2022, 4, 1)



# 2. Create a function days_until_semester_ends that will calculate how many days from now until the end of the semester. The function should take in the current date as a parameter and return the number of days until the end of the semester. The function should also display the number of days until the end of the semester in the Streamlit app. The function should be called in the app function.
# Hint: You can use the date object to create a date for the end of the semester. IE.
# end_of_semester = dt.date(2023, 12, 8)

def days_until_semester_ends(sdate) -> int:
    """Calculate the number of days until the date entered by the user.

    Args:
        date (datetime.date): The date entered by the user.

    Returns: 
        int: The number of days until the date entered by the user.
    """
    current_date = dt.datetime.now().date()
    #end_of_semester = dt.date(2023, 12, 16). I commented this out because prefer the user use the calander to select the date.
    days_diff = sdate - current_date
    if days_diff.days < 0:
        raise ValueError("The date entered is in the past") 
    return days_diff.days

#SemesterButton = sl.button("Days until the end of the semester")

# 3. Create a function days_until_new_years that will calculate how many days from now until New Year's Day. The function should take in the current date as a parameter and return the number 
# of days until New Year's Day. The function should also display the number of days until New Year's Day in the Streamlit app. The function should be called in the app function. Also include 
# an emoji of a party popper in the Streamlit app.
# Hint: You can use the date object to create a date for New Years. IE. 
# new_years = dt.date(2024, 1, 1)
# Hint: To add an emoji, use the st.write() function. IE. st.write("🎉")

def days_until_new_years(nydate) -> int:
    """Calculate the number of days until the date entered by the user.

    Args:
        date (datetime.date): The date entered by the user.

    Returns: 
        int: The number of days until the date entered by the user.
    """
    current_date = dt.datetime.now().date()
    #new_years = dt.date(2024, 1, 1). I commented this out because prefer the user use the calander to select the date.
    days_diff = nydate - current_date
    if days_diff.days < 0:
        raise ValueError("The date entered is in the past") 
    return days_diff.days


# 4. create a button that will display the number of days until New Year's Day when clicked. The button should be labeled "Days until New Year's Day". The button should call the 
# days_until_new_years function when clicked. The button should be placed below the "Calculate" button.Inside the app function call the days_until_new_years function when the button is clicked.

#NewYearsButton = sl.button("Days until New Year's Day")

# Hint: You can use the st.button() function. IE. button = st.button("Click me")
# Hint2: the days_until_new_years function takes in the current date as a parameter. You can use the dt.datetime.now().date() function to get the current date. 
# IE. current_date = dt.datetime.now().date()
# Hint3: You can use the days_until_new_years function to get the number of days until New Year's Day. IE. days_until_new_years(current_date) This is where you include the emoji  🎉


# app function from Lab9.py

def app():
    if bday:
        try:
            result = days_until_birthday(bdate)
            sl.write(result)
        except ValueError:
            sl.write("Please enter a future date")
            
    if SemesterButton:
        try:
            result = days_until_semester_ends(sdate)
            sl.write(result)
        except ValueError:
            sl.write("Please enter a future date")

    if NewYearsButton:
        try:
            result = days_until_new_years(nydate)
            sl.write((result), "🎉")
        except ValueError:
            sl.write("Please enter a future date")

if __name__ == '__main__':
    app()