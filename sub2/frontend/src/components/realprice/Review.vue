<template>
  <v-card outlined max-width="400">
    <v-card-text>
      <v-avatar size="30">
        <v-img class="card-img" src="https://cdn.vuetifyjs.com/images/john.jpg" />
      </v-avatar>
      {{ review.content.slice(0, 50) }} ...
      <span class="red lighten-4 white--text">더보기</span>
      <br />
      {{ review.reg_time }}
      <br />
      {{ review.score }}
      <br />
    </v-card-text>
  </v-card>
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