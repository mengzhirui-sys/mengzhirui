import streamlit as st
import pandas as pd
import numpy as np
import random




st.title('🏁南宁美食探索')

st.write('探索广西南宁最受欢迎的美食地点！选择你感兴趣的餐厅类型，查看评分和位置。')


# 定义数据，以便创建数据框
data = {'月份':['01月','02月','03月'],
'1号门店':[200,150,180],
'2号门店':[120,160,123],
'3号门居':[110,100,160],
'4号门店':[123,123,123]}

df=pd.DataFrame(data)




#1.带点的地图-餐厅位置

st.header("🍜南宁美食地图")# 创建简单地图
st.map (pd.DataFrame({
"latitude":[22.853838, 22.965046, 22.812200, 22.809105, 22.839699],
"longitude":[108.222177, 108.353921, 108.266629, 108.378664, 108.245804]
}))


st.title('⭐餐厅评分')
# 定义数据,以便创建数据框
data = {
      "门店": ["星艺会尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "白妈螺狮粉"],
      "评分": [4.2, 4.5, 4.0, 4.7, 4.3]
      
}

# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
# 定义数据框所用的新索引
index = pd.Series([1, 2, 3,4,5], name='序号')
# 将新索引应用到数据框上
df.index = index

# 通过x指定月份所在这一列为条形图的x轴
df_indexed = df.set_index('门店')
st.bar_chart(df_indexed)

st.title('💰不同类型餐厅价格')
# 定义数据,以便创建数据框
data = {
    '餐厅类型':['西餐', '快餐', '日料','火锅'],
    '门店':[2000, 1500, 1800, 9999]
}
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
# 定义数据框所用的新索引
index = pd.Series([1, 2, 3, 4], name='序号')
# 将新索引应用到数据框上
df.index = index

# 通过x指定月份所在这一列为折线图的x轴
df_indexed = df.set_index('餐厅类型')
st.line_chart(df_indexed)

st.title('🍲用餐高分时段')
# 定义数据,以便创建数据框
data = {
    '时间':['11', '12', '13'],
    '星艺会尝不忘':[200, 150, 180],
     "高峰柠檬鸭":[120, 160, 123],
    "复记老友粉":[110, 100, 160],
     "好友缘":[150,170,200],
    "白妈螺狮粉":[140,160,180]
    
    
}
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
# 定义数据框所用的新索引
index = pd.Series([1, 2, 3,], name='序号')
# 将新索引应用到数据框上
df.index = index

# 通过x指定月份所在这一列为面积图的x轴
df_indexed = df.set_index('时间')
st.area_chart(df_indexed)

def my_format_func(option):
    return f'{option}'

st.header(" 🍽餐厅详情")

canteen= st.selectbox('选择餐厅查看详情：', ["星艺会尝不忘","高峰柠檬鸭","复记老友粉","好友缘","白妈螺蛳粉"],format_func=my_format_func, index=2)
if canteen == '星艺会尝不忘':
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("星艺会尝不忘")
        st.text("评分")
        st.header("4.2/5.0")
    with col2:
        st.markdown("""
        **推荐菜品:**
        - 桂林米粉
        - 瘦肉粉
        - 干捞粉
        """)       
    st.text("人均消费")
    st.header("15元")
    st.subheader('当前拥挤情况')
    text1="84%拥挤" #进度条
    my_bar=st.progress(84,text=text1)

if canteen == '高峰柠檬鸭':
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("高峰柠檬鸭")
        st.text("评分")
        st.header("4.5/5.0")
    with col2:
        st.markdown("""
        **推荐菜品:**
        - 特殊套餐
        - 地方小吃
        - 时令蔬菜
        """)       
    st.text("人均消费")
    st.subheader('20元')
    st.subheader('当前拥挤情况')
    text2 = "90%拥挤"  # 进度条
    my_bar = st.progress(90, text=text2)

if canteen == '复记老友粉':
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("复记老友粉")
        st.text("评分")
        st.header("4.0/5.0")
    with col2:
        st.markdown("""
        **推荐菜品:**
        - 老友牛肉
        - 老友猪肉
        - 炒粉
        """)       
    st.text("人均消费")
    st.subheader('25元')
    st.subheader('当前拥挤情况')
    text3 = "80%拥挤"  # 进度条
    my_bar = st.progress(80, text=text3)

if canteen == '好友缘':
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("好友缘")
        st.text("评分")
        st.header("4.7/5.0")
    with col2:
        st.markdown("""
        **推荐菜品:**
        - 特殊套餐
        - 地方小吃
        - 时令蔬菜
        """)       
    st.text("人均消费")
    st.subheader('35元')
    st.subheader('当前拥挤情况')
    text4 = "94%拥挤"  # 进度条
    my_bar = st.progress(94, text=text4)

if canteen == '白妈螺蛳粉':
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("白妈螺蛳粉")
        st.text("评分")
        st.header("4.3/5.0")
    with col2:
        st.markdown("""
        **推荐菜品:**
        - 老友牛肉
        - 老友猪肉
        - 炒粉
        """)       
    st.text("人均消费")
    st.subheader('50元')
    st.subheader('当前拥挤情况')
    text5 = "86%拥挤"  # 进度条
    my_bar = st.progress(86, text=text5)
st.header(' ::game_die:: 今日午餐推荐')

if st.button("帮我选择午餐"):
    random_num=random.randint(1,5)
    if random_num ==1:
        st.write(' ## `今日推荐：星艺会尝不忘` ')
    if random_num ==2:
        st.write(' ## `今日推荐：高峰柠檬鸭` ')
    if random_num ==3:
        st.write(' ## `今日推荐：复记老友粉` ')
    if random_num ==4:
        st.write(' ## `今日推荐：好友缘` ')
    if random_num ==5:
        st.write(' ## `今日推荐：白妈螺蛳粉` ')
    st.image('https://img.shetu66.com/2023/06/12/1686543388597292.jpg')


