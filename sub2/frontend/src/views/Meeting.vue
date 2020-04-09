<template>
  <v-container class="mt-5">
    <v-card>
      <USER />
      <USER />
      <v-btn large color="blue lighten-1 white--text ma-5" rounded @click="addUser">유저 추가하기</v-btn>
    </v-card>

    /// 입력받은 유저들의 점수를 평균을 내서 결과를 반영할 예정
    <v-btn large color="blue lighten-1 white--text ma-5" rounded>검색하기</v-btn>
  </v-container>
</template>

<script>

import USER from "@/components/realprice/User";
export default {
  components: {
    USER,
  },
  data(){
    return{
      users:[]
    }
  },
  methods:{
    addUser(){
      // 버튼 눌렀을때 유저 추가 화면 나와야함
      // modal? 
    }
  }
  
};
</script>

<style>
</style>