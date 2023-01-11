import matplotlib.pyplot as plt

def hist_visualize(iris_df):
    plt.hist(iris_df['species'])
    plt.xticks(iris_df['species'])
    plt.xlabel("species", fontsize=12)
    plt.ylabel("hist", fontsize=12)
    plt.show()