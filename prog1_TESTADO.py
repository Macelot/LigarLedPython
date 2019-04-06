#############################################################
#  ########\                                                #
#  ##  _____|                                               #
#  ## |       ######\####\   #######\                       #
#  #####\     ##  _##  _##\ ##  _____|                      #
#  ##  __|    ## / ## / ## |## /                            #
#  ## |       ## | ## | ## |## |                            #
#  ########\  ## | ## | ## |\#######\                       #
#  \________| \__| \__| \__| \_______|                      #
#    Ércio       Marcelo       Cainã                        #
#                                                           #
#  Pisca - Pisca                                            #
#  Liga LED pino 12 durante 1 segundo                       #
#  Desliga LED pino 12 durante 1 segundo                    #
#                                                           #
#  Autores: Marcelo Josué Telles,                           #
#           Ércio Luis Dorneles Berna,                      #
#           Cainã Silva da Costa                            #
#                                                           #
#  Data: 03/06/2017                                         #
#############################################################

#Definindo a utilização da biblioteca GPIO
import RPi.GPIO as GPIO
#Importação da biblioteca time para utilizar temporizadores
import time
#Aqui definimos que vamos usar o numero de ordem do pino, e
#	não o numero que refere a porta
#Para usar o numero da porta, é preciso trocar a definição 
#	"GPIO.BOARD (12)" para "GPIO.BCM (18)" 
#Definindo a pinagem real
GPIO.setmode(GPIO.BOARD)
#Definindo o pino a ser utilizado 
pin_to_circuit = 12
try:
    #Definindo o pino como saída
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    while(1):
	#O valor 1 liga o LED
        GPIO.output(pin_to_circuit,1)
        print("***LIGADO***")
	#Para que possamos ver o LED ligado é
	# necessário esperar
        time.sleep(1)
        GPIO.output(pin_to_circuit,0)
        print("---DESLIGADO---")
        time.sleep(1)
except KeyboardInterrupt:
    print ("Fim")
    pass
finally:
    GPIO.cleanup()
#Fonte: Raspberry pi Fundation
