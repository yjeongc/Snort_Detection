# Snort 대시보드 프로젝트

이 프로젝트는 Snort의 네트워크 침입 탐지 결과를 시각적으로 표시하는 대시보드를 구축하는 것을 목표로 합니다. Django를 백엔드로, React를 프론트엔드로 사용하여 실시간 데이터 시각화를 제공하여 네트워크 보안 이벤트를 모니터링할 수 있도록 합니다.

## 사용 기술
- **환경**: Ubuntu 24.04
- **백엔드**: Django, Django REST Framework, CORS Headers
- **프론트엔드**: React, Chart.js (데이터 시각화용)
- **네트워크 IDS**: Snort

## 프로젝트 구조

이 프로젝트는 두 개의 주요 부분으로 구성됩니다:

- **백엔드 (BE)**: Django를 사용하여 Snort 탐지 로그를 관리하고 프론트엔드에 REST API로 제공합니다.
- **프론트엔드 (FE)**: React를 사용하여 백엔드 API에서 가져온 데이터를 사용자 친화적인 방식으로 시각화합니다.

### 폴더 구조
- `/BE` - Django 프로젝트 파일을 포함한 백엔드 폴더
  - `manage.py` - Django 관리 파일
  - `snort_project/` - Django 설정 및 메인 프로젝트 구성 파일
  - `detection/` - Snort 탐지 데이터를 처리하는 앱
  - `new_venv/` - Python 가상환경
  - `log_to_db.py` - Snort 로그를 읽어 데이터베이스에 저장하는 스크립트
- `/FE/snort-dashboard` - React 프로젝트 파일을 포함한 프론트엔드 폴더

## Snort 설정

이 프로젝트를 실행하기 위해서는 Snort가 설치되어야 합니다. 

또한, Snort를 사용할 때 아래와 같은 설정이 필요합니다.

1. **Snort 설치** (Ubuntu 예시):
   ```bash
   sudo apt install snort
   ```

2. **Snort 설정**
   `/etc/snort/snort.conf` 파일을 열어서 설정이 아래와 같이 되어 있는지 확인합니다.<br/>
     (vim을 사용한다면 / (슬래시)를 눌러서 글자를 검색할 수 있습니다)
   
   * **명령어 1**<br/> 
     snort.conf 파일을 열어서 설정이 **output alert_fast: /var/log/snort/snort.alert** 와 같이 되어 있는지 확인합니다.
     ```bash
     sudo vim /etc/snort/snort.conf
     ```
   
   * **명령어 2**<br/>
     local.rules 파일을 열어서 설정이 **include $RULE_PATH/local.rules** 와 같이 되어 있는지 확인합니다.
     ```bash
     sudo vim /etc/snort/rules/local.rules
     ```
     
3. **Snort 실행**
     * 아래 명령어로 모든 네트워크 인터페이스를 확인합니다.
     ```bash
     ip link show
     ```

    * 위 명령어로 나온 인터페이스를 넣어서 명령어를 실행해주세요.
    ```bash
    sudo snort -c /etc/snort/snort.conf -i {인터페이스_넣어주세요}
    ```
    조금 시간이 걸릴 수도 있으니 기다립니다.<br/>

4. 명령어를 입력하여 로그데이터가 잘 쌓였는지 확인합니다. 로그데이터가 쌓였다면 로그가 나오고, 쌓이지 않았다면 아무것도 나오지 않습니다.
   ```bash
   cat /var/log/snort/snort.log
   ```
     
## 설치 안내

이 프로젝트를 실행하기 위해 다음 단계를 따르세요.

### 1. 저장소 클론하기
GitHub에서 로컬 머신으로 저장소를 클론합니다:
```bash
git clone https://github.com/yjeongc/Snort_Detection.git
cd Snort_Detection
```

### 2. 백엔드 설정 (Django)

1. **백엔드 폴더로 이동**
   ```bash
   cd BE
   ```

2. **가상환경 생성 및 활성화**
   ```bash
   python3 -m venv new_venv
   source new_venv/bin/activate
   ```

3. **종속성 설치**
   - `requirements.txt` 파일을 이용하여 모든 필요한 패키지를 설치합니다:
   ```bash
   pip install -r requirements.txt
   ```

4. **데이터베이스 마이그레이션 실행**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Django 서버 실행**
   ```bash
   python manage.py runserver
   ```

### 3. 로그 데이터 수집
Snort 로그 데이터를 수집하여 Django 데이터베이스에 저장하려면 다음 스크립트를 실행하세요:
```bash
python log_to_db.py
```
위 스크립트를 실행한 후에 "{Django_서버주소}/api/alerts/"에 접속하여 데이터가 잘 들어갔는지 확인합니다.


### 4. 프론트엔드 설정 (React)

1. **프론트엔드 폴더로 이동**
   ```bash
   cd ../FE/snort-dashboard
   ```

2. **종속성 설치**
   ```bash
   npm install
   ```

3. **React 개발 서버 실행**
   ```bash
   npm start
   ```

## 전체 프로젝트 실행 방법
1. **백엔드 가상환경 활성화 및 Django 서버 실행**:
   ```bash
   cd /path/to/snort_project/BE
   source new_venv/bin/activate
   python manage.py runserver
   ```

2. **프론트엔드 실행**:
   ```bash
   cd /path/to/snort_project/FE/snort-dashboard
   npm start
   ```

3. **로그 수집 스크립트 실행** (필요한 경우):
   ```bash
   cd /path/to/snort_project/BE
   python log_to_db.py
   ```

## 문제 해결
- **ModuleNotFoundError**: 모듈을 찾을 수 없다는 오류가 발생하면, 가상환경이 활성화되어 있는지 확인하고 모든 종속성이 설치되어 있는지 확인하세요.
- **CORS 문제**: `django-cors-headers`가 설치되어 있고, React 프론트엔드에서 API 요청을 허용하도록 `settings.py`에서 올바르게 설정되어 있는지 확인하세요.
