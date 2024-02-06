import calendar

date = int(input('Enter day: '))
month = int(input('Enter month: '))
year = int(input('Enter year: '))

cal =  calendar.month(year, month)
# print(cal)
# print(type(cal))      # ==> Type: String

# print(type(calendar.monthcalendar(year, month)))       # ==> Type: List
# print(calendar.monthcalendar(year, month))          # ==> Prints list view of month
# print(min(calendar.monthcalendar(year, month)))
# print(max(calendar.monthcalendar(year, month)))

if date > 0:
    pass            # Put your logic