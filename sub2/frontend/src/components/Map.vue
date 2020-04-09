<template>
<div>
    <!-- <div>안녕하세요 나는 지도에요</div> -->
    <div id="map" style="width:700px;height:500px;" />
</div>
</template>

<script>
export default {
    props: {
        restaurants: {
            type: Array,
            default: function(){
                return [
                    {
                        title: 'A',
                        lat: 33.450705,
                        lng: 126.570677,
                    },
                    {
                        title: 'B', 
                        lat: 33.450936,
                        lng: 126.569477,
                    },
                    {
                        title: 'C', 
                        lat: 33.450879,
                        lng: 126.569940,
                    },
                    {
                        title: 'D',
                        lat: 33.451393,
                        lng: 126.570738,
                    }
                ]
            },
        },
        user: {
            type: Object,
            default: {
                lat: 33.450705,
                lng: 126.570677,
            },
        },
        // fullWidth: {
        //     type: Boolean,
        //     default: false
        // },
        // offset: {
        //     type: [Number, String],
        //     default: 24
        // },
        // title: {
        //     type: String,
        //     default: undefined
        // }
    },
    date(){
        return {
            maptest: 1,
        }
    },
    computed: {
        
    },
    mounted(){
        this.drawMap();
    },
    methods: {
        drawMap(){
            var container = document.getElementById('map'); //지도를 담을 영역의 DOM 레퍼런스
            var options = { //지도를 생성할 때 필요한 기본 옵션
                center: new kakao.maps.LatLng(this.user.lat, this.user.lng), //지도의 중심좌표.
                level: 4 //지도의 레벨(확대, 축소 정도)
            };

            var map = new kakao.maps.Map(container, options); //지도 생성 및 객체 리턴
            
            var markerPosition  = new kakao.maps.LatLng(this.user.lat, this.user.lng); 
            // 마커를 생성합니다
            var marker = new kakao.maps.Marker({
                map: map,
                position: markerPosition
            });


            var positions = this.restaurants;

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
                    position: new kakao.maps.LatLng(positions[i].lat, positions[i].lng), // 마커를 표시할 위치
                    title : positions[i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
                    image : markerImage // 마커 이미지 
                });
            }
        }
    }
}
</script>

<style>

</style>