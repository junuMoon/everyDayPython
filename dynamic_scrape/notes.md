### proxy
-  사용방법
   ```python
   requests.get(url, headers=headers, proxies={'https:' proxy})
   ```
-  proxy: 서버와 클라이언트 사이에 중계기로서 대리로 통신을 수행하는 것을 가리켜 '프록시', 그 중계 기능을 하는 것을 프록시 서버라고 부른다.
### [CDN](https://www.jsdelivr.com/network/infographic)
- CDN(Contents Delivery Network): 서버와 사용자 사이의 물리적 거리를 줄여 웹 페이지 콘텐츠 로드 지연을 최소화하는, 촘촘히 분산된 서버로 이루어진 플랫폼
- 집하장, 쿠팡 물류 센터
- CDN은 오리진을 대신하여 엔드유저와 가까운 물리적 위치 및 네트워크에서 엔드유저 요청에 응답함으로써 콘텐츠 서버의 트래픽 부하를 오프로드하고 웹 경험을 개선하여 콘텐츠 제공업체와 엔드유저 모두에게 막대한 이점을 제공합니다.
- [사용방법](https://github.com/jsdelivr/jsdelivr)
