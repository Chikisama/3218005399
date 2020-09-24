import jieba #结巴分词
import re #正则表达式库
import math

#读取文本文件
def read_text(path):
    data = ''
    file = open(path, 'r', encoding='UTF-8') #只读
    line = file.readline()
    while line:
        data += line
        line = file.readline()
    file.close()
    return data

 #文本清洗+分词
def text_clean(data):
    newtext = []
    pattern = re.compile(u"[^a-zA-Z0-9\u4e00-\u9fa5]")   #定义正则表达式匹配模式
    data = pattern.sub("",data)  # 只保留英文a-zA-z、数字0-9和中文\u4e00-\u9fa5的结果。	去除标点符号
    newtext = [i for i in jieba.cut(data, cut_all=False) if i != '']  #分词
    return newtext

#列出所有词，将listA和listB放在一个set中
#余弦公式计算文本相似度
def cos(newtext1,newtext2):
	word_set = set(newtext1).union(set(newtext2))
	word_dict = dict()
	i = 0
	for word in word_set:
		word_dict[word] = i
		i += 1
	text1_cut_index = [word_dict[word] for word in newtext1]
	text2_cut_index = [word_dict[word] for word in newtext2]
	text1_cut_index = [0]*len(word_dict)
	text2_cut_index = [0]*len(word_dict)
	for word in newtext1:
		text1_cut_index[word_dict[word]] += 1
	for word in newtext2:
		text2_cut_index[word_dict[word]] += 1
	sum = 0
	sq1 = 0
	sq2 = 0
	for i in range(len(text1_cut_index)):
		sum += text1_cut_index[i] * text2_cut_index[i]
		sq1 += pow(text1_cut_index[i], 2)
		sq2 += pow(text2_cut_index[i], 2)
	
	try:
		cos_result = round(float(sum) / (math.sqrt(sq1) * math.sqrt(sq2)), 2)
	except ZeroDivisionError:
		cos_result = 0.0
	return cos_result

if __name__ == '__main__':
	path1 = r'C:\Users\Chiki\Desktop\homework\text\orig.txt'  #论文原文的文件的绝对路径 作业要求
	path2 = r'C:\Users\Chiki\Desktop\homework\text\orig_add.txt'  #抄袭版论文的文件的绝对路径
	save_path = r'C:\Users\Chiki\Desktop\homework\rate\save.txt'   #输出结果绝对路径
	data1 = read_text(path1)
	data2 = read_text(path2)
	text1 = text_clean(data1)
	text2 = text_clean(data2)
	cos_result = cos(text1,text2)
	print("文章相似度： %.4f"%cos_result)
	#将相似度结果写入指定文件
	file = open(save_path, 'w', encoding="utf-8") #只写
	file.write("文章相似度： %.4f"%cos_result)
	file.close()
 