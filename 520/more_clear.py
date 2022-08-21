# -*- coding:UTF-8 -*-
# auther:drliu
# date:2022/5/19
# aim: 

from wordcloud import WordCloud
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# 获取文本对象
f = open('wd.txt', 'r')

# 读取文本内容
txt = f.read()

# 创建背景图片
back_groud = np.array(Image.open('back.jpg'))

# 设置停用词
stopwords = set(STOPWORDS)
stopwords.add("new")

# 创建词云对象(增加mask背景参数，stopwords停用词，max_font_size最大字体)
wd = WordCloud(background_color='white', width=1000, height=500, margin=0, mask=back_groud, stopwords=stopwords,
               max_font_size=100, scale=20)

# 使用词云对文本进行分词和词云的生成
wd_cut = wd.generate(txt)

# 获取背景颜色
img_color = ImageColorGenerator(back_groud)

# 修改字体颜色为背景色
wd_cut.recolor(color_func=img_color)

# plt生成词云图片
plt.imshow(wd_cut, interpolation="bilinear")

# 关闭坐标轴
plt.axis("off")

# 交互式展示词云图
plt.show()

# 保存词云图片
wd_cut.to_file('wd.jpg')


if __name__ == '__main__':
    main()
