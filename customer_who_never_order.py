import pandas as pd

data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
Customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
print(Customers)
data = [[1, 3], [2, 1]]
Orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})
print(Orders)
find_customers=Customers[~Customers['id'].isin(Orders['customerId'])]
result=find_customers[['id','name']].rename(columns={'name': 'Customers'})
print(result)
