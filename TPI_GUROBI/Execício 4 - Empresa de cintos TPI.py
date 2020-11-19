#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Execício 4 - Empresa de cintos TPI - PO

# Este exemplo formula e resolve o seguinte exercício/problema:
# maximizar 
# 4x1 + 3x2 z 
# sujeito a 
# 2x1 + x2 <= 1000 
# x1 + x2 <= 800
# x1 <= 400
# x2 <= 700

# x1, x2 binário
import gurobipy as gp


# In[3]:


# Crie o modelo 
m = gp.Model ( " Execício 4 - Empresa de cintos TPI " )

# Crie/Insere variáveis de decisão 
x1= m.addVar () #Quantidade de M1/dia
x2= m.addVar () #Quantidade de M2/dia
    
# Definir a função objetivo 
#Maximizar o lucro diário da empresa
m.setObjective ( 4 * x1 + 3 * x2, sense=gp.GRB.MAXIMIZE )  

# Adicionar/Insere as restrição do modelo: 2x1 + x2 <= 1000    
#addConstr adiciona restrições ao modelo

c1 = m.addConstr ( 2 * x1 + x2 <= 1000 ) #Restrição volume de produção    

# Adicionar restrição:  x1 + x2 <= 800 
c2 = m.addConstr (  x1 + x2 <= 800 )  #Restrição capacidade máxima de produção devido couro

# Adicionar restrição:   x1 <= 400
c3 = m.addConstr (  x1 <= 400 )  #Restrição disponibilidade diária de fivela para M1

# Adicionar restrição:   x2 <= 700
c4 = m.addConstr ( x2 <= 700 )  #Restrição disponibilidade diária de fivela para M2

# Adicionar restrição:  
# Não tem restrições negativas - Nâo incluí no modelo  

# Resolve/Otimize o modelo 

m.optimize () #Chamar o solver e reslver o modelo
print ("")
print ("Solução: ")
#Acessar a solução
#Imprimir o minimo de produção OU o quandto vou produzir
#Aacessando o valor dessa variável (x1 e x2) na solução ótima
print ("Quatidade M1:", x1.x)
print ("Quatidade M2:", x2.x)
   


# In[ ]:




