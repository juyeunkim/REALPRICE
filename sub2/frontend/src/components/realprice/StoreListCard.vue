<template>
  <!-- <v-card>
    <v-card-text class="text-center">
      <p class="display-1 font-weight-bold">{{ name }}</p>
      <p class="subtitle-1 font-italic">{{ tags }}</p>
    </v-card-text>
    <v-footer color="white">
      <v-col class="text-center">
        <span class="grey--text caption font-italic">{{ address }} / 📞 {{ tel }}</span>
      </v-col>
    </v-footer>
  </v-card>
   -->
    <v-card
      color="white"
      @click="clickItem()"
    >
      <div class="d-flex flex-no-wrap justify-space-between">
        <div>
          <v-card-title
            class="headline blue--text text--darken-4 font-weight-bold"
            v-text="name"
          ></v-card-title>

          <v-card-subtitle class="yellow--text text--accent-4 font-weight-bold" v-text="'평점 ' + avg_score"></v-card-subtitle>
          <v-card-text class="blue--text text--darken-4 font-weight-bold">
            {{avg_price}} 
            <v-icon small>fas fa-won-sign</v-icon>
          </v-card-text>
        </div>
        <v-avatar
          class="pa-3"
          size="125"
          tile
        >
          <v-img src="https://teamtech24.com/foodhati/foodhatiAdmin/assets/img/foodimg/default-food-image.jpg"></v-img>
          <!-- <v-img src="https://cdn.vuetifyjs.com/images/cards/halcyon.png"></v-img> -->
        </v-avatar>

      </div>
    </v-card>
</template>

<script>
export default {
  props: {
    id: {
      type: Number,
      default: ""
    },
    name: {
      type: String,
      default: ""
    },
    categories: {
      type: Array,
      default: () => new Array()
    },
    address: {
      type: String,
      default: ""
    },
    tel: {
      type: String,
      default: ""
    },
    avg_score: {
      type: Number,
      default: 0,
    },
    avg_price: {
      type: Number,
      default: 0,
    },
  },
  computed: {
    tags: function() {
      return this.categories.reduce((acc, v) => {
        return `${acc} #${v}`;
      }, "");
    }
  },
  methods: {
    clickItem(){
      this.$emit('clickItem',this.id);
    }
  }
};
</script>
