<template>
  <v-row dense>
    <v-col>
      <v-card outlined>
        <v-card>
          <v-card-text>
            {{ content }} 
            <span v-if="!more && content.length>= 50" class="red lighten-4 white--text" @click="viewMore"> 더보기</span>
            <br>
            <v-icon>{{ mdiCalendarMonth }} </v-icon>{{ review.reg_time }}
            <v-icon>{{ mdiStar }} </v-icon> {{ review.score }}
          </v-card-text>
        </v-card>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import { mdiCalendarMonth, mdiStar } from '@mdi/js';
export default {
  props: {
    review: {
      type: Object,
      default: () => new Object()
    }
  },
  data(){
    return {
      mdiCalendarMonth,
      mdiStar,
      more: false
    }
  },
  computed:{
    content: function(){
      if(!this.more) return this.review.content.slice(0, 50);
      else return this.review.content
    }
  },
  methods:{
    viewMore(){
      this.more = true
    }
  }
  
};
</script>

<style>
</style>