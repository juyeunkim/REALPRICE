<template>
<v-content>
    <div id="app-view" style="height: 100%;" v-if="landing2">
        <div id="app">
          <!-- <Card v-for="store in searchResult" :key="store.id" :store="store" /> -->
          <v-card-text class="text-center">
            <img class="start logo" :class="{show:!landing0, land: !landing1}" alt="logo" src="@/assets/logo_white.png">
            <div class="start say" :class="{show:!landing0, notShow: !landing1}">
              진짜 가격, Real Price.
            </div>
            
            <!-- <Cards :stores="RealPriceList" @clickItem="selectItem"/> -->
          </v-card-text>
        </div>
    </div>
  </v-content>
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
    // this.setMenuWhite(false);
    this.landing();
  },
  data(){
    return {
      inputPrice: '',
      searchResult: [],
      landing0: true,
      landing1: true,
      landing2: true,
    }
  },
  computed: {
    ...mapState({
      colorWhite: state => state.data.menuWhite
    })
  },
  methods: {
    // ...mapMutations("data", ["setMenuWhite"]),
    landing: function(){
      var vm = this;
      setTimeout(function(){
        vm.landing0 = false;
        setTimeout(function(){
          vm.landing1 = false;
          setTimeout(function(){
            vm.landing2 = false;
            setTimeout(function(){
              // vm.landing0 = true;
              // vm.landing1 = true;
              // vm.landing2 = true;
            }, 1000);
          }, 2000);
        }, 1500);
      }, 1000);
      
    }
  }
}
</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap');


#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
  background-color: #0F4C82;
  // padding-top: 64px;
}
.bgWhite{
  background-color: white;
}
.start{
  opacity: 0;
}
.show{
  opacity: 1;
  transition:opacity 0.3s;
}

.logo{
  width: 50vw;
  // margin: auto;
  @media screen and (max-width: 600px) {
    width: 90vw;
  }
}

.land{
  width: 19.8vw;
  @media screen and (max-width: 600px) {
    width: 50vw;
  }
  transition:width 1.5s;
}
.notShow{
  opacity: 0;
  transition:opacity 0.5s;
}

.size-20per {
  width: 50%;
  margin: auto;
  border-radius: 10rem;
  @media screen and (max-width: 600px) {
    width: 80vw;
  }
}

.say{
  font-family: 'TmonMonsori';
  font-size: 4vw;
  color: white;
  @media screen and (max-width: 600px) {
  font-size: 7vw;
    width: 90vw;
  }
}
</style>
