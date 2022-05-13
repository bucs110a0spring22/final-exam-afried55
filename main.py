import requests
import random
import mathExpression
import mathAd

def main():
  math = mathExpression.MathExpression()
  question = math.get()
  expression = question['expression']
  correctAnswer = question['answer']
  yourAnswer = input(f"Answer the question: {expression} = ")
  intAnswer = int(yourAnswer)
  fact = mathAd.MathAd(yourAnswer)
  numberFact = fact.get()
  ad = numberFact['ad']
  iseven = numberFact['iseven']
  if intAnswer == correctAnswer:
    print(f'Correct answer! You are so smart!')
  else:
    if not iseven:
      yesOrNo = input((f'\n ATTENTION: {ad} \n Do you want it? y/n'))
      if yesOrNo == 'y':
        print("Enjoy!")
      else:
        print("Ok. Practice your arithmatic!")
    else:
      print("That number is even, but it is not the correct answer.") 
main()