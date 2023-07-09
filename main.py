import streamlit as st
import smtplib
from email.mime.text import MIMEText

# 添加标题
st.title('User Study')

# 添加问题和选项
question_1 = st.text_input('question 1:')
option_1_1 = st.checkbox('option 1', key='question_1_option_1')
option_1_2 = st.checkbox('option 2', key='question_1_option_2')

question_2 = st.text_input('question 2:')
option_2_1 = st.checkbox('option 1', key='question_2_option_1')
option_2_2 = st.checkbox('option 2', key='question_2_option_2')

# 显示提交按钮
submit_button = st.button('submit')

# 创建一个字典来存储用户答案
user_answers = {}

def send_email(user_data):
    # 邮件配置
    sender_email = 'BachelorThesisT@outlook.com'
    receiver_email = 'taijunzhe@gmail.com'
    subject = '用户数据'
    message = format_user_data(user_data)

    # 创建 MIMEText 对象
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # 发送邮件
    try:
        with smtplib.SMTP('smtp.office365.com', 587) as smtp:
            smtp.starttls()
            smtp.login('BachelorThesisT@outlook.com', '1111122222t')
            smtp.send_message(msg)
        print('邮件发送成功')
    except smtplib.SMTPException as e:
        print('邮件发送失败:', str(e))

def format_user_data(user_data):
    # 格式化用户数据为邮件内容
    formatted_data = ''
    for key, value in user_data.items():
        formatted_data += f'{key}: {value}\n'
    return formatted_data

# 处理提交按钮的点击事件
if submit_button:
    # 存储用户的答案
    user_answers['question 1'] = {
        'option 1': option_1_1,
        'option 2': option_1_2
    }
    
    user_answers['question 2'] = {
        'option 1': option_2_1,
        'option 2': option_2_2
    }
    
    # 打印用户的答案
    st.write('提交的答案是:')
    for question, options in user_answers.items():
        st.write(question)
        for option, value in options.items():
            if value:
                st.write(f'- {option}')

    # 模拟用户数据
    user_data = user_answers

    # 发送邮件
    send_email(user_data)

    # 显示感谢信息或其他处理
    st.write('谢谢参与调查！')
