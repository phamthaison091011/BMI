import streamlit as st

# Bài 1:
a = st.text_input('Nhập họ và tên của bạn: ')
b = a.split()
c = len(b)
if st.button('Kiểm tra tên của bạn có bao nhiêu tiếng'):
    st.write('Tên của bạn được tạo thành từ', c, 'tiếng.')

# Bài 2:
a = st.text_input('Nhập số chứng minh nhân dân: ')
if st.button('Kiểm tra số chứng minh nhân dân'):
    if len(a) < 9 or len(a) > 11:
        st.write('Số chứng minh nhân dân của bạn nhập sai!')
    else:
        if a.isdigit():
            st.write('Số chứng minh nhân dân của bạn hợp lệ!')
        else:
            st.write('Số chứng minh nhân dân của bạn nhập sai!')

# Bài 3:
a = st.text_input('Nhập địa chỉ email của bạn: ')
if st.button('Kiểm tra email.'):
    if a.count('@') != 1:
        st.write('Địa chỉ email của bạn không hợp lệ!')
    else:
        if a.endswith('.com') and ' ' not in a:
            st.write('Địa chỉ email của bạn hợp lệ!')
        else:
            st.write('Địa chỉ email của bạn không hợp lệ!')