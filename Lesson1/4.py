second = int(input())

days = second // 86400
hours = (second - days*86400) // 3600
minutes = ((second - days*84600) - hours*3600) // 60
seconds = (((second - days*84600) - hours*3600) - minutes*60)
print('Дни: ', days, 'Часы: ', hours, 'Минуты: ', minutes, 'Секунды: ', seconds)