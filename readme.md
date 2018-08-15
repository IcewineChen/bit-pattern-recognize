# 北京理工大学模式识别代码

## content
这个repo是北理工研究生模式识别课程的大作业代码=-=
整个project包含了图像高低通滤波，曝光修补，直方图均衡化处理，各种算子进行锐化，模糊与还原
以及huffman编码及还原的内容
## requirements
首先请在测试环境上安装python2.7及pip,本次实验代码并未在python3和window环境下进行测试。

需要对opencv的python接口进行编译，详情可以参照opencv官网的编译。这有一篇博文可供参考：[mac example](https://lizonghang.github.io/2016/07/16/Mac%E4%B8%8A%E5%AE%89%E8%A3%85python-opencv/)

关于ubuntu16.04上的安装流程，可按照如下博文安装:[ubuntu example](http://blog.csdn.net/github_33934628/article/details/53122208)

之后其他依赖库可按照install.sh进行安装，如有其他依赖库报错问题或者版本问题请在requirements.txt中添加

## run
验证结果只需在项目根目录下python src/gui.py即可，点击button显示对应的题目结果。所有需要调用的函数在对应名称文件中定义。
