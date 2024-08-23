from machine import Pin, I2C
import ssd1306
import framebuf
import utime
from num_byte import zero, one, two, three, four, five, six, seven, eight, nine, ten, logo

#pulsante di carica
endstop = Pin(26, Pin.IN, Pin.PULL_UP)

reset_btn = Pin(22, Pin.IN, Pin.PULL_UP)

stato_precedente = endstop.value()
ultimo_cambio = utime.ticks_ms()

# Inizializza l'interfaccia I2C sul tuo Raspberry Pi Pico
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

# Inizializza il tuo schermo OLED
oled = ssd1306.SSD1306_I2C(128, 64, i2c)


screen_timer = 0
list_num = [zero, one, two, three, four, five, six, seven, eight, nine, ten]

shell_num = 1 #conta il numero di bossoli usati
shots = 0 #conta i coldi sparati

def yellow_str(shell_num, shots):
    oled.text(f'Shl:{shell_num}', 0, 0) #prima riga 
    oled.text(f'sht:{shots}', 0, 8)


def show_logo():
    
    buffer = bytearray(logo)
    fbuf = framebuf.FrameBuffer(buffer, 128, 64, framebuf.MONO_HLSB)
    oled.fill(0)
    oled.blit(fbuf, 0, 0)
    oled.show()
    utime.sleep(5)

#show_logo()

#Funzione per prendere il numero dalla lista
def number_on_screen(list_num, number, shell_num, shots):
    
    buffer = bytearray(list_num[number])

    fbuf = framebuf.FrameBuffer(buffer, 128, 64, framebuf.MONO_HLSB)

    oled.fill(0)

    oled.blit(fbuf, 0, 0)
    yellow_str(shell_num, shots)

    # Aggiorna lo schermo per visualizzare i disegni
    oled.show()

number_on_screen(list_num, 10, shell_num, shots)

while True:
    counter = 10
    while counter > 0:
        ora = utime.ticks_ms()
        
        if endstop.value() != stato_precedente and not endstop.value():
            shots += 1
            if utime.ticks_diff(ora, ultimo_cambio) > 100:
                stato_precedente = endstop.value()
                ultimo_cambio = ora
                counter -= 1
                print(counter)
                number_on_screen(list_num, counter, shell_num, shots)
                
        elif endstop.value():
            stato_precedente = endstop.value()
            
        if not reset_btn.value(): #pulsante di reset
            counter = 10
            number_on_screen(list_num, counter, shell_num, shots)
            shell_num += 1
            utime.sleep_ms(800) #blocco di tempo perchè se no se tengo troppo premuto il pulsante si sminchia il counter
        
        utime.sleep_ms(10)
    shell_num += 1