import streamlit as st
import os

# Set a wide layout for the app
st.set_page_config(layout="wide")

# 사이드바에서 표시할 HTML 파일을 선택합니다.
page = st.sidebar.selectbox(
    "페이지를 선택하세요",
    ("정보과제연구 계획서", "수업 조 편성기")
)

# 선택된 페이지에 따라 HTML 파일 경로를 설정합니다.
if page == "정보과제연구 계획서":
    html_file_name = "index.html"
elif page == "수업 조 편성기":
    html_file_name = "index2.html"

# HTML 파일의 전체 경로를 생성합니다.
html_file_path = os.path.join(os.path.dirname(__file__), "htmls", html_file_name)

# HTML 파일이 존재하는지 확인합니다.
if not os.path.exists(html_file_path):
    st.error(f"오류: HTML 파일을 찾을 수 없습니다. 경로: {html_file_path}")
    st.stop()

# HTML 파일의 내용을 읽어옵니다.
try:
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # HTML 내용을 Streamlit에 렌더링합니다.
    st.html(html_content)

except Exception as e:
    st.error(f"HTML 파일을 읽는 중 오류가 발생했습니다: {e}")
