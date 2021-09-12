#REQUIRES pip install flask
from flask import Flask, jsonify, request
from random import randint, randrange

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

prioridades10Heap = []
prioridades10Fifo = []

lastTimeHeap = 0
lastTimeFifo = 0

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

    for i in range(0,addNumber):
        lastPID = lastPID + 1
        new_process = {

            "prioridad"     :     randint(1, 5),
            "PID"           :     lastPID,
            "duracion"      :     randint(1,10),

        }
        try:
            
            fibonacciHeap.insert(new_process["prioridad"], new_process)
            fifo.append(new_process)

        except any:
            return jsonify({"Message" : any})

    if pbcHeap is None or pbcHeap == {}:
        pbcHeap = fibonacciHeap.delete().process
    
    if pbcFIFO is None or pbcFIFO == {}:
        pbcFIFO = fifo.pop(0)


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
    global prioridades10Heap

###################################stats#######################################

    if pbcHeap != {} :
        totalHeap = totalHeap + 1
        if len(prioridades10Heap) == 10:
            prioridades10Heap.pop(0)
        prioridades10Heap.append(pbcHeap["prioridad"])
        ponderadoHeap = ponderadoHeap + pbcHeap["prioridad"]/(pbcHeap["duracion"]+lastTimeHeap)
        lastTimeHeap = (pbcHeap["duracion"]+lastTimeHeap)

##############################################################################


    pbcHeap = fibonacciHeap.delete()
    if pbcHeap is not None:
        pbcHeap = pbcHeap.process
    else:
        pbcHeap = {}

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
    global prioridades10Fifo

###################################stats#######################################

    if pbcFIFO != {} :
        totalFifo = totalFifo + 1
        if len(prioridades10Fifo) == 10:
            prioridades10Fifo.pop(0)
        prioridades10Fifo.append(pbcFIFO["prioridad"])
        ponderadoFifo = ponderadoFifo + pbcFIFO["prioridad"]/(pbcFIFO["duracion"]+lastTimeFifo)
        lastTimeFifo = (pbcFIFO["duracion"]+lastTimeFifo)

##############################################################################


    if len(fifo) > 0:
        pbcFIFO = fifo.pop(0)
    else:
        pbcFIFO = {}

    return returnData()

##############################################################################
####################### GET /procesos/informacion ######################

@app.route('/procesos/informacion', methods=['GET'])
def getData():
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
    global prioridades10Heap

    global totalFifo
    global ponderadoFifo
    global lastTimeFifo
    global prioridades10Fifo

    return jsonify({
        "Message" : "Success",
        "pbcHeap" : pbcHeap,
        "fibonacciHeap"    : stringifyHeap(fibonacciHeap),
        "pbcFifo"   :   pbcFIFO,
        "fifo" : fifo,
        "stats" : {
            "fibonacciHeap" : {
                "finishedProcess" : totalHeap,
                "valorPonderadoPerdida" : ponderadoHeap,
                "prioridadPromedio" : promedio(prioridades10Heap)
            },
            "fifo" : {
                "finishedProcess" : totalFifo,
                "valorPonderadoPerdida" : ponderadoFifo,
                "prioridadPromedio" : promedio(prioridades10Fifo)
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
    return sum

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

    heap.printHeap()
    return result

if __name__ == '__main__':
    app.run(debug=True, port=5000)
