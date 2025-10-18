import streamlit as st
import os
from pathlib import Path
import streamlit.components.v1 as components

# 1. HTML 파일이 있는 폴더 경로 설정
# app.py와 같은 레벨에 'htmls' 폴더가 있다고 가정합니다.
HTMLS_DIR = Path(__file__).parent / "htmls"

# 2. 파일 목록 정의 (사용자 친화적인 이름과 파일명 매핑)
# '5. 노력 네트워크 최단 경로 시뮬레이터'와 'index5.html'을 추가했습니다.
FILE_MAPPING = {
    "1. 정보과제연구 계획서 (절차적 생성)": "index.html",
    "2. 수업 조 편성기 (HTML App)": "index2.html",
    "3. 숫자 퍼즐 게임 (HTML Game)": "index3.html",
    "4. 정보과제연구 계획서 (3D 시각화)": "index4.html",
    "5. 노력 네트워크 최단 경로 시뮬레이터": "index5.html",
}

def load_html_content(filepath):
    """지정된 경로의 HTML 파일을 읽어 그 내용을 반환합니다."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        st.error(f"오류: 파일을 찾을 수 없습니다. 경로를 확인해주세요: {filepath}")
        return None
    except Exception as e:
        st.error(f"파일을 읽는 중 오류가 발생했습니다: {e}")
        return None

# 3. Streamlit 앱 레이아웃 설정
# 전체 너비를 사용하도록 설정합니다.
st.set_page_config(layout="wide", page_title="HTML 파일 뷰어")

st.title("Streamlit 기반 HTML 콘텐츠 뷰어")
st.markdown("왼쪽 사이드바에서 보고 싶은 HTML 문서를 선택하세요.")

# 4. 사이드바에 파일 선택 드롭다운 생성
st.sidebar.header("HTML 문서 선택")

# 사용자 친화적인 이름 목록
display_names = list(FILE_MAPPING.keys())
selected_name = st.sidebar.selectbox("파일을 선택하세요:", display_names)

# 선택된 이름에 해당하는 실제 파일 경로 생성
selected_filename = FILE_MAPPING[selected_name]
full_filepath = HTMLS_DIR / selected_filename

# 5. 선택된 HTML 파일 내용 불러오기
html_content = load_html_content(full_filepath)

# 6. HTML 내용을 Streamlit에 표시
if html_content:
    st.subheader(f"현재 선택된 문서: {selected_name}")

    # HTML 뷰어의 높이를 4000px로 설정하여 콘텐츠가 충분히 표시되도록 수정
    components.html(
        html_content,
        height=4000, # HTML 콘텐츠가 잘 보이도록 충분히 큰 높이 설정
        scrolling=True
    )
