# DISLODGED BACKEND 💡

팀 ETT의 TTS 기술을 활용한 가상보이스 위로 전달 웹서비스🎧💽<br>

![Vector (2)](https://github.com/ETT-DISLODGED/.github/assets/110734087/eaa1b6ad-4ef0-4a84-a38a-10b8ca2a7e2a)



<br>
<br>


## 목차
- [문제정의 및 해결책(Background)](#문제정의)
  <br>
- [시작가이드(How to Build/Install)](#시작가이드)
  <br>
- [프로젝트타임라인 및 팀원소개(Timeline)](#프로젝트타임라인)
  <br>
- [스택(Stack)](#스택)
  <br>
- [서비스구조(Architecture & User flow)](#서비스구조)
  <br>
- [기능소개](#전체기능리스트)
  <br>
- [포스터와 데모영상(Poster & Demo video)](#포스터)

<br>
<br>

---

<br>

## 문제정의 
1. 많은 현대인들이 현실에서 다양한 고민을 솔직하게 표출하는 것에 어려움을 겪고 있는 것과 익명 커뮤니티의 높은 이용률을 확인
<img src="https://github.com/ETT-DISLODGED/.github/assets/110734087/c6e21341-d0a8-44d3-ae70-4d778b17a308"  width="800" >

<br>

2.기존 텍스트 기반 위로의 한계점 파악 
<br>
- 가독성 저하 등 위로에 대한 방해 요소 존재
- 대면 소통에 비해 감정 전달이 어려워 유저들이 고립감을 느끼기 쉬움.
<br>
<br>

## 해결책 
- 논문을 통해 ‘목소리’ 가 사람의 정서에 미치는 높은 영향력을 파악<br> → 텍스트와 ‘보이스 위로’를 함께 전하는 색다른 해결책 제안 <br>
<img src="https://github.com/ETT-DISLODGED/.github/assets/110734087/4cf7914a-8410-4262-b98d-d72d072acefc"  width="800" >

<br>
<br>


## 시작가이드 

### (1) 개발 환경
- Django v4.1 
- React v18.2.0


<br>



### (2) 백 실행방법(Installation) - 제출한 ZIP 파일 다운 

```
$ source myvenv/Scripts/activate
$ cd dislodged_project
$ pip install -r requirements.txt
$ python manage.py runserver

```


<br>

### (3) Try w/ test account

- ID : dislodged
- PW : 1234
<br>
*처음부터 서비스를 사용하고 싶다면 회원가입부터 진행


<br>


## 스택

<br>

### Environment
<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=for-the-badge&logo=Visual Studio Code&logoColor=white"> <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"> <img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white">



### Config
<img src="https://img.shields.io/badge/Yarn-2C8EBB?style=for-the-badge&logo=Yarn&logoColor=white">


### Development
<img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css&logoColor=white"> <img src="https://img.shields.io/badge/JS-F7DF1E?style=for-the-badge&logo=JS&logoColor=white"> <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=React&logoColor=white"> <img src="https://img.shields.io/badge/Django-2496ED?style=for-the-badge&logo=Django&logoColor=white"> <img src="https://img.shields.io/badge/AmazonS3-569A31?style=for-the-badge&logo=Amazon S3&logoColor=white"> <img src="https://img.shields.io/badge/Github Actions-2088FF?style=for-the-badge&logo=Github Actions S3&logoColor=white"> <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white"> <img src="https://img.shields.io/badge/Material UI-007FFF?style=for-the-badge&logo=Material UI&logoColor=white">



### API
<img src="https://img.shields.io/badge/Google TTS-6380E5?style=for-the-badge&logo=Google TTS&logoColor=white">

### Communtication & Tool
<img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white"> <img src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=Figma&logoColor=white"> <img src="https://img.shields.io/badge/Google Meet-00897B?style=for-the-badge&logo=Google Meet&logoColor=white">

<br>
<br>






## 프로젝트타임라인

📅2023.09 - 2024.06

|기간|내용|
|----|---|
|2023.09~2023.11| 아이디에이션 및 설문조사 진행|
|~2024.1 |서비스 세부 기능 확정 및 UI 설계|
|~2024.3|추천 기능 제외 서비스 개발 완료|
|~2024.5|모든 기능 구현 완료 및 배포 진행|
|2024.6.7|졸업 발표 진행|

<br>
<br>

## 팀원소개 - ETT 💛

|팀원|역할|이메일|💛|
|----|---|----|---|
|최유미|Backend|jain53791226@gmail.com| ![유미](https://github.com/ETT-DISLODGED/.github/assets/110734087/fbdc2a81-3220-4fcc-a208-a07fa6bf5e97) |

from 이화여대 컴퓨터공학과

<br>



## 서비스구조

- 서비스 전체구조도

<img src="https://github.com/ETT-DISLODGED/.github/assets/110734087/f2c30a70-12c4-4c4a-a2f2-0582888c9257"  width="600" >
<br>
<br>

- 유저 플로우 차트
<img src="https://github.com/ETT-DISLODGED/.github/assets/110734087/d9b1538b-86a1-41de-bdc7-2c2f36ab9c1b"  width="600" >

<br>
<br>




## 전체기능리스트 
<br>

<img src="https://github.com/ETT-DISLODGED/.github/assets/110734087/d875e3f9-7f94-4ea9-9b0b-580c9160de0e"  width="800" >



<br>
<br>

## 주요 기능 로직 및 UI 소개 ⭐
<br>

(1) 내 게시글의 댓글들 모아듣기 기능
<br>

<img src="https://github.com/ETT-DISLODGED/.github/assets/110734087/939a5dd7-666b-4efc-853e-d3421658804b"  width="800" >

<br>

(2) 유저별 맞춤 가상 보이스 추천 기능
<br>

<img src="https://github.com/ETT-DISLODGED/.github/assets/110734087/ca2c7814-3762-40d4-bdd9-e1767a83388b"  width="800" >

<br>
<br>

## 포스터
<br>
*캡스톤디자인 포스터세션에 제출했던 포스터입니다.

<br>

<img src="https://github.com/ETT-DISLODGED/.github/assets/110734087/2339438d-130e-4aee-8291-d1271b8c3f03"  width="700" >

<br>

## 데모영상 ▶️
<br>

[DISLODGED 데모 영상 시청하러 가기](https://www.youtube.com/watch?v=E3e9SRJPGZM)

<br>
<br>
