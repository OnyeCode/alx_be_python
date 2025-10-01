from datetime import datetime, timedelta

def display_current_datetime():
    global current_date
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = timedelta(days=number_of_days) + current_date
    print(f"Future date: {future_date.strftime('%y-%m-%d')}")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
