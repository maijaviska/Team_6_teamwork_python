df_pie = dataset['Gender'].value_counts(dropna=False).reset_index()
df_pie

plt.pie(df_pie['count'], labels = df_pie['Gender'], autopct='%1.1f%%')
plt.title('Transactions per gender')
plt.show()