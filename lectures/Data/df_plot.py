import matplotlib.pyplot as plt
import pandas as pd
def df_plot(df,ax=None,label=None):
    if ax is None:
        fig,ax=plt.subplots()
    if isinstance(df,pd.Series):
        if label is None:
            try:
                label=df.name
            except:
                label=''
        ax.plot(df.index.values,df.values,label=label)
    elif isinstance(df,pd.DataFrame):
        for i,col in enumerate(df.columns):
            if label is None:
                try:
                    label='%s'%col
                except:
                    label=i
            ax.plot(df.index.values,df.loc[:,col].values,label=label)
    else:
        print('df is not a dataframe')
    ax.legend()
    return ax