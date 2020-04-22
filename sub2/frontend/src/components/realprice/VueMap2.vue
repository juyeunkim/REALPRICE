<template>
  <div id="map" style="width:100%;height:400px;">

  </div>
</template>

<script>
export default {
    mounted(){
        this.drawMap();
    },
    methods: {
        drawMap: function(){
            var mapOptions = {
                center: new naver.maps.LatLng(37.3595704, 127.105399),
                zoom: 10
            }
            var map = new naver.maps.Map('map', {
                center: new naver.maps.LatLng(37.3595704, 127.105399),
                zoom: 10
            });
        },
    },
}
</script>

<style>

</style>