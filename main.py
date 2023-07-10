import streamlit as st
import smtplib
from email.mime.text import MIMEText

# 添加标题
st.title('User Study')

# 添加问题
st.subheader("Now you want to buy a pair of women's pants, so you see the following six advertisements in the search engine, which one (which ones) do you want to click the most?：")

# 广告选项
ad_options = [
    "Refined Sophistication: Elevate Your Look with Women's Trousers \n\n Achieve a sophisticated and polished look with our women's trousers. Expertly crafted with high-quality fabrics and attention to detail, these trousers offer a combination of elegance, comfort, and style, all for just $100.",
    'ad 2',
    'ad 3',
    'ad 4',
    'ad 5',
    'ad 6'
]

# 为每个广告选项添加选择框
ad_selections = {}
for option in ad_options:
    ad_selections[option] = st.checkbox(option)


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

    # 提取用户选择的广告选项
    selected_ads = [option for option, selected in ad_selections.items() if selected]
    
    # 打印用户选择的广告选项
    st.write('The ads you choose are：')
    for ad in selected_ads:
        st.write(ad)
        
    # 存储用户的答案
    user_answers['ads 1'] = ad_selections[option]
    
    user_answers['ads 2'] = {
        'option 1': option_2_1,
        'option 2': option_2_2
    }
    
    # 打印用户的答案
    st.write('your answer is:')
    for question, options in user_answers.items():
        st.write(question)
        for option, value in options.items():
            if value:
                st.write(f'- {option}')

    # 模拟用户数据
    user_data = user_answers

    # 发送邮件
    #send_email(user_data)

    # 显示感谢信息或其他处理
    st.write('Thanks for taking the survey!')





