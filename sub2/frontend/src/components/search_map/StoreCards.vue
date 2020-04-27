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
                srcUrl: "https://t1.daumcdn.net/liveboard/dispatch/6301b06e0bf04496aa2b5d3a980d551c.JPG",
                storeName: "이오카츠",
                price: "12000",
                percent: "76"
            },
            {
                id:2,
                srcUrl: "https://t1.daumcdn.net/liveboard/dispatch/6301b06e0bf04496aa2b5d3a980d551c.JPG",
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
                srcUrl: "https://t1.daumcdn.net/liveboard/dispatch/6301b06e0bf04496aa2b5d3a980d551c.JPG",
                storeName: "미나미야마",
                price: "21080",
                percent: "68"
            },
            {
                id:5,
                srcUrl: "https://t1.daumcdn.net/liveboard/dispatch/6301b06e0bf04496aa2b5d3a980d551c.JPG",
                storeName: "한성돈까스",
                price: "9500",
                percent: "66"
            }]
        })
	}
</script>


