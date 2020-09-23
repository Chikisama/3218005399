import jieba #结巴分词
import gensim #自然语言处理库 转换成向量
import re #正则表达式库
import collections #词频统计库
 
 #读取文本文件
def get_contents(path):
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
    data = pattern.sub("",data)  # 只保留英文a-zA-z、数字0-9和中文\u4e00-\u9fa5的结果。
    newtext = jieba.lcut(data)  #分词
    return newtext

 #余弦公式计算文本相似度
def cos_calc_similarity(text1,text2):
    texts=[text1,text2]
    dictionary = gensim.corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts] #只保留英文a-zA-z、数字0-9和中文\u4e00-\u9fa5的结果。
    similarity = gensim.similarities.Similarity('-Similarity-index', corpus, num_features=len(dictionary))
    test_corpus_1 = dictionary.doc2bow(text1)
    cosine_sim = similarity[test_corpus_1][1]
    return cosine_sim
 
if __name__ == '__main__':
    path1 = r'C:\Users\Chiki\Desktop\homework\text\orig.txt'  #论文原文的文件的绝对路径 作业要求
    path2 = r'C:\Users\Chiki\Desktop\homework\text\orig_add.txt'  #抄袭版论文的文件的绝对路径
    save_path = r'C:\Users\Chiki\Desktop\homework\rate\save.txt'   #输出结果绝对路径
    data1 = get_contents(path1)
    data2 = get_contents(path2)
    text1 = text_clean(data1)
    text2 = text_clean(data2)
    similarity = cos_calc_similarity(text1, text2)
    print("文章相似度： %.4f"%similarity)
    #将相似度结果写入指定文件
    file = open(save_path, 'w', encoding="utf-8") #只写
    file.write("文章相似度： %.4f"%similarity)
    file.close()
 