
# Basic Calendar Display : Display calendar for a given year/month.
import calendar
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): ")) 
cal = calendar.TextCalendar(calendar.SUNDAY)
month_calendar = cal.formatmonth(year, month)
print(month_calendar)
