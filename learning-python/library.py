import pandas as pd

df1 = pd.read_csv('pop_kor.csv')
df2 = pd.read_excel('sample.xlsx')

df2.head()

mapping = {
    '서대문서': '서대문구', '수서서': '강남구', '강서서': '강서구', '서초서': '서초구',
    '서부서': '은평구', '중부서': '중구', '종로서': '종로구', '남대문서': '중구',
    '혜화서': '종로구', '용산서': '용산구', '성북서': '성북구', '동대문서': '동대문구',
    '마포서': '마포구', '영등포서': '영등포구', '성동서': '성동구', '동작서': '동작구',
    '광진서': '광진구', '강북서': '강북구', '금천서': '금천구', '중랑서': '중랑구',
    '강남서': '강남구', '관악서': '관악구', '강동서': '강동구', '종암서': '성북구',
    '구로서': '구로구', '양천서': '양천구', '송파서': '송파구', '노원서': '노원구',
    '방배서': '서초구', '은평서': '은평구', '도봉서': '도봉구'
}

df2['구별'] = df2['관서명'].map(mapping).fillna('구 없음')
df2

# pivot = df2.pivot_table(index='구별', aggfunc='sum')
pivot = df2.drop(columns=['관서명']).pivot_table(index='구별', aggfunc='sum')
pivot.head()

pivot = pivot.drop(index='구 없음', errors='ignore')
pivot.head()

for crime in ['강간', '강도', '살인', '절도', '폭력']:
    pivot[f'{crime}검거율'] = (pivot[f'{crime}(검거)'] / pivot[f'{crime}(발생)']) * 100

pivot['검거율'] = (pivot['소계(검거)'] / pivot['소계(발생)']) * 100
pivot.head()

del_column = ['강간(검거)', '강도(검거)', '살인(검거)', '절도(검거)', '폭력(검거)', '소계(발생)', '소계(검거)']
pivot.drop(columns=del_column, inplace=True)
pivot.head()

rename_cols = {
    '강간(발생)': '강간', '강도(발생)': '강도', '살인(발생)': '살인',
    '절도(발생)': '절도', '폭력(발생)': '폭력'
}
pivot.rename(columns=rename_cols, inplace=True)
pivot.head()
