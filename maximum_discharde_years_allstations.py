import pandas as pd

df=pd.read_excel('Sarvu_serizamani.xlsx')
df1=pd.read_excel('Berak_serizamani.xlsx')
df2=pd.read_excel('Aliabad_serizamani.xlsx')
df3=pd.read_excel('Hakan_serizamani.xlsx')
df4=pd.read_excel('Babaarab_serizamani.xlsx')
df5=pd.read_excel('Vaselabad_serizamani.xlsx')
# print(df)
###################################
# ISTGAH SARVUU
years=[54,55,56,57,58,59,60,61,62,63,64,88,89,90,91,92,93,94,95,96]
print('Sarvuu years:',years)
max_dict_sarvuu={}
for year in years:
    Discharge=list(df[df['abi']==year]['discharge'])
    # print(Discharge)
    max_year=max(Discharge)
    # print(max_year)
    max_dict_sarvuu[year]=max_year
print('sarvu max:',max_dict_sarvuu)
# DF = pd.DataFrame(data=max_dict_sarvuu, index=[0])
# DF= (DF.T)
# DF.to_excel ('SARVU_BANKFULLDISCHARGE.xlsx', sheet_name = 'Sheet1')
####################################
# ISTGAH BERAK
YEARS1=list(set(list(df1['abi'])))
print('berak years:',YEARS1)
max_dict_BERAK={}
for year in YEARS1:
    Discharge=list(df1[df1['abi']==year]['discharge'])
    # print(Discharge)
    max_year=max(Discharge)
    # print(max_year)
    max_dict_BERAK[year]=max_year
print('berak max:',max_dict_BERAK)
# DF1 = pd.DataFrame(data=max_dict_BERAK, index=[0])
# DF1= (DF1.T)
# DF1.to_excel ('BERAK_BANKFULLDISCHARGE.xlsx', sheet_name = 'Sheet1')
####################################
# ISTGAH ALIABAD
YEARS2=list(set(list(df2['abi'])))
print('aliabad years:',YEARS2)
print(len(YEARS2))
max_dict_ALIABAD={}
for year in YEARS2:
    Discharge=list(df2[df2['abi']==year]['discharge'])
    # print(Discharge)
    max_year=max(Discharge)
    # print(max_year)
    max_dict_ALIABAD[year]=max_year
print('aliabad max:',max_dict_ALIABAD)
# DF2 = pd.DataFrame(data=max_dict_ALIABAD, index=[0])
# DF2= (DF2.T)
# DF2.to_excel ('ALIABAD_BANKFULLDISCHARGE.xlsx', sheet_name = 'Sheet1')
####################################
# ISTGAH HAKAN
YEARS3=list(set(list(df3['abi'])))
print('hakan years:',YEARS3)
max_dict_HAKAN={}
for year in YEARS3:
    Discharge=list(df3[df3['abi']==year]['discharge'])
    # print(Discharge)
    max_year=max(Discharge)
    # print(max_year)
    max_dict_HAKAN[year]=max_year
print('hakan max:',max_dict_HAKAN)
# DF3 = pd.DataFrame(data=max_dict_HAKAN, index=[0])
# DF3= (DF3.T)
# DF3.to_excel ('HAKAN_BANKFULLDISCHARGE.xlsx', sheet_name = 'Sheet1')
####################################
# ISTGAH BABAARAB
YEARS4=list(set(list(df4['abi'])))
print('babaarab years:',YEARS4)
max_dict_BABAARAB={}
for year in YEARS4:
    Discharge=list(df4[df4['abi']==year]['discharge'])
    # print(Discharge)
    max_year=max(Discharge)
    # print(max_year)
    max_dict_BABAARAB[year]=max_year
print('babaarab max:',max_dict_BERAK)
# DF4 = pd.DataFrame(data=max_dict_BABAARAB, index=[0])
# DF4= (DF4.T)
# DF4.to_excel ('BABAARAB_BANKFULLDISCHARGE.xlsx', sheet_name = 'Sheet1')
####################################
# ISTGAH VASELABAD
YEARS5=list(set(list(df5['abi'])))
print('vaselabad years:',YEARS5)
max_dict_VASELABAD={}
for year in YEARS5:
    Discharge=list(df5[df5['abi']==year]['discharge'])
    # print(Discharge)
    max_year=max(Discharge)
    # print(max_year)
    max_dict_VASELABAD[year]=max_year
print('vaselabad max:',max_dict_VASELABAD)
# DF5 = pd.DataFrame(data=max_dict_VASELABAD, index=[0])
# DF5= (DF5.T)
# DF5.to_excel ('VASELABAD_BANKFULLDISCHARGE.xlsx', sheet_name = 'Sheet1')
##########################################################
