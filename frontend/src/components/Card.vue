<template>
    <div class="container">
        <p class="titulo-pagina">Favoritos para Copa do Brasil</p>     
        <div>
            <b-card-group deck>
                <li class="lista mr-3" v-for="c in times" :key="c.id">
                    <div class="card border-primary mb-3 text-center" style="width: 12rem;">
                        <div class="card-header" style="font-size: 25px;">{{ c.nome_time }}</div>
                        <div class="card-body text-primary">
                            <b-button variant='info' class="ml-2 mb-2" @click="votar(c)">Votar</b-button>
                        </div>
                    </div>
                </li>
            </b-card-group>
            <b-button variant='danger' size="sm" :to="{name: 'dashboard2'}">Ver resultados parciais</b-button>
        </div> 
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Dashboard2',

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
        if (!confirm('Confirmar voto?')) {
            return;
        }
        axios.patch('http://127.0.0.1:8000/v1/enquetes/times/' + time.id + '/', { votos: time.votos + 1 })
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