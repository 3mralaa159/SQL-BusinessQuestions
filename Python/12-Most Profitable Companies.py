# Question
  Find the 3 most profitable companies in the entire world.
Output the result along with the corresponding company name.
Sort the result based on profits in descending order.
# link
https://platform.stratascratch.com/coding/10354-most-profitable-companies?code_type=2

# Answer
import pandas as pd

# Start writing code
forbes_global_2010_2014.head()

import pandas as pd
import numpy as np

result = forbes_global_2010_2014.groupby('company')['profits'].sum().reset_index().sort_values(by='profits',ascending=False)
result['rank'] = result['profits'].rank(method='min', ascending=False)
result.loc[result['rank'] <= 3,['company', 'profits']]

or
result[result['rank'] <= 3][['company', 'profits']]
