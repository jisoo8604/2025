import streamlit as st
import random

# MBTI별 공부 방법 데이터
study_tips = {
    "INTJ": "🧠 계획적이고 체계적으로 공부하세요. 장기 목표를 세우고 작은 단계로 나누어 실행하면 효과적입니다.",
    "INTP": "🔍 호기심을 기반으로 탐구하세요. 스스로 질문을 만들고 답을 찾는 과정에서 깊은 이해가 가능합니다.",
    "ENTJ": "🎯 목표를 명확히 하고 효율적인 방법을 찾으세요. 시간 관리와 우선순위 설정이 핵심입니다.",
    "ENTP": "💡 다양한 방법을 시도하며 배우세요. 토론, 발표, 창의적 프로젝트가 잘 맞습니다.",
    "INFJ": "🌌 의미 있는 맥락 속에서 공부하세요. 공부 내용을 가치나 이상과 연결하면 더 오래 기억됩니다.",
    "INFP": "💖 흥미와 열정을 기반으로 학습하세요. 감정과 연결되는 학습이 효과적입니다.",
    "ENFJ": "🤝 협력적인 환경에서 잘 배우는 타입입니다. 친구들과 스터디 그룹을 만들어 공부하세요.",
    "ENFP": "🎨 창의적인 방법으로 배우세요. 그림, 스토리텔링, 마인드맵을 활용하면 좋습니다.",
    "ISTJ": "📅 계획표와 규칙을 세우고 꾸준히 공부하는 것이 효과적입니다. 반복 학습에 강점이 있습니다.",
    "ISFJ": "📖 안정적인 환경에서 차분히 학습하세요. 복습과 정리 노트 만들기가 도움이 됩니다.",
    "ESTJ": "✅ 명확한 목표를 세우고 계획대로 실천하세요. 실용적이고 구체적인 자료가 잘 맞습니다.",
    "ESFJ": "👨‍👩‍👧 타인과의 협력이 중요합니다. 스터디 그룹이나 친구에게 설명하면서 배우세요.",
    "ISTP": "🛠 직접 문제를 풀거나 실습하면서 배우는 것이 효과적입니다. 이론보다 실제 적용에 강합니다.",
    "ISFP": "🎶 자유로운 분위기에서 배우는 것이 좋습니다. 감각적이고 시각적인 자료를 활용하세요.",
    "ESTP": "⚡ 즉흥적으로 실습하면서 배우세요. 몸으로 체험하거나 경쟁 요소를 넣으면 집중이 잘 됩니다.",
    "ESFP": "🎉 재미있고 활기찬 방법이 효과적입니다. 음악, 색깔, 활동적인 학습이 잘 맞습니다.",
}

# --------------------- Streamlit UI --------------------- #
st.set_page_config(page_title="MBTI 공부법 추천기", page_icon="📚", layout="wide")

# 배경 CSS
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%);
    color: black;
}
h1, h2, h3 {
    text-align: center;
    font-family: 'Comic Sans MS', cursive, sans-serif;
}
.result-card {
    background: white;
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.25);
    margin-top: 30px;
    font-size: 20px;
    animation: pop 1s ease;
}
@keyframes pop {
    0% { transform: scale(0.5); opacity: 0; }
    100% { transform: scale(1); opacity: 1; }
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# 타이틀
st.title("📚✨ MBTI 공부법 추천기 ✨📚")
st.markdown("### 👉 자신의 MBTI를 직접 입력하세요! (예: INFP, ESTJ)")

# 입력 박스 (직접 입력)
mbti = st.text_input("당신의 MBTI는?", "").upper().strip()

# 버튼
if st.button("🔮 공부법 확인하기!"):
    if mbti in study_tips:
        st.markdown(f"""
            <div class="result-card">
                <h2>✨ {mbti} 유형의 공부법 ✨</h2>
                <p>{study_tips[mbti]}</p>
            </div>
        """, unsafe_allow_html=True)

        # 이스터에그: 랜덤 칭찬 문구 튀어나오기
        compliments = ["🔥 완전 잘 어울려요!", "🌟 당신은 공부 천재!", "🚀 오늘도 성장하는 중!", "💎 빛나는 학습자!"]
        st.balloons()
        st.success(random.choice(compliments))
    else:
        st.error("⚠️ 올바른 MBTI 유형을 입력해주세요! (예: INTP, ESFP)")
