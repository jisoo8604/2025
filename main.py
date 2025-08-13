import streamlit as st
import random

# ------------------------------
# 데이터
# ------------------------------
mbti_makeup = {
    "INFP": {
        "스타일": "☁️ 몽환적 감성 메이크업",
        "컬러": "💜 퍼플, 말린 장미, 베이비 핑크",
        "팁": "🌙 번진 듯한 아이섀도우 + 글로시 립으로 dreamy 무드"
    },
    "ENFP": {
        "스타일": "🍑 컬러풀 러블리 메이크업",
        "컬러": "🩷 피치, 살몬 핑크, 펄 글리터",
        "팁": "💖 블러셔와 립 톤 맞춰 발랄함 업!"
    }
    # 필요하면 나머지 MBTI 추가
}

# ------------------------------
# CSS & JS로 애니메이션 효과
# ------------------------------
st.markdown("""
    <style>
    @keyframes sparkle {
        0% { opacity: 0.2; transform: scale(1);}
        50% { opacity: 1; transform: scale(1.2);}
        100% { opacity: 0.2; transform: scale(1);}
    }
    .card {
        background: linear-gradient(135deg, #ffdde1, #ee9ca7);
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 0 30px rgba(255, 105, 180, 0.5);
        animation: fadeIn 1s ease-in-out;
        color: white;
        font-size: 1.2em;
    }
    .sparkle {
        position: absolute;
        width: 15px;
        height: 15px;
        background: gold;
        border-radius: 50%;
        animation: sparkle 1.5s infinite ease-in-out;
    }
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(20px);}
        to {opacity: 1; transform: translateY(0);}
    }
    </style>
""", unsafe_allow_html=True)

# ------------------------------
# UI
# ------------------------------
st.set_page_config(page_title="MBTI 메이크업 추천", page_icon="💄")
st.title("💄✨ 반짝이는 MBTI 메이크업 추천 ✨💄")

user_mbti = st.text_input("📝 MBTI를 입력하세요 (예: INFP)", "").upper()

if st.button("💫 추천받기"):
    if user_mbti in mbti_makeup:
        result = mbti_makeup[user_mbti]
        st.markdown(f"""
            <div class="card">
                <h2>{result['스타일']}</h2>
                <p><strong>🎨 추천 컬러:</strong> {result['컬러']}</p>
                <p><strong>💡 팁:</strong> {result['팁']}</p>
            </div>
        """, unsafe_allow_html=True)

        # 반짝이 효과 랜덤 위치 생성
        for _ in range(15):
            x = random.randint(0, 80)
            y = random.randint(0, 50)
            st.markdown(
                f"<div class='sparkle' style='left:{x}%; top:{y}%; position:fixed;'></div>",
                unsafe_allow_html=True
            )
    else:
        st.warning("❗ 올바른 MBTI 유형을 입력해주세요. 예: ENFP, ISTJ")
