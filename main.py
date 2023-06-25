import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
from scripts.common_plots import scatter_line_plot

font_dirs = ['font/']
font_files = font_manager.findSystemFonts(fontpaths=font_dirs)

for font_file in font_files:
    font_manager.fontManager.addfont(font_file)

plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus']=False  # 用来正常显示负号

if __name__ == '__main__':
    # 绘制散点图
    iris = pd.read_csv('data/raw/iris.csv')
    scatter_line_plot(tbl=iris, scatter_x_col='Petal.Length', scatter_y_col='Petal.Width', \
                      line_x_col='Sepal.Length', line_y_col='Sepal.Width', \
                      x_label_name='x轴名称', scatter_y_label_name='散点图y轴名称', line_y_label_name='折线图y轴名称')
    plt.show()