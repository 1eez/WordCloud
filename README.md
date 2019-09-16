# WordCloud
用python进行文本分词并生成词云

## 需要安装的包
* `sudo pip3 install jieba`
* `sudo pip3 install wordcloud`
* wordcloud包依赖于Pillow，numpy，matplotlib 

## 特别说明
* 分词采用结巴分词，并支持自定义词库
* 根据中文无关词词库，自动生成两种词云
* chineseStopWords 是自定义的无关词库，网上下的版本在zip包里，但是太多了，删掉一些可能表示态度的词语

## 使用方法
1. 把需要生成词云的文档另存为txt纯文本，保存在/doc 文件夹下。
2. 修改1_main_function.py 中“中华人民共和国道路交通安全法.txt” 改成你要分析的文件
2. 运行1_main_function.py 程序
3. 查看输出结果包括：

*    99.统计结果_词频.txt （不是很有用）

*    99.统计结果_词云_包含无关词.png

*    99.统计结果_词云_去除无关词.png

## 文件结构说明
---/doc             放置需要分析的文件，记得另存为txt

---/font            字体文件（微软雅黑，以防中文无法显示，如需修改字体可修改这段代码

---/images          需要遮罩的图片文件，可以修改该文件修改词云图的形状

---/userdict        用户自定义字典文件，包括userdict需要包含的词，chineseStopWord需要剔除的词

0.代码手记.md         作者自己写代码时的随笔记录文件

1_main_function.py  代码主文件

99.XXXXXXX          代码生成的结果文件

README.md           本文件


## 示例图
![avatar](https://github.com/1eez/WordCloud/blob/master/99.%E7%BB%9F%E8%AE%A1%E7%BB%93%E6%9E%9C_%E8%AF%8D%E4%BA%91_%E5%8C%85%E5%90%AB%E6%97%A0%E5%85%B3%E8%AF%8D.png)

![avatar](https://github.com/1eez/WordCloud/blob/master/99.%E7%BB%9F%E8%AE%A1%E7%BB%93%E6%9E%9C_%E8%AF%8D%E4%BA%91_%E5%8E%BB%E9%99%A4%E6%97%A0%E5%85%B3%E8%AF%8D.png)

