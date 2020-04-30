<template>
  <v-content>
    <div id="app-view" style="height: 100%;">
      <v-fade-transition mode="out-in">
        <router-view />
      </v-fade-transition> 
    </div>
  </v-content>
</template>
<script>
import { mapMutations } from "vuex";
export default {
  created() {
    // console.log('routeView created');
    this.clearState();
  },
  destroyed() {
    // console.log('routeView destroyed');
  },
  methods: {
    ...mapMutations("data", ["clearState"]),
  }
}
</script>