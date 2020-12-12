# 외부 패키지에 대한 연습 문제

## 개요

이 섹션에서는 동영상에서 배운 개념을 연습할 수 있는 기회가 주어집니다. 먼저, 여러분이 유념해야 할 핵심 개념들을 검토해보십시오. 그런 다음 아래의 연습문제를 보십시오.

기억하십시오, 이것들은 여러분의 이익을 위한 것입니다. 만약 여러분이 특정한 연습이 가치가 없다고 발견되거나 너무 오랫동안 걸려있다면, 그것들을 건너뛰어도 좋습니다.

## 핵심개념

### requirements.txt
외부 패키지를 사용하는 애플리케이션으로 작업 할 때 실행하는 데 필요한 패키지를 전달해야합니다. `requiements.txt` 파일로 이 작업을 수행합니다 . 예는 다음과 같습니다:

```
colorama
prompt_toolkit
```

가상 환경이 활성화되면 다음 명령을 사용하여 모든 종속성을 설치할 수 있습니다.

```
(env) C:\> pip install -r requirements.txt
```

###  가상환경

가상 환경은 컴퓨터에 동일한 라이브러리의 여러 버전이 공존하는 데있어 핵심입니다. 다음과 같이 만듭니다.
#### 맥os / 리눅스

```
$ python3 –m venv venv
$ . venv/bin/activate
```

#### 윈도우

```
C:\> python –m venv venv
C:\> venv\scripts\activate
```

### pip

Pip은 외부 패키지를 설치하고보기 위해 명령 줄에서 사용하는 도구입니다. 여기 예시들이 있습니다 :
```bash
$ pip list
$ pip install colorama
$ pip install -r requirements.txt
$ pip uninstall requests
```

## 연습

이제 여러분 차례입니다.  이 연습에서는 문제 해결에 관한 장에서 만든 tic tac toe 게임으로 돌아갑니다. 또는 Connect 4를 통해 만든 경우 대신 해당 작업을 수행 할 수 있습니다. 당신이 할 일은 다음과 같습니다:

* 가상 환경을 만듭니다.
* 아래의 PyCharm에서 호라성 파이썬 이터프리터로 설정하십시오. `settings > project > project interpreter`.
* `colorama` 의 종속성으로 requirements.txt 파일을 만듭시오.
* `pip`을 사용하여 요구 사항을 설치합니다.
* 게임에 컬러 출력을 추가하는 데 `colorama`을 사용합니다.