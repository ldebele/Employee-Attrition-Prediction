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



def grid_plot_groupby(data, list_columns, values, ncols=1, nrows=1, l=10, w=5):
    """
        parameters:
            data: pd.DataFrame
            list_columns: list
            values: str
            ncols: int
            nrows: int
            l: int
            w: int
    """

    fig, ax = plt.subplots(figsize=(l, w), ncols=ncols, nrows=nrows)
    ax = ax.flatten()

    for i, col in enumerate(list_columns):
        data.groupby([col, values]).size().unstack().plot(kind="bar", stacked=True, ax=ax[i])




def read_info_column():
    
    employee_info = {} 

    # read text from the file
    with open('./data/raw/column_info.txt', 'r') as f:
        lines = f.readlines() 


    for line in lines:
        info = line.strip().split(" |")
        keys = str(info[1]).strip()
        values = (info[2]).strip()

        employee_info[keys] = values

    return employee_info
    