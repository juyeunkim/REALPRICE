<template>
  <v-row dense>
    <v-col cols="10">
      <v-card outlined>
        <v-card>
          <v-card-text>
            <v-avatar size="30">
              <v-img class="card-img" src="https://cdn.vuetifyjs.com/images/john.jpg" />
            </v-avatar>
            {{ review.content.slice(0, 50) }} ...
            <span class="red lighten-4 white--text">더보기</span>
            <br />
            작성일 : {{ review.reg_time }}
            <p>평점 : {{ review.score }}</p>
          </v-card-text>
        </v-card>
      </v-card>
    </v-col>
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