import pyautogui as pag
import time


file = open('C:\\code\\auto\\data\\12345.csv','r',encoding='utf-8')
text = file.readline().strip()

dong = file.readline().strip()



while dong != '':
    dong_list= dong.split(',')

    sdt = dong_list[0]
    h = dong_list[2]
    ten = dong_list[1]


    
    print(sdt)
    print(ten)
    print(h)

    

    dong = file.readline().strip()


#1
pos=pag.position(23,385)
print(pos)
time.sleep(2)
pag.doubleClick(pos)

#2
pos1=pag.position(737,644)
time.sleep(2)
pag.click(pos1)

#3
time.sleep(3)
pag.typewrite('https://chat.zalo.me/')
time.sleep(3)
pag.press('enter')




#for sdt1 in sdt:
pos4=pag.position(401,181)
time.sleep(4)
pag.click(pos4)
#5
time.sleep(4)
pag.typewrite(sdt)
time.sleep(4)
pag.press('enter')
#6
pos6=pag.position(842,568)
time.sleep(2)
pag.click(pos6)
#7
pos7=pag.position(1132,775)
time.sleep(2)
pag.click(pos7)
#8
pos8=pag.position(401,181)
time.sleep(4)
pag.click(pos8)
#9
time.sleep(4)
pag.typewrite(sdt)
time.sleep(4)
pag.press('enter')
#10
pos10=pag.position(1112,563)
time.sleep(2)
pag.click(pos10)
   
#11
time.sleep(2)
pag.typewrite('em chào'+ h + ten +'đang quan tâm đến sản phẩm bên em',)
time.sleep(2)
pag.press('enter')

#12
time.sleep(2)
pag.locateOnScreen('090.jpg')
time.sleep(2)
pag.press('enter')

    





