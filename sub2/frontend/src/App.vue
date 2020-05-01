<template>
  <v-app id="app">
    <!-- <img class="logo" alt="logo" src="@/assets/logo_white.png"> -->
    <toolbar class="compo" :class="{show: !nowLanding}"/>
    <Landing :class="{notShow: !nowLanding}" v-if="nowLanding2"/>
    <!-- <drawer /> -->
    <route-view class="compo" :class="{show: !nowLanding2}"/>
    <!-- <go-top /> -->
    <Footer class="compo" :class="{show: !nowLanding}"/>
  </v-app>
</template>

<script>
// import Drawer from "@/components/Drawer";
import Toolbar from "@/components/Toolbar";
import RouteView from "@/components/RouteView";
import Footer from "@/components/Footer"
import Landing from "@/views/Landing"
import { mapState, mapActions, mapMutations } from "vuex";

export default {
  components: {
    // Drawer,
    Landing,
    Toolbar,
    RouteView,
    Footer
  },
  data(){
    return {
      nowLanding: true,
      nowLanding2: true,
    }
  },
  computed: {
    ...mapState({
      colorWhite: state => state.data.menuWhite
    })
  },
  mounted(){
    this.landing();
  },
  methods: {
    landing: function(){
      var vm = this;
      setTimeout(function(){
         vm.nowLanding = false;
         setTimeout(function(){
          vm.nowLanding2 = false;
        }, 500);
      }, 4500);
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap');

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  /* height: 100%; */
  background-color: #0F4C82;
}
.bgWhite{
  background-color: white;
}
.compo{
  opacity: 0;
}
.show{
  opacity: 1;
  transition:opacity 0.5s;
}
.notShow{
  opacity: 0;
  transition:opacity 0.5s;
}
</style>