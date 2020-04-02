<template>
  <v-container fluid>
    <card title="QnA">
    <v-data-iterator
      :items="items"
      :items-per-page.sync="itemsPerPage"
      :page="page"
      :search="search"
      :sort-by="sortBy.toLowerCase()"
      :sort-desc="sortDesc"
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
          <template v-if="$vuetify.breakpoint.mdAndUp">
            <v-spacer></v-spacer>
            <v-select
              v-model="sortBy"
              flat
              solo-inverted
              hide-details
              :items="keys"
              prepend-inner-icon="search"
              label="Sort by"
            ></v-select>
            <v-spacer></v-spacer>
            <v-btn-toggle
              v-model="sortDesc"
              mandatory
            >
              <v-btn
                large
                depressed
                color="blue"
                :value="false"
              >
                <v-icon>mdi-arrow-up</v-icon>
              </v-btn>
              <v-btn
                large
                depressed
                color="blue"
                :value="true"
              >
                <v-icon>mdi-arrow-down</v-icon>
              </v-btn>
            </v-btn-toggle>
          </template>
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
                      <div class="text--primary" v-if="active"  v-text="item.answer"></div>
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

      <template v-slot:footer>
        <v-row class="mt-2" align="center" justify="center">
          <span class="grey--text">Items per page</span>
          <v-menu offset-y>
            <template v-slot:activator="{ on }">
              <v-btn
                dark
                text
                color="primary"
                class="ml-2"
                v-on="on"
              >
                {{ itemsPerPage }}
                <v-icon>mdi-chevron-down</v-icon>
              </v-btn>
            </template>
            <v-list>
              <v-list-item
                v-for="(number, index) in itemsPerPageArray"
                :key="index"
                @click="updateItemsPerPage(number)"
              >
                <v-list-item-title>{{ number }}</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>

          <v-spacer></v-spacer>

          <span
            class="mr-4
            grey--text"
          >
            Page {{ page }} of {{ numberOfPages }}
          </span>
          <v-btn
            fab
            dark
            color="blue darken-3"
            class="mr-1"
            @click="formerPage"
          >
            <v-icon>mdi-chevron-left</v-icon>
          </v-btn>
          <v-btn
            fab
            dark
            color="blue darken-3"
            class="ml-1"
            @click="nextPage"
          >
            <v-icon>mdi-chevron-right</v-icon>
          </v-btn>
        </v-row>
      </template>
    </v-data-iterator>
    </card>
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
  data () {
    return {
      selected: [],
      itemsPerPageArray: [4, 8, 12],
      search: '',
      filter: {},
      sortDesc: false,
      page: 1,
      itemsPerPage: 4,
      sortBy: 'name',
      keys: [
        'Name',
        'Calories',
        'Fat',
        'Carbs',
        'Protein',
        'Sodium',
        'Calcium',
        'Iron',
      ],
    }
  },
  computed: {
    numberOfPages () {
      return Math.ceil(this.items.length / this.itemsPerPage)
    },
    filteredKeys () {
      return this.keys.filter(key => key !== `Name`)
    },
    ...mapState({
      items: state => state.data.qnaList,
    })
  },
  methods: {
    nextPage () {
      if (this.page + 1 <= this.numberOfPages) this.page += 1
      this.selected = []
    },
    formerPage () {
      if (this.page - 1 >= 1) this.page -= 1
      this.selected = []
    },
    updateItemsPerPage (number) {
      this.itemsPerPage = number
    },
  },
}
</script>