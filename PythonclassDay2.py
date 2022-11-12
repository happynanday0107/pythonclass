#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello World!!!")


# In[10]:


money = True   #대소문자 구별 (T(대문자)rue,if(소문자))

if money == True:
    print("택시를 타자")
else: 
    print("걸어 가자")


# In[ ]:


money = 8000

if money >= 5000:
    print("택시를 타자")
elif money >= 1000:
    print("버스를 타자")
else:
    print("걸어가자")


# In[ ]:


# 학생의 성적을 입력 받아서 
# 점수가 90이상 이면 'A학점'입니다. 
# 점수가 80이상 이면 'B학점'입니다. 
# 점수가 70이상 이면 'C학점'입니다. 
# 점수가 60이상 이면 'D학점'입니다. 
# 나머지는 모두 'F학점'입니다. 

(순서도, 코드)


# In[16]:


score = int(input("성적을 입력하세요"))

if score >= 90 : 
    print("A학점")
elif score >= 80 :
    print("B학점")
elif score >= 70 :
    print("C학점")
elif score >= 60:
    print("D학점")
else :
    print("F학점")


# In[17]:


# While

no = 10

while no >= 0:
    print(no)
    no = no - 1


# In[20]:


prompt = "1. 덧셈 / 2. 뺄셈 / 3. 곱셈 / 4. 나눗셈 / 5. 종료"
no = 1

while no <= 4:
    print(prompt)
    no = int(input())
    


# In[21]:


no = 10

while no >= 0:
    print(no)
    no = no-1


# In[22]:


prompt = "1. 덧셈 / 2. 뺄셈 / 3. 곱셉 / 4. 나눗셈 / 5. 종료"
no = 1

while no <= 4:
    print (prompt)
    no = int(input())


# In[24]:


# while문의 경우에는 반복 횟수가 정확하지 않을 경우가 많기 때문에 조건에서 뿐만이 아니라 중간에 반복을 종료 시키는 방법도 필요하다.

no = 0

while no <= 10:  #조건식에서 빠져나가는법1
    print(no)
    no = no+1


# In[26]:


no = 0

while True:   # 불린 트루 폴스는 대문자 T,F
    print(no)
    no = no+1 # 여기까진 무한반복
    
    if no > 10: #돌다가 빠져나가는법2
        break


# In[30]:


#while문을 사용하여 1부터 100까지의 수 중 3의 배수만의 합을 구하시오. #순서도 6,7

no = 1
sum = 0

while no <=100:
    if no % 3 == 0:
        sum = sum + no
        
    no = no + 1 # (파이썬)  no += 1   (자바) no++;
    
print(sum)    


# In[36]:


#For 구문


# In[38]:


for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)


# In[43]:


math = [80, 90, 70, 70, 100]

j = 1
for i in math:
    if i > 90:
        print(j, "번째 학생은 합격입니다.")
    else:
        print(j, "번째 학생은 불합격입니다")
    j +=1


# In[44]:


for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)


# In[46]:


for i in [1,2,3,4,5,6,7,8,9,10]:
    if i % 2 == 0:
         print(i)


# In[50]:


for i in [1,2,3,4,5,6,7,8,9,10]:
    if i % 2 != 0:
        continue
        
    print(i)


# In[ ]:


# range 함수

# 숫자를 자동으로 생성해준다. for문과 함께 사용되는 경우가 아주 많다. 


# In[52]:


for i in range(1,11): # 1에서 11미만, 두번째 수는 미만
    print(i)


# In[68]:


# for 문으로 구구단 출력하기 (이중 for문) 외우기

for i in range(2,10):
    for j in range(1,10):
        print(i,"*",j ,"=", i*j)


# In[63]:


for i in range(2,10): # i는 단을 표현
    for j in range(1,10):
        print(i*j, end="\t")
    print()
              


# In[67]:


for j in range(1,10): # i는 단을 표현
    for i in range(2,10):
        print(j*i, end="\t")
    print()
              


# In[85]:


# range를 사용하여 100이하의 수중 짝수들만의 합계를 구하세요 

#range (start, stop, step)

#for i in rage(11): #start를 생략하면 0에서 시작

#for i in range(0,11,2): #step를 생략하면 1씩 증가
# print(i)


sum = 0
for i in range(0,101):
    if i%2 == 0:
        sum += i
        
print(sum)


# In[87]:


sum = 0
for i in range(0,101,2):
    sum += i
    
print(sum)


# In[90]:


# 리스트 축약/내포 List Comprehension
# 리스트룰 좀더 편리하고 직관적으로 만드는 작업이다. 

list1 = [1,2,3,4]

print(list1)

list2 = [num        for num in list1]  #덩어리 2개

print(list2)

list3 = [num*2        for num in list1]   #덩어리 2개

print(list3)

list4 = [num        for num in list1    if num%2 == 0]    #덩어리 3개

print(list4)


# In[93]:


no = 90

if no >= 80:     #추천
    print("합격입니다")
else:
    print("불합격입니다")
    
    
print("합격입니다"     if no>=80   else "불합격입니다")  #if 축약형

