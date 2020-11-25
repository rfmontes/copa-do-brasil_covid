<template>
  <div class="container">
    <CovidPaises
      v-if="loaded"
      :chartdata="chartdata"
      :options="options"/>
    <CovidPaises
      v-if="loaded"
      :chartdata="chartdata2"
      :options="options"/>
  </div>
</template>

<script>
import axios from 'axios';

import CovidPaises from '../charts/CovidPaises.vue' 

export default {
  name: 'AreaChartContainer',
  components: { 
    CovidPaises
  },
  data: () => ({
    loaded: false,
    chartdata: null,
    chartdata2: null,
    options: null,
  }),
  async mounted () {
    this.loaded = false
    try {
        const { data } = await axios.get('https://covid19-brazil-api.now.sh/api/report/v1/countries')

        let paises = data.data.map(function(e){
            return e.country
        })

        let casos = data.data.map(function(e){
            return e.cases
        })

        let mortes = data.data.map(function(e){
            return e.deaths
        })
        
        this.chartdata = {
            labels: paises,
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
        
        this.chartdata2 = {
            labels: paises,
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