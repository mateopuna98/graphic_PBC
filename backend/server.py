#REQUIRES pip install flask
from flask import Flask, jsonify, request
from random import randint, randrange
import time

from FibonacciHeap import FibonacciHeap


pbcHeap = None
fibonacciHeap = FibonacciHeap()
pbcFIFO = None
fifo = []
lastPID = 0

############################### Stats vars ###################################
totalHeap = 0
totalFifo = 0

ponderadoHeap = 0
ponderadoFifo = 0

prioridadesHeap = []
prioridadesFifo = []

lastTimeHeap = 0
lastTimeFifo = 0

tamanoColaHeap = []
tamanoColaFifo = []

tiempoPromedioHeap = []
tiempoPromedioFifo = []

limite = 100

##############################################################################

app = Flask(__name__)

##############################################################################
#####################POST /procesos/<numero_procesos>:########################


@app.route('/procesos/<int:addNumber>', methods=['POST'])
def addRandomProcess(addNumber):
    global pbcHeap
    global fibonacciHeap
    global pbcFIFO
    global fifo
    global lastPID
    global tamanoColaHeap
    global tamanoColaFifo

    print("---------------------ADDDDDD--------------------")

    for i in range(0,addNumber):
        print("generando: " + str(i))
        lastPID = lastPID + 1
        new_process = {

            "prioridad"     :     randint(1, 5),
            "PID"           :     lastPID,
            "duracion"      :     randint(2,10),
            "tiempo_creacion" : time.time()

        }
        try:
            
            fibonacciHeap.insert(new_process["prioridad"], new_process)
            fifo.append(new_process)

        except any:
            return jsonify({"Message" : any})


    print("-d-------d-----------d------------d---------d")
    fibonacciHeap.printHeap()
    print("+++++++++++++++++++++++++++++++++++++++++++++")

    tamanoHeap = (tamanoColaHeap[ len(tamanoColaHeap) - 1 ] if len(tamanoColaHeap) > 0 else 0) + addNumber
    tamanoFifo = (tamanoColaFifo[ len(tamanoColaFifo) - 1 ] if len(tamanoColaFifo) > 0 else 0) + addNumber

    if pbcHeap is None or pbcHeap == {}:
        print('as')
        pbcHeap = fibonacciHeap.delete().process
        tamanoHeap = tamanoHeap - 1
    
    if pbcFIFO is None or pbcFIFO == {}:
        pbcFIFO = fifo.pop(0)
        tamanoFifo = tamanoFifo - 1

    tamanoColaHeap = agregarConLimite(tamanoColaHeap, tamanoHeap)
    tamanoColaFifo = agregarConLimite(tamanoColaFifo, tamanoFifo)

    return returnData()

##############################################################################
####################### POST /procesos/fibonacci/delete ######################

@app.route('/procesos/fibonacci/delete', methods=['POST'])
def deleteFibonacci():
    global pbcHeap
    global fibonacciHeap
    global pbcFIFO
    global fifo

    global totalHeap
    global ponderadoHeap
    global lastTimeHeap
    global prioridadesHeap
    global tiempoPromedioHeap
    global tamanoColaHeap

    print("---------------------FIBONACIIIIIIIIIIIIIIIIIIII DELETE--------------------")

###################################stats#######################################

    if pbcHeap is not None and pbcHeap != {} :
        totalHeap = totalHeap + 1
        prioridadesHeap = agregarConLimite(prioridadesHeap, pbcHeap["prioridad"])
        ponderadoHeap = ponderadoHeap + pbcHeap["prioridad"]/(pbcHeap["duracion"]+lastTimeHeap)
        lastTimeHeap = (pbcHeap["duracion"]+lastTimeHeap)
        last  = (tamanoColaHeap[ len(tamanoColaHeap) - 1 ] if len(tamanoColaHeap) > 0 else 0)
        tamanoColaHeap = agregarConLimite(tamanoColaHeap, ( last - 1 if last > 0 else 0 ))

##############################################################################


    pbcHeap = fibonacciHeap.delete()
    if pbcHeap is not None:
        pbcHeap = pbcHeap.process
    else:
        pbcHeap = None


##############################stats2############################################

    if pbcHeap is not None and pbcHeap != {}:
        tiempoPromedioHeap = agregarConLimite(tiempoPromedioHeap, (time.time() - pbcHeap["tiempo_creacion"]))

################################################################################

    return returnData()

##############################################################################
####################### POST /procesos/fifo/delete ######################

