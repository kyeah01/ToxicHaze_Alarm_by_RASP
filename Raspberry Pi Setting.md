# Raspberry Pi 기본세팅

## 개발환경세팅

- 모바일 핫스팟을 이용한 TUI개발환경세팅을 목표로 합니다.
  [출처](https://developer-mistive.tistory.com/2)

### Putty설치

- [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)

- 본인컴퓨터에 맞는 `msi`파일을 다운받아 설치한다.



### 모바일 핫스팟 설정

- 윈도우 검색창에서 `모바일 핫스팟`을 검색한 뒤, 이름과 비밀번호를 세팅한다.



### SSH파일과 wpa_supplicant.conf 파일 설정

> 다운 받기를 원한다면 아래에서 다운받을 수 있다.
> [SSH파일](https://developer-mistive.tistory.com/attachment/cfile2.uf@9951CE4C5B5429A22C9232)
> [wpa_supplicant.conf파일](https://developer-mistive.tistory.com/attachment/cfile22.uf@9984984B5B5429A21601ED.conf)

- 텅 빈 `SSH` 파일과 `wpa_supplicant.conf`파일을 생성한다.

- `wpa_supplicant`파일은 메모장으로 켜서 파일 내용에 다음 내용을 담는다.

  ```txt
  ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
  update_config=1
  
  network={
      ssid="아까 설정한 Wifi 이름"
      psk="아까 설정한 Wifi 비밀번호"
      key_mgmt=WPA-PSK
  }
  ```

- 라즈비안이 설치된 sd카드안에 두 파일을 담아준다.



### Putty와 라즈베리파이 연결하기

- 라즈베리 파이를 컴퓨터와 연동시키면, 아까 핫스팟 설정창에서 라즈베리파이가 핫스팟에 연결된 것을 확인할 수 있다.
- 핫스팟 설정에서 `IP주소`를 확인하고 메모해둔다.
- Putty를 키고, `Host Name(or IP address)`에 방금 확인한 IP주소를 기입하고 `saved session`에 원하는 이름을 기재한다음, `Save`를 클릭한다.
- 방금 등록한 `session`을 선택하고 `open`을 클릭한다.

- 처음 연결했을때, 신뢰할 수 없는 host라고 뜨겠지만 무시하고 예를 누르면 된다.
- TUI진입 완료ㅎㅎㅎ



Raspberry Pi의 초기 아이디는 `pi`, 비밀번호는 `raspberry`다. 