import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# タイトル
st.title("🌟 Streamlit サンプルアプリ")

# 説明文
st.markdown("""
このアプリは Streamlit の基本機能をまとめたサンプルです。

以下の要素を含んでいます：
- ユーザー入力
- データフレーム表示
- 折れ線グラフの描画
""")

# 入力ウィジェット
name = st.text_input("あなたの名前を入力してください：")
if name:
    st.success(f"{name}さん、ようこそ！")

# スライダー
num_rows = st.slider("表示する行数", min_value=5, max_value=50, value=10)

# ダミーデータ
df = pd.DataFrame({
    "日付": pd.date_range(start="2024-01-01", periods=50),
    "売上": [x * 100 + (x % 5) * 200 for x in range(50)]
})

# 表の表示
st.subheader("📊 売上データ")
st.dataframe(df.head(num_rows))

# グラフ表示
st.subheader("📈 売上の推移（折れ線グラフ）")
fig, ax = plt.subplots()
ax.plot(df["日付"], df["売上"])
ax.set_xlabel("日付")
ax.set_ylabel("売上")
ax.set_title("売上推移")
st.pyplot(fig)
