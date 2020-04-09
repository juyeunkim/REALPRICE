<template>
  <v-container class="mt-5" fill-height>
    <v-card class="text-center">
      <p class="display-3 pa-2">💸💵💰</p>
      <p class="display-2 pa-5">REAL PRICE</p>
      <SEARCH @aa="bb" />
    </v-card>
    <LIST />
  </v-container>
</template>

<script>
import SEARCH from "@/components/realprice/Search";
import LIST from "@/components/realprice/List";
export default {
  components: {
    SEARCH,
    LIST
  },
  
  methods:{
    bb(){
      console.log('B')
    },
    search(){
      console.log(realPrice)
    }
  }
};
</script>