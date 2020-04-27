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
import axios from 'axios'

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
      axios
      .get('http://13.125.68.33:8080/api/getStores/')
      .then(response => {
        console.log(response.data.stores)
        this.searchResult = response.data.stores
        })

      // alert('Hello ' + this.inputPrice + '!')
      // `event` 는 네이티브 DOM 이벤트입니다
      //if (event) {
      //  alert(event.target.tagName)
      //}
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
