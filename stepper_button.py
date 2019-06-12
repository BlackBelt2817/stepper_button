import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

motor_pins_output_left = [4, 17, 27, 22]
motor_pins_output_right = [12, 16, 20, 21]

button_pins_input = [6, 13, 19, 26]

def setPins():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    motor_pins_output_left = [4, 17, 27, 22]
    motor_pins_output_right = [12, 16, 20, 21]
    
    button_pins_input = [6, 13, 19, 26]
    
    for motorPin in motor_pins_output_left:
        GPIO.setup(motorPin, GPIO.OUT)
        GPIO.output(motorPin, 0)
        
    for motorPin in motor_pins_output_right:
        GPIO.setup(motorPin, GPIO.OUT)
        GPIO.output(motorPin, 0)

    for buttonPin in button_pins_input:
        GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    
def leftForward():
    for halfstep in range(8):
        for pin in range(4):
            GPIO.output(motor_pins_output_left[pin], halfstep_seq_left[halfstep][pin])
        time.sleep(0.0009) #Don't go faster than 0.0009
    
def rightForward():
    for halfstep in range(8):
        for pin in range(4):
            GPIO.output(motor_pins_output_right[pin], halfstep_seq_right[halfstep][pin])
        time.sleep(0.0009) #Don't go faster than 0.0009

    
def leftReverse():
    for halfstep in range(8):
        for pin in range(4):
            GPIO.output(motor_pins_output_left[pin], halfstep_seq_right[halfstep][pin])
        time.sleep(0.0009) #Don't go faster than 0.0009
    
def rightReverse():
    for halfstep in range(8):
        for pin in range(4):
            GPIO.output(motor_pins_output_right[pin], halfstep_seq_left[halfstep][pin])
        time.sleep(0.0009) #Don't go faster than 0.0009

halfstep_seq_left = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]

halfstep_seq_right = [
  [0,0,0,1],
  [0,0,1,1],
  [0,0,1,0],
  [0,1,1,0],
  [0,1,0,0],
  [1,1,0,0],
  [1,0,0,0],
  [1,0,0,1]
]

fullstep_seq_left = [
  [1,0,0,0],
  [0,1,0,0],
  [0,0,1,0],
  [0,0,0,1]
]

fullstep_seq_right = [
  [0,0,0,1],
  [0,0,1,0],
  [0,1,0,0],
  [1,0,0,0]
]

motorSpins = {
    '6': leftForward,
    '13': leftReverse,
    '19': rightForward,
    '26': rightReverse
}
    
def moveMotor(how):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    motor_pins_output_left = [4, 17, 27, 22]
    motor_pins_output_right = [12, 16, 20, 21]
    button_pins_input = [6, 13, 19, 26]

    motorSpins[str(how)]()

while True:
    
    setPins()

    for pressedButton in button_pins_input:        
        if GPIO.input(pressedButton):
            moveMotor(pressedButton)

    GPIO.cleanup()


