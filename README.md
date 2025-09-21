# Identification of the PP2C Gene Family
> tools:blastp, pfam, CD-search, SMART</br>
## blastp

![](https://github.com/18297928865/gene-family/blob/FIIGURES/blastp.png)<br>

> query seqs: pep seqs of PP2C download from [tair](https://www.arabidopsis.org/browse/gene_family)
> 
> subject seqs: pep seqs of ipomoea batatas/trifida/triloba

![](https://github.com/18297928865/gene-family/blob/FIIGURES/blastp.list.png)<br>

Here we repsent the result of the previous step. Delete the duplicates in columnB, the rest of which is **blastp.list**<br>
## HMM

Reference：[tbtools](https://www.jianshu.com/p/1643f3a90642)

![](https://github.com/18297928865/gene-family/blob/FIIGURES/HMM.png)

> Input： pep seqs of ipomoea batatas/trifida/triloba
> 
> [Pfam-A.hmm](ftp://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.hmm.gz)
> 
> ID: pfam ID of the motif(s) of PP2C
Then delete the duplicates just like what we did in blastp part, the rest of which is  **HMM.genelist**<br>

Now, intersect the **blastp.genlist** and **HMM.genelist**, we will get **blastp&HMM.genelist**

![](https://github.com/18297928865/gene-family/blob/FIIGURES/hmm%26blastp.png)

Click ***copy info***, then extrct the seqs by ids. 

![](https://github.com/18297928865/gene-family/blob/FIIGURES/intersection.png)

We can see that the suquence is multi-line, it may cause some error in the following analyis. Using [this program](https://github.com/18297928865/gene-family/blob/programs/multi-mono.py) to transform it to single line, that is, **blastp&HMM.sl.fa**

```Python
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
```


![](https://github.com/18297928865/gene-family/blob/FIIGURES/multiline_program.png)

## CD-search

submit **blastp&HMM.sl.fa** to [Batch cd-search tool](https://www.ncbi.nlm.nih.gov/Structure/bwrpsb/bwrpsb.cgi)(E-value=0.00005). Check the result, and we can see some gene's motif is not classified as "PP2Cc", which should be excluded. <br/>

Besides, we can see some genes correspond to multiple transcripts. According to E-value and bit score, we choose only one trasncript left for each gene. Here, we will get **blastp&HMM.sl.CD.genelist**. Than, extract seqs by ids, we will get **blastp&HMM.sl.CD.fa**

![](https://github.com/18297928865/gene-family/blob/FIIGURES/CD-search.png)

## SMART

submit **blastp&HMM.sl.CD.fa** to [SMART](https://smart.embl.de/). Lacking of batch-SMART tools, please submit sequences one by one.

![](https://github.com/18297928865/gene-family/blob/FIIGURES/smart.png)

Delete genes' motif not calssified as PP2C family, the rest of which are the final genes of PP2C family. 
