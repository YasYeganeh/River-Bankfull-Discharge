import pandas as pd

Df=pd.read_excel('هیدرومتری_دبی_روزانه_حوضه ای_26.xlsx')
# print(len(Df))

years=list(range(53,96+1,1))
# print(years)
df_aliabad=Df[(Df['code']=='24-003') & (Df['abi'].isin(years))]
# df_aliabad.to_excel('aliabad.xlsx')
print(len(df_aliabad))
# print(Df['abi'].isin([83]))
df_vaselabad=Df[(Df['code']=='24-005') & (Df['abi'].isin(years))]
# df_vaselabad.to_excel('vaselabad.xlsx')
print(len(df_vaselabad))
df_sarvu=Df[(Df['code']=='24-013') & (Df['abi'].isin(years))]
# df_sarvu.to_excel('sarvu.xlsx')
print(len(df_sarvu))
df_berak=Df[(Df['code']=='24-017') & (Df['abi'].isin(years))]
# df_berak.to_excel('berak.xlsx')
print(len(df_berak))
df_babaarab=Df[(Df['code']=='24-043') & (Df['abi'].isin(years))]
# df_babaarab.to_excel('babaarab.xlsx')
print(len(df_babaarab))
df_hakan=Df[(Df['code']=='24-061') & (Df['abi'].isin(years))]
# df_hakan.to_excel('hakan.xlsx')
print(len(df_hakan))