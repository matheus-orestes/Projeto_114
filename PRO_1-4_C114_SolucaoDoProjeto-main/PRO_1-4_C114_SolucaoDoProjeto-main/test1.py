import pandas as pd
dataframe = pd.read_excell("/content/PRO_1-1_C114_ProductDataset/updated_product_dataset.xlsx")
print(dataframe.head())
a = 33
b = "33"
if b > a:
  print("b é maior que a")
elif b == a:
  print("a e b são iguais")
 
