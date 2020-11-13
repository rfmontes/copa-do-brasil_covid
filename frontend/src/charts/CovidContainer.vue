<template>
  <div class="container">
    <Covid
      v-if="loaded"
      :chartdata="chartdata"
      :options="options"/>
  </div>
</template>

<script>
import axios from 'axios';
import moment from "moment";

import Covid from '../charts/Covid.vue' 

export default {
  name: 'AreaChartContainer',
  components: { 
    Covid 
  },
  data: () => ({
    loaded: false,
    chartdata: null,
    options: null
  }),

  async mounted () {
    this.loaded = false
    try {
        const { data } = await axios.get('https://api.covidtracking.com/v1/us/daily.json')

        let positivos = data.map(function(e){
            return e.positive
        }).reverse()

        let datas = data.map(function(e){
            e = moment(e.date, "YYYYMMDD").format("DD/MM");
            return e
        }).reverse()

        this.chartdata = {
            labels: datas,
            datasets: [
            {
                label: 'Casos Positivos',
                backgroundColor: '#858EAB',
                pointBorderColor: "#260F26",
                pointBackgroundColor: "#858EAB",
                borderColor: '#251F47',
                borderWidth: 1,
                data: positivos
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