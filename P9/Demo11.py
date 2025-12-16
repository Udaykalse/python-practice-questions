def second_Highest(sales):
    return sorted(set(sales))[-2]


print(second_Highest([100,200,300,300]))