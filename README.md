# novice
당직표를 자동으로 생성하는 파이썬 프로그램을 작성해보고자합니다.
최종목표는 몇명이 당직을 서는지에 관계 없이 당직을 서는 인원수까지 입력받아 당직표를 짤수 있게 하여 많은 분들이 자신들의 상황에 맞춰 사용할수 있게 하는것입니다.
우선은 6명의 당직표를 짜는 상황에서 출발하여 시작해보겠습니다.

제한조건 1 : 각자 사정으로 당직이 어려운날들이 있어 그 날짜들을 미리 수집한다.
제한조건 2 : 주중 주말 당직 각각을 최대한 공평하게 짜야한다.(ex 각자 한달에 총 5번의 당직을 서는데 어떤 사람은 주중 날짜로만 5번서고, 어떤 사람은 주말 날짜로 5번서면 후자에게 불공평하다)

마지막으로 출력형식은 엑셀로 달력형식으로 날짜아래 당직자가 표시된 형태로 출력될수 있게한다.


사람이 짠다고 생각하고
0. 주중, 주말 날짜를 각자 당직 몇번 설것인지 나눈다.
1. 안된다고 한 날짜들 동그라미
2. 우선 그 날짜들에 사람들이 겹치지 않도록 우선 사람들을 배치한다.
(3. 그리고 이미 배정된 날짜 앞뒤로는 안전마진을 위해 빼놓는다)
4. 그리고 남은 날들에 순서대로 사람들을 돌아가며 배치한다. 
5. 
6. 그리고 각 사람에게 배정해야할 잔여 주중 주말 당직 일수를 계산한다. 
7. 이미 배정된 날짜




결론)-------
이런 수학적 문제해결을 생각할게 아니라

연속된 두날을 같은 사람이 서지않고,
주말, 주중개수를 처음에 배치한것처럼 만 서개하는 조합을 그냥 뽑아내라 하는게 간단할듯
근데 여기에 이제 안되는날이라는 조건이 추가된.
