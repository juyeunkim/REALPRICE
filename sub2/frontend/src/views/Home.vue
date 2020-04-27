<template>
  <div id="app">
    <v-card-text class="text-center">
      <img class="logo" alt="logo" src="../assets/logo_white.png">
      <input v-model="inputPrice" class="form-control size-20per" type="text" placeholder="가격을 찾아보세요." aria-label="Search" @keyup.enter="search">
      <Cards :stores="searchResult" />
    </v-card-text>
  </div>
</template>


<script>

import Cards from '@/components/landing/Cards.vue'
import api from '@/api/index.js'

export default {
  name: 'Landing',
  components: {
    Cards
  },
  data(){
    return {
      inputPrice: '',
      searchResult: []
    }
  },
  methods: {
    search:  function () {
      var price = parseInt(this.inputPrice)
      var data = {
        price : price,
        ulatitude : 37.272618,
        ulongitude:127.038970,
        mlatitude : 37.501235,
        mlongitude : 127.039511
      }

      api.getStores(data)
      .then(response => {
        console.log(response.data.stores)
        this.searchResult = response.data.stores
        })
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap');

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
  background-color: #0F4C82;
}

.logo{
  width: 300px;
  margin: auto;
}

.size-20per {
  width: 50%;
  margin: auto;
  border-radius: 10rem;
}
</style>
