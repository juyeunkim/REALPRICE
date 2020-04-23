<template>
  <v-row dense>
    <v-card outlined>
      <v-card max-width="400">
        <v-card-text>
          <v-avatar size="30">
            <v-img class="card-img" src="https://cdn.vuetifyjs.com/images/john.jpg" />
          </v-avatar>
          {{ review.content.slice(0, 50) }} ...
          <span class="red lighten-4 white--text">더보기</span>
          <p>작성일 : {{ review.reg_time }}</p>
          <p>평점 : {{ review.score }}</p>
        </v-card-text>
      </v-card>
      <v-card max-width="200">
        <v-card-text>
          <div>Word of the Day</div>
          <p class="display-1 text--primary">be•nev•o•lent</p>
          <p>adjective</p>
          <div class="text--primary">
            well meaning and kindly.
            <br />"a benevolent smile"
          </div>
        </v-card-text>
      </v-card>
    </v-card>
  </v-row>
</template>

<script>
export default {
  props: {
    review: {
      type: Object
    }
  }
};
</script>

<style>
</style>