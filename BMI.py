import streamlit as st

kg = st.number_input('Nhập cân nặng của bạn theo kg:')
choose = st.radio('Chọn đơn vị chiều cao.', options=['cms','dms','meters'])
cao = st.number_input('Nhập đơn vị chiều cao:')
def calculate():
    if choose == 'cms':
        bmi = kg / ((cao / 100) ** 2)
    elif choose == 'dms':
        bmi = kg / ((cao / 10) ** 2)
    else:
        bmi = kg / (cao ** 2)
    st.write(bmi)

    if bmi < 18.5:
        st.info('Nhẹ cân.')
    elif bmi <= 24.9:
        st.success('Bình thường.')
    elif bmi <= 29.9:
        st.warning('Thừa cân.')
    elif bmi <= 34.9:
        st.error('Béo phì độ 1.')
    elif bmi >= 35:
        st.error('Béo phì độ 2.')

if st.button('Calculate BMI'):
    calculate()