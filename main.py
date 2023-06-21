
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



sns.set_theme(style="darkgrid")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False

    iris = pd.read_csv('data/raw/iris.csv')
    print(iris.columns)
    # sns.relplot(data=iris, x="Sepal.Length", y="Sepal.Width", kind='line', estimator=None, col='Species')
    # plt.show()

    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax1.set_xlabel('Length', fontsize=16)
    ax1.set_ylabel('主图y轴指标名称', fontsize=16, color='tab:green')
    ax1 = sns.scatterplot(data=iris, x='Petal.Length', y='Petal.Width')
    ax1.tick_params(axis='y')

    ax2 = ax1.twinx()
    ax2.set_ylabel('副图y轴指标名称', fontsize=16, color='tab:green')
    ax2 = sns.lineplot(data=iris, x='Sepal.Length', y='Sepal.Width', color='tab:red', estimator=None)
    ax1.tick_params(axis='y')

    plt.show()