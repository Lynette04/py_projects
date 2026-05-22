import calendar
from datetime import datetime 

print("--------WELCOME TO THE CALCULATOR CALENDAR--------")
print("""---WHAT IT CAN DO---
          1. You can find out the number of months between two dates of your choice.
          2. You can find out how many months between 2 dates have either 30 or 31 days and which months they are.
        """)
print("Let's start!\n")

#collect dates from user
start_date_str  = input("Enter the start date in the format(dd/mm/yyyy): ")
end_date_str = input("Enter the end date in the format(dd/mm/yyyy): ")

try:
    start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
    print(f"\nYour start date is {start_date.strftime("%d/%m/%Y")}.")
    end_date = datetime.strptime(end_date_str, "%d/%m/%Y").date()
    print(f"Your end date is {end_date.strftime("%d/%m/%Y")}.")
    
    num_months= input("\nDo you want to know how many months are in between your dates (yes/no):").lower() 
    if num_months=='yes':
        calc_months = abs((end_date.year - start_date.year)*12 + (end_date.month - start_date.month))
        print(f"There are {calc_months} months  between {start_date} and {end_date}.")    

    months_between= input("\nDo you want to know how many months between your dates have either 30 or 31 days(yes/no): ").lower()
    if months_between=='yes':
        days = int(input("Enter the days(30 or 31): "))
        count=0 #initialize month counter to zero
        month_names=[] #list that contains the months
        
        current_year = start_date.year
        current_month = start_date.month
        
        #loop through the months from the start date to the end date
        while(current_year,current_month)<=(end_date.year, end_date.month):
            days_in_month = calendar.monthrange(current_year,current_month)[1]
            if days_in_month==days:
                count+=1
                name = f"{calendar.month_name[current_month]}{current_year}"
                month_names.append(name)
            
            current_month+=1
            if current_month > 12:
                current_month = 1
                current_year+=1
            
        print(f"There are {count} months with {days} days.")
        print(f"The months between are:", ", ".join(month_names))
        print("Bye-Bye!😊")
    else:
        print("Bye-Bye!😊")          
except ValueError:
    print("❌Invalid input, Correct format: dd/mm/yyyy")


