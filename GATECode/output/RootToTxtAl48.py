#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install uproot


# In[7]:


import uproot 
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt


# In[8]:


def HE(name0,name1):
    File = uproot.open(name0+"_"+name1+"keV.root")
    DatosEnergia = np.array(File["Singles"]["energy"].array())
    Index, Frecuencia = np.unique(DatosEnergia, return_counts=True)
    return Index, Frecuencia


# In[9]:


def main(name0,name1,NPixeles,TPixel):
#    EnergiaI=HE(name0,str(name1))[0]
#    EnergiaF=HE(name0,str(name1))[1]
#    d_E=np.column_stack((EnergiaI, EnergiaF))
#    print("Energy frequency created"+str(name1))
    File = uproot.open(name0+"_"+str(name1)+"keV.root")
    print("Upload"+str(name1))
    Pixeles=File["Singles"]["pixelID"].array()
#    PosiX=File["Singles"]["globalPosX"].array()
#    PosiY=File["Singles"]["globalPosY"].array()
    x_vals, y_vals = np.unravel_index(Pixeles, [NPixeles, NPixeles])
#    print("PosX and PosY created")
#    PosiXM=[int(round(((Ps/TPixel)+NPixeles/2),0)) for Ps in PosiX]
#    PosiYM=[int(round(((Ps/TPixel)+NPixeles/2),0)) for Ps in PosiY]
    print("Pixeles created"+str(name1))
#    Im = np.zeros((NPixeles+1,NPixeles+1))
#    for i in range (len(PosiX)):
#            Im[PosiXM[i],PosiYM[i]] += 1
    Im = np.zeros((NPixeles,NPixeles))
    for i in range (len(y_vals)):
            Im[x_vals[i],y_vals[i]] += 1
    print("Imagen created"+str(name1))
#    np.savetxt(name0+"_"+str(name1)+"_"+"_FrequencyE.txt", d_E)
    np.savetxt(name0+"_"+str(name1)+"_"+"_ImE.txt", Im)


# In[10]:


NPixeles=61
TPixel=0.055
nameS="Al48Ph2"
namePh=5
nameE1=10
nameE2=20
nameE3=21
nameE4=28
nameE5=38
nameE6=47
Step1=2
Step2=1
Step3=3
E1=np.arange(nameE1,nameE2+1,Step1)
E2=np.arange(nameE3,nameE4+1,Step2)
E3=np.arange(nameE5,nameE6+1,Step3)
E=np.concatenate((E1,E2,E3))


# In[6]:


for i in range(len(E)):
    Code=main(nameS,E[i],NPixeles,TPixel)


# In[ ]:




