<template>
    <NavBar>
        <div slot="slot-pagina" class="content-pagina">
            <div class="container">
                <p class="titulo-pagina">Consultar CEP</p>
                
                <b-form-input size="sm" class="mr-sm-2" maxlength="8" placeholder="Digite o cep" v-model="consulta" 
                style="width: 12rem; display: inline"></b-form-input>
                <b-button size="sm" style="margin-bottom: 0.5%;" @click="consultar">Consultar</b-button>

                <p>CEP: {{endereco.cep}}</p>
                <p>Endereço: {{endereco.street}} - {{endereco.city}} / {{endereco.state}}</p>
                <p>Bairro: {{endereco.neighborhood}}</p>
            </div>
        </div>
    </NavBar>
</template>

<script>
import axios from 'axios';
import NavBar from '../components/NavBar.vue'

export default {
  name: 'Dashboard3',

  components: {
    NavBar,
  },
  data() {
      return {
          endereco: [],
          consulta: '',
      }
  },
  methods: {
    consultar() {
      axios.get('https://brasilapi.com.br/api/cep/v1/' + this.consulta)
      .then(res => {
        this.endereco = res.data;
        console.log(res.data)
        console.log(this.consulta)
      })
    }
  }

}
</script>


<style scoped>

</style>