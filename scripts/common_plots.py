import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib import font_manager


font_dirs = ['../font/']
font_files = font_manager.findSystemFonts(fontpaths=font_dirs)

for font_file in font_files:
    font_manager.fontManager.addfont(font_file)

plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def scatter_line_plot(tbl, scatter_x_col, scatter_y_col, line_x_col, line_y_col, x_label_name, scatter_y_label_name,
                      line_y_label_name, output_png_name):
    """
    绘制散点图叠加折线图
    :param tbl: 数据源dataframe格式
    :param scatter_x_col: 散点图x轴字段
    :param scatter_y_col: 散点图y轴字段
    :param line_x_col: 折线图x轴字段
    :param line_y_col: 折线图y轴字段
    :param x_label_name: x轴展示名称
    :param scatter_y_label_name: 散点图y轴展示名称
    :param line_y_label_name: 折线图y轴展示名称
    :param output_png_name: 输出文件名
    """
    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax1.set_xlabel(x_label_name, fontsize=16)
    ax1.set_ylabel(scatter_y_label_name, fontsize=16, color='tab:green')
    ax1 = sns.scatterplot(data=tbl, x=scatter_x_col, y=scatter_y_col)
    ax1.tick_params(axis='y')

    ax2 = ax1.twinx()
    ax2.set_ylabel(line_y_label_name, fontsize=16, color='tab:green')
    ax2 = sns.lineplot(data=tbl, x=line_x_col, y=line_y_col, color='tab:red', estimator=None)
    ax1.tick_params(axis='y')

    plt.savefig('data/output/{}.png'.format(output_png_name))


if __name__ == '__main__':
    iris = pd.read_csv('../data/raw/iris.csv')
    scatter_line_plot(tbl=iris, scatter_x_col='Petal.Length', scatter_y_col='Petal.Width',
                      line_x_col='Sepal.Length', line_y_col='Sepal.Width',
                      x_label_name='x轴名称', scatter_y_label_name='散点图y轴名称', line_y_label_name='折线图y轴名称',
                      output_png_name='输出图片名')
