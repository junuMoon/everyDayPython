# Docker



### Volume

- 도커 컨테이너는 stop 순간 데이터는 날라감
- 따라서 도커 내 폴더/파일과 호스트 폴더/파일을 공유하는 방법으로 volume이 있음
- COMMAND: `docker create {volume-name}`
- 그러나 mac에서 도커는 VM위에 올려지기에 docker의 루트 디렉토리가 존재하지 않음
- 따라서 volume을 사용하기 위해서는 run 단계에서 특정 디렉토리를 설정할 필요가 있음
  - ```bash
    docker run -v {host-directory-path}:{container-directory-path} \
    {docker_image_name:tag}
    ```

### Docker compose

- 여러 도커 컨테이너를 관리하기 쉽도록 만든 문법
- 볼륨 설정
  - ```bash
  volumes:
    - ./:/app
    ```
  
  
  

