#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Execício 5 - Racionalização de produção TPI - PO

# Este exemplo formula e resolve o seguinte exercício/problema:
# maximizar 
# 120x1 + 150x2 z 
# sujeito a 
# 2x1 + 4x2 <= 100
# 3x1 + 2x2 <= 90
# 5x1 + 3x2 <= 120

# x1, x2 binário
import gurobipy as gp


# In[3]:


# Crie o modelo 
m = gp.Model ( " Execício 5 - Racionalização de produção TPI " )

# Crie/Insere variáveis de decisão 
x1= m.addVar () #Quantidade de P1
x2= m.addVar () #Quantidade de P2
    
# Definir a função objetivo 
#Maximizar o lucro para a empresa
m.setObjective ( 120 * x1 + 150 * x2, sense=gp.GRB.MAXIMIZE )  

# Adicionar/Insere as restrição do modelo: 2x1 + x2 <= 1000    
#addConstr adiciona restrições ao modelo

c1 = m.addConstr ( 2 * x1 + 4 * x2 <= 100 ) #Restrição do recurso R1    

# Adicionar restrição:  3x1 + 2x2 <= 90
c2 = m.addConstr (  3 * x1 + 2 * x2 <= 90 )  #Restrição do recurso R2

# Adicionar restrição:  5x1 + 3x2 <= 120
c3 = m.addConstr (  5 * x1 + 3 * x2 <= 120 )  #Restrição do recurso R3

 
# Adicionar restrição:  
# Não tem restrições negativas - Nâo incluí no modelo  

# Resolve/Otimize o modelo 

m.optimize () #Chamar o solver e reslver o modelo
print ("")
print ("Solução: ")
#Acessar a solução
#Imprimir o minimo de produção OU o quandto vou produzir
#Aacessando o valor dessa variável (x1 e x2) na solução ótima
print ("Quatidade de P1:", x1.x)
print ("Quatidade de P2:", x2.x)


# In[ ]:




