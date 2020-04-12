<template>
  <!-- MODAL START -->
  <v-dialog v-model="dialog" persistent max-width="500px">
    <template v-slot:activator="{ on }">
      <v-btn large color="blue lighten-1 white--text ma-5" rounded dark v-on="on">유저 추가하기</v-btn>
    </template>
    <v-card>
      <v-card-title>
        <span class="headline">유저 검색</span>
      </v-card-title>
      <v-card-text>
        <v-container grid-list-md>
          <v-layout wrap>
            <v-flex xs12>
              <v-text-field label="Email" />
            </v-flex>
          </v-layout>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer />
        <v-btn large color="blue lighten-1 white--text ma-5" rounded @click.native="dialog = false">닫기</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
  <!-- <v-btn large color="blue lighten-1 white--text ma-5" rounded @click="addUser">유저 추가하기</v-btn> -->
  <!-- MODAL END-->
</template>

<script>
export default {
  data() {
    return {
      dialog: false
    };
  }
};
</script>

<style>
</style>