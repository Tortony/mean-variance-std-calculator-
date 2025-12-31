import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# CSV থেকে ডেটা লোড
df = pd.read_csv('medical_examination.csv')

# 1. BMI এবং overweight কলাম
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 2. Normalize করো: 0 = good, 1 = bad
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

def draw_cat_plot():
    # 3. Cat plot এর জন্য DataFrame
    df_cat = pd.melt(df, id_vars=['cardio'], 
                     value_vars=['cholesterol', 'gluc', 'smoke', 
                                 'alco', 'active', 'overweight'])
    
    # 4. Group এবং reformat
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index()
    df_cat = df_cat.rename(columns={0: 'total'})
    
    # 5. Cat plot তৈরি
    g = sns.catplot(x='variable', y='total', hue='value', 
                    col='cardio', data=df_cat, kind='bar')
    fig = g.fig
    return fig

def draw_heat_map():

    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    
    # 7. Correlation matrix
    corr = df_heat.corr()
    
    # 8. Mask for upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # 9. Set up matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # 10. Heatmap plot
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', 
                center=0, square=True, linewidths=0.5, 
                cbar_kws={'shrink': 0.5})
    
    return fig
