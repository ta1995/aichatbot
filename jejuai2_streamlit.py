import requests
import streamlit as st

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "a6bfdaa0-974a-11ef-8313-8118934c035dd2637ab3-3985-4e9a-8e38-4d966aa9e86c"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


# CHANGE THIS to something you want your machine learning model to classify
while True:
    #question = input("제주도에 대해 궁금한 것을 물어봐 주세요>>")
    question = st.text_input("제주도에 대해 궁금한 것을 물어봐 주세요>> ", "")

    #if question != "":
    if len(question)>0:    
        #if (question == "나가기"):
        #  break

        demo = classify(question)
        label = demo["class_name"]
        confidence = demo["confidence"]

        # if confidence < 70:
        #     st.write("질문을 이해하지 못했어요. 다시 질문해 주시겠어요?")
        # elif label == "food":
        #     st.write("제주도하면 고기국수를 먹어보세요. 어디든 다 맛있답니다. 유명 흑되지집에서 먹어보는 것도 좋겠습니다.")
        #     st.write("답변 정확되:", confidence)
        # elif label == "cafe":
        #     st.write("애월에는 예쁘고 유명한 카페들이 많아요. 어디든 전망도 졸고 커피도 맛있으니 그 주에서 골라보세요. 참, 요즘엔 도넛집도 핫하다고 해요.")
        #     st.write("답변 정확되:", confidence)
        # elif label == "hotplace":
        #     st.write("제주도에서 올레길 한번은 걸어보는 것도 좋겠죠? 저녁에 야시장을 둘러 보는 것도 추천해요. 무엇보다 제주하면 바다죠? 예쁜 세화해변도 추천해요.")
        #     st.write("답변 정확되:", confidence)

        # CHANGE THIS to do something different with the result
        st.write("result: '%s' with %d%% confidence" % (label, confidence))
    else:
        st.write("검색어 입력")
