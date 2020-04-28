<template>
  <div id="landing">
    <img class="logo" alt="logo" src="@/assets/logo_white.png">
    <input v-model="inputPrice" class="form-control size-20per" type="text" placeholder="가격을 찾아보세요." aria-label="Search" @keyup.enter="search">
    <Cards :stores="searchResult" />
    <!-- <Card v-for="store in searchResult" :key="store.id" :store="store" /> -->
  </div>
</template>


<script>

import Card from '@/components/landing/Card.vue'
import Cards from '@/components/landing/Cards.vue'
import api from '@/api/index.js'
import { mapState, mapActions, mapMutations } from "vuex";

export default {
  name: 'Landing',
  components: {
    Card,
    Cards
  },
  created() {
    this.setMenuWhite(false);
  },
  data(){
    return {
      inputPrice: '',
      searchResult: []
    }
  },
  methods: {
    ...mapMutations("data", ["setMenuWhite"]),
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

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap');

#landing {
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
