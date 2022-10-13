from site import venv
from selenium import webdriver 
import selenium 
from time import sleep 
import pandas as pd
import time  
import requests
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 

driver = webdriver.Firefox(executable_path="/home/zec/Desktop/Selenium/geckodriver") 
driver.get("https://boards.greenhouse.io/deepintent/jobs/4464755004") 


driver.find_element(By.ID,'apply_button').click()
time.sleep(2)
driver.find_element(By.ID,'apply_button').click() 
time.sleep(2)  
fir_col=[] 
sec_col=[]

#first name 

ff=driver.find_element(By.CLASS_NAME,'field').text.replace('*','')
print(ff)
fir_col.append(ff)
#fir_col.append('\n')


txt=driver.find_element(By.ID,'first_name')
hh=txt.get_attribute('type')
print(hh)
sec_col.append(hh) 
#sec_col.append('\n')
#time.sleep(2)
#last name
jj=driver.find_element(By.CSS_SELECTOR,'#main_fields > div:nth-child(6) > label').text.replace('*','')
print(jj) 
fir_col.append(jj) 

kj=driver.find_element(By.ID,'last_name')
f=kj.get_attribute('type')
print(f) 
sec_col.append(f) 

#email
ema=driver.find_element(By.CSS_SELECTOR,'div.field:nth-child(7) > label').text.replace('*','')
print(ema) 
fir_col.append(ema)

mn=driver.find_element(By.ID,'email')
z=mn.get_attribute('type')
print(z) 
sec_col.append(z)
 

# #phone 

pho=driver.find_element(By.CSS_SELECTOR,'div.field:nth-child(8) > label:nth-child(1)').text.replace('*','')
print(pho) 
fir_col.append(pho)


ne=driver.find_element(By.ID,'phone')
b=ne.get_attribute('type')
print(b) 
sec_col.append(b) 



# #school 

sch=driver.find_element(By.CSS_SELECTOR,'div.education:nth-child(1) > fieldset:nth-child(2) > div:nth-child(1) > label:nth-child(1)').text
fir_col.append(sch)
print(sch)
 

# #degree
deg=driver.find_element(By.CSS_SELECTOR,'div.education:nth-child(1) > fieldset:nth-child(2) > div:nth-child(2) > label:nth-child(1)').text 
fir_col.append(deg)
print(deg) 

# #end date 

en=driver.find_element(By.CSS_SELECTOR,'div.education:nth-child(1) > fieldset:nth-child(2) > div:nth-child(3) > fieldset:nth-child(1) > legend:nth-child(1)').text 
print(en) 
fir_col.append(en)


date=driver.find_element(By.CLASS_NAME,'end-date-year.year.background-field')
fi=date.get_attribute('type') 
print(fi)
sec_col.append(fi)
 


#lin=driver.find_element(By.CSS_SELECTOR,'#custom_fields > div:nth-child(1) > label:nth-child(1)').text 
#print(lin)

#linkedin profile 
'''
lin=driver.find_element(By.ID,'custom_fields')
c=lin.find_element(By.TAG_NAME,'label').text
print(c) 
fir_col.append(c) 

dd=driver.find_element(By.ID,'job_application_answers_attributes_0_text_value')
di=dd.get_attribute('type')
print(di)
sec_col.append(di) 
'''



 



#linkedin profile
#do you know
#are you legally
do=driver.find_element(By.ID,'custom_fields')
ri=do.find_elements(By.CLASS_NAME,'field') 
for i in ri: 
    z=i.find_element(By.TAG_NAME,'label').text.replace('*,--','')
    fir_col.append(z)
    print(z) 
    try:
        dd=driver.find_element(By.ID,'job_application_answers_attributes_0_text_value')
        di=dd.get_attribute('type')
        print(di)
        sec_col.append(di) 
    except:
        print(0)


#ir_col.append(do[1])
#print(do)
'''

#are you legally 
'''
#are=driver.find_element(By.CSS_SELECTOR,'').text 
#fir_col.append(are)
#print(are) 
''' 
'''
#gender 

gen=driver.find_element(By.ID,'gender_dropdown_container')
den=gen.find_element(By.TAG_NAME,'label').text 
fir_col.append(den)
print(den) 


#are you hispanic 

his=driver.find_element(By.ID,'hispanic_ethnicity_dropdown_container')
pan=his.find_element(By.TAG_NAME,'label').text 
fir_col.append(pan)
print(pan) 

#veteran status 

vet=driver.find_element(By.ID,'veteran_status_dropdown_container') 
sta=vet.find_element(By.TAG_NAME,'label').text 
fir_col.append(sta)
print(sta) 

#disability

dis=driver.find_element(By.ID,'disability_status_dropdown_container')
lk=dis.find_element(By.TAG_NAME,'label').text
x=lk.split("-")
fir_col.append(x[0])
print(x) 


fr={
    'first':fir_col,
    'second':sec_col

} 
df = pd.DataFrame.from_dict(fr, orient='index')
df = df.transpose()

df.to_csv("mmmmmmjk.csv") 



#/home/zec/Desktop/Selenium/env/logic-365212-4428b51b2954.json

