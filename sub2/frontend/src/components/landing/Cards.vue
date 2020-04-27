<template>
  <div class="row px-1">
    <Card v-for="store in stores" v-bind:key="store.id" v-bind:srcUrl="store.srcUrl" v-bind:storeName="store.storeName" v-bind:price="store.price"/>
  </div>
</template>

<script>
	import Card from './Card.vue'
    
	export default {
		name: 'CardPages',
		components: {
			Card
        },
        props: {
            stores: {
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
        // data: () => ({
        //     stores: [{
        //         id:1,
        //         srcUrl: "https://lh3.googleusercontent.com/proxy/8w5ZGjdDSzq6TuQV9_H2NRyu32kvoAuPKZvTUMa59md9QacXywMw-47IaMDhwF3KsalgXUNWp-4m8I5Jba8vbc70Ue2oH5qpsf7uq3G4e0RYq--jtyQPIXsTzGSJDQ3hOgZNb_UAehmRzTydmXh3zXC3HovU-FkxO4WvVJMdVRo5ypNDytswZHH7hmfu58FLoDGcfmVUg-BEGzcnlv2ayl7xoFT0lY2GfyOFwRsJ5XMVT3VlyKmqM6dJuXPJ0bGeeNQJcO4AuUglnTVK_RiEaUoLAUU",
        //         storeName: "이오카츠",
        //         price: "12000"
        //     },
        //     {
        //         id:2,
        //         srcUrl: "https://lh3.googleusercontent.com/proxy/pRYP9x8cQLmLfWM0tg4hIWUq7du4ltSNNYAwo_bkrmndWZTMETfE5JIRdsrK8Lyk266Gicl0Uvq7_xAK3sl5aSSEaBmO106RN_Bz6i_FzhiCKFgnqrg7ZVlHzqeGmW0j8zf1fsiiHK9y5ggRnUxJ4B1a0zjgB991Var9xcKCuK4PETkZNwx8vuvYeTPXtdvMlf2bGw94ChKg5EI9k-OfpXJGYcV_-jD9qPyEoEnsYb34TUAQ4bQEJOQjmqR2gI7XQkOg4w4JVIyg4eIi3VXKcavUmoGTh1fXLm1ZytzaHaOuJvnQHeQ-OMOoxhwnCDSZI7KVBvoYVH57uWrPX0p9ORLxVUtjXCFSwGAAtCKhPvGURPErP5mIDq7KG8vj_lUcwiRlF8SDUqq8s2ndafEIxWY",
        //         storeName: "강남 돈까스",
        //         price: "19870"
        //     },
        //     {
        //         id:3,
        //         srcUrl: "https://t1.daumcdn.net/liveboard/dispatch/6301b06e0bf04496aa2b5d3a980d551c.JPG",
        //         storeName: "가나돈까스의 집",
        //         price: "8000"
        //     },
        //     {
        //         id:4,
        //         srcUrl: "https://lh3.googleusercontent.com/proxy/cagMmlUJNsM3LedW84sTaw9BC4oVZjnM3HQW3PY8lQ95eRKS4EfOxzNXNCaQRTV3FtxfqmkMOL-6YHJhAxdIAtDE9yDmCfLjXd6XvwNsg9p3Fr4DOU0HYAmNlirdRa1quhogKOWcurTAVbYSro-KabBVPE3sXE0D-48kkSWRA2Ht-btQ8YmdEbr5SkM",
        //         storeName: "미나미야마",
        //         price: "21080"
        //     },
        //     {
        //         id:5,
        //         srcUrl: "https://i.pinimg.com/originals/51/6f/51/516f51f23c31837500e6518cd2e00b52.jpg",
        //         storeName: "한성돈까스",
        //         price: "9500"
        //     }]
        // })
	}
</script>

<style scoped>

</style>



