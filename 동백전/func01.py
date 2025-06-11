# 데이터 프레임 정보 확인 함수
def base_info(dataframe, dfname):
	print(f"---[{dfname}]---")
	print(f'\n{dfname}.dtypes > \n\n{dataframe.dtypes}\n\n')
	print(f'\n{dfname}.index > \n{dataframe.index}\n\n')
	print(f'\n{dfname}.columns > \n{dataframe.columns}\n\n')
	print(f'\n{dfname}.ndim > \n{dataframe.ndim}\n\n')
	print(f'\n{dfname}.shape > \n{dataframe.shape}\n\n')
	print(f'\n{dfname}.values > \n {dataframe.values}\n\n')
	

# 데이터 프레임 값 출력 함수
def summary(dataframe, dfname):
	# 요약정보 출력
    f"--[{dfname}]--\n\n {dataframe.info()}"
    
	# 실제 데이터 일부 출력
    print(f"--[{dfname}]--\n\n {dataframe.head(2)}")
    print(f"--[{dfname}]--\n\n {dataframe.tail(2)}")
    
	# 통계치 출력
    print(f'--[{dfname}]--\n\n {dataframe.describe()}')
    

# 데이터 프레임 시군구명 총 거래 금액 확인 함수
def t_price(dataframe,region):
    region_df = dataframe[dataframe['시군구명'] == region] 
    total_price = region_df['총 거래금액'].sum()
    return total_price
	
	
def top_use_info(data,region):
    region_df = data[data['시군구명'] == region]
    grouped_df = region_df.groupby('업종명칭')['총 거래금액'].sum()
    most_use_category = grouped_df.idxmax()
    max_amount = grouped_df.max()
    print(f'부산광역시 {region}의 최다 업종명: {most_use_category}') 
    print(f"부산광역시 {region}의 총 '{most_use_category}' 사용금액 {max_amount}"'\n\n')

# 각 연령대 분류 함수
def cut_age(age):
    if age < 20:
        return '10대 이하'
    elif age <30:
        return '20대'
    elif age <40:
        return '30대'
    elif age <50:
        return '40대'
    else:
        return '60대 이상'
    




# import pandas as pd

# # 예시 데이터 프레임 생성 (이전 코드를 계속 사용)

# def t_price(data, district_name):
#     # 주어진 시군구명에 대한 데이터 필터링
#     district_df = data.loc[data['시군구명'] == district_name].copy()

#     # 총 거래 금액 계산
#     total_amount = district_df['총 거래금액'].sum()

#     # 최빈 사용처 및 해당 금액
#     most_common_place = district_df['업종명칭'].mode()[0]
#     most_common_amount = district_df[district_df['업종명칭'] == most_common_place]['총 거래금액'].sum()

#     # 최소 사용처 및 해당 금액
#     least_common_place = district_df['업종명칭'].value_counts().idxmin()
#     least_common_amount = district_df[district_df['업종명칭'] == least_common_place]['총 거래금액'].sum()

#     return total_amount, most_common_place, most_common_amount, least_common_place, least_common_amount

# # 행정구 목록
# districts = ['강서구', '금정구', '기장군', '남구', '동구', '동래구', '부산진구', '북구', '사상구', '사하구', '서구', '수영구', '연제구', '영도구', '중구', '해운대구']

# # 행정구별 결과 출력
# for district in districts:
#     total_amount, most_common_place, most_common_amount, least_common_place, least_common_amount = t_price(df, district)
#     print(f"{district} 총 금액 > {total_amount}")
#     print(f"{district} 최빈 사용처 > {most_common_place} (총 금액: {most_common_amount})")
#     print(f"{district} 최소 사용처 > {least_common_place} (총 금액: {least_common_amount})\n")
