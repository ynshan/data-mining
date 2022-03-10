import matplotlib.pyplot as plt
# Mac电脑中文乱码问题
plt.rcParams["font.sans-serif"] = ['Arial Unicode MS']
# plt.rcParams["axes.unicode_minus"] = False --处理坐标轴负刻度值的情况
"""
--label参数要与plt.legend(loc)配合才可以显示
--plt.xlim(xmin,xmax)x轴的数值范围，同理有plt.ylim(ymin,ymax)
--plt.grid(ls,color)绘制刻度线的网格线
--plt.axhline(y=0.0,c,ls,lw)绘制平行于x轴的直线，plt.axvline()平行于y轴
--plt.axhspan(ymin,ymax,facecolor,alpha)绘制平行于x轴的参考区域，plt.axvspan绘制平行于y轴的参考区域
--plt.annotate(string,xy,xytext,weight,color,arrowprops)添加图形内容细节的指向型注释文本
--plt.text(x,y,string,weight,color)添加图形内容细节的无指向型注释文本
--plt.xlabel(string)设置x轴的标签文本，plt.ylabel()y轴的标签文本
--plt.title(string)添加图形的标题

--plt.scatter(x,y,s,c,cmap,marker)散点图
--plt.bar(x,y,align,color,tick_label,label,hatch)柱状图，垂直于x轴
--plt.barh(x,y,align,color,tick_label,label,hatch)条形图，垂直于y轴
--plt.hist(x,bins,color,histtype,rwidth,alpha)直方图
--plt.pie(x,labels,autopct,startangle,colors)饼图
--plt.stem(x,y,linefmt,markerfmt,basefmt)绘制棉棒图
--plt.boxplot(x)箱线图
--plt.errorbar(x,y,yerr,xerr)
"""


# 折线图
def plot(x_arrays,  # x轴
         y_arrays,  # y轴
         legend,  # 图例名称
         path,  # 图片保存路径
         figure_size=(10, 8),  # 画布大小
         line_width=0.30,  # 折线图的宽度
         title='折线图',  # 柱状图的名称
         colors=None,
         x_label='',  # x轴的名称
         y_label='',  # y轴的名称
         ):
    # 设置画布大小
    plt.figure(figsize=figure_size)
    # 标题
    plt.title(title)
    plots = []
    length = len(y_arrays)
    for i in range(length):
        # 数据
        fig = plt.plot(x_arrays[i], y_arrays[i], color=colors[i], label=legend[i], lw=line_width)
        plots.append(fig)
        # 设置数字标签
        for a, b in zip(x_arrays[i], y_arrays[i]):
            plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

    # 横坐标描述
    plt.xlabel(x_label)
    # 纵坐标描述
    plt.ylabel(y_label)
    plt.legend()
    plt.savefig(path, dpi=300)
    # plt.show()

    return plt


# 并列柱状图
def bar(x_array,  # x轴
        y_arrays,  # y轴
        legend,  # 图例名称
        path,  # 图片保存路径
        figure_size=(10, 8),  # 画布大小
        bar_width=0.30,  # 柱状图的宽度
        title='柱状图',  # 柱状图的名称
        x_ticks=None,  # x轴刻度的名称
        x_label='',  # x轴的名称
        y_label=''  # y轴的名称
        ):
    # 设置画布大小
    plt.figure(figsize=figure_size)
    # 标题
    plt.title(title)
    bars = []
    length = len(y_arrays)
    for i in range(length):
        # 数据
        fig = plt.bar(x_array+(i-1)*bar_width, y_arrays[i], label=legend[i], width=bar_width, align="center", alpha=0.7)
        bars.append(fig)
        # 设置数字标签
        for a, b in zip(x_array, y_arrays[i]):
            plt.text(a+(i-1)*bar_width, b, b, ha='center', va='bottom', fontsize=10)

    # 横坐标描述
    plt.xlabel(x_label)
    # 纵坐标描述
    plt.ylabel(y_label)
    plt.xticks(x_array-bar_width/length, x_ticks)
    plt.legend()
    plt.savefig(path, dpi=300)
    plt.show()


# 堆积图
def stack_bar(x_array,  # x轴
              y_arrays,  # y轴
              legend,  # 图例名称
              path,  # 图片保存路径
              figure_size=(10, 8),  # 画布大小
              bar_width=0.30,  # 柱状图的宽度
              title='柱状图',  # 柱状图的名称
              x_ticks=None,  # x轴刻度的名称
              x_label='',  # x轴的名称
              y_label=''  # y轴的名称
              ):
    # 设置画布大小
    plt.figure(figsize=figure_size)
    # 标题
    plt.title(title)
    length = len(y_arrays)
    for i in range(length):
        if i == 0:
            plt.bar(x_array, y_arrays[i], label=legend[i], width=bar_width, align="center", alpha=0.7)
        else:
            plt.bar(x_array, y_arrays[i], bottom=y_arrays[i-1], label=legend[i], width=bar_width, align="center", alpha=0.7)
        # 设置数字标签
        for a, b in zip(x_array, y_arrays[i]):
            plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

    # 横坐标描述
    plt.xlabel(x_label)
    # 纵坐标描述
    plt.ylabel(y_label)
    plt.xticks(x_array-bar_width/length, x_ticks)
    plt.legend()
    plt.savefig(path, dpi=300)
    plt.show()


# 折线图


# 堆叠图


# 并列条形图


