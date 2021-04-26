# Data Structure w/ Flask

- ORM: Object Relational Mapper
  - [SQLAlchemy](https://dongchans.github.io/2019/28/): sql문법을 전부 파이썬 객체로 맵핑하여 그냥 파이썬 객체의 인스턴스, 메소드를 통해서 구현할 수 있다면 훨씬 더 체계적이고 가독성이 좋을 것이다. 그러한 객체와 기능의 MAPPING을 바로 ORM이라고 한다.
- route: A decorator that is used to register a *view function* for a given URL rule.
- payload: refers to an integral part of each unit of data being transmitted. It is part of the unit data that carries the real message that an app or system needs for it to act.
- constraint: 제약조건은 결점 없이 정확하고 유효한 데이터가 데이터베이스에 저장될 수 있도록 하기 위하여 데이터를 조작하는데 한계를 규정한 것이다
- cascade constraint: Delete or update the row from the parent table and automatically delete or update the matching rows in the child table

### Hash Table

- hash function: hash(key) -> index: every time enter Paul to my hash function it always return 3
- [Hashing](https://www.freecodecamp.org/news/what-is-hashing/)means using some function or algorithm to map object data to some representative integer value.
- Hashing is efficient to find or store an item in a collection.