@app.route('/procesos/fifo/delete', methods=['POST'])
def deleteFIFO():
    global pbcHeap
    global fibonacciHeap
    global pbcFIFO
    global fifo

    global totalFifo
    global ponderadoFifo
    global lastTimeFifo
    global prioridadesFifo
    global tamanoColaFifo
    global tiempoPromedioFifo

    print("---------------------FIFOOOOOOOOOOOOOOOOOOOO DELETE--------------------")

###################################stats#######################################

    if pbcFIFO is not None and pbcFIFO != {} :
        totalFifo = totalFifo + 1
        prioridadesFifo = agregarConLimite(prioridadesFifo, pbcFIFO["prioridad"])
        ponderadoFifo = ponderadoFifo + pbcFIFO["prioridad"]/(pbcFIFO["duracion"]+lastTimeFifo)
        lastTimeFifo = (pbcFIFO["duracion"]+lastTimeFifo)
        last = (tamanoColaFifo[ len(tamanoColaFifo) - 1 ] if len(tamanoColaFifo) > 0 else 0)
        tamanoColaFifo = agregarConLimite(tamanoColaFifo, ( last - 1 if last > 0 else 0))

##############################################################################


    if len(fifo) > 0:
        pbcFIFO = fifo.pop(0)
    else:
        pbcFIFO = None

##################################stats2########################################

    if pbcFIFO is not None and pbcFIFO != {}:
        tiempoPromedioFifo = agregarConLimite(tiempoPromedioFifo, (time.time() - pbcFIFO["tiempo_creacion"]))

################################################################################


    return returnData()

##############################################################################
####################### GET /procesos/informacion ######################

@app.route('/procesos/informacion', methods=['GET'])
def getData():
    print("-----------------------------------GETTTTT---------------------------")
    return returnData()
##############################################################################

def returnData():
    global pbcHeap
    global fibonacciHeap
    global pbcFIFO
    global fifo

    global totalHeap
    global ponderadoHeap
    global lastTimeHeap
    global prioridadesHeap
    global tiempoPromedioHeap
    global tamanoColaHeap

    global totalFifo
    global ponderadoFifo
    global lastTimeFifo
    global prioridadesFifo
    global tamanoColaFifo
    global tiempoPromedioFifo

    fibonacciHeap.printHeap()
    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------')

    return jsonify({
        "Message" : "Success",
        "pbcHeap" : pbcHeap,
        "fibonacciHeap"    : stringifyHeap(fibonacciHeap),
        "pbcFifo"   :   pbcFIFO,
        "fifo" : fifo,
        "estadisticas" : {
            "fibonacciHeap" : {
                "procesosTerminados" : totalHeap,
                "valorPonderadoPerdida" : round(ponderadoHeap, 2),
                "prioridadPromedio" : promedio(prioridadesHeap),
                "tamanoColaPromedio" : promedio(tamanoColaHeap),
                "tiempoEsperaPromedio" : promedio(tiempoPromedioHeap),
                "tamanoCola" : (tamanoColaHeap[len(tamanoColaHeap) - 1] if len(tamanoColaHeap) > 0 else 0)
            },
            "fifo" : {
                "procesosTerminados" : totalFifo,
                "valorPonderadoPerdida" : round(ponderadoFifo,2),
                "prioridadPromedio" : promedio(prioridadesFifo),
                "tamanoColaPromedio" : promedio(tamanoColaFifo),
                "tiempoEsperaPromedio" : promedio(tiempoPromedioFifo),
                "tamanoCola" : (tamanoColaFifo[len(tamanoColaFifo) - 1] if len(tamanoColaFifo) > 0 else 0)
            }
        }
    })

def promedio(array):
    if len(array) == 0:
        return 0
    sum = 0
    for el in array:
        sum = sum + el

    sum = sum / len(array)
    return round(sum, 2)

def agregarConLimite(array, elemento):
    global limite
    if len(array) == limite:
        array.pop(0)

    array.append(elemento)
    return array

def addTreefullTree(head):
    headJson = {
        "key" : head.key,
        "rank" : head.rank,
        "process" : head.process,
        "child" : []
    }

    if head.child is not None:
        subHead = head.child
        
        headJson["child"].append(addTreefullTree(subHead))

        nextNode = subHead.next
        while nextNode != subHead:
            headJson["child"].append(addTreefullTree(nextNode))
            nextNode = nextNode.next
    return headJson



def stringifyHeap(heap):
    result = []
    head = heap.head
    if head is None:
        return result
    result.append(addTreefullTree(heap.head))
    nextNode = head.next
    while nextNode != head:
        result.append({
            "key" : nextNode.key,
            "rank" : nextNode.rank,
            "process" : nextNode.process,
            "child" : []
        })
        nextNode = nextNode.next

    return result

if __name__ == '__main__':
    app.run(debug=True, port=5000)
