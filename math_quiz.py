


months ={1:'January', 2: 'February', 3:'March', 4:'April', 5 :'May', 6: 'June', 7: 'July', 8 :"August", 9:'September',
        10:'October', 11 :'November', 12:'December'}

month =input("Please choose wich month (1-12) you would like more information on and type'months' for all months, ex 1 = January\n")
if month in months.items():
    print('thank you for your input')

else:
    print('Please Retry')
