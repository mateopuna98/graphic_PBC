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

    updateData(state, { data }){
    
      console.log("Mutando")
      console.log(data)
      
      state.fibonacciHeap = data['fibonacciHeap']
      state.fifo = data['fifo']
      state.pbcFifo = data['pbcFifo']
      state.pbcHeap = data['pbcHeap']
      state.estadisticas = data['estadisticas']

    }

  },
  actions: {

    async getData(context) {

      await fetch('api/procesos/informacion', {method: 'GET'})
      .then(async (result) =>{

        const res = await result.json()
        context.commit('updateData', { "data":res })

      })
      .catch((e) => {console.log(e)})

    },

    async agregarProcesos(context, { cantidad }) {

      console.log(cantidad)

      await fetch(`api/procesos/${cantidad}`, {method: 'POST'})
      .then((result) => {
        console.log(result)
        context.dispatch('getData')
      })
      .catch((e) => {console.log(e)})

    }

  },
  modules: {
  }

})
