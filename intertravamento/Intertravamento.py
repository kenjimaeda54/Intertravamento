
import RPi.GPIO as gpio
import time
BOTAO1=17
BOTAO2=27
BOTAO3=23
BOTAO4=26
LED1=20
LED2=21

def action_press_button(gpi):
      gpio.output(LED1,1) 
      

def action_press_button1(gpi):
      gpio.output(LED1,0)
      
def action_press_button2(gpi):
      gpio.output(LED2,1)
     

def action_press_button3(gpi):
      gpio.output(LED2,0)
      
 
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(BOTAO1,gpio.IN,pull_up_down = gpio.PUD_DOWN)
gpio.setup(BOTAO2,gpio.IN,pull_up_down = gpio.PUD_DOWN)
gpio.setup(BOTAO3,gpio.IN,pull_up_down = gpio.PUD_DOWN)
gpio.setup(BOTAO4,gpio.IN,pull_up_down = gpio.PUD_DOWN)
gpio.setup(LED1,gpio.OUT)
gpio.setup(LED2,gpio.OUT)
gpio.add_event_detect(BOTAO1, gpio.RISING)
gpio.add_event_detect(BOTAO2, gpio.RISING)
gpio.add_event_detect(BOTAO3, gpio.RISING)
gpio.add_event_detect(BOTAO4, gpio.RISING)
estadoled = True
estadoligado = True
try:
 while True:
     if estadoled == True:
        if gpio.event_detected(BOTAO1):
            action_press_button(BOTAO1)
            estadoligado = False
        if gpio.event_detected(BOTAO2):
            action_press_button1(BOTAO2)
            estadoligado = True
     if estadoligado == True: 
        if gpio.event_detected(BOTAO3):
            action_press_button2(BOTAO3)
            estadoled = False
        if gpio.event_detected(BOTAO4):
            action_press_button3(BOTAO4)
            estadoled = True    
            
except KeyboardInterrupt:
    gpio.cleanup()
    exit()
