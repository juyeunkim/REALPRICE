<template>
  <v-container class="mt-5" fill-height>
    <SEARCH />
    <LIST />
  </v-container>
</template>

<script>

import SEARCH from "@/components/realprice/Search";
import LIST from "@/components/realprice/List";
export default {
  components:{
    SEARCH,
    LIST
  },
  
};
</script>