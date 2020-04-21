<template>
  <v-app id="app">
    <toolbar />
    <drawer />
    <route-view />
    <go-top />
  </v-app>
</template>

<script>
import Drawer from "@/components/Drawer";
import Toolbar from "@/components/Toolbar";
import RouteView from "@/components/RouteView";
import GoTop from "@/components/GoTop";

export default {
  components: {
    Drawer,
    Toolbar,
    RouteView,
    GoTop
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap');

</style>