def investment_value(start, interest_rate, tax_rate, deposit, years):
    balance = start
    for _ in range(1, years + 1):
        interest_earned = balance * interest_rate
        taxes = interest_earned * tax_rate
        balance += (interest_earned - taxes + deposit)
    return balance

def years_to_reach_goal(start, interest_rate, tax_rate, deposit, goal):
    years = 0
    balance = start
    while balance < goal:
        interest_earned = balance * interest_rate
        taxes = interest_earned * tax_rate
        balance += (interest_earned - taxes + deposit)
        years += 1
    return years

print(investment_value(start=1000, interest_rate=0.05, tax_rate=0, deposit=0, years=10))  
print(years_to_reach_goal(start=1000, interest_rate=0.05, tax_rate=0, deposit=0, goal=100000)) 
print(investment_value(start=1000, interest_rate=0.05, tax_rate=0, deposit=100, years=10))  
print(years_to_reach_goal(start=1000, interest_rate=0.05, tax_rate=0, deposit=100, goal=100000)) 
print(investment_value(start=10000, interest_rate=0.13, tax_rate=0.25, deposit=1000, years=30))  
print(years_to_reach_goal(start=10000, interest_rate=0.13, tax_rate=0.25, deposit=1000, goal=100000))  
print(investment_value(start=1, interest_rate=1, tax_rate=0, deposit=0, years=20)) 
print(years_to_reach_goal(start=1, interest_rate=1, tax_rate=0, deposit=0, goal=100000)) 

