# 오류 처리를 위한 연습

## 개요

이 섹션에서는 동영상에서 배운 개념을 연습할 수 있는 기회가 주어집니다. 먼저, 여러분이 유념해야 할 핵심 개념들을 검토해보십시오. 그런 다음 아래의 연습문제를 보십시오.

기억하십시오, 이것들은 여러분의 이익을 위한 것입니다. 만약 여러분이 특정한 연습이 가치가 없다고 발견되거나 너무 오랫동안 걸려있다면, 그것들을 건너뛰어도 좋습니다.

## 핵심개념

### try / except

오류를 처리 할 때 잘못된 값을 확인할 수 있습니다. (예: `None` 적절한 문자열이 예상되는 위치) 그러나 Python의 기본 오류 처리 접근 방식은 예외 기반입니다. 예외 발생 및 잡기.

다음은 Python에서 오류를 포착하기위한 최소 코드입니다.


```python
try:
    do_risky_thing1()
    do_risky_thing2()
    do_risky_thing3()
except Exception as x:
    # 무슨 일이 있었는지 도움받기 위해 x를 사용하여 오류를 처리하십시오.
```

###  여러 오류 유형

위의 예는 오류를 포착하는 데 좋습니다. 그러나 그것은 그것들을 모두 (거의 모두) 포착하고, 그것들을 모두 동일하게 취급합니다.

다음은 다양한 오류와 예기치 않은 오류를 처리하는데 필요한 코드입니다.


```python
try:
    do_risky_thing1()
    do_risky_thing2()
    do_risky_thing3()
except json.decoder.JSONDecodeError:
    # Handle malformed JSON error
except FileNotFoundError as fe:
    # Handle missing file error
except ValueError:
    # Handle conversion error.
except Exception as x:
    # Deal with error, use x for help on what happened.
```

**주의**: 가장 구체적인 오류가 먼저 나열되고 가장 일반적인 오류가 마지막 ( Exception)에 나열되는 것이 중요합니다 . 파이썬은 첫 번째 (최선이 아닌) 일치를 선택합니다.

## 연습

이제 여러분 차례입니다.  이 연습에서는 문제 해결에 관한 장에서 만든 tic tac toe 게임으로 돌아갑니다. 또는 Connect 4를 통해 만든 경우 대신 해당 작업을 수행 할 수 있습니다. 당신이 할 일은 다음과 같습니다:

* try / except를 사용하여 프로그램의 입력 처리 주위에 오류 처리를 추가하십시오. 가능한 한 오류를 구체적으로 설명하십시오. 오류의 원인이나 유형을 확인할 수 있으면 특정 메시지를 제공하십시오.
* 앱이 충돌하거나 문제가 발생할 수있는 다른 모든 방법을 생각해보십시오. 충돌을 일으키고 트레이스 백에서 오류 유형을 확인하고 이에 대한 적절한 오류 처리를 추가하십시오.