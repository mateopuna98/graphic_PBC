import { createStore } from 'vuex'

export default createStore({
  state: {
    estadoMonstruo: "monstruo-tranquilo",
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
    
      console.log("Mutando")
      console.log(data)
      
      state.fibonacciHeap = data['fibonacciHeap']
      state.fifo = data['fifo']
      state.pbcFifo = data['pbcFifo']
      state.pbcHeap = data['pbcHeap']
      
      state.estadisticas.fibonacciHeap.procesosTerminados = data['estadisticas']['fibonacciHeap']['procesosTerminados']
      state.estadisticas.fibonacciHeap.prioridadPromedio = data['estadisticas']['fibonacciHeap']['prioridadPromedio']
      state.estadisticas.fibonacciHeap.tamanoColaPromedio = data['estadisticas']['fibonacciHeap']['tamanoColaPromedio']
      state.estadisticas.fibonacciHeap.tiempoEsperaPromedio = data['estadisticas']['fibonacciHeap']['tiempoEsperaPromedio']
      state.estadisticas.fibonacciHeap.valorPonderaroPerdida = data['estadisticas']['fibonacciHeap']['valorPonderadoPerdida']
      state.estadisticas.fibonacciHeap.tamanoCola = data['estadisticas']['fibonacciHeap']['tamanoCola']
      
      state.estadisticas.fifo.procesosTerminados = data['estadisticas']['fifo']['procesosTerminados']
      state.estadisticas.fifo.prioridadPromedio = data['estadisticas']['fifo']['prioridadPromedio']
      state.estadisticas.fifo.tamanoColaPromedio = data['estadisticas']['fifo']['tamanoColaPromedio']
      state.estadisticas.fifo.tiempoEsperaPromedio = data['estadisticas']['fifo']['tiempoEsperaPromedio']
      state.estadisticas.fifo.valorPonderaroPerdida = data['estadisticas']['fifo']['valorPonderadoPerdida']
      state.estadisticas.fifo.tamanoCola = data['estadisticas']['fifo']['tamanoCola']


    },
    updateEstadoMonstruo(state, {estado}) {
      state.estadoMonstruo = estado
    }

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
      .then((result) => {
        console.log(result)
        context.dispatch('getData')
      })
      .catch((e) => {console.log(e)})

    },

    async excitarMonstruo(context) {
        context.commit('updateEstadoMonstruo', { 'estado': 'monstruo-excitado' })
        return new Promise(resolve => setTimeout(resolve, 2000)).then(() => {
          context.commit('updateEstadoMonstruo', { 'estado': 'monstruo-normal' })
        })
    },

    async tranquilizarMonstruo(context) {
      context.commit('updateEstadoMonstruo', { 'estado': 'monstruo-tranquilo' })
    },

    async fibonacciDelete(context) {

      await fetch('api/procesos/fibonacci/delete', { method: 'POST' })
      .then((result) => {
        console.log(result)
        context.dispatch('getData')
      })
      .catch((e) => {console.log(e)})

    },

    async fifoDelete(context) {

      await fetch('api/procesos/fifo/delete', { method: 'POST' })
      .then((result) => {
        console.log(result)
        context.dispatch('getData')
      })
      .catch((e) => {console.log(e)})

    }

  },
  modules: {
  },

  getters: {
    
    getFibonacciHeap(state) {
    
      return state.fibonacciHeap
    
    },

    getFifo(state) {

      return state.fifo

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
