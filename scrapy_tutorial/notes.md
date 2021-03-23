### [css selector two colons(::)](https://www.w3schools.com/css/css_pseudo_elements.asp)

- A pseudo-element is made of two colons (::) followed by the name of the pseudo-element.
- usage example
    - p::first-line
    - h1::before
    - h2::after

### yield and generator
- generator: function that returns iterator.
- every generator is iterator.

### [callback](https://stackoverflow.com/questions/1319074/parallel-python-what-is-a-callback)
- callback: function which will be called with argument list as soon as calculation is done
- `submit( ..., callback=work_finished, ... )`
    - Then submit will ensure work_finished() is called when the unit of distributed work is completed on the target server.
    - "call foo(x,y) when you have done some stuff in submit()"

### [secondary](https://edykim.com/ko/post/getting-started-with-sqlalchemy-part-2/)

- Quote 테이블과 Author 테이블은 One-To-Many 관계

- 두 테이블간의 relationship 객체를 만들 때 secondary 파라미터에 "author_quote"를 아규먼트로 줌

- 오류 발생

- > sqlalchemy.exc.InvalidRequestError: One or more mappers failed to initialize - can't proceed with initialization of other mappers. Triggering mapper: 'mapped class Author->author'. Original exception was: When initializing mapper mapped class Author->author, expression 'author_quote' failed to locate a name ("name 'author_quote' is not defined"). If this is a class name, consider adding this relationship() to the <class 'tutorial.models.Author'> class after both dependent classes have been defined.

- author_quote 테이블 객체를 못찾겠다는 오류 발생

- scrapy_quotes.db의 quote_tag 테이블은 M-to-M 관계를 나타내는 association table

  - `tags = relationship('Tag', secondary='quote_tag',    lazy='dynamic', backref="quote")`
  - [Lazy parameter](https://medium.com/@ns2586/sqlalchemys-relationship-and-lazy-parameter-4a553257d9ef) determines how the related objects get loaded when querying through relationships. Below listed are the four main lazy parameters. Typically when you query the database, the data get loaded at once; however, lazy parameter allows you to alternate the way they get loaded.
  - [`backref`](https://stackoverflow.com/questions/44538911/flask-sqlalchemy-backref-function-and-backref-parameter) is a simple way to also declare a new property on the another table.

