# 1번 문제

nation = ['그리스', '아테네', '독일', '베를린', '러시아', '모스크바', '미국', '워싱턴']
file = open('nation.txt', 'wt')

for n in range(0,len(nation),2):
    file.write(nation[n] + '-' + nation[n+1] + '\n')
    
file.close()
   
file = open('nation.txt','rt')
lines = file.readlines()
print('생성된 nation.txt 파일의 내용은 다음과 같습니다.')
for line in lines:
    print(line)

file.close() 

# 2번 문제

file = open('연락처.txt', 'r+')

line_list = file.readlines()

count = 0
for i in range(len(line_list)):
    if '011' in line_list[i]:
        line_list[i]=line_list[i].replace('011', '010')
        count += 1

print(f"총 {count}건의 011 데이터를 찾았습니다." + '\n' + '모든 데이터를 수정했습니다.')
file.seek(0)
file.writelines(line_list)
file.close()