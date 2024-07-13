name_df = dataset['Name'].value_counts(dropna=False).reset_index()
name_df

name_df.iloc[0:5]

plt.barh(name_df.iloc[0:5]['Name'], name_df.iloc[0:5]['count'], color='skyblue')
plt.title('Top 5 most frequent names')
plt.xlabel('Count')
plt.ylabel('Name')
