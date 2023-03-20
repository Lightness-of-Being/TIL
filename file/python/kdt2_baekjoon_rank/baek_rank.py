# windows는 powershell에서 , mac은 terminal에서
# 아래 세 문장 입력하여 설치
# pip install gspread
# pip install --upgrade oauth2client
# pip install PyOpenSSL 



from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json
import os

line = '=========================================================================================='
print()
print(line)
print('KDT 2기 백준 랭크 순위')
print(line)

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
json_key_path = os.getcwd() + "/savvy-summit-378704-c3af59953272.json"	#json_key 위치
# 코드와 json_key 파일이 같은 위치에 있어야함
credential = ServiceAccountCredentials.from_json_keyfile_name(json_key_path, scope)
gc = gspread.authorize(credential)
spreadsheet_key = "14Y9sbLUiimqzac2zSun5CoPA0m0TNv3eBCaR6tIKz8w" #스프레드시트정보
doc = gc.open_by_key(spreadsheet_key)
sheet = doc.worksheet("학습 정보")
list_of_lists = sheet.get_all_values()
list_of_lists.pop(0)

# values_list = worksheet.col_values(1)
# 열값 가져오기
# spreadsheet를 불러와 조회
# spreadsheet 일일 조회수가 초과되면 호출되지않음 ?

l = []
import http.client
conn = http.client.HTTPSConnection("solved.ac")
for i in list_of_lists:
    headers = { 'Content-Type': "application/json" }
    baekid = i[6]
    conn.request("GET", "/api/v3/user/show?handle="+ baekid, headers=headers)
    res = conn.getresponse()
    data = res.read()
    try:
        dic = json.loads(data.decode("utf-8"))
        l.append((i[0],dic['handle'],dic['tier'],dic['rating']))
    except:
        l.append((i[0],'not connect',-5,0))

tier = ['DIAMOND','PLATINUM','GOLD','SILVER','BRONZE','UNRATED']
tiern = ['I','II','III','IV','V']
l = sorted(l,key = lambda x : (-x[3],x[0]))
padding = ' '
width = 12
while True:
    print(line)
    print('번호를 입력해주세요.')
    print('[1] 나의 랭킹 보기')
    print('[2] 전체 랭킹 보기')
    print(line)
    a = int(input())
    if a==1:
        print('이름을 입력해주세요. (동명이인이 있다면 본인의 번호도 같이 적어주세요 EX) 박태양(0))')
        bid = input()
        for i in range(len(l)):
            if bid == l[i][0]:
                r = 25-l[i][2]
                try:
                    print(f'{i+1}등 | 이름: {(l[i][0])}, 백준ID: {l[i][1]} | 백준티어: {tier[r//5]} {tiern[r%5]}, SOLVED AC 점수: {l[i][3]}')
                    break
                except:
                    print(f' 이름: {(l[i][0])[:3]}, NOT CONNECTED SOLVED.AC OR WRONG ID IN SPREADSHEET')
                    break
        else:
            print('해당 이름의 학생이 없습니다.')
    else:
        print(line)
        for i in range(len(l)):
            r = 25-l[i][2]
            try:
                print(f'{i+1:0>3}등 | 이름: {(l[i][0])[:3]}, 백준ID: {l[i][1]:{padding}<{width}} | 백준티어: {tier[r//5]} {tiern[r%5]}, SOLVED AC 점수: {l[i][3]}')
            except:
                print(f'{i+1:0>3}등 | 이름: {(l[i][0])[:3]}, NOT CONNECTED SOLVED.AC OR WRONG ID IN SPREADSHEET')
        print(line)
        break

# 두 api의 모든 정보를 불러와 리스트에 저장하기 때문인지 리스트 생성까지 긴시간이 소모됨
# 각 api에서 출력에 필요하는 정보만을 불러와서 저장하면 시간이 짧아질 것이라 기대
# git에는 업로드하지 못하니 수정 사장이나 방향이 있으시다면 5회차 박태양에게 discord로 dm 주시면 감사하겠습니다
# 백준 열심히 풀었고 solved.ac에도 등록했으나 출력에 나오지 않는다면, 스프레드 시트에 등록되어있는 백준아이디가 틀렸을 확률이 매우매우 높습니다
# 매우 드물게 solved.ac 의 일부 자료만을 반환 (리스트가 만들어지는 시간이 짧음) => 왤까?
# 모두 화이팅