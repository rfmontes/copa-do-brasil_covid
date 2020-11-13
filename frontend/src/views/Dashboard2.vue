<template>
    <NavBar>
        <div slot="slot-pagina" class="content-pagina">
            <div class="container">
              <p class="titulo-pagina">Campeão da Copa do Brasil 2020</p>
              <div class="card mb-4">
                  <div class="card-header titulo-grafico">
                      <i class="fas fa-chart-area mr-1"></i>
                      Votos Computados 
                  </div>
                  <div class="card-body"><TimeContainer/></div>
              </div>
            </div>
        </div>
    </NavBar>
</template>

<script>
import axios from 'axios';

import NavBar from '../components/NavBar.vue'
import TimeContainer from '../charts/TimeContainer.vue'

export default {
  name: 'Dashboard2',

  components: {
    NavBar,
    TimeContainer,
  },

  data() {
      return {
          times: [],
      }
  },
  mounted () {
      axios.get('http://127.0.0.1:8000/v1/enquetes/times/')
      .then(res => {
          this.times = res.data;
      });
  },   
  methods: {
      votar(time) {
        if (!confirm('Você deseja realmente votar nesse time?')) {
            return;
        }
        axios.patch('http://127.0.0.1:8000/v1/enquetes/times/' + time.id + '/', { votos: time.votos += 1 })
        .then(function(res) {
            console.log(res);
        });
      }
  }

}
</script>

<style scoped>

.lista {
    list-style: none;
}

</style>