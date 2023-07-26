import streamlit as st
import smtplib
import random
from email.mime.text import MIMEText

random_number = random.random()

def main():
    if st.session_state.page == "Page 0":
        page0()
    elif st.session_state.page == "Page 1":
        page1()
    elif st.session_state.page == "Page 2":
        page2()
    elif st.session_state.page == "Page 3":
        page3()
    elif st.session_state.page == "Page 4":
        page4()
    elif st.session_state.page == "Page 5":
        page5()
    elif st.session_state.page == "Page 6":
        page6()
    elif st.session_state.page == "Page 02":
        page02()
    elif st.session_state.page == "Page 7":
        page7()
    elif st.session_state.page == "Page 8":
        page8()
    elif st.session_state.page == "Page 9":
        page9()
    elif st.session_state.page == "Page 03":
        page03()
    elif st.session_state.page == "Page 10":
        page10()
    elif st.session_state.page == "Page 11":
        page11()


def page0():
    random_number1 = random.randint(1,6)
    # 添加标题
    st.title('User Study')

    # 添加问题和选项
    question_1 = st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> Thank you for participating in our user study. This user study is part of a Bachelor Thesis. We trained a language model that can output different styles of text for online advertisements, and we want to guide and help advertisers and marketers through this model. There are three tasks in this survey. You need to complete all the three tasks.</p>
            <p style='color: black; font-size: 26px;'> ------------------------------------------------------ </p>
            <p style='color: black; font-size: 24px;'> The first task is about online advertising, which simulates the online advertisements that may appear when we use Google search engine.</p>
            <p style='color: brown; font-size: 24px;'> You will see in each advertisement with two options, "I will click on this web page." means that you want to click it subjectively, and "This Ad is attractive." means that you think the advertisement itself is attractive to other people. You can of course choose both or neither. </p>
        </div>
    """, unsafe_allow_html=True)

    if st.button("Next Page"):
        if (random_number1 == 1):
            st.session_state.page = "Page 1"
            st.experimental_rerun()
        elif (random_number1 == 2):
            st.session_state.page = "Page 2"
            st.experimental_rerun()
        elif (random_number1 == 3):
            st.session_state.page = "Page 3"
            st.experimental_rerun()
        elif (random_number1 == 4):
            st.session_state.page = "Page 4"
            st.experimental_rerun()
        elif (random_number1 == 5):
            st.session_state.page = "Page 5"
            st.experimental_rerun()
        else:
            st.session_state.page = "Page 6"
            st.experimental_rerun()

def page1():
    # 添加标题
    st.title('Task 1')
    # 添加问题和选项
    question_1 = st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> 1. Imagine now you want to buy a pair of women's pants, so you see the following six advertisements in the search engine, which one (which ones) do you want to click the most? Please read the six advertisements and answer the questions.</p>
            <p style='color: brown; font-size: 18px;'>Women's pants: Women's pants are a versatile and essential part of any woman's wardrobe. They come in various styles, fits, and fabrics, offering comfort and style for different occasions. </p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_1_1_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 1.</p>
            <h4 style='color: blue; font-size: 24px;'>Refined Sophistication: Elevate Your Look with Women's Trousers</h4>
            <p style='color: black; font-size: 16px;'>Achieve a sophisticated and polished look with our women's trousers. Expertly crafted with high-quality fabrics and attention to detail, these trousers offer a combination of elegance, comfort, and style.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_1_1 = st.checkbox("I will click on this web page.", key='question_1_option_1')
    option_1_11 = st.checkbox("This Ad is attractive.", key='question_1_option_11')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_1_2_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 2.</p>
            <h4 style='color: blue; font-size: 24px;'>Women's Pants - Watch Out For Exclusive Offers</h4>
            <p style='color: black; font-size: 16px;'>Find a Huge Range of Designers, Brands and Styles. Discover Fashion Online! Discover Inclusive Range & Styles. Enjoy Free Delivery to Switzerland.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_1_2 = st.checkbox("I will click on this web page.", key='question_1_option_2')
    option_1_22 = st.checkbox("This Ad is attractive.", key='question_1_option_22')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_1_3_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 3.</p>
            <h4 style='color: blue; font-size: 24px;'>Women's trousers in Switzerland</h4>
            <p style='color: black; font-size: 16px;'>Women's trousers are an everyday wardrobe staple. With designs from the latest collection, it's easy to create looks that are both stylish and practical.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_1_3 = st.checkbox("I will click on this web page.", key='question_1_option_3')
    option_1_33 = st.checkbox("This Ad is attractive.", key='question_1_option_33')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_1_4_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 4.</p>
            <h4 style='color: blue; font-size: 24px;'>Pants - Women's pants</h4>
            <p style='color: black; font-size: 16px;'>Sitting, kneeling, scrambling, hiking – These women's pants are durable, breathable, and deliver comfort, freedom of movement, and elemental protection.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_1_4 = st.checkbox("I will click on this web page.", key='question_1_option_4')
    option_1_44 = st.checkbox("This Ad is attractive.", key='question_1_option_44')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_1_5_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 5.</p>
            <h4 style='color: blue; font-size: 24px;'>Versatile Chic: Women's Trousers for Every Occasion</h4>
            <p style='color: black; font-size: 16px;'>Discover the versatility of our women's trousers. From casual outings to formal events, these trousers effortlessly transition between different looks, offering a perfect fit, comfort, and style.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_1_5 = st.checkbox("I will click on this web page.", key='question_1_option_5')
    option_1_55 = st.checkbox("This Ad is attractive.", key='question_1_option_55')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_1_6_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 6.</p>
            <h4 style='color: blue; font-size: 24px;'>Make a Statement: Bold Women's Trousers for the Modern Fashionista</h4>
            <p style='color: black; font-size: 16px;'>Unleash your inner fashionista with our bold women's trousers. Designed to make a statement, these trousers feature unique patterns, vibrant colors, and a perfect blend of style and comfort.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_1_6 = st.checkbox("I will click on this web page.", key='question_1_option_6')
    option_1_66 = st.checkbox("This Ad is attractive.", key='question_1_option_66')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    question_11 = st.markdown("""
        <div>
            <p style='color: black; font-size: 20px;'> Which ads do you think are generated by AI? </p>
        </div>
    """, unsafe_allow_html=True)

    option_1_111 = st.checkbox("ads 1", key='question_1_option_111')
    option_1_222 = st.checkbox("ads 2", key='question_1_option_222')
    option_1_333 = st.checkbox("ads 3", key='question_1_option_333')
    option_1_444 = st.checkbox("ads 4", key='question_1_option_444')
    option_1_555 = st.checkbox("ads 5", key='question_1_option_555')
    option_1_666 = st.checkbox("ads 6", key='question_1_option_666')
    option_1_777 = st.checkbox("I couldn't tell the difference.", key='question_1_option_777')
    # 保存答案
    st.session_state.user_answers['ads 1'] = {
        'option 1': option_1_1,
        'option 11': option_1_11,
        'option 2': option_1_2,
        'option 22': option_1_22,
        'option 3': option_1_3,
        'option 33': option_1_33,
        'option 4': option_1_4,
        'option 44': option_1_44,
        'option 5': option_1_5,
        'option 55': option_1_55,
        'option 6': option_1_6,
        'option 66': option_1_66,
        'option 111': option_1_111,
        'option 222': option_1_222,
        'option 333': option_1_333,
        'option 444': option_1_444,
        'option 555': option_1_555,
        'option 666': option_1_666,
        'option 777': option_1_777
    }

    if st.button("Next question"):
        st.session_state.page = "Page 02"
        st.experimental_rerun()

def page2():
    # 添加标题
    st.title('Task 1')
    # 添加问题和选项
    question_2 = st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> 1. Imagine now you want to buy a phone good at taking photos, so you see the following six advertisements in the search engine, which one (which ones) do you want to click the most? Please read the six advertisements and answer the questions.</p>
            <p style='color: brown; font-size: 18px;'> Phone good at taking photos: A phone good at taking photos is a phone that is excellent at taking pictures and video. It usually comes with better cameras and other equipment than similarly priced phones. The opposite is a mobile phone that emphasizes gaming performance. </p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_2_1_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 1.</p>
            <h4 style='color: blue; font-size: 24px;'>Indulge in Sophisticated Photography with our Phones</h4>
            <p style='color: black; font-size: 16px;'>Experience the ultimate photography with our sophisticated style phones. Enjoy smooth photo performance, exceptional photo quality, and a breathtaking photo experience that will leave you in awe.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_2_1 = st.checkbox("I will click on this web page.", key='question_2_option_1')
    option_2_11 = st.checkbox("This Ad is attractive.", key='question_2_option_11')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_2_2_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 2.</p>
            <h4 style='color: blue; font-size: 24px;'>Good phone and perfect experience</h4>
            <p style='color: black; font-size: 16px;'>Our mobile phones have excellent cameras to bring you a clear and excellent photography experience. Easy to operate and take great pictures with our mobile phone.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_2_2 = st.checkbox("I will click on this web page.", key='question_2_option_2')
    option_2_22 = st.checkbox("This Ad is attractive.", key='question_2_option_22')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_2_3_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 3.</p>
            <h4 style='color: blue; font-size: 24px;'>Try our professional mobile phone</h4>
            <p style='color: black; font-size: 16px;'>Try our camera phone, professional lens, specially built for you who love to take pictures. Our phone cameras handle good lighting conditions very well.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_2_3 = st.checkbox("I will click on this web page.", key='question_2_option_3')
    option_2_33 = st.checkbox("This Ad is attractive.", key='question_2_option_33')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_2_4_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 4.</p>
            <h4 style='color: blue; font-size: 24px;'>A camera phone for every environment</h4>
            <p style='color: black; font-size: 16px;'>A fantastic camera. Most phone cameras can handle good lighting conditions well, from the flagship class down to budget phones.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_2_4 = st.checkbox("I will click on this web page.", key='question_2_option_4')
    option_2_44 = st.checkbox("This Ad is attractive.", key='question_2_option_44')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_2_5_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 5.</p>
            <h4 style='color: blue; font-size: 24px;'>Stay Ahead of the Photography Curve with our Trendy Style Phones</h4>
            <p style='color: black; font-size: 16px;'>Make a fashion statement while capturing photographs that reflect your lifestyle with our trendy phones. Experience perfect focus, stunning photos, and a perfect blend of style and performance.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_2_5 = st.checkbox("I will click on this web page.", key='question_2_option_5')
    option_2_55 = st.checkbox("This Ad is attractive.", key='question_2_option_55')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_2_6_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 6.</p>
            <h4 style='color: blue; font-size: 24px;'>Unleash Your Creativity with Phones for Photo Excellence</h4>
            <p style='color: black; font-size: 16px;'>Take your photography to the next level with our bold phones. Enjoy unparalleled camera performance, exceptional photo quality, and a breathtaking photo experience that will leave you breathless.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_2_6 = st.checkbox("I will click on this web page.", key='question_2_option_6')
    option_2_66 = st.checkbox("This Ad is attractive.", key='question_2_option_66')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    question_22 = st.markdown("""
        <div>
            <p style='color: black; font-size: 20px;'> Which ads do you think are generated by AI? </p>
        </div>
    """, unsafe_allow_html=True)

    option_2_111 = st.checkbox("ads 1", key='question_2_option_111')
    option_2_222 = st.checkbox("ads 2", key='question_2_option_222')
    option_2_333 = st.checkbox("ads 3", key='question_2_option_333')
    option_2_444 = st.checkbox("ads 4", key='question_2_option_444')
    option_2_555 = st.checkbox("ads 5", key='question_2_option_555')
    option_2_666 = st.checkbox("ads 6", key='question_2_option_666')
    option_2_777 = st.checkbox("I couldn't tell the difference.", key='question_2_option_777')

    # 保存答案
    st.session_state.user_answers['ads 2'] = {
        'option 1': option_2_1,
        'option 11': option_2_11,
        'option 2': option_2_2,
        'option 22': option_2_22,
        'option 3': option_2_3,
        'option 33': option_2_33,
        'option 4': option_2_4,
        'option 44': option_2_44,
        'option 5': option_2_5,
        'option 55': option_2_55,
        'option 6': option_2_6,
        'option 66': option_2_66,
        'option 111': option_2_111,
        'option 222': option_2_222,
        'option 333': option_2_333,
        'option 444': option_2_444,
        'option 555': option_2_555,
        'option 666': option_2_666,
        'option 777': option_2_777
    }

    if st.button("Next question"):
        st.session_state.page = "Page 02"
        st.experimental_rerun()

def page3():
    # 添加标题
    st.title('Task 1')
    # 添加问题和选项
    question_3 = st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> 1. Imagine now you want to buy books in the genre of romance, so you see the following six advertisements in the search engine, which one (which ones) do you want to click the most? Please read the six advertisements and answer the questions.</p>
            <p style='color: brown; font-size: 18px;'> Books in the genre of romance: The romance genre is a popular category of books that consistently churns out bestsellers. The aim of the genre is simple, showcasing a love story where two people overcome adversity to obtain their happily ever after. </p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_3_1_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 1.</p>
            <h4 style='color: blue; font-size: 24px;'>Romance Books | Romance Novels & Love Stories</h4>
            <p style='color: black; font-size: 16px;'>Discover your new favorite romance book at our website. Shop romance best sellers, new releases, bookseller recommendations and more!</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_3_1 = st.checkbox("I will click on this web page.", key='question_3_option_1')
    option_3_11 = st.checkbox("This Ad is attractive.", key='question_3_option_11')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_3_2_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 2.</p>
            <h4 style='color: blue; font-size: 24px;'>Discover Bold and Passionate Love: Romance Books</h4>
            <p style='color: black; font-size: 16px;'>Ignite your imagination with our bold and passionate romance books. Dive into stories that push boundaries, exploring intense emotions, and celebrating the fiery connection between two souls.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_3_2 = st.checkbox("I will click on this web page.", key='question_3_option_2')
    option_3_22 = st.checkbox("This Ad is attractive.", key='question_3_option_22')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_3_3_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 3.</p>
            <h4 style='color: blue; font-size: 24px;'>Unveil Romance Tales</h4>
            <p style='color: black; font-size: 16px;'>Step into a world of refined romance with our book collection. Delve into stories that exude elegance, featuring intriguing characters, intricate plotlines, and a tapestry of emotions.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_3_3 = st.checkbox("I will click on this web page.", key='question_3_option_3')
    option_3_33 = st.checkbox("This Ad is attractive.", key='question_3_option_33')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_3_4_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 4.</p>
            <h4 style='color: blue; font-size: 24px;'>Romance Books - very cheap</h4>
            <p style='color: black; font-size: 16px;'>Get cheap Romance Books from us. With a wide range of romance novels at unbeatable prices, you'll quickly find your next read.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_3_4 = st.checkbox("I will click on this web page.", key='question_3_option_4')
    option_3_44 = st.checkbox("This Ad is attractive.", key='question_3_option_44')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_3_5_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 5.</p>
            <h4 style='color: blue; font-size: 24px;'>Experience Classic Romance Elegance</h4>
            <p style='color: black; font-size: 16px;'>Indulge in the timeless allure of classic romance with our exquisite book collection. Immerse yourself in stories that capture the essence of true love, filled with grace, passion, and undeniable charm.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_3_5 = st.checkbox("I will click on this web page.", key='question_3_option_5')
    option_3_55 = st.checkbox("This Ad is attractive.", key='question_3_option_55')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_3_6_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 6.</p>
            <h4 style='color: blue; font-size: 24px;'>Romance Books House</h4>
            <p style='color: black; font-size: 16px;'>Browse our latest titles in the Romance category to discover your next read from us.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_3_6 = st.checkbox("I will click on this web page.", key='question_3_option_6')
    option_3_66 = st.checkbox("This Ad is attractive.", key='question_3_option_66')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    question_33 = st.markdown("""
        <div>
            <p style='color: black; font-size: 20px;'> Which ads do you think are generated by AI? </p>
        </div>
    """, unsafe_allow_html=True)

    option_3_111 = st.checkbox("ads 1", key='question_3_option_111')
    option_3_222 = st.checkbox("ads 2", key='question_3_option_222')
    option_3_333 = st.checkbox("ads 3", key='question_3_option_333')
    option_3_444 = st.checkbox("ads 4", key='question_3_option_444')
    option_3_555 = st.checkbox("ads 5", key='question_3_option_555')
    option_3_666 = st.checkbox("ads 6", key='question_3_option_666')
    option_3_777 = st.checkbox("I couldn't tell the difference.", key='question_3_option_777')

    # 保存答案
    st.session_state.user_answers['ads 3'] = {
        'option 1': option_3_1,
        'option 11': option_3_11,
        'option 2': option_3_2,
        'option 22': option_3_22,
        'option 3': option_3_3,
        'option 33': option_3_33,
        'option 4': option_3_4,
        'option 44': option_3_44,
        'option 5': option_3_5,
        'option 55': option_3_55,
        'option 6': option_3_6,
        'option 66': option_3_66,
        'option 111': option_3_111,
        'option 222': option_3_222,
        'option 333': option_3_333,
        'option 444': option_3_444,
        'option 555': option_3_555,
        'option 666': option_3_666,
        'option 777': option_3_777
    }

    if st.button("Next question"):
        st.session_state.page = "Page 02"
        st.experimental_rerun()

def page4():
    # 添加标题
    st.title('Task 1')
    # 添加问题和选项
    question_4 = st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> 1. Imagine now you want to buy noise canceling headphones, so you see the following six advertisements in the search engine, which one (which ones) do you want to click the most? Please read the six advertisements and answer the questions.</p>
            <p style='color: brown; font-size: 18px;'> Noise canceling headphones: Noise-cancelling headphones suppress unwanted ambient sounds using active noise control. This is distinct from passive headphones which, if they reduce ambient sounds at all, use techniques such as soundproofing. </p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_4_1_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 1.</p>
            <h4 style='color: blue; font-size: 24px;'>Experience Pure Audio Bliss with Noise-cancelling Headphones</h4>
            <p style='color: black; font-size: 16px;'>Immerse yourself in your favorite music with our noise-reducing headphones. Enjoy crystal-clear sound, enhanced bass, and a comfortable fit.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_4_1 = st.checkbox("I will click on this web page.", key='question_4_option_1')
    option_4_11 = st.checkbox("This Ad is attractive.", key='question_4_option_11')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_4_2_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 2.</p>
            <h4 style='color: blue; font-size: 24px;'>Elevate Your Listening Experience with Noise-cancelling Headphones</h4>
            <p style='color: black; font-size: 16px;'>Indulge in the ultimate audio luxury with our noise-cancelling headphones. Enjoy crisp, immersive sound, advanced noise cancellation technology, and a sleek design.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_4_2 = st.checkbox("I will click on this web page.", key='question_4_option_2')
    option_4_22 = st.checkbox("This Ad is attractive.", key='question_4_option_22')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_4_3_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 3.</p>
            <h4 style='color: blue; font-size: 24px;'>Noise-cancelling headphones</h4>
            <p style='color: black; font-size: 16px;'>Here are the best noise-cancelling headphones money can buy, from over-ear cans to wireless earbuds for blocking out sound.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_4_3 = st.checkbox("I will click on this web page.", key='question_4_option_3')
    option_4_33 = st.checkbox("This Ad is attractive.", key='question_4_option_33')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_4_4_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 4.</p>
            <h4 style='color: blue; font-size: 24px;'>Best noise canceling headphones</h4>
            <p style='color: black; font-size: 16px;'>If you're wondering what are the best noise canceling headphones you can get, we've got you covered. Experience perfection with our noise canceling headphones.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_4_4 = st.checkbox("I will click on this web page.", key='question_4_option_4')
    option_4_44 = st.checkbox("This Ad is attractive.", key='question_4_option_44')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_4_5_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 5.</p>
            <h4 style='color: blue; font-size: 24px;'>Buy noise-canceling headphones</h4>
            <p style='color: black; font-size: 16px;'>Buy noise-canceling headphones? Delivered on Sunday and in the evening. Noise-canceling headphones at Switzerland: free delivery & returns</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_4_5 = st.checkbox("I will click on this web page.", key='question_4_option_5')
    option_4_55 = st.checkbox("This Ad is attractive.", key='question_4_option_55')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_4_6_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 6.</p>
            <h4 style='color: blue; font-size: 24px;'>Immerse Yourself in Sound with Noise-cancelling Headphones</h4>
            <p style='color: black; font-size: 16px;'>Experience the freedom of exceptional sound quality with our noise-cancelling headphones. Whether you're in a noisy environment or on the go, enjoy immersive audio and peace of mind.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_4_6 = st.checkbox("I will click on this web page.", key='question_4_option_6')
    option_4_66 = st.checkbox("This Ad is attractive.", key='question_4_option_66')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    question_44 = st.markdown("""
        <div>
            <p style='color: black; font-size: 20px;'> Which ads do you think are generated by AI? </p>
        </div>
    """, unsafe_allow_html=True)

    option_4_111 = st.checkbox("ads 1", key='question_4_option_111')
    option_4_222 = st.checkbox("ads 2", key='question_4_option_222')
    option_4_333 = st.checkbox("ads 3", key='question_4_option_333')
    option_4_444 = st.checkbox("ads 4", key='question_4_option_444')
    option_4_555 = st.checkbox("ads 5", key='question_4_option_555')
    option_4_666 = st.checkbox("ads 6", key='question_4_option_666')
    option_4_777 = st.checkbox("I couldn't tell the difference.", key='question_4_option_777')

    # 保存答案
    st.session_state.user_answers['ads 4'] = {
        'option 1': option_4_1,
        'option 11': option_4_11,
        'option 2': option_4_2,
        'option 22': option_4_22,
        'option 3': option_4_3,
        'option 33': option_4_33,
        'option 4': option_4_4,
        'option 44': option_4_44,
        'option 5': option_4_5,
        'option 55': option_4_55,
        'option 6': option_4_6,
        'option 66': option_4_66,
        'option 111': option_4_111,
        'option 222': option_4_222,
        'option 333': option_4_333,
        'option 444': option_4_444,
        'option 555': option_4_555,
        'option 666': option_4_666,
        'option 777': option_4_777
    }

    if st.button("Next question"):
        st.session_state.page = "Page 02"
        st.experimental_rerun()

def page5():
    # 添加标题
    st.title('Task 1')
    # 添加问题和选项
    question_5 = st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> 1. Imagine now you want to buy a sheath dress, so you see the following six advertisements in the search engine, which one (which ones) do you want to click the most? Please read the six advertisements and answer the questions.</p>
            <p style='color: brown; font-size: 18px;'> Sheath dress: In fashion, a sheath dress is a fitted, straight cut dress, often nipped at the waistline with no waist seam. </p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_5_1_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 1.</p>
            <h4 style='color: blue; font-size: 24px;'>Sheath Dresses for Women</h4>
            <p style='color: black; font-size: 16px;'>Shop women's sheath dresses from us for a stylish selection of sheath dresses for work, casual occasions and more. Explore our wide selection today!</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_5_1 = st.checkbox("I will click on this web page.", key='question_5_option_1')
    option_5_11 = st.checkbox("This Ad is attractive.", key='question_5_option_11')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_5_2_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 2.</p>
            <h4 style='color: blue; font-size: 24px;'>Sheath Dresses For Women</h4>
            <p style='color: black; font-size: 16px;'>From your everyday look to a formal ensemble, we have the dresses to meet your style needs. Shop for Sheath women's casual, special occasion, cocktail, and party dresses, formal gowns, and more, available in missy, plus, and petite sizes.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_5_2 = st.checkbox("I will click on this web page.", key='question_5_option_2')
    option_5_22 = st.checkbox("This Ad is attractive.", key='question_5_option_22')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_5_3_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 3.</p>
            <h4 style='color: blue; font-size: 24px;'>Sleek Sheath Dresses</h4>
            <p style='color: black; font-size: 16px;'>Achieve an aura of sophistication with our sleek sheath dresses. Tailored to perfection, these dresses embody refined elegance.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_5_3 = st.checkbox("I will click on this web page.", key='question_5_option_3')
    option_5_33 = st.checkbox("This Ad is attractive.", key='question_5_option_33')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_5_4_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 4.</p>
            <h4 style='color: blue; font-size: 24px;'>From Desk to Dinner: Versatile Sheath Dresses</h4>
            <p style='color: black; font-size: 16px;'>Discover the versatility of our sheath dresses. From office meetings to evening soirees, these dresses effortlessly transition with you.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_5_4 = st.checkbox("I will click on this web page.", key='question_5_option_4')
    option_5_44 = st.checkbox("This Ad is attractive.", key='question_5_option_44')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_5_5_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 5.</p>
            <h4 style='color: blue; font-size: 24px;'>On-Trend Chic: Trendy Sheath Dresses for Fashionistas</h4>
            <p style='color: black; font-size: 16px;'>Stay ahead of the fashion curve with our collection of trendy sheath dresses. Designed with the latest trends in mind, these dresses combine style and sophistication.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_5_5 = st.checkbox("I will click on this web page.", key='question_5_option_5')
    option_5_55 = st.checkbox("This Ad is attractive.", key='question_5_option_55')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_5_6_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 6.</p>
            <h4 style='color: blue; font-size: 24px;'>Elegant Sheath Dress</h4>
            <p style='color: black; font-size: 16px;'>High Quality Dresses at Low Cost 1000+ Styles, Colours & Size. With many years of experience, we pride ourselves on our quality materials and service.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_5_6 = st.checkbox("I will click on this web page.", key='question_4_option_6')
    option_5_66 = st.checkbox("This Ad is attractive.", key='question_5_option_66')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    question_55 = st.markdown("""
        <div>
            <p style='color: black; font-size: 20px;'> Which ads do you think are generated by AI? </p>
        </div>
    """, unsafe_allow_html=True)

    option_5_111 = st.checkbox("ads 1", key='question_5_option_111')
    option_5_222 = st.checkbox("ads 2", key='question_5_option_222')
    option_5_333 = st.checkbox("ads 3", key='question_5_option_333')
    option_5_444 = st.checkbox("ads 4", key='question_5_option_444')
    option_5_555 = st.checkbox("ads 5", key='question_5_option_555')
    option_5_666 = st.checkbox("ads 6", key='question_5_option_666')
    option_5_777 = st.checkbox("I couldn't tell the difference.", key='question_5_option_777')

    # 保存答案
    st.session_state.user_answers['ads 5'] = {
        'option 1': option_5_1,
        'option 11': option_5_11,
        'option 2': option_5_2,
        'option 22': option_5_22,
        'option 3': option_5_3,
        'option 33': option_5_33,
        'option 4': option_5_4,
        'option 44': option_5_44,
        'option 5': option_5_5,
        'option 55': option_5_55,
        'option 6': option_5_6,
        'option 66': option_5_66,
        'option 111': option_5_111,
        'option 222': option_5_222,
        'option 333': option_5_333,
        'option 444': option_5_444,
        'option 555': option_5_555,
        'option 666': option_5_666,
        'option 777': option_5_777
    }

    if st.button("Next question"):
        st.session_state.page = "Page 02"
        st.experimental_rerun()

def page6():
    # 添加标题
    st.title('Task 1')
    # 添加问题和选项
    question_6 = st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> 1. Imagine now you want to buy fantasy books, so you see the following six advertisements in the search engine, which one (which ones) do you want to click the most? Please read the six advertisements and answer the questions.</p>
            <p style='color: brown; font-size: 18px;'>Fantasy books: Fantasy literature is literature set in an imaginary universe, often but not always without any locations, events, or people from the real world. Magic, the supernatural and magical creatures are common in many of these imaginary worlds. </p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_6_1_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 1.</p>
            <h4 style='color: blue; font-size: 24px;'>Fantasy Books</h4>
            <p style='color: black; font-size: 16px;'>Click to View Our Range of Fantasy Books Including all Best Sellers and New Releases。With Something For Everyone, A Top Selling Title Makes The Perfect Gift.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_6_1 = st.checkbox("I will click on this web page.", key='question_6_option_1')
    option_6_11 = st.checkbox("This Ad is attractive.", key='question_6_option_11')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_6_2_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 2.</p>
            <h4 style='color: blue; font-size: 24px;'>Experience Enchanting Worlds: Fantasy Books</h4>
            <p style='color: black; font-size: 16px;'>Immerse yourself in the timeless allure of fantasy with our collection of classic books. Unleash your imagination and embark on magical adventures.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_6_2 = st.checkbox("I will click on this web page.", key='question_6_option_2')
    option_6_22 = st.checkbox("This Ad is attractive.", key='question_6_option_22')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_6_3_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 3.</p>
            <h4 style='color: blue; font-size: 24px;'>Fantasy Fiction Books & Box Sets</h4>
            <p style='color: black; font-size: 16px;'>Get cheap Fantasy Books from us. With a wide range of fantasy fiction books and box sets to choose from, you'll quickly find your next read.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_6_3 = st.checkbox("I will click on this web page.", key='question_6_option_3')
    option_6_33 = st.checkbox("This Ad is attractive.", key='question_6_option_33')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_6_4_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 4.</p>
            <h4 style='color: blue; font-size: 24px;'>Unleash Your Imagination: Epic Fantasy Books </h4>
            <p style='color: black; font-size: 16px;'>Dive into the realm of epic fantasy with our bold selection of books. Discover captivating worlds, mythical creatures, and heroic quests.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_6_4 = st.checkbox("I will click on this web page.", key='question_6_option_4')
    option_6_44 = st.checkbox("This Ad is attractive.", key='question_6_option_44')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_6_5_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 5.</p>
            <h4 style='color: blue; font-size: 24px;'>Indulge in Enthralling Tales: Refined Fantasy Books</h4>
            <p style='color: black; font-size: 16px;'>Escape into enchanting narratives with our curated collection of fantasy books. Lose yourself in captivating storytelling and embark on extraordinary journeys.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_6_5 = st.checkbox("I will click on this web page.", key='question_6_option_5')
    option_6_55 = st.checkbox("This Ad is attractive.", key='question_6_option_55')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    option_6_6_description = st.markdown("""
        <div>
            <p style='font-size: 24px;'>Ad 6.</p>
            <h4 style='color: blue; font-size: 24px;'>Shop Online for Fantasy Books</h4>
            <p style='color: black; font-size: 16px;'>Discover the best books in Fantasy Books with fast shipping. The perfect book is waiting for you.</p>
            <p style='color: green; font-size: 14px;'>www.example.com</p>
            <p style='font-size: 12px;'>Ad</p>
        </div>
    """, unsafe_allow_html=True)

    option_6_6 = st.checkbox("I will click on this web page.", key='question_6_option_6')
    option_6_66 = st.checkbox("This Ad is attractive.", key='question_6_option_66')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    question_66 = st.markdown("""
        <div>
            <p style='color: black; font-size: 20px;'> Which ads do you think are generated by AI? </p>
        </div>
    """, unsafe_allow_html=True)

    option_6_111 = st.checkbox("ads 1", key='question_6_option_111')
    option_6_222 = st.checkbox("ads 2", key='question_6_option_222')
    option_6_333 = st.checkbox("ads 3", key='question_6_option_333')
    option_6_444 = st.checkbox("ads 4", key='question_6_option_444')
    option_6_555 = st.checkbox("ads 5", key='question_6_option_555')
    option_6_666 = st.checkbox("ads 6", key='question_6_option_666')
    option_6_777 = st.checkbox("I couldn't tell the difference.", key='question_6_option_777')

    # 保存答案
    st.session_state.user_answers['ads 6'] = {
        'option 1': option_6_1,
        'option 11': option_6_11,
        'option 2': option_6_2,
        'option 22': option_6_22,
        'option 3': option_6_3,
        'option 33': option_6_33,
        'option 4': option_6_4,
        'option 44': option_6_44,
        'option 5': option_6_5,
        'option 55': option_6_55,
        'option 6': option_6_6,
        'option 66': option_6_66,
        'option 111': option_6_111,
        'option 222': option_6_222,
        'option 333': option_6_333,
        'option 444': option_6_444,
        'option 555': option_6_555,
        'option 666': option_6_666,
        'option 777': option_6_777
    }

    if st.button("Next question"):
        st.session_state.page = "Page 02"
        st.experimental_rerun()

def page02():
    random_number2 = random.randint(1,3)
    # 添加标题
    st.title('User Study')
    # 添加问题和选项
    question_7 = st.markdown("""
        <div>
            <p style='color: black; font-size: 24px;'> The second task is about marketing emails. There are three emails, one is general marketing emails, which is for all user groups. The other two are personalized marketing emails, which are personalized for different user profiles.</p>
            <p style='color: brown; font-size: 24px;'> Each email has two options, "I think this email is relevant to me." means that you subjectively believe that this email contains the information you want to know., and "This email is attractive." means that you think the email itself is attractive to other people. You can of course choose both or neither.</p>
        </div>
    """, unsafe_allow_html=True)

    if st.button("Next Page"):
        if (random_number2 == 1):
            st.session_state.page = "Page 7"
            st.experimental_rerun()
        elif (random_number2 == 2):
            st.session_state.page = "Page 8"
            st.experimental_rerun()
        else:
            st.session_state.page = "Page 9"
            st.experimental_rerun()

def page7():
    st.title('Task 2')
    question_7 = st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> 2. Imagine you are a male college student names James who usually likes to play the piano. You have three emails in your mailbox selling music lessons. Your task is to read three emails and answer questions.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行

    # 广告图片
    st.markdown("""generalized email 1""", unsafe_allow_html=True)
    email_image = "email_musecore.jpg"
    st.image(email_image, width=500)

    option_7_0 = st.checkbox("I think this email is relevant to me.", key='question_7_option_0')
    option_7_00 = st.checkbox("This email is attractive.", key='question_7_option_00')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行

    email_preview_7_1 = """ personalized email 2
    ## Expand Your Musical Horizons - Exclusive music Lessons Offer Inside! ##

    From: Musecore@gmail.com
    To: James@gmail.com

    --- 

    Hey James,

    As a fellow male student and a piano enthusiast, I have an exciting opportunity for you. Our music lessons are designed to enhance your skills in the musical instrument.

    Discover the beauty of music in the comfort of your own home! Our experienced instructors will create a lesson plan tailored to your goals. Practice your skills, record music.

    Limited spaces available, so secure your spot now! Reply for more details and an exclusive offer that will transport you to the music world.

    Strike a musical balance!
    
    Musecore Team

    --- 
    
    """
    option_7_1_description = st.markdown(email_preview_7_1, unsafe_allow_html=True)

    option_7_1 = st.checkbox("I think this email is relevant to me.", key='question_7_option_1')
    option_7_11 = st.checkbox("This email is attractive.", key='question_7_option_11')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行

    email_preview_7_2 = """ personalized email 3
    ## Try our newest music course! ##

    From: Musecore@gmail.com
    To: James@gmail.com

    --- 

    Hey James,

    We have the latest online music courses! It is specially set up for male college students who like music, and the time is flexible. 
    
    You will form your own independent musical thinking in the process of learning, and better complete each of your musical works.

    Quantities are limited, please reply immediately for more information if you are interested!

    Parley musical love!

    Best regards,  
    Musecore Team

    --- 
    
    """
    option_7_2_description = st.markdown(email_preview_7_2, unsafe_allow_html=True)

    option_7_2 = st.checkbox("I think this email is relevant to me.", key='question_7_option_2')
    option_7_22 = st.checkbox("This email is attractive.", key='question_7_option_22')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    question_77 = st.markdown("""
        <div>
            <p style='color: black; font-size: 20px;'> Which email do you think is generated by AI? </p>
        </div>
    """, unsafe_allow_html=True)

    option_7_000 = st.checkbox("generalized email 1", key='question_7_option_000')
    option_7_111 = st.checkbox("personalized email 2", key='question_7_option_111')
    option_7_222 = st.checkbox("personalized email 3", key='question_7_option_222')

    # 保存答案
    st.session_state.user_answers['email 1'] = {
        'option 1': option_7_1,
        'option 11': option_7_11,
        'option 2': option_7_2,
        'option 22': option_7_22,
        'option 0': option_7_0,
        'option 00': option_7_00,
        'option 000': option_7_000,
        'option 111': option_7_111,
        'option 222': option_7_222
    }

    if st.button("Previous question"):
        st.session_state.page = "Page 0"
        st.experimental_rerun()

    if st.button("Next question"):
        st.session_state.page = "Page 03"
        st.experimental_rerun()

def page8():
    st.title('Task 2')
    question_8 = st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> 2. Imagine you are a female conpany employees names Lina who wants to relax. You have three emails in your mailbox selling vacation plans. Your task is to read three emails and answer questions.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行

    email_preview_8_0 = """ generalized email 1
    ## Find your next luxury break with Beyond Queues: Luxury Travel ##

    From: Beyondqueues@gmail.com
    To: Lina@gmail.com

    --- 

    Find amazing vacation rentals from the world's most exotic locations. Explore the wonderous landscapes whilst relaxing at your leisure.

    Beyondqueues Team

    --- 
    
    """
    option_8_0_description = st.markdown(email_preview_8_0, unsafe_allow_html=True)

    option_8_0 = st.checkbox("I think this email is relevant to me.", key='question_8_option_0')
    option_8_00 = st.checkbox("This email is attractive.", key='question_8_option_00')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行

    email_preview_8_1 = """ personalized email 2
    ## Your Luxury Travel summer specials. ##

    From: Beyondqueues@gmail.com
    To: Lina@gmail.com

    --- 

    Dear Mrs Lina
 
    It's time for summer, sun and fun in the water! Enjoy the warmest season of the year with beautiful hotel stays and unforgettable leisure experiences on the water and in the mountains. And best of all – you’ll travel comfortably, affordably and sustainably.

    Quantities are limited, please reply immediately for more information if you are interested!

    Beyondqueues Team

    --- 
    
    """
    option_8_1_description = st.markdown(email_preview_8_1, unsafe_allow_html=True)

    option_8_1 = st.checkbox("I think this email is relevant to me.", key='question_8_option_1')
    option_8_11 = st.checkbox("This email is attractive.", key='question_8_option_11')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行

    email_preview_8_2 = """ personalized email 3
    ## Embrace Tranquility - Exclusive Vacation Offer Inside! ##

    From: Beyondqueues@gmail.com
    To: Lina@gmail.com

    --- 

    Hey Lina,

    In need of a well-deserved break? As a female professional who wants to unwind and recharge, I have an exciting vacation plan tailored just for you. Step away from the office and immerse yourself in breathtaking landscapes that will transport you to a world of serenity.

    Indulge in mesmerizing vistas, explore hidden gems, and unwind amidst nature's wonders. Our curated package offers a perfect blend of relaxation and adventure, creating unforgettable memories for you and your colleagues.

    Limited availability, so don't miss out on this exclusive offer. Reply now for more details and embark on a journey of serenity with our exceptional vacation plans.

    Rediscover tranquility!
 
    Beyondqueues Team

    --- 
    
    """
    option_8_2_description = st.markdown(email_preview_8_2, unsafe_allow_html=True)

    option_8_2 = st.checkbox("I think this email is relevant to me.", key='question_8_option_2')
    option_8_22 = st.checkbox("This email is attractive.", key='question_8_option_22')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    question_88 = st.markdown("""
        <div>
            <p style='color: black; font-size: 20px;'> Which email do you think is generated by AI? </p>
        </div>
    """, unsafe_allow_html=True)

    option_8_000 = st.checkbox("generalized email 1", key='question_8_option_000')
    option_8_111 = st.checkbox("personalized email 2", key='question_8_option_111')
    option_8_222 = st.checkbox("personalized email 3", key='question_8_option_222')

    # 保存答案
    st.session_state.user_answers['email 2'] = {
        'option 1': option_8_1,
        'option 11': option_8_11,
        'option 2': option_8_2,
        'option 22': option_8_22,
        'option 0': option_8_0,
        'option 00': option_8_00,
        'option 000': option_8_000,
        'option 111': option_8_111,
        'option 222': option_8_222
    }

    if st.button("Previous question"):
        st.session_state.page = "Page 0"
        st.experimental_rerun()

    if st.button("Next question"):
        st.session_state.page = "Page 03"
        st.experimental_rerun()

def page9():
    st.title('Task 2')
    question_9 = st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> 2. Imagine you are a middle-aged female employee names Elice. You have three emails in your mailbox selling vitamin C health products. Your task is to read three emails and answer questions.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行

    email_preview_9_0 = """ generalized email 1
    ## A Guide to Vitamin C: Health Benefits and Best Sources ##

    From: Fullscript@gmail.com
    To: Elice@gmail.com

    --- 

    Many of us live fast-paced, hyper-productive, busy lifestyles, and the last thing we want is to be down and out with a bug. When it comes to preventing ailments, there are simple steps we can take to support our immune system.
    
    Luckily, vitamin C is known for its immunity-boosting properties, not to mention a whole range of other health benefits. Supplement with Vitamin C with our product!

    Fullscript Team

    --- 
    
    """
    option_9_0_description = st.markdown(email_preview_9_0, unsafe_allow_html=True)

    option_9_0 = st.checkbox("I think this email is relevant to me.", key='question_9_option_0')
    option_9_00 = st.checkbox("This email is attractive.", key='question_9_option_00')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行

    email_preview_9_1 = """ personalized email 2
    ## Elevate Your Immune System - Exclusive Vitamin C Offer Inside! ##

    From: Fullscript@gmail.com
    To: Elice@gmail.com

    --- 

    Hey Elice,

    As a vulnerable female professional, I understand the importance of your immune system. That's why I'm thrilled to introduce our exclusive vitamin C supplement, which will enhance your defenses and boost your overall well-being.

    Discover a range of immuneboosting nutrients that support optimal functioning of your immune cells! 

    Limited availability, so don't miss out on this exclusive offer. Reply now for more details and elevate your immune system with our exceptional vitamin C.

    Invest in yourself, thrive!

    Fullscript Team

    --- 
    
    """
    option_9_1_description = st.markdown(email_preview_9_1, unsafe_allow_html=True)

    option_9_1 = st.checkbox("I think this email is relevant to me.", key='question_9_option_1')
    option_9_11 = st.checkbox("This email is attractive.", key='question_9_option_11')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行

    email_preview_9_2 = """ personalized email 3
    ## Best Vitamin C products especially for you! ##

    From: Fullscript@gmail.com
    To: Elice@gmail.com

    --- 

    Hey Elice,

    Please pay attention to our latest vitamin C health products! It is especially recommended for middle-aged female employees like you to improve immunity, work and live better!
    
    Quantities are limited, please reply immediately for more information if you are interested!

    Invest in yourself, thrive!
 
    Fullscript Team

    --- 
    
    """
    option_9_2_description = st.markdown(email_preview_9_2, unsafe_allow_html=True)

    option_9_2 = st.checkbox("I think this email is relevant to me.", key='question_9_option_2')
    option_9_22 = st.checkbox("This email is attractive.", key='question_9_option_22')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    question_99 = st.markdown("""
        <div>
            <p style='color: black; font-size: 20px;'> Which email do you think is generated by AI? </p>
        </div>
    """, unsafe_allow_html=True)

    option_9_000 = st.checkbox("generalized email 1", key='question_9_option_000')
    option_9_111 = st.checkbox("personalized email 2", key='question_9_option_111')
    option_9_222 = st.checkbox("personalized email 3", key='question_9_option_222')

    # 保存答案
    st.session_state.user_answers['email 3'] = {
        'option 1': option_9_1,
        'option 11': option_9_11,
        'option 2': option_9_2,
        'option 22': option_9_22,
        'option 0': option_9_0,
        'option 00': option_9_00,
        'option 000': option_9_000,
        'option 111': option_9_111,
        'option 222': option_9_222
    }

    if st.button("Previous question"):
        st.session_state.page = "Page 0"
        st.experimental_rerun()

    if st.button("Next question"):
        st.session_state.page = "Page 03"
        st.experimental_rerun()

def page03():
    random_number3 = random.randint(1,2)
    # 添加标题
    st.title('User Study')
    # 添加问题和选项
    question_10 = st.markdown("""
        <div>
            <p style='color: black; font-size: 24px;'> The third task is about online advertising that might appear when we use social media. Some of the ads are generated by our model.</p>
            <p style='color: brown; font-size: 24px;'> Each advertisement has two options, "I will click on this Ad." means that you want to click it subjectively, and "This Ad is attractive." means that you think the advertisement itself is attractive to other people. You can of course choose both or neither. </p>
        </div>
    """, unsafe_allow_html=True)

    if st.button("Next Page"):
        if (random_number3 == 1):
            st.session_state.page = "Page 10"
            st.experimental_rerun()
        else:
            st.session_state.page = "Page 11"
            st.experimental_rerun()

def page10():
    # 添加标题
    st.title('Task 3')
    # 添加问题和选项
    question_10 = st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> 3. Imagine now you want to buy a man's jacket, so you see the following six advertisements in the social media platform, which one (which ones) do you want to click the most? 3.Please read the six advertisements and answer the questions.</p>
            <p style='color: brown; font-size: 18px;'>Jacket: A jacket typically has sleeves, and fastens in the front or slightly on the side. A jacket is generally lighter, tighter-fitting, and less insulating than a coat, which is outerwear. </p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    # 广告图片
    ad_image = "ad_jacket.jpg"
    st.image(ad_image, width=500)

    # 广告文本描述
    ad_description_10_1 = """ Ad 1. 
    
    **Elevate Your Look with Women's Trousers**
    
    Our Seasonal Sale Is Live! Free Worldwide Shipping. Experience The Entire Collection Today. Elevate Your Style.
    
    <p style='color: blue; font-size: 14px;'>[Shop Now]</p>
    """
    option_10_1_description = st.markdown(ad_description_10_1, unsafe_allow_html=True)

    option_10_1 = st.checkbox("I will click on this web page.", key='question_10_option_1')
    option_10_11 = st.checkbox("This Ad is attractive.", key='question_10_option_11')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    # 广告图片
    ad_image = "ad_jacket.jpg"
    st.image(ad_image, width=500)

    # 广告文本描述
    ad_description_10_2 = """ Ad 2. 
    
    **Stay Ahead of the Trends: Trendy Men's Jackets for the Fashion-Forward**
    
    Be a trendsetter with our collection of trendy men's jackets. Designed with the latest fashion trends in mind, these jackets combine style and functionality.
    
    <p style='color: blue; font-size: 14px;'>[Shop Now]</p>
    """
    option_10_2_description = st.markdown(ad_description_10_2, unsafe_allow_html=True)

    option_10_2 = st.checkbox("I will click on this web page.", key='question_10_option_2')
    option_10_22 = st.checkbox("This Ad is attractive.", key='question_10_option_22')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    # 广告图片
    ad_image = "ad_jacket.jpg"
    st.image(ad_image, width=500)

    # 广告文本描述
    ad_description_10_3 = """ Ad 3. 
    
    **Men's Jackets**
    
    Denim, leather, hooded, bomber, and sports jackets are the perfect styles to complete casual outfits. While tailored and textured styles add a special style note. From windbreakers to biker jackets, overshirts to padded designs, our online collection of jackets for men has every occasion covered.
    
    <p style='color: blue; font-size: 14px;'>[Shop Now]</p>
    """
    option_10_3_description = st.markdown(ad_description_10_3, unsafe_allow_html=True)

    option_10_3 = st.checkbox("I will click on this web page.", key='question_10_option_3')
    option_10_33 = st.checkbox("This Ad is attractive.", key='question_10_option_33')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    # 广告图片
    ad_image = "ad_jacket.jpg"
    st.image(ad_image, width=500)

    # 广告文本描述
    ad_description_10_4 = """ Ad 4. 
    
    **Elevate Your Look with Men's Jackets**
    
    Achieve a sophisticated and polished look with our men's jackets. Crafted with attention to detail and superior quality, these jackets offer a timeless appeal and exceptional comfort.
    
    <p style='color: blue; font-size: 14px;'>[Shop Now]</p>
    """
    option_10_4_description = st.markdown(ad_description_10_4, unsafe_allow_html=True)

    option_10_4 = st.checkbox("I will click on this web page.", key='question_10_option_4')
    option_10_44 = st.checkbox("This Ad is attractive.", key='question_10_option_44')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    # 广告图片
    ad_image = "ad_jacket.jpg"
    st.image(ad_image, width=500)

    # 广告文本描述
    ad_description_10_5 = """ Ad 5. 
    
    **Men's Coats & Jackets**
    
    Discover men's coats and jackets with us. Shop a range of styles from leather and denim jackets, to trench and rain coats. Order today!
    
    <p style='color: blue; font-size: 14px;'>[Shop Now]</p>
    """
    option_10_5_description = st.markdown(ad_description_10_5, unsafe_allow_html=True)

    option_10_5 = st.checkbox("I will click on this web page.", key='question_10_option_5')
    option_10_55 = st.checkbox("This Ad is attractive.", key='question_10_option_55')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    # 广告图片
    ad_image = "ad_jacket.jpg"
    st.image(ad_image, width=500)

    # 广告文本描述
    ad_description_10_6 = """ Ad 6. 
    
    **Men's Jackets for Every Occasion**
    
    Discover the versatility of our men's jackets. From casual outings to formal events, these jackets effortlessly elevate your style. With a perfect fit, premium materials, and versatility.
    
    <p style='color: blue; font-size: 14px;'>[Shop Now]</p>
    """
    option_10_6_description = st.markdown(ad_description_10_6, unsafe_allow_html=True)

    option_10_6 = st.checkbox("I will click on this web page.", key='question_10_option_6')
    option_10_66 = st.checkbox("This Ad is attractive.", key='question_10_option_66')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    question_106 = st.markdown("""
        <div>
            <p style='color: black; font-size: 20px;'> Which ads do you think are generated by AI? </p>
        </div>
    """, unsafe_allow_html=True)

    option_10_111 = st.checkbox("ads 1", key='question_10_option_111')
    option_10_222 = st.checkbox("ads 2", key='question_10_option_222')
    option_10_333 = st.checkbox("ads 3", key='question_10_option_333')
    option_10_444 = st.checkbox("ads 4", key='question_10_option_444')
    option_10_555 = st.checkbox("ads 5", key='question_10_option_555')
    option_10_666 = st.checkbox("ads 6", key='question_10_option_666')
    option_10_777 = st.checkbox("I couldn't tell the difference.", key='question_10_option_777')

    # 保存答案
    st.session_state.user_answers['ads 10'] = {
        'option 1': option_10_1,
        'option 11': option_10_11,
        'option 2': option_10_2,
        'option 22': option_10_22,
        'option 3': option_10_3,
        'option 33': option_10_33,
        'option 4': option_10_4,
        'option 44': option_10_44,
        'option 5': option_10_5,
        'option 55': option_10_55,
        'option 6': option_10_6,
        'option 66': option_10_66,
        'option 111': option_10_111,
        'option 222': option_10_222,
        'option 333': option_10_333,
        'option 444': option_10_444,
        'option 555': option_10_555,
        'option 666': option_10_666,
        'option 777': option_10_777
    }

    if st.button("Previous question"):
        st.session_state.page = "Page 02"
        st.experimental_rerun()

    # 提示用户输入ID
    user_id = st.text_input("You can enter your nickname (optional)")

    # 显示提交按钮
    submit_button = st.button('submit')
    # 处理提交按钮的点击事件
    if submit_button:

        # 打印用户的答案
        st.write('your answer is saving...please wait for a few seconds...')

        # 模拟用户数据
        user_data = st.session_state.user_answers

        def send_email(user_data, random_number, user_id):
            # 邮件配置
            sender_email = 'BachelorThesisT@outlook.com'
            receiver_email = 'taijunzhe@gmail.com'
            subject = '用户数据'
            message = format_user_data(user_data, random_number, user_id)

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

        def format_user_data(user_data, random_number, user_id):
            # 格式化用户数据和随机数为邮件内容
            formatted_data = ''
            for key, value in user_data.items():
                formatted_data += f'{key}: {value}\n'
            formatted_data += f'Random Number: {random_number}\n'
            formatted_data += f'User Id: {user_id}\n'
            return formatted_data

        # 发送邮件
        send_email(user_data, random_number, user_id)

        # 显示感谢信息或其他处理
        st.write('Thanks for taking the survey!')

def page11():
    # 添加标题
    st.title('Task 3')
    # 添加问题和选项
    question_11 = st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> 3. Imagine now you're hoping to spend a week on vacation with your family, so you see the following six advertisements in the social media platform, which one (which ones) do you want to click the most? 3.Please read the six advertisements and answer the questions.</p>
            <p style='color: brown; font-size: 18px;'></p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    # 广告图片
    ad_image = "ad_vacation.jpg"
    st.image(ad_image, width=500)

    # 广告文本描述
    ad_description_11_1 = """ Ad 1. 
    
    **Create Unforgettable Memories on Your Family Vacation**
    
    Escape the routine and embark on a week-long adventure with your loved ones. Our family-friendly vacation packages offer endless fun and excitement for all ages. From thrilling activities to relaxing beach days, make your family vacation truly unforgettable.
    <p style='color: blue; font-size: 14px;'>[Shop Now]</p>
    """
    option_11_1_description = st.markdown(ad_description_11_1, unsafe_allow_html=True)

    option_11_1 = st.checkbox("I will click on this web page.", key='question_11_option_1')
    option_11_11 = st.checkbox("This Ad is attractive.", key='question_11_option_11')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    # 广告图片
    ad_image = "ad_vacation.jpg"
    st.image(ad_image, width=500)

    # 广告文本描述
    ad_description_11_2 = """ Ad 2. 
    
    **Enjoy your vacation!**
    
    Plan your ultimate vacation with us! With our prime city center location, you'll be within reach of iconic landmarks. Enjoy the comfort of our modern rooms and suites and treat yourself to culinary delights at our cozy Restaurant and pool bar.
    
    <p style='color: blue; font-size: 14px;'>[Shop Now]</p>
    """
    option_11_2_description = st.markdown(ad_description_11_2, unsafe_allow_html=True)

    option_11_2 = st.checkbox("I will click on this web page.", key='question_11_option_2')
    option_11_22 = st.checkbox("This Ad is attractive.", key='question_11_option_22')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    # 广告图片
    ad_image = "ad_vacation.jpg"
    st.image(ad_image, width=500)

    # 广告文本描述
    ad_description_11_3 = """ Ad 3. 
    
    **Enjoy All-Inclusive Family Fun on Your One-Week Vacation**
    
    Leave the planning to us and immerse yourself in a week of worry-free family fun. Our all-inclusive vacation packages cover accommodations, meals, and exciting activities for the whole family. Experience the joy of quality time together.
    
    <p style='color: blue; font-size: 14px;'>[Shop Now]</p>
    """
    option_11_3_description = st.markdown(ad_description_11_3, unsafe_allow_html=True)

    option_11_3 = st.checkbox("I will click on this web page.", key='question_11_option_3')
    option_11_33 = st.checkbox("This Ad is attractive.", key='question_11_option_33')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    # 广告图片
    ad_image = "ad_vacation.jpg"
    st.image(ad_image, width=500)

    # 广告文本描述
    ad_description_11_4 = """ Ad 4. 
    
    **Looking for a short vacation?**
    
    We have a lot of tour packages for your consideration!
    Travelling is an immersive experience that combines vibrant culture, breathtaking landscapes, and warm hospitality. From exploring ancient temples and bustling markets to relaxing on pristine beaches and savouring tantalising cuisine, we offer a diverse and unforgettable journey for every traveller.
    It's time to take a break and plan a trip with your friends and family!
    
    <p style='color: blue; font-size: 14px;'>[Shop Now]</p>
    """
    option_11_4_description = st.markdown(ad_description_11_4, unsafe_allow_html=True)

    option_11_4 = st.checkbox("I will click on this web page.", key='question_11_option_4')
    option_11_44 = st.checkbox("This Ad is attractive.", key='question_11_option_44')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    # 广告图片
    ad_image = "ad_vacation.jpg"
    st.image(ad_image, width=500)

    # 广告文本描述
    ad_description_11_5 = """ Ad 5. 
    
    **Indulge in a Relaxing One-Week Vacation for the Whole Family**
    
    Take a break from the hustle and bustle of everyday life and treat your family to a week of relaxation and rejuvenation. Our vacation retreats provide a tranquil oasis where you can unwind and create precious memories together.
    
    <p style='color: blue; font-size: 14px;'>[Shop Now]</p>
    """
    option_11_5_description = st.markdown(ad_description_11_5, unsafe_allow_html=True)

    option_11_5 = st.checkbox("I will click on this web page.", key='question_11_option_5')
    option_11_55 = st.checkbox("This Ad is attractive.", key='question_11_option_55')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    # 广告图片
    ad_image = "ad_vacation.jpg"
    st.image(ad_image, width=500)

    # 广告文本描述
    ad_description_11_6 = """ Ad 6. 
    
    **A Journey to Escape the Earth**
    
    We offer custom travel experiences and innovative corporate travel. You can access resources across private family vacations, humanity discovery, deluxe golf club, global business visit exclusively. Let our team plan you a luxury vacation today!
    
    <p style='color: blue; font-size: 14px;'>[Shop Now]</p>
    """
    option_11_6_description = st.markdown(ad_description_11_6, unsafe_allow_html=True)

    option_11_6 = st.checkbox("I will click on this web page.", key='question_11_option_6')
    option_11_66 = st.checkbox("This Ad is attractive.", key='question_11_option_66')

    st.markdown("""
        <div>
            <p style='color: black; font-size: 26px;'> ----------------------------------------------------------------------------- </p>
        </div>
    """, unsafe_allow_html=True)  # 添加空行
    st.markdown("<br>", unsafe_allow_html=True)  # 添加空行
    
    question_116 = st.markdown("""
        <div>
            <p style='color: black; font-size: 20px;'> Which ads do you think are generated by AI? </p>
        </div>
    """, unsafe_allow_html=True)

    option_11_111 = st.checkbox("ads 1", key='question_11_option_111')
    option_11_222 = st.checkbox("ads 2", key='question_11_option_222')
    option_11_333 = st.checkbox("ads 3", key='question_11_option_333')
    option_11_444 = st.checkbox("ads 4", key='question_11_option_444')
    option_11_555 = st.checkbox("ads 5", key='question_11_option_555')
    option_11_666 = st.checkbox("ads 6", key='question_11_option_666')
    option_11_777 = st.checkbox("I couldn't tell the difference.", key='question_11_option_777')

    # 保存答案
    st.session_state.user_answers['ads 11'] = {
        'option 1': option_11_1,
        'option 11': option_11_11,
        'option 2': option_11_2,
        'option 22': option_11_22,
        'option 3': option_11_3,
        'option 33': option_11_33,
        'option 4': option_11_4,
        'option 44': option_11_44,
        'option 5': option_11_5,
        'option 55': option_11_55,
        'option 6': option_11_6,
        'option 66': option_11_66,
        'option 111': option_11_111,
        'option 222': option_11_222,
        'option 333': option_11_333,
        'option 444': option_11_444,
        'option 555': option_11_555,
        'option 666': option_11_666,
        'option 777': option_11_777
    }

    if st.button("Previous question"):
        st.session_state.page = "Page 02"
        st.experimental_rerun()

    # 提示用户输入ID
    user_id = st.text_input("You can enter your nickname (optional)")

    # 显示提交按钮
    submit_button = st.button('submit')
    # 处理提交按钮的点击事件
    if submit_button:

        # 打印用户的答案
        st.write('your answer is saving...please wait for a few seconds...')

        # 模拟用户数据
        user_data = st.session_state.user_answers

        def send_email(user_data, random_number, user_id):
            # 邮件配置
            sender_email = 'BachelorThesisT@outlook.com'
            receiver_email = 'taijunzhe@gmail.com'
            subject = '用户数据'
            message = format_user_data(user_data, random_number, user_id)

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

        def format_user_data(user_data, random_number, user_id):
            # 格式化用户数据和随机数为邮件内容
            formatted_data = ''
            for key, value in user_data.items():
                formatted_data += f'{key}: {value}\n'
            formatted_data += f'Random Number: {random_number}\n'
            formatted_data += f'User Id: {user_id}\n'
            return formatted_data

        # 发送邮件
        send_email(user_data, random_number, user_id)

        # 显示感谢信息或其他处理
        st.write('Thanks for taking the survey!')

if __name__ == "__main__":
    # 初始化页面状态
    if "page" not in st.session_state:
        st.session_state.page = "Page 0"
    
    if "user_answers" not in st.session_state:
        st.session_state.user_answers = {}

    # 运行主函数
    main()

