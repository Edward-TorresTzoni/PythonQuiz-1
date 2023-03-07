print('QUIZ!')
print('----------')
#Project1 - Put a number, in this case 80000, and add 10% more to the total.
#Then write the total as a proper number.

money = float(input('Enter the amount of money, and we\'ll add 10% more: $'))
tenPercentMore = money * 0.10
totalOutcome = money + tenPercentMore
print("Your total will be ${:,.2f}".format(totalOutcome))

print('----------')
#Project2 - Enter four test scores and print both total scores and average of all scores.
AllScores = 4
ListOfScores = []
for counter in range (AllScores):
    testScore = int(float(input('Please enter four scores: ')))
    
    averageScores = sum(ListOfScores) / AllScores
    
    ListOfScores.append(testScore)
    
if len(ListOfScores) == AllScores:
        print("Sum: ", sum(ListOfScores))
        print("Average: ", averageScores)

print('----------')
#Project3 - Enter my name, first and last, and enter my age. Then, show my status.
FirstName = input('Please enter your first name: ')
LastName = input('Now your last name: ')
Age = input('Finally, enter your age: ')
print(FirstName, LastName, ',', Age)

print('----------')
#Project4 - Ask the customer to enter their sales, and show the commission they'll pay.
salesToBe_Paid = float(input('How much money will you put in this sale? $'))
if salesToBe_Paid >= 50000.00 and salesToBe_Paid <= 65000.00:
    CommissionAdded1 = 70000 * 0.10
    totalSales = salesToBe_Paid + CommissionAdded1
    print('You\'ll pay 10% in commissions.')
    print("Your overall sales total: ${:,.2f}".format(totalSales))
elif salesToBe_Paid >= 70000.00 and salesToBe_Paid <= 80000.00:
    CommissionAdded2 = 80000 * 0.20
    totalSales = salesToBe_Paid + CommissionAdded2
    print('You\'ll pay 20% in commissions.')
    print("Your overall sales total: ${:,.2f}".format(totalSales))
elif salesToBe_Paid >= 90000.00 and salesToBe_Paid <= 100000.00:
    CommissionAdded3 = 90000 * 0.30
    totalSales = salesToBe_Paid + CommissionAdded3
    print('You\'ll pay 30% in commissions.')
    print("Your overall sales total: ${:,.2f}".format(totalSales))

#Project5 is involved in this. Add more money according to how much the user added in sales. Then show total.

print('----------')
#Project6 - Enter four test scores, and write the grade for the appropriate test score.
#Further, project an error if the average test scores is more than 100.
print('You have four test scores to give a grade. Submit their total score and I\'ll assign the grade.')

for counter in range (4):
    Input_TestScore = int(input('Enter scores from the test: '))    
    print(Input_TestScore)
    if Input_TestScore < 60: print('F')
    elif Input_TestScore >= 60 and Input_TestScore <= 69:print('D')
    elif Input_TestScore >= 70 and Input_TestScore <= 79:print('C')
    elif Input_TestScore >= 80 and Input_TestScore <= 89:print('B')
    elif Input_TestScore >= 90 and Input_TestScore <= 100:print('A')
    else:print("Invalid test score, restart the process.")
