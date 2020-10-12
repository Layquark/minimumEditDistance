## 最小编辑距离实验报告

**人工智能82班    李家正   2184111493**

### 问题的引入

编辑距离（Edit Distance），又称Levenshtein距离，是指两个字串之间，由一个转成另一个所需的最少编辑操作次数。许可的编辑操作包括将一个字符替换成另一个字符，插入一个字符，删除一个字符。一般来说，编辑距离越小，两个串的相似度越大。我们需要使用DP(动态规划)或者迭代来进行具体的实现。

### 数学形式化

对于两个字符串，一共存在着四种操作：

- 删除一个字符     a) Insert a character

  $matrix[i][j]=matrix[i-1][j]+1$

- 插入一个字符     b) Delete a character

  $matrix[i][j]=matrix[i][j-1]+1$

- 修改一个字符     c) Replace a character

  $matrix[i][j]=matrix[i-1][j]+flag$

- 保留一个字符     d) Keep a character

  $matrix[i][j]=matrix[i-1][j]$

根据这四种操作的性质并且结合操作实际，我们总是选择最小的距离，我们有把字符串str1转换到字符串str2，我们会得到分段函数：
$$
matrix[i,j]=
	\begin{cases}
		0, & \text{if $i$=0,$j$=0}\\
		j,& \text{if $i$=0,$j$>0 }\\
		i,& \text{if $i$>0,$j$=0}\\
		min(matrix[i-1][j]+1,matrix[i][j-1]+1,matrix[i-1][j-1]+flag)& \text{if $i$,$j$>0}
	\end{cases}
$$

$$
flags=
	\begin{cases}
		0 & \text{if str1[i]==str2[j]}&\\
		1,& \text{if str1[i]!=str2[j]}
	\end{cases}
$$



### 计算形式化

可以利用迭代或者动态规划，建立$matrix[i][j]$矩阵来存放每一点的MED，并且记录他的上一步操作是什么，在第一次迭代的时候把所有可能路径的操作放在List列表中，在计算出结果后只需遍历List即可找回当时的操作记录。不需要重新对$matrix$进行二次遍历，提高了效率。

![1600616496378](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\1600616496378.png)

### 编程实现

```python
import numpy as np
def mini(delete,insert,keep):
    if delete<insert and delete <keep:
        return delete,"delete"
    elif insert<delete and insert<keep:
        return insert,"insert"
    else:
        return keep,"keep"
def mini2(delete,insert,replace):
    if delete<insert and delete <replace:
        return delete,"delete"
    elif insert<delete and insert<replace:
        return insert,"insert"
    else:
        return replace,"replace"
    
def miniEditDistance(str1,str2):
    len1=len(str1);
    len2=len(str2);
    List=[];
    matrix=np.zeros((len1+1,len2+1))
    for row in range(1,len1+1):
        matrix[row][0]=row;
    for col in range(1,len2+1):
        matrix[0][col]=col;
    for row in range(1,len1+1):
        for col in range(1,len2+1):
            if str1[row-1]==str2[col-1]:
                matrix[row,col],temp=mini(matrix[row-1,col]+1,matrix[row,col-1]+1,matrix[row-1,col-1])
                List.append(temp);
            else:
                matrix[row,col],temp=mini2(matrix[row-1,col]+1,matrix[row,col-1]+1,matrix[row-1,col-1]+1)
                List.append(temp);
    row =len1;
    col =len2;
    while row !=0 and col !=0:
        if List[(row-1)*len2+col-1]=="delete":
            print('%-10s'%str1[0:row],'%-10s'%str2[0:col],"delete ",str1[row]);
            row=row-1;
            col=col;
            continue
        if List[(row-1)*len2+col-1]=="insert":
            print('%-10s'%str1[0:row],'%-10s'%str2[0:col],"insert a ",str2[col]);
            row=row;
            col=col-1;
            continue
        if List[(row-1)*len2+col-1]=="keep":
            print('%-10s'%str1[0:row],'%-10s'%str2[0:col],"keep the same");
            row=row-1;
            col=col-1;
            continue
        if List[(row-1)*len2+col-1]=="replace":
            print('%-10s'%str1[0:row],'%-10s'%str2[0:col],"replace ",str1[row-1],"with ",str2[col-1]);
            row=row-1;
            col=col-1;
            continue
    print(matrix[-1][-1])
miniEditDistance('expection','intention')
```

```markdown
expection  intention  keep the same
expectio   intentio   keep the same
expecti    intenti    keep the same
expect     intent     keep the same
expec      inten      replace  t with  t
expe       inte       keep the same
exp        int        replace  e with  e
ex         in         replace  p with  t
e          i          replace  x with  n
```



### 评估

#### 1.准确性

在进行了多次实验后，结果均是正确。证明了MED动态规划的有效性

#### 2.复杂度

```
Running time: 0.17652879999999993 Seconds
Running time: 0.25646545111555555 Seconds
```

由上可知，我们降低了时间复杂度，但是程序建立了List来存储，所以提高了空间复杂度。
