import altair as alt
import pandas as pd

alberta = pd.read_csv('alberta/alberta-babynames-percents.csv').assign(region='alberta')
usa = pd.read_csv('usa/usa-babynames.csv').assign(region='usa')
df = pd.concat((alberta,usa)).drop('number_total', axis=1)

chosen = ('Ezra Spencer Ewan Ethan Noah Oliver Liam Aaron Alex Alexander Archie Cameron Ian Colin Declan Edward ' +
          'Isaac Lawrence Leo Lewis Miles Nicholas Quinn Samuel Sawyer Seth Thomas Timothy')
data = df[df.babyname.isin(chosen.split()) & df.sex.isin(['Male'])]
alt.Chart(data).mark_line().encode(x='year',
                                   y='fraction',
                                   facet=alt.Facet('babyname', columns=8),
                                   color='region').save('a.html')
