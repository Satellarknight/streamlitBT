import streamlit as st

# 添加标题
st.title('调查问卷')

# 添加问题和选项
question_1 = st.text_input('问题 1:')
option_1_1 = st.checkbox('选项 1', key='question_1_option_1')
option_1_2 = st.checkbox('选项 2', key='question_1_option_2')

question_2 = st.text_input('问题 2:')
option_2_1 = st.checkbox('选项 1', key='question_2_option_1')
option_2_2 = st.checkbox('选项 2', key='question_2_option_2')

# 显示提交按钮
submit_button = st.button('提交')

# 创建一个字典来存储用户答案
user_answers = {}

# 处理提交按钮的点击事件
if submit_button:
    # 存储用户的答案
    user_answers['问题 1'] = {
        '选项 1': option_1_1,
        '选项 2': option_1_2
    }
    
    user_answers['问题 2'] = {
        '选项 1': option_2_1,
        '选项 2': option_2_2
    }
    
    # 打印用户的答案
    st.write('提交的答案是:')
    for question, options in user_answers.items():
        st.write(question)
        for option, value in options.items():
            if value:
                st.write(f'- {option}')

    # 显示感谢信息或其他处理
    st.write('谢谢参与调查！')