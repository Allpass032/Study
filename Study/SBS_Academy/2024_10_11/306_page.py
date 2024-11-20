# 1번 문제

class Quiz:

    answer = ['경기도','강원도','충청남도','충청북도','전라남도','전라북도','경상남도','경상북도','제주특별자치도']
    
    @classmethod
    def challenge(cls):
        # correct_answer = cls.answer
        while True:
            user_answer = input('정답은?')
 
            if len(cls.answer) == 0:
                print('모든 도를 맞혔습니다. 성공입니다.')
                break
            
            if user_answer in cls.answer:
                print('정답입니다.')
                cls.answer.remove(user_answer)
            else:
                raise Exception('틀렸습니다.')   

              
try:
  print('우리나라의 9개 모든 도를 맞히는 퀴즈입니다. 하나씩 대답하세요')
  Quiz.challenge()
except Exception as e:
  print(e)