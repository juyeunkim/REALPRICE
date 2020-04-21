<template>
  <v-container class="mt-5">
    <v-card>
      <USER v-for="user in selectedUser" :key="user.email" :user="user" />
      <UserSearch />
    </v-card>/// 입력받은 유저들의 점수를 평균을 내서 결과를 반영할 예정
    <v-btn large color="blue lighten-1 white--text ma-5" rounded>검색하기</v-btn>
  </v-container>
</template>

<script>
import USER from "@/components/realprice/User";
import UserSearch from "@/components/realprice/userSearch";

export default {
  components: {
    USER,
    UserSearch
  },
  computed: {
    selectedUser: function() {
      return this.$store.getters["data/selectedUser"];
    }
  },
  methods: {}
};
</script>

<style>
</style>