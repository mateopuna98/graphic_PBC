<template>
    <div class="pcb">
        <h1 class="h1-sub pbc"> PCB {{type}}</h1>

        <div  v-if="estadoMonstruo === 'monstruo-tranquilo'" class="monstruo-tranquilo"></div>
        <div  v-if="estadoMonstruo === 'monstruo-excitado'" class="monstruo-excitado"></div>
        <div v-else-if="estadoMonstruo === 'monstruo-normal'" class="monstruo-normal"></div>
        
        <p class="pbc">Información del proceso:</p>
        <div class="processData">

          <div class="dataRow">
            <p class="title">PID:</p>
            <p class="data">{{ PID }}</p>
          </div>

        </div>
        <div class="processData">

          <div class="dataRow">
            <p class="title">Prioridad:</p>
            <p class="data">{{ prioridad }}</p>
          </div>

        </div>

        <div class="countdown">
          
          <p class="pbc">Progreso proceso actual:</p>
          
          <div class="bar">

            <div :id="`${type}progress`" class="progress">
              <div :id="`${type}progress__fill`" class="progress__fill"></div>
              <span :id="`${type}progress__text`" class="progress__text">0%</span>
            </div>

          </div>

        </div>

    </div>
</template>


<script>
export default {
    name: 'PCB',
    props: {
        type: String,
        process: Object,
        estadoMonstruo: String
    },
    data() {
      return {
        timeLeft : 0,
        counting : false
      }
    },
    methods: {
      setNewRemainingTime(time) {
        this.timeLeft = time
      },
      timer_loop() {

        if (this.process !== null) {

          if (this.$store.getters.getEstadoMonstruo(this.type) === "monstruo-tranquilo") {

            this.$store.commit('updateEstadoMonstruo', { 'estado' : 'monstruo-normal', 'monstruo' : this.type })

          }

          setTimeout(() =>{
            
            if (this.timeLeft > 0) {
              this.timeLeft--
              this.updateProgressBar(document.querySelector(`#${this.type}progress`), this.percentage)
              this.timer_loop()
            }else {
              this.counting = false
              this.$store.dispatch(this.type + 'Delete')
            }
          }, 1000)
          
          
        }

      },
      updateProgressBar(progressBar, value) {
        progressBar.querySelector('.progress__fill').style.width = `${100-value}%`
        progressBar.querySelector('.progress__text').textContent = `${100-value}%`
      }
    },

    created() {
      
      this.timer_loop()
    
    },
    computed: {

      totalTime(){

        if (this.process === null) {
          return 0
        } 
        return this.process['duracion']

      },

      percentage() {

        if (this.process === null) {
          return 0
        } 
        
        return parseInt((this.timeLeft/this.process['duracion'])*100,10)

      },

      PID() {

        if (this.process === null) {
        
          return "Null"
        
        }

        return this.process['PID']

      },

      prioridad() {

        if (this.process === null) {

          return "Null"

        }
        
        return this.process['prioridad']

      }

    },
    watch: {
      process: function(val) {
        if (val === null) {
          this.timeLeft = 0
          this.$store.dispatch('tranquilizarMonstruo', {'monstruo' : this.type})
        } else {
          this.timeLeft = val['duracion']
          if (!this.counting) {
            this.updateProgressBar(document.querySelector(`#${this.type}progress`), 100)
            this.counting = true
            this.timer_loop()
          }
        }
      }

    }
}

</script>


<style scoped>

.monstruo-normal {
  width: 190px;
  height: 240px;
  margin: 2% auto;
  background: url('https://treehouse-code-samples.s3.amazonaws.com/CSS-DD/codepen/blog/monster.png') left center;
  -webkit-animation: play .6s steps(10) infinite;
}

.monstruo-excitado {
  width: 190px;
  height: 240px;
  margin: 2% auto;
  background: url('https://treehouse-code-samples.s3.amazonaws.com/CSS-DD/codepen/blog/monster.png') left center;
  -webkit-animation: play .15s steps(10) infinite;
}

.monstruo-tranquilo {
  width: 190px;
  height: 240px;
  margin: 2% auto;
  background: url('https://treehouse-code-samples.s3.amazonaws.com/CSS-DD/codepen/blog/monster.png') left center;

}

@-webkit-keyframes play {
  100% { background-position: -1900px; }
}

.pbc {
  text-align: center;
}

.processData {
  display: grid;
  grid-template-rows: 33% 33%;
}

.dataRow {
  display: grid;
  grid-template-columns: 50% 50%;
  margin-top: -1vh;
}

.title {
  text-align: left;
  margin-left: 1vw;
}

.data {
  text-align: right;
  margin-right: 1vw;
}

.countdown {

  display: grid;
  grid-template-rows: 50% 50%;
  margin-top: -1vh;

}

.bar {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.progress {

  width: 80%;
  height: 3vh;
  background: #52a6bf8c;
  border-radius: 5px;
  position: relative;
  overflow: hidden;

}

.progress__fill{
  width: 0%;
  height: 100%;
  background: #52a6bf;
  border-radius: 5px;
}

.progress__text{
  position: absolute;
  top: 50%;
  right: 5px;
  transform: translateY(-50%);

}

</style>