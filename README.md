# Determining Avoidance path Autonomous Driving Robot Software

회피경로 판단 자율주행 로봇 소프트웨어 (Determining Avoidance path Autonomous Driving Robot Software)

지정된 미션을 완수하는 자율주행 로봇 소프트웨어. 주행 중에 방해물을 인식하면 회피 경로를 판단해서 이동한다.

![](/images/SRA-MPSR-ADR-introduction(h).gif)

서울로봇아카데미에서 진행한 자율주행 경진대회(핑크랩 주관)에서 1등을 수상하였다.

![](/images/SRA-MPSR-ADR-Presentation1.jpg)
(발표 당시 사진)

![](/images/SRA-MPSR-ADR-Prize1.jpg)
(민형기 박사님과 한컷 ^^)

![](/images/SRA-MPSR-ADR-Prize2.png)
(상장과 고퀄리티의 상품)


## 소프트웨어 구조

![](/images/SRA-MPSR-ADR-Architecture1.png)

- Robotics SW in Laptop
- Pinklab_minibot_robot
- Same ROS_DOMAIN_ID


## 주요 기능

- 지정된 미션 달성 (Mission Accomplishment)
- 물체 인식 (Object Recognition)
- 회피 경로 판단 (Avoidance path Determination)


### 미션 설명

1. A, B, C, D 지역으로 구분되는 맵 만들기
2. A 지점에서 출발한 로봇이 B 지점에 도착하면 오른쪽을 보게 만들기
	- 오른쪽의 기준은 로봇이 주행하던 방향 기준으로 대략 90도
3. 2번 완료 후, C 지점으로 이동시키고 도착 후에는 한 바퀴 회전하기
4. 3번 완료 후, D 지점으로 이동하여 미션 완료

- 중간에 장애물이 발생하는 상황에 적절하게 대처하며 진행
	- ex. 장애물 인식 시 잠시 멈추었다 회피하여 가기 등

### 맵과 의사코드(Pseudo Code)

![](/images/SRA-MPSR-ADR-map-pseudo-code1.jpg)


## 작동 방법

- 라즈베리파이에서 로봇(미니봇) 기동
```bash
ros2 launch minibot_bringup bringup_robot.launch.py
```

- Laptop에서 Navigation 실행
```bash
ros2 launch minibot_navigation2 bringup_launch.py map:=`ros2 pkg prefix minibot_navigation2`/share/minibot_navigation2/maps/<map-name>.yaml
```

- 회피경로 판단 자율주행 소프트웨어 실행
	- https://github.com/refigo/SRA-MPSR/blob/main/mission/DAP_AD_Robot.py
```bash
(venv) python3 DAP_AD_Robot.py
```


## 사용 기술

- ROS2
- Navigation2
- OpenCV
- YOLO
- Python


## 작동 영상 & 발표 자료

### 작동 영상

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/CBDW2zIgzkc/0.jpg)](https://www.youtube.com/watch?v=CBDW2zIgzkc)

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/Tdbis9xDE4c/0.jpg)](https://www.youtube.com/watch?v=Tdbis9xDE4c)


### 발표 자료

- [발표_PDF](https://drive.google.com/file/d/1J01boAPUOi5oCoNPTHGVJpkkqi3rjGjF/view)


## Contact

Mijong Go - dev.mijonggo@gmail.com

