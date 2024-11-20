# 2번 문제 풀이

file = open('연락처.txt', 'rt')
line_list = file.readlines()

count = 0
for i in range(len(line_list)):
    if '011' in line_list[i]:
        line_list[i] = line_list[i].replace('011', '010')
        count += 1
file.close()

file = open('연락처.txt', 'wt')

for line in line_list:
    file.write(line)
file.close()

print(f"총 {count}건의 011 데이터를 찾았습니다." + '\n' + '모든 데이터를 수정했습니다.')