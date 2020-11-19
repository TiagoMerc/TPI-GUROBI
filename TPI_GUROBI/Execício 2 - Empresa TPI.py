#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Execício 2 - Empresa TPI - PO

# Este exemplo formula e resolve o seguinte exercício/problema:
# maximizar 
# 100x1 + 150x2 z 
# sujeito a 
# 2x1 + 3x2 <= 120 
#  x1 <= 40 
#  x2 <= 30 
# x1, x2 binário
import gurobipy as gp


# In[15]:


# Crie o modelo 
m = gp.Model ( " Execício 2 - Empresa  " )

# Crie/Insere variáveis de decisão 
x1= m.addVar () #Quantidade de P1
x2= m.addVar () #Quantidade de P2 
    
# Definir a função objetivo 
#Maximizar o lucro da empresa
m.setObjective ( 100 * x1 + 150 * x2, sense=gp.GRB.MAXIMIZE )  

# Adicionar/Insere as restrição do modelo: 2x1 + 3x2 <= 120   
#addConstr adiciona restrições ao modelo

c1 = m.addConstr ( 2 * x1 + 3 * x2 <= 120   ) #Restrição por tempo de produção     

# Adicionar restrição:  x1 <= 40  #Restrição por produção
c2 = m.addConstr ( x1 <= 40 )  

# Adicionar restrição:  x2 <= 30 #Restrição por produção
c3 = m.addConstr ( x2 <= 30 )  

# Adicionar restrição:  
# Não tem restrições negativas - Nâo incluí no modelo  

# Resolve/Otimize o modelo 

m.optimize () #Chamar o solver e reslver o modelo
print ("")
print ("Solução: ")
#Acessar a solução
#Imprimir o minimo de produção OU o quandto vou produzir
#Aacessando o valor dessa variável (x1) na solução ótima
print ("Quantidade de P1:", x1.x)
print ("Quantidade de P2:", x2.x)
   




# In[ ]:





# In[ ]:




