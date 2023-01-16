para=[]
print("enter a para :")
while True:
    line=input()
    if line:
        para.append(line)
    else:
        break
print(para)
out='\n'.join(para)
print(out)