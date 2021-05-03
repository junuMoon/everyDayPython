# Everyday Python

get a bit of python everyday

---

### Scrapy Tutorial
- 2021.03.22-2021.03.25
- [scrapy tutorial part](https://towardsdatascience.com/a-minimalist-end-to-end-scrapy-tutorial-part-i-11e350bcdec0)
- start project
- parse function
- asynchronous crawling with callback function
- [notes](./scrapy_tutorial/notes.md)
- https://github.com/my8100/scrapydweb

---

### [Flask Tutorial](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g)
- 2021.03.17-2021.03.25

---

### Dynamic Scrapy

- 2021.03.26
- how to scrape dynamic web page
- CDN
- Proxy

---

### [Flask with TDD](https://www.youtube.com/watch?v=eAPmXQ0dC7Q&t=851s)

- 2021.03.26-2021.04.05
- TDD
  1. Write only enough of a unit test to fail.
  2. Write only enough production code to make the failing unit test pass.
- BackEnd structure:
  - model
  - database
  - App(API)
  - templates(HTML)
  - static(CSS, JavaScript)
- JavaScript Asynchoronus
  - Callback, Promise, Async function
- furthther subject:
  - JavaScript tutorial
  - Node.JS
  - Deploy keras model with flask 
  - python advanced
  - TDD
    - w/ python
    - w/ javascript
    - TDD is a hitchhiker's guide to the programming

---

### [Python Intermediate](https://www.inflearn.com/course/프로그래밍-파이썬-중급-인프런-오리지널)

- 2021.04.04-
- First Class Object
- Closure
- [Decorator](https://www.youtube.com/watch?v=FsAPt_9Bf3U): Wow now I can decorate my decorators while I'm using my decorated functions
- Iterator: object with a state so that where it's at during its iteration.
- Concurrency: 병렬
- Asynchronous: 비동기
- further subject:
  - asynchronous scraping, scrapy
  - unittest, pytest

---

### [TensorFlow Tutorial](https://www.youtube.com/watch?v=HPjBY1H-U4U&list=PLhhyoLH6IjfxVOdVC1P1L5z5azs0XjMsb&index=2)

- 2021.04.05-
- to understand the core of DL models, need to have prerequisites knowledge:
  - Statistic
  - Calculs
  - Vector
- so first, study light just to handle the model w/o deep understanding

---

### [Over The Wire for LINUX](https://www.inflearn.com/course/linux-3#)

- 2021.04.04-
- learn linux with war game
- It interests me a lot

---

### [JavaScript Tutorial](https://www.youtube.com/channel/UC_4u-bXaba7yrRz_6x6kb_w)

- 2021.04.03-
- It's whole different language compared to python!
  - very flowy, I think.

---

### [Django Report Proejct](https://www.youtube.com/watch?v=tLq20htu3ss&t=11299s)

- 2021.04.10-2021.04.22
- [DB migration](https://life-with-coding.tistory.com/68): 스키마의 버전관리 방법.
- [Meta Class](https://tech.ssut.me/understanding-python-metaclasses/): 메타클래스는 99%의 사용자는 전혀 고려할 필요가 없는 흑마법입니다. 만약 당신이 이게 정말로 필요할지에 대한 의문을 갖는다면, 필요하지 않습니다. (이게 진짜로 필요한 사람은 이게 진짜로 필요하다고 알고 있으면서, 왜 필요한지에 대해 설명할 필요가 없는 사람들입니다.)
- [Inner Class](https://has3ong.tistory.com/236): Meta 옵션이란 Inner class로 사용하여 상위 클래스에게 meta data를 제공하는것입니다.
- [Property Decorator](https://www.daleseo.com/python-property/): 클래스를 사용하는 측면에서는 일반 필드에 접근하는 것처럼 보이지만 내부적으로 getter와 setter 메서드가 호출이 됩니다.

---

### [Data Structure in Flask API](https://www.youtube.com/watch?v=74NW-84BqbA)

- 2021.04.24-2021.04.26
- ORM: Object Relational Mapper
  - [SQLAlchemy](https://dongchans.github.io/2019/28/): sql문법을 전부 파이썬 객체로 맵핑하여 그냥 파이썬 객체의 인스턴스, 메소드를 통해서 구현할 수 있다면 훨씬 더 체계적이고 가독성이 좋을 것이다. 그러한 객체와 기능의 MAPPING을 바로 ORM이라고 한다.
- route: A decorator that is used to register a *view function* for a given URL rule.
- payload: refers to an integral part of each unit of data being transmitted. It is part of the unit data that carries the real message that an app or system needs for it to act.
- constraint: 제약조건은 결점 없이 정확하고 유효한 데이터가 데이터베이스에 저장될 수 있도록 하기 위하여 데이터를 조작하는데 한계를 규정한 것이다
- cascade constraint: Delete or update the row from the parent table and automatically delete or update the matching rows in the child table
- [Binary Search Tree](https://junumoon.github.io/posts/til_recursive_function_without_return/): 

#### Hash Table

- hash function: hash(key) -> index: every time enter Paul to my hash function it always return 3
- [Hashing](https://www.freecodecamp.org/news/what-is-hashing/)means using some function or algorithm to map object data to some representative integer value.
- Hashing is efficient to find or store an item in a collection.

---
### [Dokcer Tutorial](https://www.youtube.com/watch?v=fqMOX6JJhGo)

- 2021.04.26-28
- docker is awesome!
  - why? I dunno yet!
  - but awesome anyway!
- docker container is upon OS and virtual machine is upon Infrastructure
  - ![도커](https://images.contentstack.io/v3/assets/blt300387d93dabf50e/bltb6200bc085503718/5e1f209a63d1b6503160c6d5/containers-vs-virtual-machines.jpg)

- Next step: Microservice using docker

---

### [Microservice](https://www.youtube.com/watch?v=0iB5IPoTDts&t=739s)

- 2021.04.28-
- **마이크로서비스**(microservice)는 애플리케이션을 [느슨하게 결합된](https://ko.wikipedia.org/wiki/결합) 서비스의 모임으로 구조화하는 [서비스 지향 아키텍처](https://ko.wikipedia.org/wiki/서비스_지향_아키텍처)(SOA) 스타일의 일종인 [소프트웨어 개발](https://ko.wikipedia.org/wiki/소프트웨어_개발) 기법이다. 마이크로서비스 아키텍처에서 서비스들은 [섬세](https://ko.wikipedia.org/w/index.php?title=서비스_입자성_원칙&action=edit&redlink=1)(fine-grained)하고 [프로토콜](https://ko.wikipedia.org/wiki/프로토콜)은 가벼운 편이다. 애플리케이션을 더 조그마한 여러 서비스로 분해할 때의 장점은 [모듈성](https://ko.wikipedia.org/wiki/모듈성_(프로그래밍))을 개선하고 애플리케이션의 이해, 개발, 테스트를 더 쉽게 해주고 애플리케이션 침식에 더 탄력적으로 만들어 준다.[[1\]](https://ko.wikipedia.org/wiki/마이크로서비스#cite_note-Micro_Chen-1) 규모가 작은 자율적인 팀들이 팀별 서비스를 독립적으로 개발, [전개](https://ko.wikipedia.org/wiki/소프트웨어_전개), 규모 확장을 할 수 있게 함으로써 병렬로 [개발](https://ko.wikipedia.org/wiki/소프트웨어_개발)할 수 있게 한다.[[2\]](https://ko.wikipedia.org/wiki/마이크로서비스#cite_note-2) 또, 지속적인 [리팩터링](https://ko.wikipedia.org/wiki/리팩터링)을 통해 개개의 서비스 아키텍처가 하나로 병합될 수 있게 허용한다.[[3\]](https://ko.wikipedia.org/wiki/마이크로서비스#cite_note-Ach_Chen-3) 마이크로서비스 기반 아키텍처는 [지속적 배포](https://ko.wikipedia.org/wiki/지속적_배포)와 전개(디플로이)를 가능케 한다.[[1\]](https://ko.wikipedia.org/wiki/마이크로서비스#cite_note-Micro_Chen-1)[[4\]

---

## Network programming

- Following microservice tutorial, there was need to understand the basic of networking

### [Network Programming w/ Python](https://www.youtube.com/watch?v=FGdiSJakIS4)

- 2021.05.03-
- [A Beginner's guide to Web Sockets](https://www.youtube.com/watch?v=8ARodQ4Wlf4&t=1582s): Web Socket is an udpate of HTTP
