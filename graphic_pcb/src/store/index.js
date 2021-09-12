import { createStore } from 'vuex'

export default createStore({
  state: {

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
        valorPonderaroPerdida: 0
      },
      fifo: {
        procesosTerminados: 0,
        prioridadPromedio: 0,
        tamanoColaPromedio: 0,
        tiempoEsperaPromedio: 0,
        valorPonderaroPerdida: 0
      }
    }


  },
  mutations: {
  },
  actions: {

    async getData() {

      const res = await fetch('http://localhost:5000/procesos/informacion', { method : 'GET' })
      const data = await res.json()

      console.log(data)

    }

  },
  modules: {
  }

})
