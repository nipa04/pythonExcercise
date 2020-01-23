# from datetime import datetime
# a = ['7-Mar-14', '10-Mar-14', '11-Mar-14', '14-Mar-14', '15-Mar-14', '17-Mar-14', '22-Mar-14', '23-Mar-14', '25-Mar-14', '1-Nov-13', '5-Nov-13', '8-Nov-13', '23-Nov-13', '24-Nov-13', '25-Nov-13', '26-Nov-13', '3-Dec-13', '9-Dec-13', '13-Dec-13', '9-Jan-14', '17-Jan-14', '20-Jan-14', '8-Feb-14', '9-Feb-14', '10-Feb-14', '11-Feb-14', '12-Feb-14', '16-Feb-14', '17-Feb-14', '19-Feb-14', '22-Feb-14', '26-Feb-14', '28-Feb-14', '2-Mar-14', '4-Mar-14', '31-Mar-14', '1-Apr-14', '2-Apr-14', '4-Apr-14', '6-Apr-14', '8-Apr-14',
#      '9-Apr-14', '15-Apr-14', '16-Apr-14', '17-Apr-14', '18-Apr-14', '20-Nov-13', '5-Dec-13', '15-Dec-13', '15-Jan-14', '19-Jan-14', '26-Jan-14', '3-Feb-14', '6-Feb-14', '14-Feb-14', '21-Feb-14', '24-Feb-14', '1-Mar-14', '5-Mar-14', '12-Mar-14', '19-Mar-14', '20-Mar-14', '21-Mar-14', '24-Mar-14', '26-Mar-14', '27-Mar-14', '29-Mar-14', '30-Mar-14', '7-Apr-14', '10-Apr-14', '11-Apr-14', '12-Apr-14', '27-Nov-13', '16-Jan-14', '27-Jan-14', '6-Mar-14', '13-Mar-14', '16-Mar-14', '18-Mar-14', '28-Mar-14', '3-Apr-14', '5-Apr-14']
# a.sort(key=lambda date: datetime.strptime(date, "%d-%b-%y"))
# print(a)
numbers = [2, 4, 6, 8, 10]
lgNum = numbers[0]

for number in numbers:
    if number > lgNum:
        lgNum = number
print(lgNum)
