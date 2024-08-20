# for site 

import pandas as pd
import plotly.express as px

# Read the Excel file
df = pd.read_excel('D:/M/7877/4.xlsx', sheet_name='Лист3')

# Extract data
country_names = df.iloc[2:234, 1].tolist()  # Country Names from B3 to B234
religious_backgrounds = df.iloc[2:234, 2].tolist()  # Religious Backgrounds from C3 to C234
values = df.iloc[7:239, 12].astype(float).tolist()  # Values from M8 to M239

# Ensure all lists have the same length by truncating to the smallest size
min_length = min(len(country_names), len(religious_backgrounds), len(values))
country_names = country_names[:min_length]
religious_backgrounds = religious_backgrounds[:min_length]
values = values[:min_length]

# Create a DataFrame with the cleaned data
data = {
    'Country': country_names,
    'Religious Background': religious_backgrounds,
    'Reincarnation Belief Survey': values
}
df_cleaned = pd.DataFrame(data)

# Create the scatter plot
fig = px.scatter(df_cleaned, x='Country', y='Reincarnation Belief Survey', color='Religious Background',
                 hover_data=['Country', 'Religious Background', 'Reincarnation Belief Survey'])

# Customize the layout
fig.update_layout(
    title='Relationship Between Country Names, Religious Backgrounds, and Reincarnation Belief Survey',
    xaxis_title='Country',
    yaxis_title='Reincarnation Belief Survey',
    xaxis_tickangle=-45,
    legend_title='Religious Background',
    height=600,
    width=1200,
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
    annotations=[
        dict(
            x=1,
            y=-0.15,
            showarrow=False,
            text="Created and Analyzed by Homam Al Safadi",
            xref="paper",
            yref="paper",
            xanchor='right',
            yanchor='top',
            font=dict(size=12, color='gray', family='Arial')
        )
    ]
)

# Save the plot as an HTML file
fig.write_html('D:/M/7877/relationship_plot.html')

# Display the plot in the notebook (if you're using a Jupyter Notebook)
fig.show()
