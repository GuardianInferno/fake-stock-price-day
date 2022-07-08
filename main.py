import numpy as np
import matplotlib.pyplot as plt
import random as rand
import pandas as pd
import datetime as dt

mu_sign = [-1, 1]
items = ['soap', 'hairclip', 'flashlight']

mu = rand.random() * 0.001 * rand.choice(mu_sign)
print(mu)
sigma= 0.01
print(sigma)
start_price = 5
np.random.seed(0)
returns = np.random.normal(loc=mu, scale=sigma, size=1440) #1440 is minutes in one day
price = start_price*(1+returns).cumprod()

plt.plot(price)
plt.ylabel('price')
plt.xlabel('time(min)')


plt.show()