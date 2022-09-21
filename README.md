##목적
일정 시간 마다 ecs task 최소값을 조정하는 기능

## 환경

- 인프라
  - event-bridge
  - lambda
- 언어
  - serverless.js
  - python

## 실행 방법

- serverless.js 설치
  ```
  npm install -g serverless
  ```
- node_modules 설치

  ```
  npm install
  ```

- deploy
  ```
  serverless deploy
  ```

## 환경 변수

- slackToken
- clusterName
- serviceName
