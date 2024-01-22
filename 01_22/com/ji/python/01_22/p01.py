
'''
sss = ['ㅋㅋㅋ','ㅁㅁㅁ','ㅂㅂㅂ','ㅎㅎㅎ','ㅁㅁㅋㅋㅋ','ㄹㄹㄹ']

for s in sss:
    print(s.find('ㅋㅋㅋ'))
'''
    
# 찾는 문자열이 존재하는 경우    : 그 문자열이 있는 시작 인덱스값을 리턴
    # 찾는 문자열이 존재하지 않는 경우 : -1 리턴
    # 조조(맹덕), 유비(현덕), 손권(중모)
    # 책을 읽어보며 > 위의 인물들이 몇 번 언급되는지 카운팅할 것
    # 인물, 언급횟수 의 형태로 > CSV 파일에 저장

res1,res2,res3 = 0,0,0
wc = {"유비":0,"조조":0,"손권":0}

for i in range(1,11):  
    
    fn = "tk%02d.txt"%i   
    c1,c2,c3 = 0,0,0    
             
    with open("C:/Users/sdedu/Desktop/threekingdoms/"+fn, "r", encoding="UTF-8") as f:
        
        for line in f.readlines():
            line = line.replace('\n',"")
            line = line.split(" ")
            
            for word in line:
            
                if((word.find('유비') != -1) or (word.find('현덕') != -1)):
                    wc['유비'] += 1
                    c1 += 1    
                if((word.find('조조') != -1) or (word.find('맹덕') != -1)):
                    c2 += 1
                    wc['조조'] += 1         
                if((word.find('손권') != -1) or (word.find('중모') != -1)):
                    c3 += 1
                    wc['손권'] += 1

    
    print(f"{i}권에서 각각 불린 횟수")
    print(f"유비(현덕) : {c1}")
    print(f"조조(맹덕) : {c2}")
    print(f"손권(중모) : {c3}")
    print("-"*30)
                 

with open("C:/Users/sdedu/Desktop/threekingdoms/result.csv", "w", encoding="UTF-8") as f:
    f.write(f"유비(현덕),{wc['유비']},조조(맹덕),{wc['조조']},손권(중모),{wc['손권']}")   
      
print("1~10권 까지의 총 합")
print(f"유비(현덕) : {wc['유비']}")
print(f"조조(맹덕) : {wc['조조']}")
print(f"손권(중모) : {wc['손권']}")