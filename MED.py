import numpy as np
import time
start =time.clock()
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
            print('%-10s'%str1[0:row],'%-10s'%str2[0:col],"replace ",str1[row],"with ",str2[col]);
            row=row-1;
            col=col-1;
            continue
    print(matrix[-1][-1])
miniEditDistance('expection','intention')
end = time.clock()
print('Running time: %s Seconds'%(end-start))
