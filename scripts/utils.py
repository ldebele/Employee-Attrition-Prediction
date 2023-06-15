import matplotlib.pyplot as plt



def group_by(data, index, values):
    """
        parameters - 
            data: DataFrame
            index: str
            values: str
    """

    fig, ax = plt.subplots(figsize=(8, 4))

    # groupby and plot
    data.groupby([index, values]).size().unstack().plot(kind='bar', stacked=True, ax=ax)
