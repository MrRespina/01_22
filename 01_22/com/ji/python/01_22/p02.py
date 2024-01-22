from http.client import HTTPConnection
from json import loads

# http://openapi.seoul.go.kr:8088
# 2021 ~ 2023년 3년치 데이터를
# 연,월,일,노선번호,정류장명(역명),승차총승객수,하차총승객수

# 정류장명(익명)에 > ,가 들어있을 수도 있으니 ,를 .으로 변경하여 저장할 것.
# 인원수 관련 > 정수형으로 저장.


hc = HTTPConnection("openapi.seoul.go.kr:8088")

for y in range(21,24):
    
    with open(f"C:\\Users\\sdedu\\Desktop\\Dev\\prac\\bus\\20{y}.csv", "a", encoding="UTF-8") as f:
    
        for m in range(1,13):
        
            if m in [1,3,5,7,8,10,12]:
                dd = 31
            elif m == 2:
                dd = 28
            else:
                dd = 30
                
            for d in range(1,dd+1):
                
                for start in range(1,41000,1000): # 한 페이지에 보여줄 데이터 수
                    
                    res = "%02d%02d%02d"%(y,m,d)
                    hc.request("GET", f"/4f626857416f6c6c3632586a416843/json/CardBusStatisticsServiceNew/{start}/{start+999}/20{res}")
                    resBody = hc.getresponse().read()
                    bData = loads(resBody)
                    
                    if "CardBusStatisticsServiceNew" in bData:
                        
                        for b in bData["CardBusStatisticsServiceNew"]["row"]:
                    
                            route = b['BUS_ROUTE_NO'].replace(',','.')
                            station = b['BUS_STA_NM'].replace(',','.')
                            ride = int(b['RIDE_PASGR_NUM'])
                            alight = int(b['ALIGHT_PASGR_NUM'])
                            '''
                            print(f'년 : 20{y}')
                            print(f'월 : {m}')
                            print(f'일 : {d}')
                    
                            print(f"노선 번호 : {route}")          
                            print(f"역명 : {station}")
                            print(f"승차 총 승객수 : %d"%ride)
                            print(f"하차 총 승객수 : %d"%alight)
                            print("-"*40)
                            '''
                            f.write(f"20{y},{m},{d},{route},{station},{ride},{alight}\n")
        
                print(f"20{y}-{m:02d}-{d:02d} 완료")
                            