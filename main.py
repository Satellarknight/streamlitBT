import streamlit as st
import smtplib
import random
from email.mime.text import MIMEText

random_number = random.random()

def main():
    if st.session_state.page == "Page 1":
        page1()
    elif st.session_state.page == "Page 2":
        page2()
    elif st.session_state.page == "Page 3":
        page3()

def page1():
    # 添加标题
    st.title('User Study')
    # 添加问题和选项
    question_1 = st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> 1. Now you want to buy a pair of women's pants, so you see the following six advertisements in the search engine, which one (which ones) do you want to click the most?：</p>
            <p style='color: brown; font-size: 18px;'>Women's pants: Women's pants are a versatile and essential part of any woman's wardrobe. They come in various styles, fits, and fabrics, offering comfort and style for different occasions. </p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    option_1_1 = st.checkbox("click this option", key='question_1_option_1')
    option_1_1_description = st.markdown("""
        <div>
            <h4 style='color: blue; font-size: 24px;'>Refined Sophistication: Elevate Your Look with Women's Trousers</h4>
            <p style='color: black; font-size: 16px;'>Achieve a sophisticated and polished look with our women's trousers. Expertly crafted with high-quality fabrics and attention to detail, these trousers offer a combination of elegance, comfort, and style.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    option_1_2 = st.checkbox("click this option", key='question_1_option_2')
    option_1_2_description = st.markdown("""
        <div>
            <h4 style='color: blue; font-size: 24px;'>Women's Pants - Watch Out For Exclusive Offers</h4>
            <p style='color: black; font-size: 16px;'>Find a Huge Range of Designers, Brands and Styles. Discover Fashion Online! Discover Inclusive Range & Styles. Enjoy Free Delivery to Switzerland.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    option_1_3 = st.checkbox("click this option", key='question_1_option_3')
    option_1_3_description = st.markdown("""
        <div>
            <h4 style='color: blue; font-size: 24px;'>Women's trousers - Switzerland</h4>
            <p style='color: black; font-size: 16px;'>Women's trousers are an everyday wardrobe staple. With designs from the latest collection, it's easy to create looks that are both stylish and practical.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    option_1_4 = st.checkbox("click this option", key='question_1_option_4')
    option_1_4_description = st.markdown("""
        <div>
            <h4 style='color: blue; font-size: 24px;'>Pants - Women's</h4>
            <p style='color: black; font-size: 16px;'>Sitting, kneeling, scrambling, hiking – These women's pants are durable, breathable, and deliver comfort, freedom of movement, and elemental protection.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    option_1_5 = st.checkbox("click this option", key='question_1_option_5')
    option_1_5_description = st.markdown("""
        <div>
            <h4 style='color: blue; font-size: 24px;'>Versatile Chic: Women's Trousers for Every Occasion</h4>
            <p style='color: black; font-size: 16px;'>Discover the versatility of our women's trousers. From casual outings to formal events, these trousers effortlessly transition between different looks, offering a perfect fit, comfort, and style.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    option_1_6 = st.checkbox("click this option", key='question_1_option_6')
    option_1_6_description = st.markdown("""
        <div>
            <h4 style='color: blue; font-size: 24px;'>Make a Statement: Bold Women's Trousers for the Modern Fashionista</h4>
            <p style='color: black; font-size: 16px;'>Unleash your inner fashionista with our bold women's trousers. Designed to make a statement, these trousers feature unique patterns, vibrant colors, and a perfect blend of style and comfort.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    # 保存答案
    st.session_state.user_answers['ads 1'] = {
        'option 1': option_1_1,
        'option 2': option_1_2,
        'option 3': option_1_3,
        'option 4': option_1_4,
        'option 5': option_1_5,
        'option 6': option_1_6
    }

    if st.button("Next Page"):
        st.session_state.page = "Page 2"
        st.experimental_rerun()

def page2():
    st.title('User Study')
    question_2 = st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> 2. Imagine you are a male college student who usually likes to play the piano. You have three emails in your mailbox selling guitar lessons, which one is your favourite?</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    option_2_1 = st.checkbox("click this option", key='question_2_option_1')
    email_preview_2_1 = """
    ## Expand Your Musical Horizons - Exclusive Guitar Lessons Offer Inside!

    From: sender@gmail.com
    To: recipient@gmail.com

    --- 

    Hey [Name],

    Looking to broaden your musical repertoire?Employee of a male singer who enjoys playing games, I have an exciting opportunity for you. Discover the magic of guitar with our exclusive lessons tailored to the needs of your fellow singer.

    Unleash your creativity, strum your favorite tunes, and gain a deeper understanding of musical theory. Come along for the ultimate experience that'll introduce you to the magic of music.

    Limited spaces available, so secure your spot now! Reply for more details and an exclusive offer that'll transport you to a world of musical wonderland.

    Parley musical love!

    --- 

    Best regards,  
    Sender
    """
    option_2_1_description = st.markdown(email_preview_2_1, unsafe_allow_html=True)
   
    option_2_2 = st.checkbox(" \n\n ", key='question_2_option_2')
    option_2_3 = st.checkbox(" \n\n ", key='question_2_option_3')

    # 保存答案
    st.session_state.user_answers['email 2'] = {
        'option 1': option_2_1,
        'option 2': option_2_2,
        'option 3': option_2_3,
    }

    if st.button("Previous Page"):
        st.session_state.page = "Page 1"
        st.experimental_rerun()

    if st.button("Next Page"):
        st.session_state.page = "Page 3"
        st.experimental_rerun()

def page3():
    question_3 = st.text_input('question 3:')
    option_3_1 = st.checkbox(" \n\n ", key='question_3_option_1')
    option_3_2 = st.checkbox(" \n\n ", key='question_3_option_2')
    option_3_3 = st.checkbox(" \n\n ", key='question_3_option_3')
    option_3_4 = st.checkbox(" \n\n ", key='question_3_option_4')
    option_3_5 = st.checkbox(" \n\n ", key='question_3_option_5')
    option_3_6 = st.checkbox(" \n\n ", key='question_3_option_6')

    # 保存答案
    st.session_state.user_answers['ads 3'] = {
        'option 1': option_3_1,
        'option 2': option_3_2,
        'option 3': option_3_3,
        'option 4': option_3_4,
        'option 5': option_3_5,
        'option 6': option_3_6
    }

    if st.button("Previous Page"):
        st.session_state.page = "Page 2"
        st.experimental_rerun()

    # 显示提交按钮
    submit_button = st.button('submit')
    # 处理提交按钮的点击事件
    if submit_button:

        # 打印用户的答案
        st.write('your answer is:')
        for question, options in st.session_state.user_answers.items():
            st.write(question)
            for option, value in options.items():
                if value:
                    st.write(f'- {option}')

        # 模拟用户数据
        user_data = st.session_state.user_answers

        def send_email(user_data, random_number):
            # 邮件配置
            sender_email = 'BachelorThesisT@outlook.com'
            receiver_email = 'taijunzhe@gmail.com'
            subject = '用户数据'
            message = format_user_data(user_data, random_number)

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

        def format_user_data(user_data, random_number):
            # 格式化用户数据和随机数为邮件内容
            formatted_data = ''
            for key, value in user_data.items():
                formatted_data += f'{key}: {value}\n'
            formatted_data += f'Random Number: {random_number}\n'
            return formatted_data

        # 发送邮件
        send_email(user_data, random_number)

        # 显示感谢信息或其他处理
        st.write('Thanks for taking the survey!')

if __name__ == "__main__":
    # 初始化页面状态
    if "page" not in st.session_state:
        st.session_state.page = "Page 1"
    
    if "user_answers" not in st.session_state:
        st.session_state.user_answers = {}

    # 运行主函数
    main()




