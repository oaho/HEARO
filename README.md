# Project : <img src = "https://github.com/AIVLE-School-Third-Big-Project/Big_project_3_9/assets/124108607/9ccd7bd2-54e3-4789-b3be-c0f1f3a533a0" width="3%"></img>Hear-o(실시간 위험 상황 감지 자동 신고 서비스)
**HEAR On-call** : 서비스가 응급 상황을 감지하면 해당 응급 상황에 대처할 수 있는 대상을 호출하거나 알림을 보내는 역할을 나타냄

## Description

위급 상황 발생 시 안전 확보가 어려운 1인가구의 증가와 범죄에 노출되기 쉬운 여성,아동 등 사회적 취약계층을 겨냥한 범죄가 증가함에 따라 개인의 안전 확보의 중요성이 부각되고 있다.
이에 따라 예상치 못한 위급 상황 발생 시 스스로 안전 확보가 어려운 모든 국민들을 보호하기 위해 인공지능 모델을 활용하여 실시간으로 음성 및 주변음향을 분석, 위급 상황으로 판단될 때 자동으로 구조 요청을 하는 어플리케이션이다.
위급 상황을 유형별로 분류하여 각 유형에 맞게 기관에 신고한다.

### class

|**번호**|**유형**|**신고**|
|:------:|---|---|
|0|일반 상황(실내, 실외)||
|1|치안 안전(강제추행, 강도범죄, 절도범죄, 폭력범죄)|112|
|2|갇힘|119|
|3|전기사고|119|
|4|가스사고|119|
|5|화재|119|
|6|응급의료|119|
|7|안전사고(낙상,붕괴)|119|
|8|일반 도움요청|119|

## Dataset

[**AI HUB**](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=170) 에 공개된 위급상황 음성/음향 데이터 35만여개 중 5만개를 추출하여 사용

### 위급 상황 음성/음향 데이터
    - 성별 : 남성, 여성
    - 연령대 : 유아, 청소년, 노인, 기타
    - 상황 : 치안안전, 소방안전, 자연재해, 사고활동, 일반(위급), 일반(정상)
### 위급 상황 AI 학습용 데이터셋
    - 16개 클래스(중분류)1,000건 이상의 상황‧3,500시간
    - 음성/음향 단일 데이터셋, 음성/음향 복합 데이터셋

## Model : BEATs

[**BEATs**](https://github.com/microsoft/unilm/tree/master/beats)는 Audio classification 과제에서 음소 시퀀스로 인해 쉽게 얻을 수 없었던 음향 토크나이저의 문제를 SSL(self-supervised learning)모델의 반복적인 학습으로 해결한 모델이다. 또한 [**ESC-50 dataset**](https://paperswithcode.com/sota/audio-classification-on-esc-50)에서 98.1% 정확도를 보이는 SOTA 모델인 audio pretrained framework BEATs를 Pretrained model로 사용하여 Fine-Tuning 하였다.<br>
![chart (1)](https://github.com/AIVLE-School-Third-Big-Project/Big_project_3_9/assets/124108607/1c5a554a-1d27-41fe-99d6-03c896ff47cd)<br>
**위험 상황 음향 데이터 약 5만개를 사용하여 학습한 결과 약 95% 정확도를 예상할 수 있다.**
