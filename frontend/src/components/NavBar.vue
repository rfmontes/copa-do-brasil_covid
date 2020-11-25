<template>
<div class="main">
    <div class="content">
        <div class="navbar">
            <b-navbar class="content-navbar" toggleable="lg" type='dark'>
                <b-navbar-brand href="/">Logo Empresa</b-navbar-brand>

                <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

                <b-collapse id="nav-collapse" is-nav>
                    <b-navbar-nav>
                        <b-nav-item :to="{name: 'home'}">Home</b-nav-item>
                        <b-nav-item :to="{name: 'dashboard1'}">Covid-19</b-nav-item>
                        <b-nav-item :to="{name: 'dashboard2'}">Times</b-nav-item>
                        <b-nav-item :to="{name: 'dashboard3'}">Consultar CEP</b-nav-item>
                    </b-navbar-nav>

                    <!-- Right aligned nav items -->
                    <b-navbar-nav class="ml-auto">
                        <b-nav-item-dropdown right>
                        <!-- Using 'button-content' slot -->
                        <template v-slot:button-content>
                            <em>Usuário</em>
                        </template>
                        <b-dropdown-item href="#">Perfil</b-dropdown-item>
                        <b-dropdown-item to="#">Sair</b-dropdown-item>
                        </b-nav-item-dropdown>
                    </b-navbar-nav>
                </b-collapse>
            </b-navbar>
        </div>

        <div class="content-pagina">
            <slot name="slot-pagina"></slot>
        </div>
        
    </div>

</div>
</template>

<script>
export default {
    name: 'NavBar',

}
</script>


<style scoped>

.content {
    width: 100%;
    min-height: 100vh;
    background-color: #BDF8A3;
}

.navbar {
    width: 100%;
    height: 60px;
    padding: 0;
    background-color: #42B395;
}

.content-navbar {
    padding: 25px;
}

</style>
