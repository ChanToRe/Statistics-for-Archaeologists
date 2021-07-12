import math
import pandas as pd
import numpy as np
from numpy import linspace
import scipy.stats
import matplotlib.pyplot as plt

data = pd.read_csv("/Users/jch/Desktop/test.csv") #data load

#교차분할표
crosstab = pd.crosstab(data.Sex, data.RorL)
print(crosstab)
print("-------------------------------------------")

#카이제곱검정
#연속성 수정 O
chi2, pvalue, df, expected = scipy.stats.chi2_contingency(crosstab, correction=True)
print('chi^2 = ', chi2) #x2
print('p-value = ', pvalue) #p-value
print('자유도 = ', df) #자유도
print('e-expected = ', expected) #expected value
print("-------------------------------------------")
#연속성 수정 X
chi2_2, pvalue_2, df_2, expected_2 = scipy.stats.chi2_contingency(crosstab, correction=False)
print('chi^2 = ', chi2_2) #x2
print('p-value = ', pvalue_2) #p-value
print('자유도 = ', df_2) #자유도
print('e-expected = ', expected_2) #expected value
print("-------------------------------------------")

#카이제곱분포
chi2_graph = np.linspace(0.5, 50, 200)
y = (1 / (math.gamma(df / 2) * (1 / 2 ** (df / 2)))) * (chi2_graph ** ( df / 2 - 1)) * np.exp(- chi2_graph / 2)

#시각화
plt.figure(figsize=(6, 6))
plt.plot(chi2_graph, y, label=r'$\chi^2-distribution$')
plt.axvline(x=chi2, color='red', linestyle = ':')
plt.axvline(x=chi2_2, color='blue', linestyle = ':')
plt.text(chi2, .4, '  result1($\chi^2$)  \n=  ' + str(round(chi2, 4)) + '  ', horizontalalignment='right', color='red')
plt.text(chi2_2, .6, '  result2($\chi^2$)\n  =' + str(round(chi2_2, 4)), horizontalalignment='left', color='blue')
plt.xlabel(r'$\chi^2$')
plt.ylabel('y')
plt.grid()
plt.title('$\chi^2$ (df=1)')
plt.legend()
plt.show()