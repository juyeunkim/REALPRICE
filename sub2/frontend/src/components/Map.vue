<template>
<div>
    <div v-if="this.positions">{{this.positions.length}}</div>
    <div id="map"/>
</div>
</template>

<script>
export default {
    props: {
        restaurants: {
            type: Array,
            default: function(){
                return []
            },
        },
        user: {
            type: Object,
            default: {
                latitude: 33.450705,
                longitude: 126.570677,
            },
        },
    },
    date(){
        return {
        }
    },
    computed: {
        positions() {
            return this.restaurants;
        },
        point(){
            return this.user;
        },
    },
    mounted(){
        this.drawMap(this.positions);
    },
    updated(){
        this.drawMap(this.positions);
    },
    methods: {
        drawMap(positions){
            var container = document.getElementById('map'); //지도를 담을 영역의 DOM 레퍼런스
            var options = { //지도를 생성할 때 필요한 기본 옵션
                center: new kakao.maps.LatLng(this.point.latitude, this.point.longitude), //지도의 중심좌표.
                level: 5 //지도의 레벨(확대, 축소 정도)
            };

            var map = new kakao.maps.Map(container, options); //지도 생성 및 객체 리턴
            
            var markerPosition  = new kakao.maps.LatLng(this.point.latitude, this.point.longitude); 
            // 마커를 생성합니다
            var marker = new kakao.maps.Marker({
                map: map,
                position: markerPosition
            });

            // 마커 이미지의 이미지 주소입니다
            var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png"; 
                
            for (var i = 0; i < positions.length; i ++) {
                
                // 마커 이미지의 이미지 크기 입니다
                var imageSize = new kakao.maps.Size(24, 35); 
                
                // 마커 이미지를 생성합니다    
                var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize); 

                // 마커를 생성합니다
                var marker = new kakao.maps.Marker({
                    map: map, // 마커를 표시할 지도
                    position: new kakao.maps.LatLng(positions[i].latitude, positions[i].longitude), // 마커를 표시할 위치
                    title : positions[i].store_name, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
                    image : markerImage // 마커 이미지 
                });

            }
        }
    }
}
</script>

<style lang="scss">
#map {
    height: calc(60vw - 260px);
    width: 100%;
    // height: calc(60vw - 260px);
    // width: calc(100vw - 260px);
    @media screen and (max-width: 900px) {
        height: 60vw;
        width: 100%;
    }
}
.wrap {position: absolute;left: 0;bottom: 40px;width: 288px;height: 132px;margin-left: -144px;text-align: left;overflow: hidden;font-size: 12px;font-family: 'Malgun Gothic', dotum, '돋움', sans-serif;line-height: 1.5;}
.wrap * {padding: 0;margin: 0;}
.wrap .info {width: 286px;height: 120px;border-radius: 5px;border-bottom: 2px solid #ccc;border-right: 1px solid #ccc;overflow: hidden;background: #fff;}
.wrap .info:nth-child(1) {border: 0;box-shadow: 0px 1px 2px #888;}
.info .title {padding: 5px 0 0 10px;height: 30px;background: #eee;border-bottom: 1px solid #ddd;font-size: 18px;font-weight: bold;}
.info .close {position: absolute;top: 10px;right: 10px;color: #888;width: 17px;height: 17px;background: url('https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/overlay_close.png');}
.info .close:hover {cursor: pointer;}
.info .body {position: relative;overflow: hidden;}
.info .desc {position: relative;margin: 13px 0 0 90px;height: 75px;}
.desc .ellipsis {overflow: hidden;text-overflow: ellipsis;white-space: nowrap;}
.desc .jibun {font-size: 11px;color: #888;margin-top: -2px;}
.info .img {position: absolute;top: 6px;left: 5px;width: 73px;height: 71px;border: 1px solid #ddd;color: #888;overflow: hidden;}
.info:after {content: '';position: absolute;margin-left: -12px;left: 50%;bottom: 0;width: 22px;height: 12px;background: url('https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/vertex_white.png')}
.info .link {color: #5085BB;}
</style>