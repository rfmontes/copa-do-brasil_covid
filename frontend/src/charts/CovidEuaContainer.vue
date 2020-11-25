<template>
  <div class="container">
    <CovidEua
      v-if="loaded"
      :chartdata="chartdata"
      :options="options"/>
      <br>
    <CovidEua
      v-if="loaded"
      :chartdata="chartdata2"
      :options="options"/>
  </div>
</template>

<script>
import axios from 'axios';
import moment from "moment";

import CovidEua from '../charts/CovidEua.vue' 

export default {
  name: 'AreaChartContainer',
  components: { 
    CovidEua 
  },
  data: () => ({
    loaded: false,
    chartdata: null,
    options: null,
    chartdata2: null
  }),

  async mounted () {
    this.loaded = false
    try {
        const { data } = await axios.get('https://api.covidtracking.com/v1/us/daily.json')
        
        let positivos = data.map(function(e){
            return e.positive
        }).reverse()
        
        let mortes = data.map(function(e){
            return e.death
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

        this.chartdata2 = {
            labels: datas,
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