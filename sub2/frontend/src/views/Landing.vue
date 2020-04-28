<template>
  <div id="app">
    <img class="logo" alt="logo" src="@/assets/logo_white.png">
    <input v-model="inputPrice" class="form-control size-20per" type="text" placeholder="가격을 찾아보세요." aria-label="Search" @keyup.enter="search">
    <Cards v-for="store in searchResult" :key="store.id" :store="store" />
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
      var data = {
        price : parseInt(this.inputPrice),
        ulatitude : 37.272618,
        ulongitude:127.038970,
        mlatitude : 37.501235,
        mlongitude : 127.039511,
        radius:1000
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

<style>
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
  width: 25%;
  margin: auto;
  border-radius: 10rem;
}
</style>
