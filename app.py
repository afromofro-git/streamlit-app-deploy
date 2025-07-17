import streamlit as st

st.title("サンプルアプリ②: 少し複雑なWebアプリ")

st.write("##### 動作モード1: 文字数カウント")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで文字数をカウントできます。")
st.write("##### 動作モード2: BMI値の計算")
st.write("入力フォームに体重(kg)と身長(m)を入力し、「実行」ボタンを押すことでBMI値を計算できます。")

selected_item = st.radio(
    "動作モードを選択してください",
    ["文字数カウント", "BMI値の計算"]
)

st.divider()

if selected_item == "文字数カウント":
    input_message = st.text_input("文字数のカウント対象となるテキストと入力してください。")
    text_count = len(input_message)

else:
    height = st.text_input(label = "身長(cm)を入力してください。")
    weight = st.text_input(label = "体重(kg)を入力してください。")
    
if st.button("実行"):
    st.divider()
    if selected_item == "文字数カウント":
        if input_message:
            st.write(f"文字数は {text_count} です。")
        else:
            st.error("カウント対象となるテキストを入力してから「実行」ボタンを押してください。")
    else:
        if height and weight:
            try:
                bmi = round(int(weight) / ((int(height) / 100) ** 2), 1)
                st.write(f"あなたのBMIは {bmi} です。")
            except ValueError as e:
                st.error("身長と体重には数値を入力してください。")
        else:
            st.error("身長と体重を入力してから「実行」ボタンを押してください。")
            