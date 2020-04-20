<template>
  <v-container class="mt-5" fill-height>
    <v-card-text class="text-center">
      <p class="display-2 pa-5">테스트도 식후경</p>
      <p class="display-3 pa-2">🍱🍜🥡</p>
      <p class="display-3 pa-2">🍰🍔</p>
    </v-card-text>
    <v-btn
      color="primary"
      dark
      @click.stop="dialog = true"
    >
      Open Dialog {{selectedNum}}
    </v-btn>
    <v-dialog
      v-model="dialog"
      max-width="290"
    >
      <STOREDETAIL @close="dialog = false"/>
    </v-dialog>
    <LIST
      :restaurants="this.SearchRealPrice"
    />
  </v-container>
</template>

<script>
import STOREDETAIL from '@/components/realprice/StoreDetail';
import LIST from "@/components/realprice/List";
import { mapState, mapActions } from "vuex";
export default {
  components: {
    STOREDETAIL,
    Map,
    LIST,
  },
  data () {
    return {
      dialog: false,
      selectedNum: 100,
    }
  },
  computed: {
    ...mapState({
      SearchRealPrice: state => state.data.searchRealPrice,
    })
  },
  methods: {
    
  },
}
</script>