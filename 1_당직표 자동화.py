import datetime
import calendar
from pytimekr import pytimekr #요거는 import pytimekr만 적었을때는 오류났었음.
import random
# 달력 정보 가져오기 : 날짜들을 주중과 주말로 분류하여 저장한다.
# 첫번째 생각 : 달력정보를 가져와 주중과 주말을 분리하여 딕셔너리 형태로 주중 = {'날짜':'요일'}, 주말 = {'날짜':'요일'} 로 정리한다.
# 재고해본 생각 : 꼭 딕셔너리 형태로 적용할 필요는 없고 리스트를 주중, 주말 두개로 만들어 날짜만 따로 모인다. 주중 =[1,2,3,...31],주말 = [6,7,....27,28]
# this_month = input('당직표를 짜려는 달이 몇월인가요?')
this_month = 10

# not_this_day_1 = input('안되는 날을 입력해주세요')
#구글스프레드 시트에 입력받아서 가져올수 있도록 처리해야
not_this_day_1 =[1,2,7,9]
not_this_day_2 =[1,11,29,30]
not_this_day_3=[2,7,29]
not_this_day_4=[1,5,9]
not_this_day_5=[31]
not_this_day_6=[22,23,24]

# 입력받은 안되는 날도 주중과 주말로 나눔?
# 각자 주중몇개 주말 몇개 가져갈지도 나눠야
# 주중을 많이 가져가게 되는 사람들은 주말 더 주는것에서는 제외해야

# 모나드님 말대로도 짜보고
# 내방식대로도 짜보자

# 누구에게 배정해도 괜찮은날 
#당직표를 짜려는 달의 공휴일을 추출합니다.
x=pytimekr.holidays(year=2022) #대체공휴일까지 추출되지는 않는다. 10.10은 공휴일로 나오지 않음
holidays =[]
for i in x:
    if str(i).split('-')[1] == '10':
    # if str(i).split('-')[1] == str(this_month)
        holidays.append(int(str(i).split('-')[2])) #str로 바꿧다가 다시 int로 바꾸는게 뻘짓같기도 하고ㅠ 근데 날짜들이 '03','09' 이렇게들 출력됨

#주중과 주말 또는 공휴일로 날짜를 분리합니다.       
days_of_month = calendar.monthrange(2022,this_month)[1]
weekday_list =[]
weekend_list= []
for i in range(days_of_month):
    if calendar.weekday(2022,this_month,i+1) == 5 or calendar.weekday(2022,this_month,i+1)==6 or i+1 in holidays: 
        #이걸 좀더 간단히 쓸수 없나
        #if calendar.weekday(2022,this_month,i+1) == 5 or 6 라 했더니  weekday_list =[], weekend_list= [1,2,...31]이 생성됨
        weekend_list.append(i+1)
    else:
        weekday_list.append(i+1)

#각 당직자에게 최대한 공평하게 주중과 주말 각각 당직을 설 일수를 배정합니다.
a=len(weekday_list)
b=a//6
c=(days_of_month-a)//6
initial_distribute_1 = [b,c]
initial_distribute_2 = [b,c]
initial_distribute_3 = [b,c]
initial_distribute_4 = [b,c]
initial_distribute_5 = [b,c]
initial_distribute_6 = [b,c]
initial_set = [initial_distribute_1,initial_distribute_2,initial_distribute_3,initial_distribute_4,initial_distribute_5,initial_distribute_6]
final_set=[]
z = (a)%6

if (a)%6 + (days_of_month-a)%6 == 7:
    y=random.choice(initial_set)
    y[0]+=1
    y[1]+=1
    final_set.append(y)
    initial_set.remove(y)

    while z>1:
        w=random.choice(initial_set)
        w[0]+=1
        final_set.append(w)
        initial_set.remove(w)
        z-=1
    for i in initial_set:
        i[1]+=1
        final_set.append(i)
else:
    if (a)%6 ==1:
        y=random.choice(initial_set)
        y[0]+=1
        final_set = initial_set
    else:
        y=random.choice(initial_set)
        y[1]+=1
        final_set = initial_set
print(final_set)

duty_1=[]
duty_2=[]
duty_3=[]
duty_4=[]
duty_5=[]
duty_6=[]
duties =[duty_1,duty_2,duty_3,duty_4,duty_5,duty_6]
        
#이제 각 당직자에게 날짜를 정해진 날짜만큼 날짜를 배분합니다.

#랜덤으로 배분해보되, 안되는날이 배정되어있으면 
#다시 랜덤배정시켜서 조건이 만족되야 배정이 최종끝납니다.

#처음에 duty_1등은 []이므로 교집합이 당연히{}이어서
#duty_1 !=[]의 조건을 추가해주었습니다.

t= (set(duty_1)&set(not_this_day_1)=={} and
set(duty_2)&set(not_this_day_2)=={} and
set(duty_3)&set(not_this_day_3)=={} and   
set(duty_4)&set(not_this_day_4)=={} and   
set(duty_5)&set(not_this_day_5)=={} and   
set(duty_6)&set(not_this_day_6)=={} and
duty_1 !=[] and
duty_2 !=[] and
duty_3 !=[] and
duty_4 !=[] and
duty_5 !=[] and
duty_6 !=[] )

while t==False:
    p=0
    while p<6:
        y=weekday_list
        z=weekend_list
        k=random.sample(y,int(final_set[p][0]))
        q=random.sample(z,int(final_set[p][1]))
        duties[p]+=k+q
        p+=1
        for i in k:
            y.remove(i)
        for j in q:
            z.remove(j)
    if t==True:
        print(duties)
        break

# while t==False:
#     p=0
#     while p<5:
#         y=weekday_list
#         z=weekend_list
#         k=random.sample(y,int(final_set[p][0]))
#         q=random.sample(z,int(final_set[p][1]))
#         duties[p]+k+q
#         for i in k:
#             y.remove(i)
#         for j in q:
#             z.remove(j)
#         p+=1
#     if t==True:
#         break
print(duties)


# initial_week = int(len(weekday_list)//6)
# initial_weekend = int(len(weekend_list)//6)
# initial_distribute_1 = [initial_week,initial_weekend]
# initial_distribute_2 = [initial_week,initial_weekend]
# initial_distribute_3 = [initial_week,initial_weekend]
# initial_distribute_4 = [initial_week,initial_weekend]
# initial_distribute_5 = [initial_week,initial_weekend]
# initial_distribute_6 = [initial_week,initial_weekend]

# initial_set = [initial_distribute_1,initial_distribute_2,initial_distribute_3,initial_distribute_4,initial_distribute_5,initial_distribute_6]
# a=int(len(weekday_list)%6)
# b=int(len(weekend_list)%6)
# x=[1,2,3,4,5,6]
# exemption=[]
# while a>0:
#     y=random.choice(initial_set)
#     exemption.append(y)
#     y[0]+=1
#     initial_set.remove(y)
#     a-=1

print(weekday_list)
print(weekend_list)


    