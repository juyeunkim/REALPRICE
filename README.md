# **Real Price** - SSAFY Bigdata project 

## **INDEX**
1. [기획 의도](#기획-의도)
1. [테스트](#테스트)
1. [사용 메뉴얼](#사용-메뉴얼)
1. [팀 구성](#팀-구성)
1. [개발 노트](#개발-노트)
1. [회의록](#회의록)
1. [메타데이터](#메타데이터)
1. [기술스택](#기술스택)
1. [사용 툴](#사용-툴)

## **기획 의도**

 ### Background

> - 가성비
>
> 가격이 저렴하고 맛집이라고 알려진 'A음식점'
>
> 하지만 현재 위치에서 가는 비용, 시간을 따져보면 .. 글쎄? 저렴하지 않는것 같은데 ..
>
> > 가성비 대비 맛집은 어디일까?
>
> - 선호도
>
> 누구에게나 음식점을 선택하는 기준이 다르다.
>
> A 는 '맛이 가장 중요한 우선순위이고 B는  '가격' C는 '위치' 이다
>
> > 나의 선호도를 반영한 맞춤형 맛집은 어디일까?

 ###  Purpose

> 사용자 **선호**에 맞춘 **가성비** 맛집을 추천하자

 ###  Target

> 1. 약속 잡으려는 사람들
> 2. 맞춤 음식점을 추천 받고싶은 사람

 ###  Our Service

> - 맛집 추천 **(메인 기능)**
>
>   > [기준]
>   >
>   > > - 거리
>   > > - 가격
>   > > - 맛
>   >
>   > 3가지 기준 중에서 우선순위를 선택하면 맞춤형 음식첨을 추천한다
>   >
>   > [사용자]
>   >
>   > > - 혼자서 음식점 고르기 ( 개인 취향 )
>   > > - 여러명이서 음식점 고르기 ( 다양한 취향을 분석 )
>
> - 개인 취향 (음식 필터링)
>
>   > 개인정보 등록시, 회원정보 입력하면 해당 음식은 제외한 결과를 보여준다
>
> - 리뷰 (만족도)
>
>   > 음식점을 다녀온 후 만족도를 작성
>   >
>   > 예상 비용과 실제 비용 비교를 통해 신뢰도를 제공한다.

## **테스트** 

 - Web Site Address
    http://i02a206.p.ssafy.io 
 - User
   
   > ID : tester@gmail.com  
   >
   > PASSWORD : !1q2w3e4r



## **사용 메뉴얼**

현재 위치를 입력받고 가격, 맛, 거리 별 중요도를 선택한다



## **팀 구성**

#### [FRONT]

> **김주연** @juyeunkim
>
> **전경윤** @kingjky

#### [BACK]

> **박정환** @hwxnii
>
> **정구헌** @honeion

#### [DATA]

>  **백창현** @Baek

## **개발 노트**

> [SUB1 정리](sub1/SUB1정리.md)  
> SUB2 부터는 기본기능을 제외하고는 계획한 프로젝트 설계에 맞게 진행함

## **회의록**

 - Zoom을 활용해서 회의함
   - 아이디어 회의 및 스켈레톤 코드 체크 **[0323(월)](meetingLog/0323(월).md)**
   - 아이디어 피드백에 따른 주제 선정 및 서비스와 기능 정의 **[0326_목](meetingLog/0326(목).md)**
   - 데이터 관련 회의 및 Sub2 과제 시작 **[0331_화](meetingLog/0331(화).md)**
   - 데이터 활용 기준 회의 **[0406_월](meetingLog/0406(월).md)** 
   - 현재 진행사항 및 금주 진행 예정 사항 공유 **[0407_화](meetingLog/0407(화).md)**

## **메타데이터**

## **기술스택**
![vue](https://img.shields.io/badge/vue-4.3.0-blue?logo=Vue.js)![javascript](https://img.shields.io/badge/javascript-es6-yellowgreen?logo=javascript)
![django](https://img.shields.io/badge/django-2.2.7-yellow?logo=django)
![html](https://img.shields.io/badge/html-html5-red?logo=html5)![css](https://img.shields.io/badge/css-css3-red?logo=css3)
![mysql](https://img.shields.io/badge/mysql-8.0.19-success?logo=mysql)

## **사용 툴**

- Visual Studio Code 
- MySQL Workbench
- git(git bash) / gitlab(lab.ssafy.com) / jira (jira.ssafy.com)