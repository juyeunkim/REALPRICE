<template>
    <v-container fill-height fluid grid-list-xl>
      <v-layout justify-center wrap mt-5>
        <v-flex xs12 md8>
          <card title="FAQ">
            <v-form>
              <v-container py-0>
                <v-layout wrap>
                  <v-flex xs12 md12>
                    <v-list two-line>
                      <v-list-item-group
                        v-model="selected"
                        multiple
                        active-class="pink--text"
                      >
                        <template v-for="(item, index) in items">
                          <v-list-item :key="item.title">
                            <template v-slot:default="{ active }">
                              <v-list-item-content>
                                <v-list-item-title v-text="item.title"></v-list-item-title>
                                <div class="text--primary" v-if="active" v-text="item.subtitle"></div>
                              </v-list-item-content>
                            </template>
                          </v-list-item>

                          <v-divider
                            v-if="index + 1 < items.length"
                            :key="index"
                          ></v-divider>
                        </template>
                      </v-list-item-group>
                    </v-list>
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
    storeName: "",
    loading: true,
    selected: [],
  }),
  computed: {
    ...mapState({
      items: state => state.data.faq,
    })
  },
};
</script>