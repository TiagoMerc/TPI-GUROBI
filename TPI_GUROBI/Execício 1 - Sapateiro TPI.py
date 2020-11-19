#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Execício 1 - Sapateiro TPI - PO

# Este exemplo formula e resolve o seguinte exercício/problema:
# maximizar 
# 5x1 + 2x2 z 
# sujeito a 
# 2x1 + x2 <= 6 
# 10x1 + 12x2 <= 60 
# x1, x2 binário
import gurobipy as gp


# In[8]:


# Crie o modelo 
m = gp.Model ( " Execício 1 - Sapateiro " )

# Crie/Insere variáveis de decisão 
x1= m.addVar () #Quantidade de sapatos por hora
x2= m.addVar () #Quantidade de cintos por hora 
    
# Definir a função objetivo 
#Maximizar o lucro pro hora
m.setObjective ( 5 * x1 + 2 * x2, sense=gp.GRB.MAXIMIZE )  

# Adicionar/Insere as restrição do modelo: 2x1 + x2 <= 6  
#addConstr adiciona restrições ao modelo 
c1 = m.addConstr ( 2 * x1 + x2 <= 6  )      

# Adicionar restrição: 10x1 + 12x2 <= 60 
c2 = m.addConstr ( 10 * x1 + 12 * x2 <= 60 )  

# Adicionar restrição:  
# Não tem restrições negativas - Nâo incluí no modelo  

# Resolve/Otimize o modelo 

m.optimize () #Chamar o solver e reslver o modelo
print (" ")
print ("Solução: ")
#Acesar a solução
#Imprimir o minimo de produção OU o quanto vou produzir
#Aacessando o valor dessa variável (x1) na solução ótima
print ("Quantidade de sapatos por hora:", x1.x)
print ("Quantidade de cintos por hora:", x2.x)

   


# In[ ]:





# In[ ]:




