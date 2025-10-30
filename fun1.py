import streamlit as st
import pandas as pd
import datetime
import random
from pathlib import Path
import time

# 页面配置（深色模式更浪漫）
st.set_page_config(
    page_title="专属恋爱密码本",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 自定义CSS：动态效果+美化样式
st.markdown("""
    <style>
    .heart {
        animation: heartbeat 1.5s infinite;
        color: #ff4d6d;
        font-size: 20px;
    }
    @keyframes heartbeat {
        0% { transform: scale(1); }
        14% { transform: scale(1.1); }
        28% { transform: scale(1); }
        42% { transform: scale(1.1); }
        70% { transform: scale(1); }
    }
    .memory-box {
        background-color: #fff0f3;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .quote-popup {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: #ffccd5;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        animation: slideUp 0.5s ease-out;
    }
    @keyframes slideUp {
        from { transform: translateY(100px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    .title {
        background: linear-gradient(90deg, #ff8fa3, #c0fdff);
        -webkit-background-clip: text;
        color: transparent;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 初始化数据（本地保存回忆，避免重启丢失）
def init_data():
    # 初始化密码（默认1314）
    if 'password' not in st.session_state:
        st.session_state.password = "1314"
    # 初始化纪念日（可自定义）
    if 'anniversary' not in st.session_state:
        st.session_state.anniversary = datetime.date(2022, 11, 23)  # 替换成你们的纪念日
    # 加载本地回忆
    if 'memories' not in st.session_state:
        st.session_state.memories = []
        if Path("love_memories.txt").exists():
            with open("love_memories.txt", "r", encoding="utf-8") as f:
                st.session_state.memories = [line.strip() for line in f.readlines() if line.strip()]

# 保存回忆到本地文件
def save_memory(text):
    if text:
        st.session_state.memories.append(text)
        with open("love_memories.txt", "a", encoding="utf-8") as f:
            f.write(text + "\n")
        return True
    return False

# 随机情话库
love_quotes = [
    "今天的风很甜，因为它路过你那里时偷了一块糖～",
    "想把你藏进我的口袋，这样每天都能带着可爱出门啦～",
    "你一笑，连空气都变成了草莓味的～",
    "我有两个愿望：你在身边，在你身边～",
    "遇见你之后，连发呆都变成了甜甜的事～"
]

# 初始化
init_data()

# 标题+动态爱心
st.markdown('<h1 class="title">🔒 专属我们的恋爱密码本 🔒</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center;" class="heart">❤️ 加载中... 正在偷偷藏起对你的喜欢 ❤️</p>', unsafe_allow_html=True)
time.sleep(1)  # 加载动画延迟

# 密码输入
password = st.text_input("输入恋爱密码解锁", type="password")

# 密码正确后显示内容
if password == st.session_state.password:
    # 清除加载提示
    st.empty()
    
    # 1. 纪念日倒计时（动态更新）
    st.subheader("💑 我们的纪念日")
    today = datetime.date.today()
    days_together = (today - st.session_state.anniversary).days
    next_anniversary = datetime.date(today.year, st.session_state.anniversary.month, st.session_state.anniversary.day)
    if next_anniversary < today:
        next_anniversary = datetime.date(today.year + 1, st.session_state.anniversary.month, st.session_state.anniversary.day)
    days_to_next = (next_anniversary - today).days
    
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"已经在一起 **{days_together} 天**")
    with col2:
        st.success(f"距离下一个纪念日还有 **{days_to_next} 天**")

    # 2. 专属暗号（带hover效果）
    st.subheader("💌 专属暗号库")
    codes = {
        "🍬": "你是我的专属甜豆",
        "🌙": "今晚的月色很美（=我想你）",
        "🐱": "你撒娇的样子像小胖猫咪",
        "520": "我爱你呀",
        "1314": "一生一世和你在一起"
    }
    # 用HTML表格实现hover效果
    st.markdown("""
        <table style="width:100%; border-collapse: collapse;">
            <tr style="background-color: #f8f9fa;">
                <th style="padding: 10px; text-align: left; border-bottom: 2px solid #ffccd5;">暗号</th>
                <th style="padding: 10px; text-align: left; border-bottom: 2px solid #ffccd5;">专属含义</th>
            </tr>
    """, unsafe_allow_html=True)
    for symbol, meaning in codes.items():
        st.markdown(f"""
            <tr style="transition: background-color 0.3s;">
                <td style="padding: 10px; border-bottom: 1px solid #ffeef2;">{symbol}</td>
                <td style="padding: 10px; border-bottom: 1px solid #ffeef2;">{meaning}</td>
            </tr>
        """, unsafe_allow_html=True)
    st.markdown("</table>", unsafe_allow_html=True)

    # 3. 回忆记录（带本地保存+历史展示）
    st.subheader("📝 独家回忆")
    new_memory = st.text_area(
        "记录只有我们懂的小细节",
        placeholder="比如：之前和笨琪一起去西安，还想每天都呆在一起"
    )
    if st.button("💾 保存这条回忆", use_container_width=True):
        if save_memory(new_memory):
            st.success("回忆已锁存！永远不会消失～")
            # 随机弹出情话
            st.markdown(f"""
                <div class="quote-popup">
                    <p>{random.choice(love_quotes)}</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("先输入回忆内容再保存呀～")

    # 展示历史回忆
    if st.session_state.memories:
        st.subheader("✨ 回忆收藏夹")
        for i, mem in enumerate(reversed(st.session_state.memories)):  # 最新的在前面
            st.markdown(f'<div class="memory-box"><strong>回忆 {len(st.session_state.memories)-i}：</strong><br>{mem}</div>', unsafe_allow_html=True)

    # 4. 修改密码+纪念日
    st.subheader("🔐 秘密设置")
    with st.expander("修改专属密码", expanded=False):
        new_pwd = st.text_input("新密码", type="password", placeholder="比如你们的纪念日：20230520")
        confirm_pwd = st.text_input("确认新密码", type="password")
        if st.button("确认修改密码", use_container_width=True):
            if new_pwd == confirm_pwd and new_pwd:
                st.session_state.password = new_pwd
                st.success("密码修改成功！下次用新密码解锁哦～")
            elif not new_pwd:
                st.warning("新密码不能为空呀～")
            else:
                st.error("两次输入的密码不一样！再检查下～")

    with st.expander("修改纪念日", expanded=False):
        new_anniv = st.date_input("我们的纪念日", st.session_state.anniversary)
        if st.button("确认修改纪念日", use_container_width=True):
            st.session_state.anniversary = new_anniv
            st.success("纪念日更新成功！每一刻都值得纪念～")

# 密码错误提示
else:
    if password:
        st.error("❌ 密码不对哦～ 再想想我们的专属密码？")
    st.info("💡 初始密码是 1314，快输入解锁我们的小秘密～")

# 底部动态爱心
st.markdown("""
    <div style="text-align: center; margin-top: 30px;">
        <p class="heart">❤️ 这是只属于我们的小世界 ❤️</p>
        <p style="color: #999; font-size: 12px;">悄悄告诉你：每隔一段时间会有小惊喜哦～</p>
    </div>
""", unsafe_allow_html=True)
