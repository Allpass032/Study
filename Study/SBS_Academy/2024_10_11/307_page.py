# 307 page 2번 문제

import random

class Updown:
    
    def play(self):
        answer = random.randint(1,100)
        count = 0
        
        while True:
            
            try:
              user_answer = int(input("입력(1~100)"))
            
            except ValueError:
              print('정수만 입력할 수 있습니다.')
            
            except Exception:
              print('알 수 없는 예외가 발생했습니다.')
            
            else: 
              if answer == user_answer:
                  print(f"{count}번만의 정답입니다.")
                  break
              elif user_answer not in range(1,101):
                  print("1~100 사이만 입력하세요")
                  continue
              elif user_answer > answer:
                  print("Down!")
                  count += 1
              else:
                  print("Up!")
                  count += 1              

game = Updown()
game.play()