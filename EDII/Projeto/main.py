from umqtt.simple import MQTTClient
from time import sleep, sleep_ms
from machine import Pin, ADC, PWM
import _thread
import network
import dht
import gc
gc.collect()


def read_dht():
    global temp
    temp = 0
    dht_pin.measure()
    temp = int(dht_pin.temperature())


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-
# =-=-=-               ALARME                    =-=-=-
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-
buzzer = PWM(Pin(19), duty=0)
buzzer.duty(0)
ldr = ADC(Pin(34))
presença_detectada = False
btn_alarme = Pin(18, Pin.IN, Pin.PULL_DOWN)
anterior_btn_alarme = 1
global alarme
alarme = False

def armar_alarme():
    buzzer.duty(650)
    sleep(0.1)
    buzzer.duty(0)
    sleep(0.1)
    buzzer.duty(650)
    sleep(0.1)
    buzzer.duty(0)
    
    
def desarmar_alarme():
    buzzer.duty(650)
    sleep(0.1)
    buzzer.duty(0)
    

def soar_alarme():
        buzzer.duty(650)
        sleep(0.1)
        buzzer.duty(0)
        sleep(0.1)


presenca_detectada = False
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-
# =-=-=-       Definição dos tópicos             =-=-=-
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-
topicos = {
    'porta_01': 'portas/01',
    'porta_02': 'portas/02',
    'porta_03': 'portas/03',
    'porta_04': 'portas/04',
    'porta-malas':'portas/05',
    'pressao_pneu_01': 'sensor/pressao/pneu_01',
    'pressao_pneu_02': 'sensor/pressao/pneu_02',
    'pressao_pneu_03': 'sensor/pressao/pneu_03',
    'pressao_pneu_04': 'sensor/pressao/pneu_04',
    'cinto': 'sensor/cinto',
    'dht': 'sensor/dht11',
    'alarme': 'sensor/alarme'
    
    }

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-
# =-=-=-           MULTCALLBACK                  =-=-=-
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-
global p1
p1 = None
global p2
p2 = None
global p3
p3 = None
global p4
p4 = None


global descalibrados
descalibrados = True

def mult_callback(topico, msg):
    global descalibrados
    global p1
    global p2
    global p3
    global p4
    
    if topico == b'sensor/pressao/pneu_01':
        pressao_callback(topico, msg)
        psi_01 = int(msg.decode())
        if 30 < psi_01 < 34 :
            p1 = True
        else:
            p1 = False
        
    elif topico == b'sensor/pressao/pneu_02':
        pressao_callback(topico, msg)
        psi_02 = int(msg.decode())
        if 30 < psi_02 < 34 :
            p2 = True
        else:
            p2 = False
        
        
    elif topico == b'sensor/pressao/pneu_03':
        pressao_callback(topico, msg)
        psi_03 = int(msg.decode())
        if 30 < psi_03 < 34 :
            p3 = True
        else:
            p3 = False
        
        
    elif topico == b'sensor/pressao/pneu_04':
        pressao_callback(topico, msg)
        psi_04 = int(msg.decode())
        if 30 < psi_04 < 34 :
            p4 = True
        else:
            p4 = False
            
    elif topico == b'sensor/cinto':
        cinto_callback(topico, msg)
        #print(topico, msg)
        if msg == b'true':
            cintos_ok.value(1)
        elif msg == b'false':
            cintos_ok.value(0)
        
        
    elif topico == b'portas/01' or b'portas/02' or b'portas/03' or b'portas/04':
        portas_callback(topico, msg)
        global cont_portas
        if msg == b'abrir':
            cont_portas += 1
        elif msg == b'fechar':
            cont_portas -= 1
        
 
    
        
        
        
    
        
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-
         
         
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-
# =-=-=-       Callbacks unitários               =-=-=-
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-
clk = Pin(2, Pin.OUT)
clk.value(0)
def clock():
    while True:
        clk.value(1)
        sleep(0.3)
        clk.value(0)
        sleep(0.3)

