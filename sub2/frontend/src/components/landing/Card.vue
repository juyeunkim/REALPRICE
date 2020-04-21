<template>
  <mdb-card class='wd23'>
    <mdb-card-image class="imgBox" :src="srcUrl" alt="Card image cap"></mdb-card-image>
    <mdb-card-body class="rem4">
      <mdb-card-title class="fsize-4">{{ storeName }}</mdb-card-title>
      <mdb-card-text class="price-font" style="font-size:2.5rem; color:black;">{{ wonDisplay }}</mdb-card-text>
    </mdb-card-body>
  </mdb-card>
</template>

<script>
	import { mdbCard, mdbCardImage, mdbCardBody, mdbCardTitle, mdbCardText } from 'mdbvue';
    
	export default {
		name: 'CardPage',
        props: {
            srcUrl: String,
            storeName: String,
            price: String
        },
		components: {
			mdbCard,
			mdbCardImage,
			mdbCardBody,
			mdbCardTitle,
			mdbCardText
		},
        computed:{
            wonDisplay: function() {
                return this.price.replace(/(\d)(?=(?:\d{3})+(?!\d))/g, '$1,') + '원';
            }
        }
	}
</script>

<style scoped>
@font-face { font-family: 'TmonMonsori'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_two@1.0/TmonMonsori.woff') format('woff'); font-weight: normal; font-style: normal; }

.wd23 {
  width: 18rem;
  margin: 2rem;
  max-width: 18rem;
}

.fsize-4 {
    font-size: 2rem;
}

.rem4 {
    padding-top: 1.25rem;
    padding-bottom: 1.25rem;
}

.imgBox {
    min-height: 18rem;
}

div.imgBox > img {
    min-height: 18rem;
}

.price-font {
    font-family: 'TmonMonsori';
}
</style>