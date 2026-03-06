# Carrinho de Controle Remoto para Micro:bit
# Controle por botões A e B

from microbit import *

class RCCar:
    """Carrinho de controle remoto para Micro:bit"""
    
    def __init__(self):
        # Pinos dos motores (ajuste conforme sua ligação)
        self.motor_left_forward = pin8 # Motor esquerdo - frente
        self.motor_left_backward = pin12 # Motor esquerdo - trás
        self.motor_right_forward = pin13 # Motor direito - frente
        self.motor_right_backward = pin14 # Motor direito - trás
        
        self.speed = 512 # 0-1023
        self.is_moving = False
    
    def forward(self):
        """Mover para frente"""
        self.motor_left_forward.write_analog(self.speed)
        self.motor_right_forward.write_analog(self.speed)
        self.motor_left_backward.write_analog(0)
        self.motor_right_backward.write_analog(0)
        display.show("→")
        self.is_moving = True
    
    def backward(self):
        """Mover para trás"""
        self.motor_left_backward.write_analog(self.speed)
        self.motor_right_backward.write_analog(self.speed)
        self.motor_left_forward.write_analog(0)
        self.motor_right_forward.write_analog(0)
        display.show("←")
        self.is_moving = True
    
    def turn_left(self):
        """Virar à esquerda"""
        self.motor_left_forward.write_analog(0)
        self.motor_right_forward.write_analog(self.speed)
        self.motor_left_backward.write_analog(0)
        self.motor_right_backward.write_analog(0)
        display.show("◀")
        self.is_moving = True
    
    def turn_right(self):
        """Virar à direita"""
        self.motor_left_forward.write_analog(self.speed)
        self.motor_right_forward.write_analog(0)
        self.motor_left_backward.write_analog(0)
        self.motor_right_backward.write_analog(0)
        display.show("▶")
        self.is_moving = True
    
    def stop(self):
        """Parar o carrinho"""
        self.motor_left_forward.write_analog(0)
        self.motor_left_backward.write_analog(0)
        self.motor_right_forward.write_analog(0)
        self.motor_right_backward.write_analog(0)
        display.show("■")
        self.is_moving = False
    
    def increase_speed(self):
        """Aumentar velocidade"""
        self.speed = min(1023, self.speed + 100)
        display.scroll(int(self.speed / 10))
    
    def decrease_speed(self):
        """Diminuir velocidade"""
        self.speed = max(0, self.speed - 100)
        display.scroll(int(self.speed / 10))

# Criar o carrinho
car = RCCar()
display.show("▶")

# Loop principal
while True:
    if button_a.is_pressed():
        car.forward()
        sleep(100)
    elif button_b.is_pressed():
        car.backward()
        sleep(100)
    
    if accelerometer.get_x() > 400: # Inclinar para direita
        car.turn_right()
        sleep(100)
    elif accelerometer.get_x() < -400: # Inclinar para esquerda
        car.turn_left()
        sleep(100)
    else:
        if not button_a.is_pressed(2) and not button_b.is_pressed(2):
            car.stop()
    
    sleep(50)
