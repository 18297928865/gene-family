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
Then delete the duplicates just like what we did in blastp part, the rest of which is  **HMM.list**<br>

Now, intersect the **blastp.list** and **HMM.list**, we will get **blastp&HMM.list**

![](https://github.com/18297928865/gene-family/blob/FIIGURES/hmm%26blastp.png)

Click ***copy info***, then extrct the seqs. 

![](https://github.com/18297928865/gene-family/blob/FIIGURES/intersection.png)


We can see that the suquence is multi-line, it may cause some error in the following analyis. 
