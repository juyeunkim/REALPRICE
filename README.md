# **Real Price** - SSAFY Bigdata project 

## **기술스택**

![vue](https://img.shields.io/badge/vue-4.3.0-blue?logo=Vue.js)![javascript](https://img.shields.io/badge/javascript-es6-yellowgreen?logo=javascript)
![django](https://img.shields.io/badge/django-2.2.7-yellow?logo=django)
![html](https://img.shields.io/badge/html-html5-red?logo=html5)![css](https://img.shields.io/badge/css-css3-red?logo=css3)
![mysql](https://img.shields.io/badge/mysql-8.0.19-success?logo=mysql)

## 테스트 

 - Web Site Address
   http://i02a206.p.ssafy.io 

 - User

   > ID : tester@gmail.com  
   >
   > PASSWORD : !1q2w3e4r

- [HowToRun](HowToRun.md)

## INDEX

1. [기획 의도](#기획-의도)
1. [사용 메뉴얼](#사용-메뉴얼)
1. [팀 구성](#팀-구성)
1. [개발 노트](#개발-노트)
1. [회의록](#회의록)
1. [메타데이터](#메타데이터)
1. [사용 툴](#사용-툴)

## **기획 의도**

 ### Background

- 가성비

" 주머니에 있는 5천원으로 먹을 수 있는 맛집이 있을까? "

지갑에 돈도 없고,, 멀면 교통비도 내야하지만..
맛있는 음식점을 먹고 싶어 !

> 가성비 대비 맛집은 어디일까?



 ###  Purpose

> 사용자 **원하는 금액**에 맞춘 **가성비** 맛집을 추천하자



 ###  Target

1. 약속 잡으려는 사람들
2. 맞춤 음식점을 추천 받고싶은 사람



 ###  Our Service

- 맛집 추천 **(메인 기능)**

  1. 메뉴 모드
     가격을 입력하면, 메뉴로 음식점 추천

     > 메뉴가 포함된 음식점 리스트 + 상세페이지 확인

  2. 지도 모드
     가격을 입력하면, 지도 반경 내 음식점 추천

     > 평점, 메뉴, 교통비, 가격이 포함된 음식점 리스트 + 상세페이지 확인

     - 지도 위치 조정
       지도 크기를 조정하여 재검색

     - 태그 기능
       원하는 태그를 통해 음식점 필터링

  3. 음식점 상세페이지

     - 음식점의 정보 + 음식 가격과 교통비 확인
     - 가격 내에 먹을 수 있는 메뉴 확인
     - 실제 음식점을 다녀간 사람들의 리뷰 만족도 및 리뷰 확인

  




## **사용 메뉴얼**

1. 메인 화면에서 가격을 입력

   1.1 음식점 클릭시, 상세페이지 이동

2. 지도 모드를 선택하여 가격을 입력

   2.1 지도 크기를 조정하여 다시 검색
   2.2 태그를 선택하여 음식점 필터링
   2.3 음식점 클릭시, 상세페이지 이동

   

## **Our Team**

#### [FRONT]

> **김주연** @juyeunkim
>
> **전경윤** @kingjky
>
> **백창현** @Baek

#### [BACK]

> **박정환** @hwxnii
>
> **정구헌** @honeion
>
> **백창현** @Baek

## **개발 노트**


> [SUB1 정리](sub1/SUB1정리.md)  
> SUB2 부터는 기본기능을 제외하고는 계획한 프로젝트 설계에 맞게 진행함
>
> [김주연_개발노트](개발노트.md)

## **회의록**

 - Zoom을 활용해서 회의함
   - 아이디어 회의 및 스켈레톤 코드 체크 **[0323(월)](meetingLog/0323(월).md)**
   - 아이디어 피드백에 따른 주제 선정 및 서비스와 기능 정의 **[0326_목](meetingLog/0326(목).md)**
   - 데이터 관련 회의 및 Sub2 과제 시작 **[0331_화](meetingLog/0331(화).md)**
   - 데이터 활용 기준 회의 **[0406_월](meetingLog/0406(월).md)** 
   - 현재 진행사항 및 금주 진행 예정 사항 공유 **[0407_화](meetingLog/0407(화).md)**
   - 알고리즘, 기능 수정 및 UI 회의 **[0421_화](meetingLog/0421(화).md)**
   -  서비스의 기능 수정  **[0423_목](meetingLog/0423(목).md)**
    -  서비스 문제점 개선 **[0424_금](meetingLog/0424(금).md)**
   

## **메타데이터**



## **사용 툴**

- Visual Studio Code 
- MySQL Workbench
- git(git bash) / gitlab(lab.ssafy.com) / jira (jira.ssafy.com)