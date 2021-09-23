import time as t
import math as m
with open('noi.txt', 'w') as file:
    file.write('sub kiddi\n')
with open('kiddi.txt', 'w') as file:
    file.write('sub nói\n')    
c=float(0)
sleep_time = 0.2
while True:
    with open('noi.txt', 'a') as file:
        file.write('KIDDI{}\n'.format('!'*int((m.sin(c)+1)*20)))

    t.sleep(sleep_time)

    with open('kiddi.txt', 'a') as file:
        file.write('NÓI{}\n'.format('!'*int((m.cos(c)+1)*20)))
    c += 0.1
    t.sleep(sleep_time)
