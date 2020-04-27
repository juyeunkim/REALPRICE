<template>
<div>
    <div v-show="false">{{positions.length}}</div>
    <div v-show="false">{{point.latitude}}</div>
    <div v-show="false">{{point.longitude}}</div>
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
        this.drawMap(this.positions, this.point);
    },
    updated(){
        this.drawMap(this.positions, this.point);
    },
    methods: {
        drawMap(positions, point){
            const vm = this;

            var container = document.getElementById('map'); //지도를 담을 영역의 DOM 레퍼런스
            var options = { //지도를 생성할 때 필요한 기본 옵션
                center: new kakao.maps.LatLng(point.latitude, point.longitude), //지도의 중심좌표.
                level: 5 //지도의 레벨(확대, 축소 정도)
            };

            var map = new kakao.maps.Map(container, options); //지도 생성 및 객체 리턴
            
            var markerPosition  = new kakao.maps.LatLng(point.latitude, point.longitude); 
            
            var imageSize = new kakao.maps.Size(24, 35); 
            var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png"; 
            var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize); 
            // 마커를 생성합니다
            var marker = new kakao.maps.Marker({
                map: map,
                position: markerPosition,
                image : markerImage
            });
                
            for (var i = 0; i < positions.length; i ++) {

                // 마커를 생성합니다
                var marker = new kakao.maps.Marker({
                    map: map, // 마커를 표시할 지도
                    position: new kakao.maps.LatLng(positions[i].latitude, positions[i].longitude), // 마커를 표시할 위치
                });

                // 인포윈도우에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다
                var iwContent =
                `<div id="small"><div>${positions[i].store_name}</div><div class="price-font">${positions[i].avg_price}</div></div>`;

                // 인포윈도우를 생성합니다
                var infoWindow = new kakao.maps.InfoWindow({
                    content : iwContent,
                    disableAutoPan : true,
                });
                
                


                kakao.maps.event.addListener(marker, 'click', makeClickListener(positions[i].id));
                kakao.maps.event.addListener(marker, 'mouseover', makeOverListener(map, marker, infoWindow));
                kakao.maps.event.addListener(marker, 'mouseout', makeOutListener(map, marker, infoWindow));

            }
            const m = document.getElementById('map');
            const w = m.getBoundingClientRect().width;
            const h = m.getBoundingClientRect().height;
            const r = (w>h? h/16 : w/16) * (Math.pow(2,map.getLevel()));

            var circle = new kakao.maps.Circle({
                map: map,
                center : new kakao.maps.LatLng(this.point.latitude, this.point.longitude),
                radius: r,
                strokeWeight: 2,
                strokeColor: 'red',
                strokeOpacity: 0.8,
                strokeStyle: 'dashed',
                fillColor: 'blue',
                fillOpacity: 0.1 
            });
            vm.$emit('drawCircle', circle.getPosition(), r);


            kakao.maps.event.addListener(map, 'zoom_changed', zoomChanged(map, circle));
            kakao.maps.event.addListener(map, 'bounds_changed', boundsChanged(map, circle));

            function makeClickListener(id) {
                return function() {
                    vm.$emit('clickItem', id);
                    // console.log('mouseClick ' + i)
                };
            }
            function makeOverListener(map, marker, infowindow) {
                return function() {
                    infowindow.open(map, marker);
                };
            }
            function makeOutListener(map, marker, infowindow) {
                return function() {
                    infowindow.close();
                };
            }
            function zoomChanged(map, circle) {
                return function() {
                    var center = map.getCenter();
                    var level = map.getLevel();

                    // console.log(level);
                    var mapObj = document.getElementById('map');
                    var width = mapObj.getBoundingClientRect().width;
                    var height = mapObj.getBoundingClientRect().height;

                    var radius = (width>height? height/16 : width/16) * (Math.pow(2,level));
                    // var radius = 28.125 * (Math.pow(2,level));

                    circle.setPosition(center);
                    circle.setRadius(radius);
                    circle.setMap(map);

                    vm.$emit('drawCircle', center, radius);
                };
            }
            function boundsChanged(map, circle) {
                return function() {
                    var center = map.getCenter();
                    var level = map.getLevel();

                    var mapObj = document.getElementById('map');
                    var width = mapObj.getBoundingClientRect().width;
                    var height = mapObj.getBoundingClientRect().height;

                    // circle.setPosition(center);
                    var radius = (width>height? height/16 : width/16) * (Math.pow(2,level));

                    circle.setPosition(center);
                    circle.setRadius(radius);
                    circle.setMap(map);

                    vm.$emit('drawCircle', center, radius);
                };
            }
        }
    }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap');
@font-face { font-family: 'TmonMonsori'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_two@1.0/TmonMonsori.woff') format('woff'); font-weight: normal; font-style: normal; }
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
.price-font {
    font-family: 'TmonMonsori';
}
#small{
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    // border: solid 1px red;
    width: 150px;
    text-align: center;
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