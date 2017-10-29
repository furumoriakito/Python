#條件判斷式
num=5566
print('The number is',num)
#If 常用操作符號(語法),< 小於,<= 小於或等於,> 大於,>= 大於或等於,== 等於,!= 不等於
if num==5566:
    print("I love 5566")
num=1234
print('The number is',num)
if num==5566:
    print("I love 5566")
#num==5566它的意思是說，num這個變數是否和右邊的 5566是相等的，兩個等號就是表示進行相等的比較
#==If中使用到

#程式區塊縮排

num = 5566
if num == 5566:
    print('I love 5566')
    print('5566 is the best')
    print('5566 awesome')
#這邊教的是打程式碼要排版好,TAB要會用

#判斷條件
#相等    A==B
#不等於  A!=B
#大於    A>B
#小於    A<B
#大於等於 A>=B
#小於等於 A<=B 注意不要顛倒 X =<,=>,請記得等號永遠都是放在後面

age = 20
if age >= 18:
    print ('drink wine')
if age < 18:
    print('drink water')

#if-else 判斷式

age = 17
if age >= 18:
    print ('drink wine')
else:
    print ('drink water')
#這裡是講If age大於等於18 print drink wine如果不是 print drink water

#if-else 判斷式語法

#if 條件:
#   成立時執行的程式片段
#else:
#   不成立時執行的程式片段

#邏輯運算式

#邏輯運算子
#且  A and B
#或  A or B
#否定 not A
#以下有兩個句子做比較
#國文成積高於 50 分 且 數學成積高於 50 分
#這個就是說國文和數學都要50
#國文成積高於 50 分 或 數學成積高於 50 分
#這個是國文和數學其中1個是50就好

#以下是且(and)的用法
math = 50
chinese = 50
if math > 50 and chinese > 50:
    print("You are qualified")
#因為數學和國文沒大於50所以沒印出來,就算其中一科有60還是不會印出來
#必須當math大於50，且chinese大於50時，才會印出

#以下是或(or)的用法
math = 60
chinese = 50
if math > 50 or chinese > 50:
    print ("You are qualified")
#因為數學有大於50所以有印出來,這個是國文或數學其中有一科達到大於50
#就會印出來

# 以下是否定(not)的用法
#國文成績不低於60分

math = 50
chinese = 60
if math > 50 or not chinese < 60:
    print ("You are qualified")
#如果數學大於50"或"國文"不"低於60就會印出來,國文剛好60符合條件
#原本chinese < 60是指國文成績是否小於60，前面加一個 not 就是否定的意思，所以就變成了國文成績不低於60
#not也可以用在變數這邊

math = 50
not chinese < 50
if math > 50 or chinese > 50:
    print("You are No.1")
#這邊就是數學50,國文不小於50

#數學成績大於60，或國文成績大於80且英文成績大於80

math = 50
chinese = 50
english = 81
if math > 60 or (chinese > 80 and english > 80):
    print("You are Good!!")
#用括號把後面的條件先括起來，表示他們會優先運算，這和先乘除後加減的概念是一樣的，
#雖然 and 運算會先進行，然而為了能清楚讓人讀懂，最好還是用括號將欲優先運算之邏輯括起來