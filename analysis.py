import pandas as pd
import matplotlib.pyplot as plt
""" Loading the dataset """

df=pd.read_csv('students.csv')

""" Calculating total scores for each student """

df["Total"]=df[["Math","Science","English"]].sum(axis=1)

""" Calculating average scores for each student """

df["Average"]=df["Total"]/3
print(df)
""" Finding the student with the highest average score """

topper=df.loc[df["Average"].idxmax()]
print(topper["Name"],topper["Average"])

""" Visualizing the average scores of all students"""

plt.bar(df["Name"],df["Average"])
plt.xlabel('Students')
plt.ylabel('Average')
plt.show()