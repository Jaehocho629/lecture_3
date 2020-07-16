import func_module

# func_module.module_show()

nowdate = func_module.date_now()
now_year = nowdate.year
now_month = nowdate.month
now_day = nowdate.day



# print(nowdate)
print(now_year,"년",now_month,"월",now_day,"일")

x_mas = nowdate.replace(month = 12, day=25)

date_xmas = '{}년 {}월 {}일'.format(x_mas.year , x_mas.month ,x_mas.day)
print(date_xmas)