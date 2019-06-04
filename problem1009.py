name = input()
salary = float(input())
totalSold = float(input())
finalSalaryPercentValue = (totalSold * 15) / 100
finalSalary = salary + finalSalaryPercentValue
print("TOTAL = R$ " + str("{:.2f}".format(finalSalary)))