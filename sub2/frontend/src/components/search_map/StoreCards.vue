<template>
  <div class="cards">
      <v-skeleton-loader
        ref="skeleton"
        :boilerplate="false"
        type="list-item-avatar-three-line"
        :tile="false"
        height="20vh"
        :loading="loading"
        transition="fade-transition"
        class="mx-auto"
      >
        <div>
          <StoreCard class="card" v-for="store in stores" :key="store.id" :store="store" @clickItem="selectItem"/>
          <!-- <v-btn depressed large color="normal" @click="$emit('next')">More...</v-btn> -->
          <!-- <v-btn
          class="mx-2"
          fab dark color="#0F4C82"
          > -->
          <v-btn class="btn" block color="#0F4C82" dark
            @click="$emit('next')"
            v-if="(stores.length < total)">
            <v-icon dark>mdi-plus</v-icon>
          </v-btn>
        </div>
      </v-skeleton-loader>
      <div v-if="isSearched && !(this.stores.length > 0)">
        <img class="no-result" alt="logo" src="@/assets/crying.png">
        <p class="no-result-font">해당 금액으로 먹을 수 있는 메뉴가 없습니다.</p>
      </div>
  </div>
</template>

<script>
import StoreCard from './StoreCard.vue'
  
export default {
  name: 'StoreCards',
  components: {
    StoreCard
  },
  props: {
    stores: {
        type: Array,
        default: function(){
            return [];
        },
    },
    total: {
        type: Number,
        default: 0,
    },
    isSearched: {
        type: Boolean,
        default: false,
    }
  },
  computed: {
    loading(){
      if(this.stores.length > 0 || (this.isSearched)){
        return false;
      } else{
        return true;
      }
    },
    storeList() {
        return this.stores;
    }
  },
  methods: {
    selectItem(id) {
      this.$emit("clickItem", id);
    },
    hoverItem(id){
      this.$emit("hover", id);
    },
    outItem(){
      this.$emit("out");
    }
  }
}
</script>

<style lang="scss" scoped>
.no-result{
  width: 2vw;
  margin: 0.3vw;
}
.no-result-font{
  font-size:0.7vw;
}
.card{
  @media screen and (max-width: 600px) {
    display: inline-block;
    width: 30vw;
    height: 40vw;
    margin-right: 5vw;
  }
}
.btn{
  @media screen and (max-width: 600px) {
    // position: fixed;
    margin-top: 10vw;
    display: flex;
    float: right;
  }
}
</style>
