
#%%
import pandas as pd
import os


#%%
file = 'Resources/Tables/23173_table.csv'


#%%
census_df = pd.read_csv(file, encoding='ISO-8859-1')
census_df.head()


#%%
drop_col = census_df.drop(['Unnamed: 1', 'Unnamed: 3', 'Unnamed: 4'], axis=1)
drop_col.head()


#%%
dropna = drop_col.dropna(how='any')
dropna.head()


#%%
dropna.index.name = '23220'


#%%
dropna.head()


#%%
df = dropna.rename(columns={"Subject": "Subject", "ZCTA5 23173": "Estimate", 'Unnamed: 5': 'Margin of Error',                            'Unnamed: 6': 'Percent', 'Unnamed: 7': 'Percent Margin of Error'})
df.head()


#%%
test_file = 'Resources/Tables/23224_table.csv'
df = pd.read_csv(test_file, encoding='ISO-8859-1')
df.head()


#%%
def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles


#%%
dirName = 'Resources/Tables'
listoffiles= getListOfFiles(dirName)
listoffiles


#%%
Richmond_zipcodes = ['23173', '23219', '23220', '23221', '23222', '23223',                      '23224', '23225', '23226', '23227', '23228', '23229', '23230', '23231', '23233','23234', '23235',                     '23236', '23238', '23294']
table_dfs =[]
for zipcode in Richmond_zipcodes:
    df_name = zipcode
    table_dfs.append(df_name)
    
table_dfs    


#%%

list_of_dfs = []
for df, file in zip(table_dfs, listoffiles):
    df = pd.read_csv(file)
    list_of_dfs.append(df)
list_of_dfs[2].head()


#%%
clean_dfs = []
count = 0
for df in list_of_dfs:
    drop_col = df.drop(['Unnamed: 1', 'Unnamed: 3', 'Unnamed: 4'], axis=1)
    if 'Unnamed: 8' in drop_col:
        print(f'found col 8 in df')
        drop_col = drop_col.drop(columns=['Unnamed: 8'])
    df_rename_col = drop_col.rename(columns={"Subject": "Subject", (f"ZCTA5 {Richmond_zipcodes[count]}"): "Estimate", 'Unnamed: 5': 'Margin of Error',                                              'Unnamed: 6': 'Percent', 'Unnamed: 7': 'Percent Margin of Error'})
    df_dropna = df_rename_col.dropna(how='any')
    count = count + 1
    clean_dfs.append(df_dropna)
    
    
    
    


#%%
df_rename_col.head()


#%%
clean_dfs[0].head()


#%%
clean_dfs[0].to_html('test.html')


#%%
df_rename_col.to_html('test1.html')


#%%



