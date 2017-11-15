from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt

#Ver 0.0.1
#Simple code using usage code
#overall code for testing macd, stoch, and sma without having
#to run usage code so many times
#takes in user input: stock name

stock = raw_input('Enter name of stock: ')
s1 = 'Moving Average Convergence Divergence for ' + stock
s2 = 'Stochastic for '+ stock
s3 = 'Simple Moving Average for '+ stock

ti = TechIndicators(key='GSD3E3P11LSBZG5O', output_format='pandas')
data, meta_data = ti.get_macd(symbol=stock, interval='monthly')
data.plot()
plt.title(s1)
print(data.head())
plt.show()

ti1 = TechIndicators(key='GSD3E3P11LSBZG5O', output_format='pandas')
data, meta_data = ti1.get_stoch(symbol=stock, interval='1min')
data.plot()
plt.title(s2)
print(data.head())
plt.show()

ti2 = TechIndicators(key='GSD3E3P11LSBZG5O', output_format='pandas')
data, meta_data = ti2.get_sma(symbol=stock, interval='monthly', time_period=60)
data.plot()
plt.title(s3)
print(data.head())
plt.show()