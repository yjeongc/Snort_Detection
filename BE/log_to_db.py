import os
import django

# Django 설정 파일을 사용하도록 환경 변수 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'snort_project.settings')
django.setup()

from detection.models import SnortAlert

def save_log_to_db():
    # Snort 로그 파일을 열어서 읽기
    try:
        with open('/var/log/snort/snort.alert', 'r', encoding='utf-8', errors='ignore') as log_file:
            for line in log_file:
                # 로그 라인을 파싱하여 데이터베이스에 저장
                data = parse_log_line(line)
                if data:  # 유효한 데이터만 저장
                    SnortAlert.objects.create(
                        alert_message=data['message'],
                        source_ip=data['src_ip'],
                        destination_ip=data['dst_ip'],
                        protocol=data['protocol']
                    )
    except FileNotFoundError:
        print("Log file not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

def parse_log_line(line):
    # 로그 라인을 파싱하는 함수 (예시)
    parts = line.split()
    if len(parts) > 5:
        return {
            "message": parts[3],
            "src_ip": parts[4],
            "dst_ip": parts[6],
            "protocol": parts[5]
        }
    return None

if __name__ == "__main__":
    save_log_to_db()
