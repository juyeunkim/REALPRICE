<template>
  <div class="storeDetail">
      <v-card>
            <v-card-title class="headline">{{store.store_name}} {{store.avg_score}}</v-card-title>

            <v-card-text>
              주소: {{store.address}}<br>
              전화번호: {{store.tel}}<br>
              카테고리: {{store.category}}<br>
              평균가격: {{store.avg_price}}<br>
              평균평점: {{store.avg_score}}<br>
              
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>

              <v-btn
                color="green darken-1"
                text
                @click="emitClose"
              >
                닫기
              </v-btn>
            </v-card-actions>
          </v-card>
  </div>
</template>

<script>
export default {
  props: {
      store: {
          type: Object,
          default: () => new Object(),
      },
  },
  computed: {
    tags: function() {
      return this.store.categories.reduce((acc, v) => {
        return `${acc} #${v}`;
      }, "");
    }
  },
  methods: {
      emitClose: function () {
          this.$emit('close')
      }
  },
}
</script>

<style>

</style>