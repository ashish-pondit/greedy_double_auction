#import all the necessary pacakages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


buyer=pd.read_csv('buyer.csv')
seller=pd.read_csv('seller.csv')


# In[3]:


seller[seller.item==1]


# In[4]:


seller['ask']=seller.MC*10+3
seller['bid']=0
seller['bidder']=''


# In[5]:


buyer['bid']=0
buyer['seller']=''


# In[6]:
print(seller.head())

# In[11]:
check=True
temp=''
new_seller=pd.DataFrame()
#for item
for i in range(1,6):
    print('starting bid for item no :',i)
    
    print('---------------------------------------------------------------------')
    print('---------------------------------------------------------------------')
    print('---------------------------------------------------------------------')
    s=seller[seller.item==i].sort_values(by='MC').reset_index(drop=True)
    b=buyer[buyer.item==i].sort_values(by='MB').reset_index(drop=True)
    check=True
    while check:
        #for seller
        
        for j in range(0,10):
            level=0
            no_tran=0
            #for buyer
            if s.loc[j,'bidder']=='':
                print('seller ',s.loc[j,'seller'],' asking',s.loc[j,'ask'],'for item ',s.loc[j,'item'])
                check_buyer=True
                while check_buyer:
                    #print('entering buyer saturation level')
                    for k in range(0,len(b.buyer)):
                        if s.loc[j,'ask']<(b.loc[k,'MB']-1) and s.loc[j,'bid']<(b.loc[k,'MB']-1) and b.loc[k,'buyer']!=s.loc[j,'bidder']:
                            if s.loc[j,'bid']==0:
                                print(b.loc[k,'buyer'],'is bidding ',s.loc[j,'ask'],'for item ',s.loc[j,'item'])
                                s.loc[j,'bid']=s.loc[j,'ask']
                                s.loc[j,'bidder']=b.loc[k,'buyer']
                            elif s.loc[j,'bid']>0:
                                print(b.loc[k,'buyer'],'is bidding ',s.loc[j,'bid']+1,'for item ',s.loc[j,'item'])
                                s.loc[j,'bid']=s.loc[j,'bid']+1
                                s.loc[j,'bidder']=b.loc[k,'buyer']
                            else:
                                pass
                            
                        else:
                            no_tran+=1
                    #print('exiting buyer saturation level')
                    if s.loc[j,'bidder']==temp and temp!='':
                        level=level+1
                    else:
                        pass
                    temp=s.loc[j,'bidder']
                    
                    if level>=5 or no_tran>=20:
                        check_buyer=False
                    else:
                        pass
                    
                    #print('setting parameter to exit buyer level')
                
                
                b=b[b.buyer!=s.loc[j,'bidder']]
                b=b.reset_index(drop=True)
                #print('removed buyer who had successful bid ',s.loc[j,'bidder'])
                if s.loc[j,'bidder']!='':
                    
                    print('A bidding has completed')
                    print('#######################################################################')
                    print('#######################################################################')
                    print('#######################################################################')
                else:
                    print('no one bid')
                
            
            else:
                pass
            #t=s[s.bidder!='']['bidder']
            #print('all')
            #b=b[[p not in t for p in b.buyer]]
            
        #b=b[b.item==i].sort_values(by='MB').reset_index(drop=True)
        
        
        #print('buyer call complete')
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        for l in range(0,10):
            if s.loc[l,'bidder']=='':
                if s.loc[l,'ask']>(s.loc[l,'MC']+1):
                    print(s.loc[l,'seller'],'is decreasing bid by 1')
                    s.loc[l,'ask']=s.loc[l,'ask']-1
                elif s.loc[l,'ask']<=(s.loc[l,'MC']+1):
                    print('cannot decrease bid impossiable')
                    s.loc[l,'bidder']='impossiable'
                else:
                    pass
            
            
            
        check=bool(sum(s.bidder==''))    
        print('printing value of check',check)   
            
    new_seller=pd.concat([new_seller,s],ignore_index=True)        
            
# In[9]:

new_seller[new_seller.bid>0].bid.sum()/22
print('average sell price per item')

# In[10]:

print('All bidding report')
print(new_seller)






