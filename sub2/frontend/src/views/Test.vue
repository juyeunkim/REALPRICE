<template>
  <v-container class="mt-5" fill-height>
    <v-card-text class="text-center">
      <p class="display-2 pa-5">테스트도 식후경</p>
      <p class="display-3 pa-2">🍱🍜🥡</p>
      <p class="display-3 pa-2">🍰🍔</p>
    </v-card-text>
  </v-container>
</template>

<script>

import { mapState, mapActions } from "vuex";
export default {
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