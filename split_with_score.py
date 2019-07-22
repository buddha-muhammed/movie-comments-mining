
# coding: utf-8

# In[4]:


import pandas as pd

comments = []
score= []
with open('all_comments.txt', 'r', encoding='utf-8') as f:
    for k in f:
        info = k.split(',')
        if len(info) == 6:
            comments.append([info[3],info[4]])
        

raw = pd.DataFrame(comments,columns = ['comments','score'])

#取出异常数据（本数据集有score处异常的数据）
count = 0
abnor = []
for k in raw.score:
    try:
        float(k)
    except:
        abnor.append(count)
    count = count + 1

raw_2 = raw.drop(abnor)

neg = raw_2[raw_2['score'].apply(lambda x:float(x) <3)]

neg.comments.to_csv('comments_sets/复仇者联盟4_差评.txt',index = False)

mid = raw_2[raw_2['score'].apply(lambda x:float(x) >= 3 and float(x) < 4)]

mid.comments.to_csv('comments_sets/复仇者联盟4_中评.txt',index = False)

pos = raw_2[raw_2['score'].apply(lambda x:float(x) > 4)]

pos.comments.to_csv('comments_sets/复仇者联盟4_好评.txt',index = False)

