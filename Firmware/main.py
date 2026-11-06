from machine import ADC, Pin
import time

adc = ADC(29)
stat = Pin(25, Pin.IN, Pin.PULL_UP)

print('hello NiroRPI devboard')
print('firmware v0.5 06.11.2026')
print('Author: Nurazkhan')
print('--------------------------------')
print('Thanks to HackClub!')

while True:
    
    # reading GPIO29 which is connected to +Vbat by voltage dividers 100k 
    vbat = adc.read_u16() * 6.6/65535
    # percentage charge assumed that 4.2 = 100% and 3.2V is 0%, so the difference is intermediate percentage
    percentage_charge = int((vbat-3.2)*100)


    if vbat > 3:
        print(f'Battery Connected')
        print(f'Charge is: {percentage_charge}')
    else:
        print('batter is not Connected')

    time.sleep(1)