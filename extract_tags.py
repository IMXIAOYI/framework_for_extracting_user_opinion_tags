from nltk.parse.stanford import StanfordDependencyParser
import string
import re
path_to_jar = 'stanford-parser-full-2017-06-09/stanford-parser.jar'
path_to_models_jar = 'stanford-parser-full-2017-06-09/stanford-parser-3.8.0-models.jar'
dependency_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)

###读入yelp_testing2.txt, 把每个评论根据，和. 分成一个个字符串，把结果打印出来 同时保存到列表里，一个循环结束写入文件


f = open("yelpreviews.txt","r")  
lines = f.readlines()#读取全部内容  
f.close()

output=[]
for i in lines:
	if(i!="\n"):
		templist=re.split(r'[,:;\n|?!.()]+',i.lower())
		output.append(templist)


shuchu= open(r'result_v2_part9.txt','w')

for review in output:
	for line in review:
		print("\n")
		string=line
		length=False
		total=string.split()

		if(len(total)>0):
			length=True	

		if(length==True):
			length=False
			if (total[0]=="and" or total[0]=="but" or total[0]=="or"):
				string=""
				if(len(total)-1>0):
					for i in range(1,len(total),1):
						string=string+total[i]+" "
					print(string)
					length=True
					result1 = dependency_parser.raw_parse(string)
					dep1=result1.__next__()
					final1=list(dep1.triples())
					for i in final1:
						print(i)
				else:
					length=False
			else:
				length=True
				string=""
				for i in range(0,len(total),1):
					string=string+total[i]+" "
				print(string)
				result1 = dependency_parser.raw_parse(string)
				dep1=result1.__next__()
				final1=list(dep1.triples())
				for i in final1:
					print(i)

            	




		i=0
		nsubj=False
		while (length==True and i<len(final1)):
	
			if(final1[i][1]=="amod"):
				if(i+1<=len(final1)-1):
					if((final1[i+1][1]=="amod" and (final1[i+1][2][1]=="JJ" or final1[i+1][2][1]=="JJS"))
					or  (final1[i+1][1]=="compound" and (final1[i+1][2][1]=="NN" or final1[i+1][2][1]=="NNS"))):
						if(i+2<=len(final1)-1):
							if(final1[i+2][1]=="compound" and (final1[i+2][2][1]=="NN" or final1[i+2][2][1]=="NNS")):
								temp=""
								temp=final1[i][2][0]+" "+final1[i+1][2][0]+" "+final1[i+2][2][0]+" "+final1[i][0][0]
								print(temp)
								shuchu.writelines(temp+'\n')
								i=i+2
							else:
								temp=""
								#temp=final1[i+1][2][0]+" "+final1[i+1][0][0]+" "+final1[i][0][0]
								temp=final1[i][2][0]+" "+final1[i+1][2][0]+" "+final1[i][0][0]
								print(temp)
								shuchu.writelines(temp+'\n')
								i=i+1

						else:
							temp=""
							#temp=final1[i+1][2][0]+" "+final1[i+1][0][0]+" "+final1[i][0][0]
							temp=final1[i][2][0]+" "+final1[i+1][2][0]+" "+final1[i][0][0]
							print(temp)
							shuchu.writelines(temp+'\n')
							i=i+1
					else:
						temp=""
						temp=final1[i][2][0]+" "+final1[i][0][0]
						print(temp)
						shuchu.writelines(temp+'\n')
				else:
						temp=""
						temp=final1[i][2][0]+" "+final1[i][0][0]
						print(temp)
						shuchu.writelines(temp+'\n')


			elif(final1[i][1]=="nsubj" and (final1[i][2][1]=="NN" or final1[i][2][1]=="NNS")):
				t=1
				penduan=True
				#while(i+t<=len(final1)-1 and t<=4):
				while(i+t<=len(final1)-1):
					if((final1[i+t][1]=="neg"  or final1[i+t][1]=="advmod") and final1[i+t][0][1]=="JJ"):
						if(i+t+1<=len(final1)-1):
							if(final1[i+t+1][1]=="advmod" and final1[i+t+1][0][1]=="JJ"):
								temp=""
								temp=final1[i][2][0]+" "+final1[i+t][2][0]+" "+final1[i+t+1][2][0]+" "+final1[i+t][0][0]
								print(temp)
								shuchu.writelines(temp+'\n')
								penduan=False
								nsubj=True
								#print(1)
								i=i+1
							else:
								temp=""
								temp=final1[i][2][0]+" "+final1[i+t][2][0]+" "+final1[i+t][0][0]
								print(temp)
								shuchu.writelines(temp+'\n')
								penduan=False
								nsubj=True
						else:
							temp=""
							temp=final1[i][2][0]+" "+final1[i+t][2][0]+" "+final1[i+t][0][0]
							print(temp)
							shuchu.writelines(temp+'\n')
							penduan=False
							nsubj=True
							#i=i+t
					if(final1[i+t][1]=="cc" and final1[i+t][0][1]=="JJ"):
						if(i+t+1<=len(final1)-1):
							if(final1[i+t+1][1]=="conj" and final1[i+t+1][2][1]=="JJ"):
								temp=""
								temp=final1[i+t][0][0]+" "+final1[i+t][2][0]+" "+final1[i+t+1][2][0]+" "+final1[i][2][0]
								print(temp)
								shuchu.writelines(temp+'\n')
								penduan=False
								nsubj=True

					t=t+1
				if(penduan==True and final1[i][0][1]=="JJ"):
					temp=""
					temp=final1[i][0][0]+" "+final1[i][2][0]
					print(temp)
					shuchu.writelines(temp+'\n')

			elif(nsubj==False and final1[i][1]=="cc" and final1[i][0][1]=="JJ"):
				if(i+1<=len(final1)-1):
					if(final1[i+1][1]=="conj" and final1[i+1][2][1]=="JJ"):
						if(i+2<=len(final1)-1):
							if(final1[i+2][1]=="amod" and (final1[i+2][0][1]=="NN" or final1[i+2][0][1]=="NNS")):
								temp=""
								temp=final1[i][0][0]+" "+final1[i][2][0]+" "+final1[i+1][2][0]+" "+final1[i+2][2][0]+" "+final1[i+2][0][0]
								print(temp)
								shuchu.writelines(temp+'\n')
								i=i+2
							else:
								temp=""
								temp=final1[i][0][0]+" "+final1[i][2][0]+" "+final1[i+1][2][0]
								print(temp)
								shuchu.writelines(temp+'\n')
						else:
							temp=""
							temp=final1[i][0][0]+" "+final1[i][2][0]+" "+final1[i+1][2][0]
							print(temp)
							shuchu.writelines(temp+'\n')


			elif(final1[i][1]=="neg" and final1[i][0][1]=="JJ"):
				temp=""
				temp=final1[i][2][0]+" "+final1[i][0][0]
				print(temp)
				shuchu.writelines(temp+'\n')


			elif(nsubj==False and final1[i][1]=="advmod" and final1[i][0][1]=="JJ"):
				#if(i+1<=len(final1)-1 ):
				if(i+1<=len(final1)-1):
					if(final1[i+1][1]=="advmod" and final1[i+1][0][1]=="JJ"):
						temp=""
						temp=final1[i][2][0]+" "+final1[i+1][2][0]+" "+final1[i][0][0]
						print(temp)
						shuchu.writelines(temp+'\n')
						#print(1)
						i=i+1
					else:
						temp=""
						temp=final1[i][2][0]+" "+final1[i][0][0]
						print(temp)
						shuchu.writelines(temp+'\n')
						#print(2)
				else:
						temp=""
						temp=final1[i][2][0]+" "+final1[i][0][0]
						print(temp)
						shuchu.writelines(temp+'\n')
						#print(3)

			i=i+1



shuchu.close()



