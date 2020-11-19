#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Execício 3 - Rede de Televisão TPI - PO

# Este exemplo formula e resolve o seguinte exercício/problema:
# maximizar 
# 30000x1 + 10000x2 z 
# sujeito a 
# 20x1 + 10x2 <= 80 
#  x1 + x2 >= 5 
# x1, x2 binário
import gurobipy as gp


# In[5]:


# Crie o modelo 
m = gp.Model ( " Execício 3 - Rede de Televisão  " )

# Crie/Insere variáveis de decisão 
x1= m.addVar () #Frequência semanal A
x2= m.addVar () #Frequência semanal B 
    
# Definir a função objetivo 
#Maximizar o levar ao ar para obter o número máximo de telespectadores
m.setObjective ( 30000 * x1 + 10000 * x2, sense=gp.GRB.MAXIMIZE )  

# Adicionar/Insere as restrição do modelo: 20x1 + 10x2 <= 80    
#addConstr adiciona restrições ao modelo

c1 = m.addConstr ( 20 * x1 + 10 * x2 <= 80    ) #Restrição de música     

# Adicionar restrição:   x1 + x2 >= 5 
c2 = m.addConstr (  x1 + x2 >= 5 )  #Restrição propagaanda
 
# Adicionar restrição:  
# Não tem restrições negativas - Nâo incluí no modelo  

# Resolve/Otimize o modelo 

m.optimize () #Chamar o solver e reslver o modelo
print ("")
print ("Solução: ")
#Acessar a solução
#Imprimir o minimo de produção OU o quandto vou produzir
#Aacessando o valor dessa variável (x1 e x2) na solução ótima
print ("Frequência A:", x1.x)
print ("Frequência B:", x2.x)
   


# In[ ]:




