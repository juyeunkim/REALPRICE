<template>
  <mdbCard class="wd23" @click.native="selectItem()">
    
    <mdbCardImage v-if="store.srcUrl!=null" class="imgBox" :src="store.srcUrl" alt="Card image cap" />
    <mdbCardImage v-else class="imgBox" :src="require('@/assets/logo_ver1.png')" alt="Card image cap" />
    <mdbCardBody class="rem4">
      <mdbCardTitle class="fsize-4">{{ store.storeName }}</mdbCardTitle>
      <div class="price-font" style="color:black;">{{ wonDisplay }}</div>
    </mdbCardBody>
  </mdbCard>
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
            // return String(this.store.price).replace(/(\d)(?=(?:\d{3})+(?!\d))/g, '$1,') + '원';
            return String(this.store.price + this.store.distanceCost).replace(/(\d)(?=(?:\d{3})+(?!\d))/g, "$1,") + "원";
        }
    },
    methods: {
        selectItem() {
            this.$emit("clickItem", this.store.id);
        }
    }
}
</script>

<style lang="scss" scoped>
@font-face { font-family: 'TmonMonsori'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_two@1.0/TmonMonsori.woff') format('woff'); font-weight: normal; font-style: normal; }

.wd23 {
  width: 20vw;
  height: 25vw;
  margin: 1vw;
  position: static;
  /* width: 18rem;
  margin: 2rem; */
  /* max-width: 18rem; */
    .fsize-4 {
        font-size: 2vw;
        /* padding-bottom: 1vw; */
        /* font-size: 2rem; */
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
        padding-top: 1vw;
    }
    @media screen and (max-width: 500px) {
        position: relative;
        width: 90vw;
        height: 25vw;
        .imgBox {
            position: absolute;
            width: 25vw;
            height: 25vw;
            /* min-height: 18rem; */
        }
        div.imgBox > img {
            height: 30vw;
            // min-height: 18rem;
        }
        .fsize-4 {
            position: absolute;
            top: 5vw;
            left: 40vw;
            font-size: 5vw;
            /* padding-bottom: 1vw; */
            /* font-size: 2rem; */
        }
        .price-font {
            position: absolute;
            top: 15vw;
            left: 40vw;
            font-size: 6vw;
            padding-top: 1vw;
        }
    }
}


</style>