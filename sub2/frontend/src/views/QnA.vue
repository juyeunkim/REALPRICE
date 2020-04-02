<template>
    <v-container fill-height fluid grid-list-xl>
      <v-layout justify-center wrap mt-5>
        <v-flex xs12 md8>
          <card title="QnA">
            <v-form>
              <v-container py-0>
                <v-layout wrap>
                  <v-flex v-if="!writing" xs12 md12>
                    <v-data-iterator
                      :items="items"
                      :items-per-page.sync="itemsPerPage"
                      :page="page"
                      :search="search"
                      hide-default-footer
                    >
                      <template v-slot:header>
                        <v-toolbar
                          dark
                          color="blue darken-3"
                          class="mb-1"
                        >
                          <v-text-field
                            v-model="search"
                            clearable
                            flat
                            solo-inverted
                            hide-details
                            prepend-inner-icon="search"
                            label="Search"
                          ></v-text-field>
                        </v-toolbar>
                      </template>
                      <template v-slot:default="props">
                        <v-list-item-group
                          v-model="selected"
                          multiple
                        >
                        <template v-for="(item, index) in props.items">
                          <!-- <v-row>
                            <v-col
                              v-for="(item, index) in props.items"
                              :key="item.name"
                              cols="12"
                              sm="6"
                              md="4"
                              lg="3"
                            > -->
                              <v-list-item
                                :key="item.title"
                              >
                                <template v-slot:default="{ active }">
                                  <v-list-item-content>
                                      <v-list-item-title v-text=" item.title"></v-list-item-title>
                                      <div class="text--primary" v-if="active"  v-text="item.question"></div>
                                      <div class="my-5 text--primary" v-if="active"  v-text="item.answer"></div>
                                  </v-list-item-content>

                                  <v-list-item-action>
                                    <v-list-item-action-text v-text="item.writer"></v-list-item-action-text>
                                    <v-row justify="space-around">
                                      <v-icon v-if="item.answer" color="green">mdi-message-reply-text</v-icon>
                                      <v-icon v-if="item.lock" color="orange darken-2">mdi-lock</v-icon>
                                      <v-icon v-if="!item.lock" color="grey lighten-1">mdi-lock-open-variant</v-icon>
                                    </v-row>
                                  </v-list-item-action>
                                </template>
                              </v-list-item>
                              <v-divider
                                v-if="index + 1 < items.length"
                                :key="index"
                              ></v-divider>
                        </template>
                        </v-list-item-group>
                          <!-- </v-col>
                        </v-row> -->
                      </template>

                    </v-data-iterator>
                    <div align="center">
                      <v-pagination
                        class="text-center"
                        v-model="page"
                        :length="numberOfPages"
                      ></v-pagination>
                    </div>
                    <div align="right">
                      <v-btn
                        class="mx-2" fab dark color="primary"
                        @click="writing = !writing"
                      >
                        <v-icon dark>mdi-pencil</v-icon>
                      </v-btn>
                    </div>
                  </v-flex>
                  <v-flex v-if="writing" xs12 md12>
                    <v-text-field
                      label="제목을 입력하세요"
                      v-model="title"
                    ></v-text-field>
                    <v-textarea
                      v-model="question"
                      :auto-grow="true"
                      :clearable="true"
                      rows = 3
                      :solo="true"
                      placeholder="내용을 입력하세요"
                    ></v-textarea>
                    <div align="right">
                      <v-switch
                        v-model="lock"
                        :inset="true"
                        label="비밀 글"
                      ></v-switch>
                    </div>
                    <div align="right">
                      <v-btn
                        class="mx-2" fab dark color="red"
                        @click="writing = !writing"
                      >
                        <v-icon dark>fa-times</v-icon>
                      </v-btn>
                      <v-btn
                        class="mx-2" fab dark color="blue"
                        @click="submit"
                      >
                        <v-icon dark>fa-check</v-icon>
                      </v-btn>
                    </div>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-form>
          </card>
          <v-divider class="mx-4" />
        </v-flex>

      </v-layout>
    </v-container>
</template>

<script>
import Card from "@/components/Card";
import StoreListCard from "@/components/StoreListCard";
import { mapState, mapActions } from "vuex";
export default {
  components: {
    Card,
    StoreListCard
  },
  data: () => ({
    title: "",
    question: "",
    lock: false,
    writing: false,
    storeName: "",
    loading: true,
    selected: [],
    itemsPerPageArray: [4, 8, 12],
    search: '',
    filter: {},
    sortDesc: false,
    page: 1,
    itemsPerPage: 4,
  }),
  computed: {
    ...mapState({
      items: state => state.data.qnaList,
    }),
    numberOfPages () {
      return Math.ceil(this.items.length / this.itemsPerPage)
    },
  },
  methods: {
    ...mapActions("data", ["postQuestion"]),
    submit: function() {
      const params = {
        title: "Q " + this.title,
        writer: "이용자",
        question: this.question,
        lock: this.lock,
      };
      this.postQuestion(params);
      this.writing = !this.writing
    },
  }
};
</script>