def high_Salary(salaries,limit):
    return [s for s in salaries if s>limit]


print(high_Salary([20000,50000,30000], 30000))