<template>
<div>
    <div id="map"/>
</div>
</template>

<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=eac48c3548025ce4e0b61b1512b4282c"></script>

<script>
export default {
    props: {
    },
    mounted(){
        this.drawMap();
    },
    methods: {
        drawMap(){
            var container = document.getElementById('map');
            var options = {
                center: new kakao.maps.LatLng(33.450701, 126.570667),
                level: 3
            };

            var map = new kakao.maps.Map(container, options);
        }
    }
}
</script>

<style lang="scss">
#map {
    height: calc(60vw - 20.5vw);
    width: 100%;
    // height: calc(60vw - 260px);
    // width: calc(100vw - 260px);
    @media screen and (max-width: 900px) {
        height: 60vw;
        width: 100%;
    }
}

</style>