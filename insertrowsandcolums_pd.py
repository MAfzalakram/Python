import pandas as pd
# Creating a dictionary with Names and CGPA as Columns
table = {"Names":["Ali", "Ahmad", "Aslam"], "CGPA": [2.67, 3.92,4.0]}
df = pd.DataFrame(table)

#Creating a new row to insert at the end of dataframe
new_row = {"Names": "Aslam", "CGPA": [3.33]}
new_df_row = pd.DataFrame(new_row)
df =pd.concat([df,new_df_row],ignore_index = True)

#Creating third column as Fee and merge with dataframe
new_column = {"Fee" : [1000,3000,5000,6000]}
new_df_column = pd.DataFrame(new_column)

df["Fee"] = new_df_column
sum = df["Fee"].cumprod()
print(sum)
