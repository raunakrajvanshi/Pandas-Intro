import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from pylab import * 


Cand2009 = pd.read_csv("LS2009Candidate.csv")
Cand2014 = pd.read_csv("LS2014Candidate.csv")

#Check the length of states
print(len(Cand2009['State name'].unique()))
Cand2009['State name'].unique()


Merged0914 = pd.concat([Cand2009,Cand2014])
print(len(Merged0914['Party Abbreviation'].unique()))

Merged0914['Alliance'] = Merged0914['Party Abbreviation']

#Maps party abbreviations to three alliances: UPA, NDA, and Others.
Merged0914['Alliance']=Merged0914['Alliance'].replace(to_replace=['INC','NCP', 'RJD', 'DMK', 'IUML', 'JMM','JD(s)','KC(M)','RLD','RSP','CMP(J)','KC(J)','PPI','MD'],value='UPA')
Merged0914['Alliance']=Merged0914['Alliance'].replace(to_replace=['BJP','SS', 'LJP', 'SAD', 'RLSP', 'AD','PMK','NPP','AINRC','NPF','RPI(A)','BPF','JD(U)','SDF','NDPP','MNF','RIDALOS','KMDK','IJK','PNK','JSP','GJM','MGP','GFP','GVP','AJSU','IPFT','MPP','KPP','JKPC','KC(T)','BDJS','AGP','JSS','PPA','UDP','HSPDP','PSP','JRS','KVC','PNP','SBSP','KC(N)','PDF','MDPF'],value='NDA')
Merged0914['Alliance']=Merged0914['Alliance'].replace(to_replace=['YSRCP','AAAP', 'IND', 'AIUDF', 'BLSP', 'JKPDP', 'JD(S)', 'INLD', 'CPI', 'AIMIM', 'KEC(M)','SWP', 'NPEP', 'JKN', 'AIFB', 'MUL', 'AUDF', 'BOPF', 'BVA', 'HJCBL', 'JVM','MDMK'],value='Others')

#Filters rows where the 'Position' is 1, groups the data by 'Alliance' and 'Year', and calculates the sum of 'Position' for each group.
seatsWon = Merged0914[(Merged0914.Position==1)].groupby(['Alliance','Year'])['Position'].sum().reset_index()
seatsWon = seatsWon.pivot(index='Alliance', columns='Year', values='Position').reset_index().fillna(0).sort_values([2014,2009], ascending=False).reset_index(drop = True)

#Creating Pie Charts:
colors  = ("orange", "green", "red", "cyan", "brown", "grey", "blue", "indigo", "beige", "yellow","cadetblue","khaki")
# Creating a 1x2 subplot for pie charts
plt.figure(figsize=(20,8))
plt.subplot(1,2,1)
plt.pie(seatsWon[2009], labels=seatsWon['Alliance'], colors=colors, autopct='%1.1f%%')
# Adding a white circle in the middle for aesthetics
myCircle1=plt.Circle( (0,0), 0.7, color='white')
fig = plt.gcf()
fig.suptitle("Winning Percentages by Alliances and Major Political Parties", fontsize=14) 
ax = fig.gca() 
ax.add_patch(myCircle1)

label = ax.annotate("2009", xy=(0, 0), fontsize=30, ha="center",va="center")

ax.axis('off')
ax.set_aspect('equal')
ax.autoscale_view()



plt.subplot(1,2,2)
plt.pie(seatsWon[2014], labels=seatsWon['Alliance'], colors=colors,autopct='%1.1f%%')
myCircle2=plt.Circle( (0,0), 0.7, color='white')
fig = plt.gcf() 
ax = fig.gca() 
ax.add_patch(myCircle2)

label = ax.annotate("2014", xy=(0, 0), fontsize=30, ha="center",va="center")

ax.axis('off')
ax.set_aspect('equal')
ax.autoscale_view()

plt.show();