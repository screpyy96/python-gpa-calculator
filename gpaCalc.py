def valid():
    while True:
        try:
            x=int(input())
        except ValueError:
            print('input valid char')
            continue

        else:
            if x >=0 and x<=100:
                return x
                break
            else:
                print('please input a valid number')

                
def moduleResults(Y):
    if Y == 'F':
        return 'Failed the Module'
    elif Y == 'P':
        return 'Passed the Module'
    elif Y == 'C':
        return 'Credit'
    elif Y == 'B':
        return 'Distinction '
    elif Y == 'A':
        return 'Upper Distinction'

def moduleMark(mark):
        if mark >=0 and mark <= 39:
            return 'F',0
        else:
           if mark >=40 and mark <= 49:
                return  'P', 2
           else:
                if mark >=50 and mark <= 59:
                    return 'C', 3
                else:
                    if mark >=60 and mark <=69:
                        return 'B',4
                    else:
                        return 'A', 5
                    

while True:
    print('**********Welcome**********')
    user=input('What is your Name? \n')
    print('Hi', user, '! Welcome to your GPA Calculator\n')
    print('Please enter your English grade \n')
    english = valid()
    print('Please enter your Math grade')
    math=valid()
    print('Please enter your Database grade')
    database=valid()
    print('Please enter your Programming grade')
    programming = valid()
    
  #calculate grades
    englishMark, englishCredit = moduleMark(english)
    mathMark, mathCredit = moduleMark(math)
    databaseMark, databaseCredit = moduleMark(database)
    programmingMark, programmingCredit = moduleMark(programming)
  
    print('English Grade:', english,', Credit: ', englishCredit, 'You have ', moduleResults(englishMark))
    print('Math Grade', math,', Credit: ', mathCredit, 'You have ', moduleResults(mathMark))
    print('Database Grade', database,', Credit: ', databaseCredit, 'You have ', moduleResults(databaseMark))
    print('Programming Grade', programming,', Credit: ', mathCredit, 'You have ', moduleResults(programmingMark))
    print('************************************************')
    #GPA Formula
    gpa = (englishCredit*2+mathCredit*3+databaseCredit*3+programmingCredit*2)/10
    print ('Your GPA: *****', gpa, ' *****')
    
    print('To exit type < N >, to start again type any < Y > \n')
    y = input()
    if y == 'y':
        continue
    elif y == 'n':
        print('Enjoy your Holiday \n')
        break
   
    
exit()
    



