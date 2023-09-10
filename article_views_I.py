import pandas as pd
data = [[1, 3, 5, '2019-08-01'], [1, 3, 6, '2019-08-02'], [2, 7, 7, '2019-08-01'], [2, 7, 6, '2019-08-02'], [4, 7, 1, '2019-07-22'], [3, 4, 4, '2019-07-21'], [3, 4, 4, '2019-07-21']]
Views = pd.DataFrame(data, columns=['article_id', 'author_id', 'viewer_id', 'view_date']).astype({'article_id':'Int64', 'author_id':'Int64', 'viewer_id':'Int64', 'view_date':'datetime64[ns]'})
Find_views=Views[Views['author_id']==Views['viewer_id']]
result=Find_views['author_id'].unique()
sorted_result=sorted(result)
sorted_df = pd.DataFrame(sorted_result,columns=['id'])
print(sorted_df)

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    artical_views=views[views['author_id']==views['viewer_id']]
    ids=artical_views['author_id'].unique()
    sorted_list=sorted(ids)
    Final_sorted_list=pd.DataFrame(sorted_list,columns=['id'])
    print(Final_sorted_list)
