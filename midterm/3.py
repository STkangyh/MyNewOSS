# CSV 파일에서 데이터 읽기
with open('people_data.csv', 'r') as file:
    lines = file.readlines()

# 데이터 전처리: 헤더 제거, 각 줄을 리스트로 변환
data_lines = [line.strip().split(',') for line in lines[1:]]

# 전체 데이터에서 나이와 키 정보 추출
ages = [int(line[2]) for line in data_lines if len(line) > 2]  # IndexError 방지
heights_male = [int(line[4]) for line in data_lines if len(line) > 4 and line[1] == 'Male']  # IndexError 방지

# 평균 연령 계산
average_age = sum(ages) / len(ages) if ages else 0  # 빈 리스트 예외 처리

# 남성의 평균 키 계산
average_height_male = sum(heights_male) / len(heights_male) if heights_male else 0  # 빈 리스트 예외 처리

# 국가별 빈도수 카운트
country_count = {}
for line in data_lines:
    if len(line) > 3:
        country = line[3]
        if country in country_count:
            country_count[country] += 1
        else:
            country_count[country] = 1

# 가장 빈도가 높은 국가 찾기
most_frequent_country = max(country_count, key=country_count.get) if country_count else "No data"
most_frequent_count = country_count[most_frequent_country] if country_count else 0

# 결과 출력
print(f"Average age: {average_age:.2f}")
print(f"Average height(Male): {average_height_male:.2f}")
print(f"The most frequent country: {most_frequent_country} ({most_frequent_count} times)")

# 출력 결과
'''
Average age: 30.22
Average height(Male): 178.25
The most frequent country: Japan (8 times)
'''