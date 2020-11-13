<template>
  <div class="container">
    <Time
      v-if="loaded"
      :chartdata="chartdata"
      :options="options"/>
  </div>
</template>

<script>
import axios from 'axios';

import Time from '../charts/Time.vue' 

export default {
  name: 'AreaChartContainer',
  components: { 
    Time 
  },
  data: () => ({
    loaded: false,
    chartdata: null,
    options: null
  }),

  async mounted () {
    this.loaded = false
    try {
        const { data } = await axios.get('http://127.0.0.1:8000/v1/enquetes/times/')

        let times = data.map(function(e){
            return e.nome_time
        })

        let contagem = data.map(function(e){
            return e.votos
        })

        this.chartdata = {
            labels: times,
            datasets: [
            {
                label: 'Votos computados',
                backgroundColor: '#858EAB',
                pointBorderColor: "#260F26",
                pointBackgroundColor: "#858EAB",
                borderColor: '#251F47',
                borderWidth: 1,
                data: contagem
            },
            ]
        }
        this.options = {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
            }
        }
        this.loaded = true

    } catch (e) {
    console.error(e)
    }
  }
}
</script>