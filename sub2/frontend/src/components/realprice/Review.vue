<template>
  <v-row dense>
    <v-col>
      <v-card outlined>
        <v-card>
          <v-card-text>
            {{ content }} 
            <span v-if="!more && content.length>= 50" class="red lighten-4 white--text" @click="viewMore"> 더보기</span>
            <br>
            <div class="reviewinfo">
              <img class="recommend" src="../../assets/calendar.png"> <strong> {{ review.reg_time }} </strong>
              <img class="recommend" src="../../assets/star.png"> <strong> {{ review.score }} </strong>              
              <img v-if="review.score>=3" class="recommend" src="../../assets/good.png">
              <img v-else class="recommend" src="../../assets/bad.png">
            </div>
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
      more: false,
    }
  },
  computed:{
    content: function(){
      if(!this.more) return this.review.content.slice(0, 50);
      else return this.review.content
    },
  },
  methods:{
    viewMore(){
      this.more = true
    }
  }
  
};
</script>

<style>

.reviewinfo{
  margin-top: 10px;
  
}

.recommend{
  width: 2vw;
}
</style>