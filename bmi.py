weight = input('請輸入體重(公斤):')
height = input('請輸入身高(公分):')
weight = float(weight) 
height = float(height)
height = height / 100 #換算成公尺
bmi = weight / (height * height)
bmi = int(bmi)
if bmi < 18.5 : 
   print('您的BMI值為', bmi , '體重過輕')
elif bmi >=18.5 and bmi < 24 :
   print('您的BMI值為', bmi , '正常體重')
elif bmi >= 24 and bmi < 27:
   print('您的BMI值為', bmi , '過重')
elif bmi >= 27 and bmi < 30:
   print('您的BMI值為', bmi , '輕度肥胖')
elif bmi >= 30 and bmi < 35:
   print('您的BMI值為', bmi , '中度肥胖')
elif bmi >= 35:
   print('您的BMI值為', bmi , '重度肥胖，你該減肥了呦')






