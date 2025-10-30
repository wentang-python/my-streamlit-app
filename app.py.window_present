import streamlit as st
import random
import time

# 设置页面
st.set_page_config(
    page_title="暖心提示小助手",
    page_icon="💖",
    layout="centered"
)

# 应用标题和描述
st.title("💖 暖心提示小助手")
st.markdown("随机显示温馨提示的小应用～")
st.markdown("---")

# 定义颜色方案（保持原程序的配色）
bg_schemes = [
    {'bg': '#FFE4E6', 'fg': '#BE123C'},  # 粉红
    {'bg': '#F0F9FF', 'fg': '#0369A1'},  # 蓝色
    {'bg': '#F0FDF4', 'fg': '#15803D'},  # 绿色
    {'bg': '#FEF7CD', 'fg': '#854D0E'},  # 黄色
    {'bg': '#FAF5FF', 'fg': '#7C3AED'},  # 紫色
]

# 暖心提示语列表（保持原样）
tips = [
    "在干嘛", "笨蛋琪", "所有烦恼都消失", "小胖脸",
    "好好加油", "早点休息", "期待下一次见面", "顺顺利利",
    "每天元气满满", "你很棒了", "每天都要开心", "记得想我",
    "按时吃饭啊笨", "记得回我消息啊笨", "多笑笑啊笨", "相信你"
]

# 控制按钮
col1, col2 = st.columns(2)
with col1:
    if st.button("🎯 开始显示提示", type="primary"):
        # 创建占位符用于动态更新
        tip_placeholder = st.empty()
        
        # 显示多个提示窗口
        for i in range(10):  # 显示10次提示
            # 随机选择颜色和提示语
            scheme = random.choice(bg_schemes)
            tip = random.choice(tips)
            
            # 使用HTML/CSS创建浮动卡片效果
            tip_placeholder.markdown(
                f"""
                <div style="
                    background-color: {scheme['bg']};
                    color: {scheme['fg']};
                    padding: 30px;
                    border-radius: 15px;
                    border: 2px solid {scheme['fg']};
                    text-align: center;
                    margin: 20px 0;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                    animation: fadeIn 0.5s ease-in;
                ">
                    <h2 style="margin: 0; font-size: 24px;">{tip}</h2>
                    <p style="margin: 10px 0 0 0; opacity: 0.7;">提示 #{i+1}</p>
                </div>
                <style>
                @keyframes fadeIn {{
                    from {{ opacity: 0; transform: translateY(-10px); }}
                    to {{ opacity: 1; transform: translateY(0); }}
                }}
                </style>
                """, 
                unsafe_allow_html=True
            )
            
            # 等待一段时间后显示下一个（模拟原程序的延时）
            time.sleep(1.5)
        
        # 最后显示结束信息
        tip_placeholder.success("🎉 所有提示显示完成！可以再次点击按钮重新开始～")

with col2:
    if st.button("🔄 重置"):
        st.rerun()

# 提示信息统计
st.markdown("---")
st.subheader("📊 提示库统计")
st.write(f"当前共有 **{len(tips)}** 条温馨提示语")
st.write(f"可用颜色方案：**{len(bg_schemes)}** 种")

# 显示所有提示语
with st.expander("📝 查看所有提示语"):
    cols = st.columns(3)
    for i, tip in enumerate(tips):
        with cols[i % 3]:
            st.info(f"{i+1}. {tip}")

# 页脚
st.markdown("---")
st.caption("✨ 基于原 tkinter 程序转换的 Streamlit 网页版 | 温馨每一天")
