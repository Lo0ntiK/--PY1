money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

summ_before_salary = money_capital
while True:
    summ_before_salary -= spend
    if summ_before_salary < 0:
        break
    summ_before_salary += salary
    month += 1
    spend *= (1+increase)
print(month)

