import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Step 1, Data Import and Preprocessing
df = pd.read_csv('medical_examination.csv')

# Step 2, Add Overweight column
# Formula, BMI = weight(in kg) / (height(in m))**2
df['overweight'] = (df['weight'] / (df['height']/100)**2 > 25).astype(int)

#Step 3, Normalize cholesterol and glucose
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Step 4, Create categorical plot
def draw_cat_plot():
    # Step 5, Melt the data
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Step 6, Group and count
    df_cat = (df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total'))

    # Step 7, Draw categorical plot, import seaborn
    fig = sns.catplot(data=df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar').fig
    
    # Step 8, Return the figure
    return fig

# Step 10, Create draw_heat_map()
def draw_heat_map():
    # Step 11, Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # Step 12, Calculate correlation matrix
    corr = df_heat.corr()

    # Step 13, Generate mask for upper triangle, import numpy
    mask = np.triu(corr)

    # Step 14, Set up matplotlib figure, import matplotlib
    fig, ax = plt.subplots(figsize=(12,12))

    # Step 15, Draw Heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", center=0, square=True, linewidths=0.5, cbar_kws={"shrink": 0.5})

    # Step 16, Return fig
    return fig



cat_fig = draw_cat_plot()
cat_fig.show()

heat_fig = draw_heat_map()
heat_fig.show()

plt.show()