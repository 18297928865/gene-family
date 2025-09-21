fr1=input("enter the file path of multi-line fasta")
fw1=input("enter the path of output")

fr=open(fr1, 'r')  #读文件
fw=open(fw1, 'w')  #写文件
seq={}
for line in fr:
    if line.startswith('>'):    #判断字符串是否以‘>开始’
        name=line.split()[0]    #以空格为分隔符。
        seq[name]=''
    else:
        seq[name]+=line.replace('\n', '')
fr.close()
for i in seq.keys():
    fw.write(i)
    fw.write('\n')
    fw.write(seq[i])
    fw.write('\n')
fr.close()