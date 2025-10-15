import streamlit as st
import os
from pathlib import Path
import streamlit.components.v1 as components

# 1. HTML 파일이 있는 폴더 경로 설정
# app.py와 같은 레벨에 'htmls' 폴더가 있다고 가정합니다.
HTMLS_DIR = Path(__file__).parent / "htmls"

# 2. 파일 목록 정의 (사용자 친화적인 이름과 파일명 매핑)
# 사용자가 이전에 업로드한 파일 이름을 기반으로 매핑합니다.
FILE_MAPPING = {
    "1. 정보과제연구 계획서 (절차적 생성)": "index.html",
    "2. 수업 조 편성기 (HTML App)": "index2.html",
    "3. 숫자 퍼즐 게임 (HTML Game)": "index3.html",
    "4. 정보과제연구 계획서 (3D 시각화)": "index4.html",
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

    # Streamlit components.v1.html을 사용하여 HTML을 임베드합니다.
    # height와 scrolling=True를 설정하여 HTML 내용이 스크롤 가능하게 만듭니다.
    # *주의*: HTML 콘텐츠의 복잡도에 따라 높이(height)를 조절해야 할 수 있습니다.
    # 임베드된 콘텐츠가 전체 높이를 차지하도록 임의로 높이를 높게 설정했습니다.
    components.html(
        html_content,
        height=800, # 초기 높이 설정 (필요에 따라 조절 가능)
        scrolling=True
    )
    
    # 원본 코드 표시 (디버깅 및 참고용)
    with st.expander("원본 HTML 코드 보기"):
        st.code(html_content, language="html")

# 7. 참고 사항
st.sidebar.markdown("---")
st.sidebar.info(
    "**실행 전 확인 사항:**\n"
    "1. `app.py`와 같은 위치에 `htmls` 폴더가 있어야 합니다.\n"
    "2. `htmls` 폴더 안에 다음 4개 파일이 정확한 이름으로 존재해야 합니다:\n"
    "   - `index.html`\n"
    "   - `index2.html`\n"
    "   - `index3.html`\n"
    "   - `index4.html`\n"
)
st.sidebar.code("pip install streamlit")

st.sidebar.success("Streamlit 실행 명령어:\nstreamlit run app.py")
