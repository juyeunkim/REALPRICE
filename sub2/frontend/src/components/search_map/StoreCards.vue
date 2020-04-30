<template>
  <div>
    <div v-if="!(stores.length > 0)">
      <v-skeleton-loader
        ref="skeleton"
        :boilerplate="false"
        type="list-item-avatar-three-line"
        :tile="false"
        height="20vh"
        class="mx-auto"
      ></v-skeleton-loader>
      <v-skeleton-loader
        ref="skeleton"
        :boilerplate="false"
        type="list-item-avatar-three-line"
        :tile="false"
        height="20vh"
        class="mx-auto"
      ></v-skeleton-loader>
      <v-skeleton-loader
        ref="skeleton"
        :boilerplate="false"
        type="list-item-avatar-three-line"
        :tile="false"
        height="20vh"
        class="mx-auto"
      ></v-skeleton-loader>
      <v-skeleton-loader
        ref="skeleton"
        :boilerplate="false"
        type="list-item-avatar-three-line"
        :tile="false"
        height="20vh"
        class="mx-auto"
      ></v-skeleton-loader>
    </div>
    <div v-if="(stores.length > 0)">
      <StoreCard v-for="store in stores" :key="store.id" :store="store" @clickItem="selectItem"/>
      <!-- <v-btn depressed large color="normal" @click="$emit('next')">More...</v-btn> -->
      <!-- <v-btn
      class="mx-2"
      fab dark color="#0F4C82"
      > -->
      <v-btn block color="#0F4C82" dark
      @click="$emit('next')" v-if="(stores.length < total)">
        <v-icon dark>mdi-plus</v-icon>
      </v-btn>
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
    }
  },
  computed: {
    storeList() {
        return this.stores;
    }
  },
  methods: {
    selectItem(id) {
      this.$emit("clickItem", id);
    }
  }
}
</script>


