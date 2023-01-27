import numpy as np
from datetime import datetime as dt

currentYear = dt.now().year
currentYear2 = dt.now().year

month = str(input('Digite o número correspondente do mês: '))
month2 = str(int(month) + 1)

if (int(month) < 10):
  month = '0' + month

if (int(month2) < 10):
  month2 = '0' + month2
elif (int(month2) > 12):
  month2 = '01'
  currentYear2 = currentYear2 + 1

input = '{y}-{m}'.format(y=currentYear, m=month)
input2 = '{y}-{m}'.format(y=currentYear2, m=month2)

qtSun = np.busday_count(input, input2,weekmask='Sun')
qtMon = np.busday_count(input, input2,weekmask='Mon')
qtTue = np.busday_count(input, input2,weekmask='Tue')
qtWed = np.busday_count(input, input2,weekmask='Wed')
qtThu = np.busday_count(input, input2,weekmask='Thu')
qtFri = np.busday_count(input, input2,weekmask='Fri')
qtSat = np.busday_count(input, input2,weekmask='Sat')

gramasSun = qtSun * 600 #bife
gramasMon = qtMon * 400 #frango
gramasTue = qtTue * 400 #figado
gramasWed = qtWed * 400 #frango
gramasThu = qtThu * 400 #figado
gramasFri = qtFri * 400 #frango
gramasSat = qtSat * 400 #frango

kgChicken = (gramasMon + gramasWed + gramasFri + gramasSat) / 1000
kgFigado = (gramasTue + gramasThu) / 1000
kgBife = gramasSun / 1000

approximateValueChickenKg = 20
approximateValueFigadoKg = 25
approximateValueBifeKg = 33

costForecastChicken = approximateValueChickenKg * kgChicken
costForecastFigado = approximateValueFigadoKg * kgFigado
costForecastBife = approximateValueBifeKg * kgBife
costForecastTotal = costForecastChicken + costForecastFigado + costForecastBife

print('')
print('PREVISÃO DE CONSUMO EM KG COM PROTEÍNA:')
print('Frango: {kg}KG'.format(kg=kgChicken))
print('Fígado: {kg}KG'.format(kg=kgFigado))
print('Bife: {kg}KG'.format(kg=kgBife))

print('')
print('PREVISÃO DE GASTOS COM PROTEÍNA:')
print('Gasto previsto com Frango: R$ {exp}'.format(exp=costForecastChicken))
print('Gasto previsto com Fígado: R$ {exp}'.format(exp=costForecastFigado))
print('Gasto previsto com Bife: R$ {exp}'.format(exp=costForecastBife))
print('Gasto previsto Total: R$ {exp}'.format(exp=costForecastTotal))
