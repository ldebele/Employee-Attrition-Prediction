import matplotlib.pyplot as plt



def plot_groupby(data, index, values):
    """
        parameters:
            data: pd.DataFrame
            index: str
            values: str
    """

    fig, ax = plt.subplots(figsize=(8, 4))

    # groupby and plot
    data.groupby([index, values]).size().unstack().plot(kind='bar', stacked=True, ax=ax)
