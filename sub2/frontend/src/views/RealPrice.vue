<template>
  <v-container class="mt-5" fill-height>
    <v-layout column>
      <v-flex>
        <v-card class="text-center">
          <p class="display-3 pa-2">💸💵💰</p>
          <p class="display-2 pa-5">REAL PRICE</p>
          <SEARCHFORM />
        </v-card>
      </v-flex>
      <v-flex>
        <v-btn
          color="primary"
          dark
          @click.stop="dialog = true"
        >
          Open Dialog
        </v-btn>
        <v-dialog
          v-model="dialog"
          max-width="700"
        >
          <STOREDETAIL :store="selectedStore" @close="closeDetail" />
        </v-dialog>
        <v-layout row>
          <v-flex xs8>
            <Map :restaurants="RealPriceList" :user="multicampus" @clickItem="selectItem"/>
          </v-flex>
          <v-flex xs4>
            <LIST :restaurants="RealPriceList" @clickItem="selectItem" />
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import STOREDETAIL from '@/components/realprice/StoreDetail';
import SEARCHFORM from "@/components/realprice/SearchForm";
import LIST from "@/components/realprice/List";
import Map from "@/components/Map";
import { mapState, mapActions, mapMutations } from "vuex";

export default {
  components: {
    STOREDETAIL,
    SEARCHFORM,
    LIST,
    Map
  },
  data() {
    return {
      selectedStore: null,
      dialog: false,
      multicampus: {
        latitude: 37.50128969810118,
        longitude: 127.03960183847694,
      }
    }
  },
  computed: {
    ...mapState({
      RealPriceList: state => state.data.realPriceList,
    })
  },
  destroyed() {
      this.clearRealPrice();
  },
  methods:{
    ...mapMutations("data", ["clearRealPrice"]),
    selectItem: function(id){
      
      this.RealPriceList.forEach(el => {
        if(el.id == id){
          this.selectedStore = el;
        }
      });
      
      this.dialog = true;
    },
    getReviews(){
      consol.log('!!!')
      this.$store.dispatch("data/getReviews", this.selectedStore.id);
    },
    closeDetail(){
      dialog = false;
      this.selectedStore = null;
    }
  },
};
</script>