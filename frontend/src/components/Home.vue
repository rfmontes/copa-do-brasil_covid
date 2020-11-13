<template>
    <NavBar>
        <div slot="slot-pagina" class="content-pagina">
            <div class="container">
                <h1 class="text-center mb-5 home">Home</h1>
                <Card/>
            </div>
        </div>
    </NavBar>
</template>

<script>
import NavBar from '../components/NavBar.vue'
import Card from '../components/Card.vue'

export default {
  name: 'Home',

  components: {
    NavBar,
    Card,
  }

}
</script>


<style scoped>

.home {
  font-size: 50px;
}

</style>
