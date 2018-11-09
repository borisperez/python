df_titanic["Class"] = ''

def classDescription(x):
    if x  == 1:
        return  'Upper'
    elif x  == 2:
        return 'Middle'      
    elif x  == 3:
        return  'Lower'
    else:
        return 'Not Identified'

df_titanic['Class'] = df_titanic.apply(lambda row: classDescription(row['Pclass']), axis=1)


df_titanic.head()
    
