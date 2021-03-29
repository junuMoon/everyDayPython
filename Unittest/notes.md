### Dependency Inversion

> We don't have to load eveyrtime. And we may wish we want use differente model.
> Ratehr than have name entity depend on this specific model. It should depend on instruction that would pass to it.

### [TestDouble](https://medium.com/@SlackBeck/단위-테스트-케이스와-테스트-더블-test-double-2b88cccd6a96)
> 또한 독립적이라는 것은 어떤 테스트도 다른 테스트에 의존하지 않는다는 것을 의미한다. 어느 순서로든, 어떤 개별 테스트라도 실행해 볼 수 있어야 한다. 처음 것을 실행할 때 그 밖의 다른 테스트에 의존해야 하는 상황을 원하지는 않을 것이다.
> 모든 테스트는 섬이어야 한다.

- 독립적인 테스트 케이스를 작성 하기 위해서는 어떻게 해야 할까? 
하나의 방법은 테스트 대상을 의존하는 것으로부터 격리(Isolation) 시키는 것이다.
프로그래밍 관점에서 격리 시킨다는 것은 테스트 대상이 의존하는 것을 실제가 아닌 다른 것으로 대체 하는 것이다. 이렇게 대체 하는 것을 Stub/Mock/Fake로 부른다.
- 테스트 더블(Test Double): stub, mock, fake

### [__call__](https://jinmay.github.io/2019/12/03/python/python-callable/)
- 인스턴스가 호출 됐을 때 실행되도록 만드는 매직메소드

### TypeError: 'bool' ojbect is not subscriptable
- It basically means that the object implements the __getitem__() method. In other words, it describes objects that are "containers", meaning they contain other objects. This includes strings, lists, tuples, and dictionaries.
- subscript: a word, letter, number, or symbol written or printed just below another word, letter, number, or symbol, usually in a smaller size
