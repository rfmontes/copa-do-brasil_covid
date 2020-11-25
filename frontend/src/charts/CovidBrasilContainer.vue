<template>
  <div class="container">
    <CovidBrasil
      v-if="loaded"
      :chartdata="chartdata"
      :options="options"/>
      <br>
    <CovidBrasil
      v-if="loaded"
      :chartdata="chartdata2"
      :options="options"/>
  </div>
</template>

<script>
import axios from 'axios';

import CovidBrasil from '../charts/CovidBrasil.vue' 

export default {
  name: 'AreaChartContainer',
  components: { 
    CovidBrasil
  },
  data: () => ({
    loaded: false,
    chartdata: null,
    chartdata2: null,
    options: null,
    dados: [],
    estados: []
  }),
  async mounted () {
    this.loaded = false
    try {
        const { data } = await axios.get('https://covid19-brazil-api.now.sh/api/report/v1')

        let estados = data.data.map(function(e){
            return e.uf
        })

        let casos = data.data.map(function(e){
            return e.cases
        })

        let mortes = data.data.map(function(e){
            return e.deaths
        })
        
        this.chartdata = {
            labels: estados,
            datasets: [
            {
                label: 'Mortes',
                backgroundColor: '#FD4659',
                pointBorderColor: "#4A0100",
                pointBackgroundColor: "#FD4659",
                borderColor: '#4A0100',
                borderWidth: 1,
                data: mortes
            },
            ]
        }
        
        this.chartdata2 = {
            labels: estados,
            datasets: [
            {
                label: 'Casos Positivos',
                backgroundColor: '#858EAB',
                pointBorderColor: "#260F26",
                pointBackgroundColor: "#858EAB",
                borderColor: '#251F47',
                borderWidth: 1,
                data: casos
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