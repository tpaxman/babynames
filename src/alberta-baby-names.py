import pandas as pd
import seaborn as sns

# URL = 'https://open.alberta.ca/dataset/11245675-b047-49fc-8bd1-cc2ce8314a6d/resource/e8aac308-c754-484c-b446-0c57ed0e8d37/download/baby-names-frequency.xlsx'
# df = pd.read_excel(URL, )

# import all alberta babynames data
raw = pd.read_csv('alberta-babynames.csv')
raw['name'] = raw['name'].str.strip()

# select boy names only
boys = raw[raw['gender'] == 'Boy']

# add first initial to the table
boys['initial'] = boys['name'].str[0]

# select only certain names
# name_choices = 'Aaron Isaac Seth Ethan Ezra Colin Samuel Simon Cameron'
name_choices = 'Aaron Alex Alexander Archie Cameron Christopher Colin Declan Edward Edwin Ernest Isaac Jude Landen Lane Lawrence Leo Lewis Maxwell Miles Mitchell Nicholas Orson Oscar Patrick Quinn Samuel Sawyer Seth Simon Theodore Thomas Timothy Tyler'
choices = boys[boys['name'].isin(name_choices.split())]
#sns.relplot(data=choices, x='year', y='frequency', hue='name', kind='line', col='initial', col_wrap=5)
sns.relplot(data=choices, x='year', y='frequency', kind='line', col='name', col_wrap=10)

totals = boys.groupby('name')['frequency'].sum().sort_values(ascending=False)




NAME_PICKS = 'Theodore Alexander Maxwell Colin Oliver Ethan'.split()
#df = df[df['name'].isin(NAME_PICKS)]
df = df.groupby('name')['frequency'].sum()

sns.set(font_scale=2)
sns.relplot(data=df,
            hue='name',
            x='year',
            y='frequency',
            kind='line',)


boys.loc[boys.year>2015].groupby(['year', 'name'])['frequency'].sum().reset_index().pivot_table(values='frequency', index='name', columns='year', aggfunc=max, dropna=True).sort_values(2019, ascending=False)
boys.loc[(boys.year>2015) & (boys.frequency > 2)].groupby(['year', 'name'])['frequency'].sum().reset_index().pivot_table(values='frequency', index='name', columns='year', aggfunc=max, dropna=True).sort_values(2019, ascending=False)