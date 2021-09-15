import Vue from 'vue'
import Vuex from 'vuex'
import obtenerPosicionHijosFibonacci from "../utils/graphicUtils.js"
import _ from "lodash" 
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    estadoMonstruoFIFO: "monstruo-tranquilo",
    estadoMonstruoFibonacci: "monstruo-tranquilo",
    fibonacciHeap: [],
    fifo: [],
    pbcFifo: null,
    pbcHeap: null,
    estadisticas: {
      fibonacciHeap: {
        procesosTerminados: 0,
        prioridadPromedio: 0,
        tamanoColaPromedio: 0,
        tiempoEsperaPromedio: 0,
        valorPonderadoPerdida: 0,
        tamanoCola: 0
      },
      fifo: {
        procesosTerminados: 0,
        prioridadPromedio: 0,
        tamanoColaPromedio: 0,
        tiempoEsperaPromedio: 0,
        valorPonderadoPerdida: 0,
        tamanoCola: 0
      }
    }


  },
  mutations: {

    updateData(state, { data }){
        
      state.fibonacciHeap = data['fibonacciHeap']
      state.fifo = data['fifo']
      if (state.pbcFifo === null && data['pbcFifo'] !== null) {
        
        state.pbcFifo = data['pbcFifo']
      
      }else if (data['pbcFifo'] !== null  && (state.pbcFifo['PID'] !== data['pbcFifo']['PID'])) {
        state.pbcFifo = data['pbcFifo']
      } else if (state.pbcFifo !== null && data['pbcFifo'] === null) {
        state.pbcFifo = null
      }


      if (state.pbcHeap === null && data['pbcHeap'] !== null) {
         
        state.pbcHeap = data['pbcHeap']

      } else if (data['pbcHeap'] !== null  && (state.pbcHeap['PID'] !== data['pbcHeap']['PID'])) {
        state.pbcHeap = data['pbcHeap']
      } else if (state.pbcHeap !== null && data['pbcHeap'] === null) {
        state.pbcHeap = null
      }
      
      state.estadisticas.fibonacciHeap.procesosTerminados = data['estadisticas']['fibonacciHeap']['procesosTerminados']
      state.estadisticas.fibonacciHeap.prioridadPromedio = data['estadisticas']['fibonacciHeap']['prioridadPromedio']
      state.estadisticas.fibonacciHeap.tamanoColaPromedio = data['estadisticas']['fibonacciHeap']['tamanoColaPromedio']
      state.estadisticas.fibonacciHeap.tiempoEsperaPromedio = data['estadisticas']['fibonacciHeap']['tiempoEsperaPromedio']
      state.estadisticas.fibonacciHeap.valorPonderadoPerdida = data['estadisticas']['fibonacciHeap']['valorPonderadoPerdida']
      state.estadisticas.fibonacciHeap.tamanoCola = data['estadisticas']['fibonacciHeap']['tamanoCola']
      
      state.estadisticas.fifo.procesosTerminados = data['estadisticas']['fifo']['procesosTerminados']
      state.estadisticas.fifo.prioridadPromedio = data['estadisticas']['fifo']['prioridadPromedio']
      state.estadisticas.fifo.tamanoColaPromedio = data['estadisticas']['fifo']['tamanoColaPromedio']
      state.estadisticas.fifo.tiempoEsperaPromedio = data['estadisticas']['fifo']['tiempoEsperaPromedio']
      state.estadisticas.fifo.valorPonderadoPerdida = data['estadisticas']['fifo']['valorPonderadoPerdida']
      state.estadisticas.fifo.tamanoCola = data['estadisticas']['fifo']['tamanoCola']
    },
    updateEstadoMonstruos(state, {estado}) {
      state.estadoMonstruoFIFO = estado
      state.estadoMonstruoFibonacci = estado
    },
    updateEstadoMonstruo(state, {estado, monstruo}) {
      state['estadoMonstruo' + monstruo] = estado
    },

  },
  actions: {

    async getData(context) {
      // Usa este metodo para recibir informacion del backend

      await fetch('api/procesos/informacion', {method: 'GET'})
      .then(async (result) =>{

        const res = await result.json()
        context.commit('updateData', { "data":res })

      })
      .catch((e) => {console.log(e)})
    },

    async agregarProcesos(context, { cantidad }) {
      // Usa este metodo para agregar procesos y actualizar automaticamente vuex

      await fetch(`api/procesos/${cantidad}`, {method: 'POST'})
      .then(async (result) => {
        const res = await result.json()
        context.commit('updateData', { "data":res })
      })
      .catch((e) => {console.log(e)})

    },

    async excitarMonstruo(context) {
        context.commit('updateEstadoMonstruos', { 'estado': 'monstruo-excitado' })
        return new Promise(resolve => setTimeout(resolve, 2000)).then(() => {
          context.commit('updateEstadoMonstruos', { 'estado': 'monstruo-normal' })
        })
    },

    async tranquilizarMonstruo(context, { monstruo }) {

      context.commit('updateEstadoMonstruo', { 'estado': 'monstruo-tranquilo', 'monstruo' : monstruo })
    },

    async FibonacciDelete(context) {

      await fetch('api/procesos/fibonacci/delete', { method: 'POST' })
      .then(async (result) => {
        const res = await result.json()
        context.commit('updateData', { "data":res })
      })
      .catch((e) => {console.log(e)})

    },

    async FIFODelete(context) {

      await fetch('api/procesos/fifo/delete', { method: 'POST' })
      .then(async (result) => {
        const res = await result.json()
        context.commit('updateData', { "data":res })
      })
      .catch((e) => {console.log(e)})

    }

  },
  modules: {
  },

  getters: {
    
    getFibonacciHeap(state) {
      if (!state.fibonacciHeap.length || typeof state.fibonacciHeap === 'undefined' || state.fibonacciHeap === null) {
          return []
      } 
      const heap = _.cloneDeep(state.fibonacciHeap)
      let j = 0
      const nodosHeap = heap.map((proceso, index) => {
        j += 1
        const nodo = {data: {id : proceso.process.PID.toString()}, position: {x: 100 + 70 * j, y: 100 }, style : {'background-color': '#52a6bf'}}
        if(index === 0) {
          nodo.data.label =  'PID: ' + proceso.process.PID + ' prioridad: ' + proceso.process['prioridad']
        }
        return nodo
      }) 

      let lastPID = undefined   
      const aristasHeap = heap.map(p => {
        const cPID = p.process.PID.toString()
        if(!lastPID){
          lastPID = cPID;
          return
        }
        const arista = {data: {id: lastPID + cPID, source: lastPID, target: cPID }}
        lastPID = cPID
        return arista
      }).filter(p => p)

      const  head = _.cloneDeep(heap[0])
      if(!head.child.length) {
        return nodosHeap.concat(aristasHeap)
      }
      const {nodosHijos, aristasHijos} = obtenerPosicionHijosFibonacci(head)
    
      return nodosHeap.concat(nodosHijos).concat(aristasHeap).concat(aristasHijos)
    },

    getFifo(state) {

      const nodes = []

      let x = 0
      let y  = 100

      let lastPID = null

      state.fifo.forEach((process) => {

        x +=150

        nodes.push({
          data : {
            id: process['PID'],
            label: 'PID:' + process['PID'] + ' prioridad: ' + process['prioridad'],

          },
          position : {
            x: x,
            y: y
          },
          style : {
            'background-color': '#52a6bf'
          }
        })

        if (lastPID !== null) {

          nodes.push({
            data: {
              id: 'ed' + lastPID + '-' + process['PID'],
              source: lastPID,
              target: process['PID']
            }
          })

        }

        lastPID = process.PID

      })

      return nodes

    },

    getPBCFibonacciHeap(state) {
      
      return state.pbcHeap

    },

    getPBCFifo(state) {

      return state.pbcFifo

    },

    getEstadisticas(state) {

      return state.estadisticas

    }

  }
})
