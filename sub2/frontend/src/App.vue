<template>
  <v-app id="app">
    <toolbar />
    <img class="logo" alt="logo" src="@/assets/logo_white.png">
    <!-- <drawer /> -->
    <route-view />
    <!-- <go-top /> -->
    <Footer />
  </v-app>
</template>

<script>
// import Drawer from "@/components/Drawer";
import Toolbar from "@/components/Toolbar";
import RouteView from "@/components/RouteView";
import GoTop from "@/components/GoTop";
import Footer from "@/components/Footer"

export default {
  components: {
    // Drawer,
    Toolbar,
    RouteView,
    GoTop,
    Footer
  },
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
</style>