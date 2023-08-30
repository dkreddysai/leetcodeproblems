import pandas as pd
data = [['0', 'Y', 'N'], ['1', 'Y', 'Y'], ['2', 'N', 'Y'], ['3', 'Y', 'Y'], ['4', 'N', 'N']]
Products = pd.DataFrame(data, columns=['product_id', 'low_fats', 'recyclable']).astype({'product_id':'int64', 'low_fats':'category', 'recyclable':'category'})
print(Products)
find_products = Products[(Products['low_fats'] == 'Y') & (Products['recyclable'] == 'Y')]
result= find_products[['product_id']]

print("Output:")
print(result)