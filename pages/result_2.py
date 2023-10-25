import streamlit as st
import re
from bardapi import Bard
from utils import clear_messages
import traceback

def render():
    st.title("result_2")
    
    if st.button("처음으로"):
        clear_messages()
        st.session_state.page = 'get_user_info'
    
    if 'prep_question' not in st.session_state:
        st.session_state.prep_questions = \
        {
            0 : ['0. 칼로리는 어떤 방식에 의해 계산되는거야?', '저희 프로그램은 스코필드 계산법을 사용해 적정 칼로리를 계산합니다.'],
            1 : ['1. 성인 하루 평균 필요 칼로리는 어느정도야?', '개인에 따른 차이가 존재하지만 일반적으로 성인이 하루에 필요한 칼로리는 대략 2000~2500칼로리입니다.'],
            2 : ['2. 트랜스 지방이 뭐야?', '트랜스 지방은 일부 식품 가공 과정에서 생성되는 불포화 지방산의 한 형태입니다. 트랜스 지방은 다양한 가공식품에 포함되어 있는데, 제품의 보관성과 맛을 개선하는데 도움이 되지만 심혈관 질환의 위험성을 증가시키는것으로 알려져 있습니다. 또한, 국내 가공식품은 0~0.5g의 트랜스지방이 포함되어 있을 경우 0g으로 표기할 수 있습니다.'],
            3 : ['3. 나트륨 함량이 높으면 어떤 악영향이 있을까?', '과도한 나트륨 섭취는 고혈압과 같은 건강 문제를 초래할 수 있으므로, 하루 권장 나트륨 섭취량인 2000mg를 넘지 않도록 주의해야 합니다.'],
            4 : ['4. 설탕 함량이 높은 음식을 자주 먹으면 어떤 문제가 있을까?', '설탕 함유량이 높은 음식을 자주 섭취하면, 체중 증가와 비만, 2형 당뇨병, 심혈관 질환 등의 위험성이 증가합니다. 또한 구강 건강 문제(예: 충치)를 야기할 수 있습니다.'],
            5 : ['5. 포화지방과 불포화지방의 차이점은 무엇일까?', '포화지방은 탄소 원자 사이에 단일 결합만 있는 지방으로, 주로 동물성 식품에 있습니다. LDL 콜레스테롤을 높여 심혈관 질환 위험을 증가시킬 수 있습니다. 불포화지방은 하나 이상의 탄소-탄소 이중 결합을 가진 지방으로, 식물성 오일과 어류 등에서 찾아볼 수 있습니다. 건강한 심장 기능 유지에 도움이 됩니다. 따라서, 포화지방 섭취는 줄이고 불포화지방 섭취를 증가시켜야 합니다.'],
            6 : ['6. 인공 향료와 천연 향료의 차이점이 뭐야?', '인공 향료와 천연 향료 모두 같은 화학적 구조를 가지지만, 인공 향료는 화학적으로 합성되며, 천연 향료는 자연에서 얻어집니다.']
        }
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
        for _, v in st.session_state.prep_questions.items():
            st.session_state.messages.append({"role": "assistant", "content": v[0]})

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if user_input := st.chat_input("What is up?"):
        # 입력값이 0~9이면 사전질문으로 대체해서 화면 표시
        if len(user_input) == 1 and re.match('[0-9]', user_input): 
            # Display user message in chat message container
            st.chat_message("user").markdown(st.session_state.prep_questions[int(user_input)][0])
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": st.session_state.prep_questions[int(user_input)][0]})
            response = st.session_state.prep_questions[int(user_input)][1]
        else:
            # Display user message in chat message container
            st.chat_message("user").markdown(user_input)
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": user_input})
            try:
                print("bard api 호출 시도")
                user_input =\
                f'''
                다음은 나의 성별, 키, 몸무게, 일일 소모 칼로리야.

                성별 : {st.session_state.user_info['gender']},
                키 : {st.session_state.user_info['height']},
                몸무게 : {st.session_state.user_info['weight']},
                일일 소모 칼로리 : {st.session_state.user_info['calories']}\n
                
                이상 나에 대한 정보를 인지한 상태에서 다음 질문에 답변하되
                건강, 영양, 식품 등에 대한 질문이 아니라면 위 정보는 무시하고 그냥 답변해줘.
                또한 질문에 대한 답변만을 표시하고 왜 그런식으로 답변을 하는지에 대한 정보는 표시하지 말아줘\n
                ''' + user_input
                response = Bard().get_answer(user_input)['content']
            except Exception as e:
                print("bard api 호출 실패")
                traceback.print_exc()
                st.warning('bard api 호출 실패!')
        
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
