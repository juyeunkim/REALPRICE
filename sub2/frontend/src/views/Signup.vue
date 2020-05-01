<template>
  <div>
    <v-container fluid>
      <v-layout row>
        <v-flex xs12 md6 offset-md3>
          <v-card>
            <v-toolbar color="indigo" dark>
              <v-toolbar-title>회원 가입</v-toolbar-title>
            </v-toolbar>
            <v-card-text>
              <span class="title">Personal Info</span>

              <!-- 이메일 -->
              <v-text-field
                v-model="email"
                :rules="emailRules"
                label="Email을 입력하세요"
                class="mt-5"
                required
                @keyup.enter="submit"
              />
              <v-btn color="primary" @click="checkEmail">이메일 중복체크</v-btn>

              <!-- 비밀번호 -->
              <v-text-field
                v-model="password"
                :rules="[() => password.length > 0 || 'This field is required']"
                label="Password을 입력하세요"
                class="mt-5"
                required
                type="password"
                @keyup.enter="submit"
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
              <v-text-field
                v-model="name"
                :rules="nameRules"
                label="Name을 입력하세요"
                class="mt-5"
                required
                @keyup.enter="submit"
              />

              <!-- 성별 -->
              성별
              <v-radio-group v-model="gender" row>
                <v-radio label="남자" value="남" @keyup.enter="submit" />
                <v-radio label="여자" value="여" />
              </v-radio-group>

              <!-- 태어난날 -->
              <v-select v-model="born_year" :items="years" label="출생년도" @keyup.enter="submit" />

              <!-- 휴대폰 번호 -->
              <v-text-field
                v-model="phone"
                :rules="phoneRules"
                label="010-0000-0000"
                class="mt-5"
                required
                @keyup.enter="submit"
              />

              <!-- 주소 -->
              <v-text-field
                v-model="address"
                :rules="[() => password.length > 0 || 'This field is required']"
                label="주소를 입력하세요"
                class="mt-5"
                required
                @keyup.enter="submit"
              />

              <!-- 취향 -->
              <v-combobox
                v-model="tags"
                :items="items"
                hide-selected
                hint="리스트에 없다면 추가해주세요"
                label="싫어하는 음식(재료)를 선택해주세요"
                multiple
                persistent-hint
                small-chips
              >
                <template v-slot:no-data>
                  <v-list-item>
                    <v-list-item-content>
                      <v-list-item-title>
                        음식을 추가하고
                        <kbd>enter</kbd> 를 눌러주세요
                      </v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </template>
              </v-combobox>

            </v-card-text>

            <v-divider class="mt-5" />
            <v-card-actions>
              <!-- <v-btn flat>Cancel</v-btn> -->
              <v-spacer />
              <v-btn color="primary" @click="submit">회원가입</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import api from "../api/index";
export default {
  data: () => {
    return {
      // 기본 정보
      years: ["1989", "1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997"],
      items: ["오이", "고수", "민트"],
      tags: [], // 선택한 취향
      
      // 유효성 검사
      nameRules: [
        v => !!v || "Name is required",
        v => v.length <= 10 || "Name must be less than 10 characters"
      ],
      emailRules: [
        v => !!v || "E-mail is required",
        v =>
          /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) ||
          "E-mail must be valid"
      ],
      phoneRules: [
        v => !!v || "Phone is required",
        v =>
          /^[0-9]{3}-([0-9]{3}|[0-9]{4})-[0-9]{4}$/.test(v) ||
          "Phone must be valid"
      ],

      // 회원정보
      email: "",
      password: "",
      password1: "",
      born_year: "",
      name: "",
      phone: "",
      gender: "",
      tag: "",
      address: ""
    };
  },
  watch: {
    // password1: function() {
    //   this.checkPw();
    // },
    tags: function() {
      this.test();
    }
  },
  methods: {
    test() {
      this.tag = this.tags.toString();
      console.log(this.tag);
    },
    checkPw() {
      // 비밀번호 일치하는지 체크
      if (this.password != this.password1) {
        this.nameRules;
        console.log(this.password1);
      }
    },
    submit() {
      // 회원가입으로 넘어감
      this.tag = this.tags.toString();
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
          username: this.name,
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

        api
          .signup(data)
          .then(res => {
            console.log(res);
            this.$alert("회원가입 성공", "Success", "success");
            this.$router.push("/");
          })
          .catch(exp => {
            console.log(exp);
            this.$alert("회원가입 실패", "Warning", "warning");
          });
      } else {
        this.$alert("항목을 모두 입력해주세요", "Warning", "warning");
      }
    },
    checkEmail(){
      api.checkUsedEmail(this.email)
        .then(res=>{
          if(res.data.status=='204')
            this.$alert("사용가능한 이메일입니다", "Success", "success");
          else if(res.data.status=='200')
            this.$alert("이미 사용중인 이메일입니다", "Warning", "warning");
        })
        .catch(exp=>{
          this.$alert("올바른 이메일을 작성해주세요", "Warning", "warning");
        })
    }
  }
};
</script>

<style>
</style>