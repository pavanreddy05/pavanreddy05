from flask import Flask
import random
import datetime
randapp = Flask(__name__)
@randapp.route("/")
def rand():
    d = datetime.datetime.now()
    if d.hour >= 6 and d.hour < 12:
        print('Good Morning Sir/Madam')
    if d.hour >= 12 and d.hour < 4:
        print('Good Afternoon Sir/Madam')
    if d.hour >=16 and d.hour < 20:
        print('Good Evening Sir/Madam')
    if d.hour >= 20 :
        print('Good Night Sir/Madam')
    print('Take a deep breathe and note down the below number ')
    number = random.randint(1111,9999)
    print('The secret number is : ',number)
    return print('The secret number is : ',number)
