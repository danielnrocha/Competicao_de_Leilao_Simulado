#Importando bibliotecas
import scipy.stats as st
import scipy.integrate as inte
import numpy as np
import pandas as pd

#g é a probabilidade de um custo de produção x ser inferior ao valor mínimo de
#uma amostra de 7 elementos com distribuição double weibull
g= lambda x: (1-st.dweibull.cdf(x,2.29,41.57,24.71))**7

#Pegando os custos dados
custos=np.matrix(pd.read_excel("custos_g7 (2).xlsx",index_col=0))
lcustos=[]
for i in range(100):
    lcustos+=[custos[i,0]]
    
#Escolhendo estratégia ótima para cada custo.
#Obs.:Como a função scipy.integrate.quad só dá a integral em um intervalo e
#não a equação da integral e se sabe que a integral de g tende a 0 no infinito,
#a integral de g(x) é igual a -inte.quad(g,x,np.inf).
lb=[]
for i in range(100):
    lb+=[custos[i,0]+(inte.quad(g,custos[i,0],np.inf)[0]/g(custos[i,0]))]

#Escrevendo planilha de lances
d={'Custos': lcustos,"Lances": lb}
df1=pd.DataFrame(d)
df1.to_excel('Lances.xlsx')
