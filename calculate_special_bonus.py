import pandas as pd
data = [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]]
employees = pd.DataFrame(data, columns=['employee_id', 'name', 'salary']).astype({'employee_id':'int64', 'name':'object', 'salary':'int64'})
employees['bonus'] = employees.apply(lambda row: row['salary'] if (row['employee_id'] % 2 == 1 and row['name'][0] != 'M') else 0, axis=1)
result = employees[['employee_id', 'bonus']].sort_values(by='employee_id')

# Display the result
print(result)