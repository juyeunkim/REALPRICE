<template>
  <mdb-card class="wd23">
    
    <mdb-card-image v-if="store.srcUrl!=null" class="imgBox" :src="store.srcUrl" alt="Card image cap" />
    <mdb-card-image v-else class="imgBox" src="https://eatforum.org/content/uploads/2018/05/table_with_food_top_view_900x700.jpg" alt="Card image cap" />
    <div class="rem4">
      <div class="fsize-4">{{ store.storeName }}</div>
      <div class="price-font" style="color:black;">{{ wonDisplay }}</div>
    </div>
  </mdb-card>
</template>

<script>
	import { mdbCard, mdbCardImage, mdbCardBody, mdbCardTitle, mdbCardText } from 'mdbvue';
    
	export default {
		name: 'CardPage',
		components: {
			mdbCard,
			mdbCardImage,
			mdbCardBody,
			mdbCardTitle,
			mdbCardText
		},
        props: {
            store: {
            type: Object,
            default: () => new Object()
        }
        },
        computed:{
            wonDisplay: function() {
                return String(this.store.price).replace(/(\d)(?=(?:\d{3})+(?!\d))/g, '$1,') + '원';
            }
        }
	}
</script>

<style scoped>
@font-face { font-family: 'TmonMonsori'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_two@1.0/TmonMonsori.woff') format('woff'); font-weight: normal; font-style: normal; }

.wd23 {
  width: 20vw;
  height: 25vw;
  margin: 1vw;
  /* width: 18rem;
  margin: 2rem; */
  /* max-width: 18rem; */
}

.fsize-4 {
    font-size: 2vw;
    /* font-size: 2rem; */
}

.rem4 {
    padding-top: 1vw;
    /* padding-bottom: 1vw; */
    /* padding-top: 1.25rem;
    padding-bottom: 1.25rem; */
}

.imgBox {
    height: 15vw;
    /* min-height: 18rem; */
}

div.imgBox > img {
    height: 30vw;
    /* min-height: 18rem; */
}

.price-font {
    font-family: 'TmonMonsori';
    font-size: 3vw;
}
</style>