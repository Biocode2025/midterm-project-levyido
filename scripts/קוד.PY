amino_acids=['A','R','N','D','C','E','Q','G','H','I','L','K','M','F','P','S','T','W','Y','V']

file=open('data/''קוד של גנים.txt','r')
counts = {}
"מאפס מונה לכל אחד מהחומצות"
for amino in amino_acids: 
  counts[amino]=0

count2=0 
for line in file:
  line=line.strip()
  if line.startswith(">") :
       continue
  else:
   
    "סופר כמה פעמים כל חומצה מופיעה"
    for amino in line:
      "בודק אם האות היא חומצת אמינו"
      if amino in counts:
       counts[amino]+=1
      else:
         count2+=1
countsum=0
"בודק כמה חומצות אמינו יש בסך הכל"
for value in counts.values():
  countsum+=value
percamino={}
i=0
file2=open('results/''תשובות.txt','w') 

"מדפיס לכל אות כמה כמה אחוזים היא מהכלל"
for amino in amino_acids:
 
  percamino[amino]= counts[amino]/countsum*100
  if percamino[amino]-5>0:
     print("amino acid " + amino_acids[i] + " appears "+ str(round(percamino[amino],2)) + "%, " + str(round(percamino[amino]-5,2)) + "% above 5%")

 
  else:
     print("amino acid " + amino_acids[i] + " appears "+ str(round(percamino[amino],2)) + "%, "+ str(round((percamino[amino]-5)*(-1),2))+"% below 5%")

  file2.write(amino_acids[i] + "," + str(round(percamino[amino],2)) + "%" + "\n")
  i+=1 
print(count2)  
file.close()
file2.close()


