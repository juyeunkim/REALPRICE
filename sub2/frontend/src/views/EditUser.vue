<template>
  <div>
    <v-container fluid>
      <v-layout row wrap>
        <v-flex xs12 md6 offset-md3>
          <v-card>
            <v-toolbar color="indigo" dark>
              <v-toolbar-title>회원정보 수정</v-toolbar-title>
            </v-toolbar>
            <v-card-text>
              <span class="title">Personal Info</span>

              <!-- 이메일 -->
              <v-text-field
                v-model="email"
                :rules="emailRules"
                class="mt-5"
                label="Email"
                required
                readonly
              />

              <!-- 비밀번호 -->
              <v-text-field
                v-model="password"
                :rules="[() => password.length > 0 || 'This field is required']"
                label="Password"
                class="mt-5"
                required
                type="password"
              />

              <!-- 비밀번호 다시 -->
              <!-- <v-text-field
                v-model="password1"
                :rules="[() => password1.length > 0 || 'This field is required']"
                label="Password 확인"
                class="mt-5"
                required
                type="password"
              />-->

              <!-- 이름 -->
              <v-text-field v-model="name" :rules="nameRules" label="Name" class="mt-5" required />

              <!-- 휴대폰 번호 -->
              <v-text-field v-model="phone" :rules="phoneRules" label="휴대폰" class="mt-5" required />

              <!-- 주소 -->
              <v-text-field
                v-model="address"
                :rules="[() => address.length > 0 || 'This field is required']"
                label="주소"
                class="mt-5"
                required
              />

              <!-- 취향 -->
              <!-- TODO : 추가로 입력받을수 있도록 -->
              <v-select
                v-model="tags"
                :items="items"
                label="싫어하는 음식(재료)를 선택해주세요"
                chips
                multiple
                tags
              />

              <!-- </v-select> -->
            </v-card-text>

            <v-divider class="mt-5" />
            <v-card-actions>
              <!-- <v-btn flat>Cancel</v-btn> -->
              <v-spacer />
              <v-btn color="primary" @click="submit">수정</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import Axios from "axios";
export default {
  data: () => ({
    // 회원정보
    email: "test",
    password: "",
    password1: "",
    name: "test",
    phone: "010-000-0000",
    tag: "",
    address: ""
  }),
  methods: {
    submit() {
      // 회원가입으로 넘어감

      if (
        this.email != "" &&
        this.password != "" &&
        this.born_year != "" &&
        this.name != "" &&
        this.phone != "" &&
        this.gender != ""
      ) {
        var data = {
          email: this.email,
          password: this.password,
          profile: {
            gender: this.gender,
            born_year: this.born_year,
            name: this.name,
            address: this.address,
            phone: this.phone,
            tag: this.tag
          }
        };

        console.log(data);
        // Axios
    //     Axios.post("/api/users/", data)
    //       .then(res => {
    //         console.log(res);
    //         this.$alert("회원가입 성공", "Success", "success");
    //       })
    //       .catch(exp => {
    //         console.log("실패");
    //         this.$alert("회원가입 실패", "Warning", "warning");
    //       });
    //   } else {
    //     this.$alert("항목을 모두 입력해주세요", "Warning", "warning");
      }

      // TODO : 어떤 페이지로 넘어가는지
    }
  }
};
</script>

<style>
</style>