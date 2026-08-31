from datetime import datetime, timedelta

# ===== Task 1: Print today's date in DD-MM-YYYY format =====
today = datetime.now()
formatted_date = today.strftime("%d-%m-%Y")
print("Today's date:", formatted_date)

print()

# ===== Task 2: Print the current time in HH:MM:SS format =====
formatted_time = today.strftime("%H:%M:%S")
print("Current time:", formatted_time)

print()

# ===== Task 3: Calculate your age in days =====
birth_date = datetime(2004, 5, 15)  # replace with your actual date of birth (YYYY, M, D)
age_in_days = (today - birth_date).days
print("Your age in days:", age_in_days)

print()

# ===== Task 4: Find the date after 100 days from today =====
future_date = today + timedelta(days=100)
print("Date after 100 days:", future_date.strftime("%d-%m-%Y"))

print()

# ===== Task 5: Calculate the difference between your birthday and today's date =====
birthday_this_year = datetime(today.year, birth_date.month, birth_date.day)

if birthday_this_year < today:
    birthday_this_year = datetime(today.year + 1, birth_date.month, birth_date.day)

days_until_birthday = (birthday_this_year - today).days
print("Days until your next birthday:", days_until_birthday)