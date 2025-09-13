import streamlit as st
import os
import streamlit.components.v1 as components

# HTML 파일을 담고 있는 폴더 경로 설정
# The folder containing the HTML files
HTMLS_FOLDER = "htmls"

# Streamlit 앱의 페이지 설정
# Set the title for the Streamlit app
st.set_page_config(
    page_title="HTML 파일 뷰어",
    layout="wide"
)

# 폴더 내의 HTML 파일 목록 가져오기
# Get a list of HTML files in the specified folder
def get_html_files():
    try:
        files = [f for f in os.listdir(HTMLS_FOLDER) if f.endswith('.html')]
        return sorted(files)
    except FileNotFoundError:
        st.error(f"'{HTMLS_FOLDER}' 폴더를 찾을 수 없습니다. '{HTMLS_FOLDER}' 폴더가 'app.py'와 같은 위치에 있는지 확인해주세요.")
        return []

html_files = get_html_files()

# 사이드바에 파일 선택 위젯 생성
# Create a file selection widget in the sidebar
if not html_files:
    st.warning("HTML 파일이 없습니다. 'htmls' 폴더에 파일을 추가해주세요.")
else:
    st.sidebar.header("HTML 파일 선택")
    selected_file = st.sidebar.radio(
        "파일 목록",
        html_files
    )

    # 선택된 파일 내용 읽기
    # Read the content of the selected file
    with open(os.path.join(HTMLS_FOLDER, selected_file), "r", encoding="utf-8") as f:
        html_content = f.read()

    # Streamlit에 HTML 내용 렌더링
    # Render the HTML content in Streamlit
    st.header(f"'{selected_file}'")
    components.html(html_content, height=800, scrolling=True)

    st.markdown("---")
    st.info("왼쪽 사이드바에서 다른 HTML 파일을 선택하세요.")
