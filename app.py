from dotenv import load_dotenv
load_dotenv()

#LLM : input_messageをプロンプトに渡す処理
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

#画面作成
import streamlit as st

st.title("専門家アプリ")

#ラジオボタン
st.write("##### 専門家選択：どちらの専門家にききたいか選択してください")
selected_item = st.radio(
    "専門家を選択してください。",
    ["優しい専門家", "厳しい専門家"]
)
st.divider()

#入力フォーム
st.write("専門家に聞きたいことを入力して「実行」ボタンを押してください。")
input_message = st.text_input(label="聞きたい内容はなんですか？")

#実行ボタン
if st.button("実行"):
    st.divider()
    
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    #優しい専門家の応答
    if selected_item == "優しい専門家":
        messages = [
            SystemMessage(content="You are a kind and helpful expert. Always respond in a gentle and supportive manner."),
            HumanMessage(content=input_message),
        ]

        result = llm(messages)

    #厳しい専門家の応答
    elif selected_item == "厳しい専門家":
        messages = [
            SystemMessage(content="You are a strict and no-nonsense expert. Always respond in a direct and firm manner."),
            HumanMessage(content=input_message),
        ]
    
        result = llm(messages)

        st.write(f"専門家の回答：{result.content}")
   
   


