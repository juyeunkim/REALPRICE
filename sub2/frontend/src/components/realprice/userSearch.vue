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
              <v-text-field v-model="email" label="Email을 입력해주세요" />
            </v-flex>
            <div v-if="email != ''">
              <div v-for="e in filteredList" :key="e.email" class="card">
                <button @click="addChips(e)">{{ e.email }}</button>
              </div>
            </div>
          </v-layout>
        </v-container>
      </v-card-text>
      {{ chips }}
      <v-card-actions>
        <v-spacer />
        <v-btn
          large
          color="blue lighten-1 white--text ma-5"
          rounded
          @click="addUser"
        >추가</v-btn>
        <v-btn
          large
          color="blue lighten-1 white--text ma-5"
          rounded
          @click.native="dialog = false"
        >닫기</v-btn>
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
      dialog: false,
      email: "",
      chips:[],
      selected:[],
    };
  },
  computed: {
    userList: function() {
      return this.$store.getters["data/users"];
    },
    filteredList() {
      return this.userList.filter(list => {
        return list.email.toLowerCase().includes(this.email.toLowerCase());
      });
    }
  },
  created() {
    this.$store.dispatch("data/getUsers");
  },
  methods:{
    addUser(){
      this.$store.dispatch("data/selectedUser", this.selected)
      // this.$store.state.selectedUser  = this.chips
      // console.log(this.$store.state.selectedUser)
      this.$alert("유저 추가 성공", "Success", "success");
      this.dialog = false;
      //// 유저가 추가 될 수 있도록
    },
    addChips(e){
      if(!this.chips.includes(e.email)) {
        this.chips.push(e.email)
        this.selected.push(e)
      }
      else {
        var index = this.chips.indexOf(e.email);
        if (index !== -1) {
          this.chips.splice(index, 1);
          this.selected.splice(index, 1);
        }
      }
    }
  }
};
</script>

<style>
</style>