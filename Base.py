# 기본 출력
print('1'+'1')

# 줄바꿈 방법 작은 따옴표 '''
print('''
이야이야
호
''')

# 문자열 반복 출력 * 연산자 사용
print('오키'*10)

# 문자열 길이 출력 len()함수 사용 ,배열에도 사용 가능
print(len('123'))

# 문자열 치환 방법 .replace('문자열1','문자열2')
print('aaabbbccc'.replace('a','d'))

# 배열에서 min(), max() 등 편리한 함수가 내장되어 있다.
grades = [1,2,3,4,5]
print(max(grades),min(grades))

# import statistics 모듈을 이용하면 더 다양한 함수를 이용 가능하다