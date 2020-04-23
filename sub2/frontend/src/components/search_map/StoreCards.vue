<template>
  <div>
    <StoreCard v-for="store in stores2" v-bind:key="store.id" v-bind:srcUrl="store.srcUrl" v-bind:storeName="store.storeName" v-bind:price="store.price" v-bind:percent="store.percent"/>
  </div>
</template>

<script>
	import StoreCard from './StoreCard.vue'
    
	export default {
		name: 'StoreCards',
		components: {
			StoreCard
        },
        props: {
            stores2: {
                type: Array
            }
        },
        // data: () => ({
        //     storesData: {
        //         id:String,
        //         srcUrl: String,
        //         storeName: String,
        //         price: String
        //     }
        // }),
        // watch: {
        //     sotore(stores){
        //         this.storesData = stores
        //     }
        // }
        data: () => ({
            stores2: [{
                id:1,
                srcUrl: "https://lh3.googleusercontent.com/proxy/-oyyAgFrUNxAafWB9DU0UhQOaSsj5xK9-3_RlCAyNrChORri7y7HWNPysCRqA8yLcSbWFgzvgqgF7pR60yZZTvcr5xMImbo_4Zr2b1LnHbGmEzlh1h0t6mLwssBr9vQoQELpi-nnzS-IZEpgUcdrnKUHLtYVL_C-Z4pMNmIFO4bsXO7gCFiqvZMTby61exbtq0CNUDqjRofJim0fMsO-Bm4mt6poD4_dM-3dTH87myNa8BtjWQPgxS6fVGDodCZ1in2zjKZIWiC6cEgl1KmTEpHLiVg",
                storeName: "이오카츠",
                price: "12000",
                percent: "76"
            },
            {
                id:2,
                srcUrl: "https://lh3.googleusercontent.com/proxy/jS4i5cCRSEEU74hs1nExlt22sBl4pikpf8dhc8rjoLWwwZNbzpsHWCdQCYKTzddIbwWJH1P7eu0WJ94hHe9WwdqrQwCzy3sOd12t9aS-EPoqV2cwg_T19EO8s011dj4R-F5Sxna0ML6UkOqEvSKVDpFhr9cLxKoGmdb7OT1mCM0g1hFVKY2pR97xAIpPk7uRYXPxNKlhm9e-ah_uP3doNTr16lg15FhchLtwH5RIRo0Egv1hjIqdX67sz6B5jqjvvC8QnnFV_pyQWr62LwfgKvL6RL76BgxTlL-dDyffSR-CIfjScxHkRHlQFiVFmH1JJtsZ5srFT8LJSwj38b1JNChLOQMeAQkzbSTz6QyEKXngMc8bFx5ahommRJhI06limBLQxe23OR4kyFxicMF8JV0",
                storeName: "강남 돈까스",
                price: "19870",
                percent: "74"
            },
            {
                id:3,
                srcUrl: "https://t1.daumcdn.net/liveboard/dispatch/6301b06e0bf04496aa2b5d3a980d551c.JPG",
                storeName: "가나돈까스의 집",
                price: "8000",
                percent: "70"
            },
            {
                id:4,
                srcUrl: "https://lh3.googleusercontent.com/proxy/B-sE-Sggpv8A1cP9yLsA1tp9deiJS0z91a-NPiggDZlfGikJQfNgmtlt65W2Fvlr_y1BU6nndBbhiOKC9iot-b_ebZFRvrk6_apUOBqO0QwMmXKOlU4Cldq9rvIvsraMTmnPgn3VaaGOIHuruPldp2Ha_qXHpf3Pk5eFriGwXwhbCYt6FgHEzNVcOug",
                storeName: "미나미야마",
                price: "21080",
                percent: "68"
            },
            {
                id:5,
                srcUrl: "https://i.pinimg.com/originals/51/6f/51/516f51f23c31837500e6518cd2e00b52.jpg",
                storeName: "한성돈까스",
                price: "9500",
                percent: "66"
            }]
        })
	}
</script>


