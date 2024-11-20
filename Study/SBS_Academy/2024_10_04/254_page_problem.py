# 1번 문제 풀이(파일 존재하지 않을 경우는 배우지 않았음)

while True:
    what_copy = input('복사할 파일명을 입력하세요')
    if what_copy.split('.')[-1] != 'txt':
        print('복사할 수 없는 파일입니다.')
        continue
    else:
        break