global cont_portas
cont_portas = 0



def portas_callback(topico, msg):
    pass


def pressao_callback(topico, msg):
    pass
        
        
        
def cinto_callback(topico, msg):
    pass

    
    
    
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-
# =-=-=-       Conexões necessárias              =-=-=-
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-

print('Iniciando...')
estacao = network.WLAN(network.STA_IF)
estacao.active(True)
estacao.connect('Janaina@bcnet', 'Wxi0689.')
while estacao.isconnected() == False:
    pass
print(estacao.ifconfig())
servidor = 'broker.hivemq.com'
cliente = MQTTClient('NodeMCU', servidor, 1883)
cliente.set_callback(mult_callback)
cliente.connect()
print('Conexao realizada.')
cliente.subscribe('portas/#')
cliente.subscribe('sensor/#')
cliente.subscribe('sensor/cinto')
cliente.subscribe('sensor/pressao/#')

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-
# =-=-=-       Definição dos pinos             =-=-=-
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-

saida_q = Pin(15, Pin.IN)
dht_pin = dht.DHT11(Pin(4))

portas_ok = Pin(14, Pin.OUT)
cintos_ok = Pin(27, Pin.OUT)
pneus_ok = Pin(26, Pin.OUT)
func_geral_ok = Pin(25, Pin.OUT).value(1)


led_verde = Pin(22, Pin.OUT)
led_vermelho = Pin(5, Pin.OUT)


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-
# =-=-=-           Loop principal                =-=-=-
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-
'''
Colocar o label para indicar se está tudo ok ou não
'''

        
def publicar_dht():
    global conteudo
    while True:
        read_dht()
        conteudo = '{"temperatura" : ' + str(temp) + '}'
        cliente.publish(topicos['dht'].encode(), conteudo.encode())
        sleep(5)      
        
        

def esperar_msg():
    while True:
        cliente.wait_msg()
    
try:
    global cont_portas
    global descalibrados
    global alarme
    cintos_ok.value(0)
    pneus_ok.value(0)
    portas_ok.value(1)
    cont_portas = 0
    _thread.start_new_thread(clock, ())
    _thread.start_new_thread(esperar_msg, ())
    _thread.start_new_thread(publicar_dht, ())
    descalibrados = False
    while True:
        gc.collect()
        btn_alarme_pressionado = btn_alarme.value()
        valor_ldr = ldr.read()
        
        if valor_ldr < 1000:
            presenca_detectada = True
        
        if btn_alarme_pressionado and anterior_btn_alarme == 0:
            alarme = not alarme
            if alarme:
                armar_alarme()
            else:
                desarmar_alarme()
        
        
        if presenca_detectada and alarme:
            soar_alarme()
        if presenca_detectada and not alarme:
            presenca_detectada = False
            
        anterior_btn_alarme = btn_alarme_pressionado
        
        if p1 and p2 and p3 and p4:
            descalibrados = False
        else:
            descalibrados = True
        
        if cont_portas == 0:
            portas_ok.value(1)
        else:
            portas_ok.value(0)
            
        if descalibrados:
            pneus_ok.value(0)
        elif not descalibrados:
            pneus_ok.value(1)
            
        led_verde.value(saida_q.value())
        led_vermelho.value(not saida_q.value())
        '''print(f'Portas OK: {portas_ok.value()}')
        print(f'Pneus OK: {pneus_ok.value()}')
        print(f'Cinto OK: {cintos_ok.value()}')
        print(f'Qtde. portas abertas: {cont_portas}')
        print(f'Saida Q: {saida_q.value()}\n')'''
        sleep(0.2)

finally:
    gc.collect()
    cliente.disconnect()
    estacao.disconnect()
    estacao.active(False)
    _thread.exit()
    print("Fim.")



    



