# coding:utf-8

#=============================================
#
#     根据doc目录下的txt文件，生成大数据词云
#
# @作者： lordli
# @日期： 2019-09-05
# @更新： 1. 分为分词，生成词云两个步骤
#        2. 生成两张词云，一张包含无关词，一张不包含
#
#=============================================

from os import path
from collections import Counter
import jieba
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)

jieba.load_userdict(path.join(d,'userdict/userdict.txt'))  # 导入用户自定义词典，这里的词是要整合一起的

# 加载stopwords无关词库，这里的词不显示在词云里
def load_stopwords():
    filepath = path.join(d,'userdict/chineseStopWords.txt')
    stopwords = [line.strip() for line in open(filepath,encoding='utf-8').readlines()]
    return stopwords

# 分词并且返回结果
def word_segment(text):

    # 计算每个词出现的频率，并存入txt文件
    jieba_word=jieba.cut(text,cut_all=False) # cut_all是分词模式，True是全模式，False是精准模式，默认False
    data=[]
    for word in jieba_word:
        data.append(word)
    dataDict=Counter(data)
    with open(path.join(d,'99.统计结果_词频.txt'),'w') as fw:
        for k,v in dataDict.items():
            fw.write("%s,%d\n" % (k,v))

    # 返回分词后的结果
    jieba_word=jieba.cut(text,cut_all=False) # 这行代码为啥又写一遍？？没看懂，删掉会报错
    seg_list=' '.join(jieba_word)
    return seg_list

#根据分词统计结果，生成词云
def generate_wordcloud(text):

    # 设置显示方式
    sharp_mask = np.array(Image.open(path.join(d, "images/circle_mask.png")))
    font_path=path.join(d,"font/msyh.ttf")

    stopwords = set(load_stopwords())

    # 把wordCloud官方的英文的无关词列表添加进无关词数组中
    for word in STOPWORDS:
        stopwords.add(word)

    # 再添加一些自定义的不需要的词
    stopwords.add('DLTE')

    print('生成词云需要一些时间，请耐心等候…')

    wc = WordCloud(background_color="white",# 设置背景颜色
           max_words=2000, # 词云显示的最大词数
           mask=sharp_mask,# 设置背景图片
           stopwords=stopwords, # 设置停用词
           font_path=font_path, # 兼容中文字体，不然中文会显示乱码
           )
    # 生成词云
    wc.generate(text)
    # 生成的词云图像保存到本地
    wc.to_file(path.join(d, "99.统计结果_词云_去除无关词.png"))

    wc = WordCloud(background_color="white",
           max_words=2000,
           mask=sharp_mask,
           font_path=font_path,
           )
    wc.generate(text)
    # 生成的词云图像保存到本地
    wc.to_file(path.join(d, "99.统计结果_词云_包含无关词.png"))

    # 显示图像
    plt.imshow(wc, interpolation='bilinear')
    # interpolation='bilinear' 表示插值方法为双线性插值
    plt.axis("off")# 关掉图像的坐标
    plt.show()

if __name__ == '__main__':
    # 读取文件
    text = open(path.join(d, 'doc/中华人民共和国道路交通安全法.txt')).read()

    # 分词
    text = word_segment(text)

    # 生成词云
    generate_wordcloud(text)
