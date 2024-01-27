import streamlit as st
import pandas as pd
import plotly.express as px
import openpyxl



## need improvment##
## Ahmed Alsrehy##

st.set_page_config(layout="wide",page_title="المسح الإقتصادي الشامل")

file_upload = st.sidebar.file_uploader("**ملف الإنتاجية فقط**",type=['xlsx'])
if file_upload is not None:
    df = pd.read_excel(file_upload)
    df = df.iloc[1:, :]
    # full_data = 'حالة جمع البيانات'
    # some_data = 'Unnamed: 12'
    # refuse_data = 'Unnamed: 13'
    # closed_data = 'Unnamed: 14'
    # temp_data = 'Unnamed: 15'
    # othertime_data = 'Unnamed: 16'
    # other_data = 'Unnamed: 17'
    # self_data = 'Unnamed: 18'
    # unders_data = 'Unnamed: 19'
    # unoccu_data = 'Unnamed: 20'
    # person_data = 'Unnamed: 21'
    # notwork = 'Unnamed: 22'
    # new_data =  'حالة الإكتمال'
    # uncomplate_data = 'Unnamed: 26'
    # colmplate_data = 'Unnamed: 27'
    # return_data = 'Unnamed: 28'
    # percentage_data = 'نسبة الاكتمال'
    # occandwork_data = 'حالة الاشغال'
    # camp_data = 'Unnamed: 31'
    # work_data = 'Unnamed: 32'
    # workandout = 'Unnamed: 33'


    # df = df.rename(columns={''})
    st.markdown("""
                   <h2 style="text-align: center">المسح الإقتصادي الشامل <br> منطقة المدينة المنورة</h2>

                   """, unsafe_allow_html=True)

    with st.expander(" ", expanded=True):
        e_supervisor = df[df['منطقة العمل'] == 'مشرف منطقة']
        if len(e_supervisor) >1:
            st.write("more than 1")
        col1,col2 = st.columns([1,2])
        with col1:
            st.metric("**:green[الإنتاجية]**", "{:,}%".format
                (e_supervisor['نسبة الاكتمال'].unique()[0]))


            st.success("**:green[مكتملة]   {:,}**".format
                (e_supervisor['Unnamed: 27'].unique()[0]))

            st.info("**:blue[غير مكتملة]   {:,}**".format
                (e_supervisor['Unnamed: 26'].unique()[0]))


            st.error("**:red[جديدة]   {:,}**".format
                (e_supervisor['حالة الإكتمال'].unique()[0]))


        colmplate = e_supervisor['Unnamed: 27'].unique()[0]
        uncomplate = e_supervisor['Unnamed: 26'].unique()[0]
        new = e_supervisor['حالة الإكتمال'].unique()[0]
        colors = ['green', 'blue', 'red']

        fig = px.pie(e_supervisor, values=[colmplate, uncomplate, new], names=['المكتملة', 'غير مكتملة', 'جديد'],
                     height=350)
        fig.update_traces(
                      marker=dict(colors=colors, ))

        with col2:
            st.plotly_chart(fig,use_container_width=True)


    co1 , co2 = st.columns(2)
    with co1:
        with st.expander("**مستوى المشرف**", expanded=True):
            full = e_supervisor['حالة جمع البيانات'].unique()[0]
            part = e_supervisor['Unnamed: 12'].unique()[0]
            refuse = e_supervisor['Unnamed: 13'].unique()[0]
            not_found = e_supervisor['Unnamed: 21'].unique()[0]
            st.markdown("""
                       <h2 style="text-align: center">جمع البيانات</h2>

                       """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                    st.metric("**أعطت كامل البيانات**", "{:,}✅".format(full))
                    st.metric("**أعطت بعض البيانات**", "{:,}⌛".format(part))


            with col2:
                    st.metric("**رفض إعطاء البيانات**", "{:,}⛔".format(refuse))
                    st.metric("**المدلي غير متواجد حالياً**", "{:,}📆".format(not_found))



        with st.expander("**المزيد ➕**"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("**مغلقة نهائياً**",
                          "{:,}".format(e_supervisor['Unnamed: 14'].unique()[0]))
                st.metric("**مغلقة مؤقتاً**",
                          "{:,}".format(e_supervisor['Unnamed: 15'].unique()[0]))
                st.metric("**يطلب الزيارة مرة أخرى وقت آخر**",
                          "{:,}".format(e_supervisor['Unnamed: 16'].unique()[0]))
            with col2:
            
                st.metric(
                    "**أخرى**", "{:,}".format(e_supervisor['Unnamed: 17'].unique()[0]))
                st.metric("**إستيفاء ذاتي**",
                          "{:,}".format(e_supervisor['Unnamed: 18'].unique()[0]))


            with col3:
                st.metric(
                    "**خالية**", "{:,}".format(e_supervisor['Unnamed: 20'].unique()[0]))
                st.metric("**ليست منشأة**",
                          "{:,}".format(e_supervisor['Unnamed: 22'].unique()[0]))
                st.metric("**تحت التأسيس**",
                          "{:,}".format(e_supervisor['Unnamed: 19'].unique()[0]))

    with co2:
        with st.expander("**مستوى المشرف**", expanded=True):
            st.markdown("""
                      <h2 style="text-align: center">حالة الإشغال</h2>

                      """, unsafe_allow_html=True)
            col1, col2= st.columns(2)
            with col1:
                st.metric("**للعمل فقط 🏢**"
                         , "{:,}".format(e_supervisor['Unnamed: 32'].unique()[0]))
                st.metric("**للسكن والعمل**",
                          "{:,}".format(e_supervisor['حالة الاشغال'].unique()[0]))

            with col2:
                st.metric("**خالي ومعد للعمل**",
                          "{:,}".format(e_supervisor['Unnamed: 33'].unique()[0]))
                st.metric("**منشأة حكومية 🏛**"
                         , "{:,}".format(e_supervisor['Unnamed: 39'].unique()[0]))




        with st.expander("**المزيد ➕ -**"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("**لم يتم العثور عليها 🔍**"
                         , "{:,}".format(e_supervisor['Unnamed: 38'].unique()[0]))

                st.metric("**معسكر عمل**",
                          "{:,}".format(e_supervisor['Unnamed: 31'].unique()[0]))
   

            with col2:
            

                st.metric("**تابع للوحة العقارية**",
                          "{:,}".format(e_supervisor['Unnamed: 35'].unique()[0]))
                st.metric(
                    "**اخرى**", "{:,}".format(e_supervisor['Unnamed: 36'].unique()[0]))
            with col3:
                st.metric("**.ليست منشأة**",
                          "{:,}".format(e_supervisor['Unnamed: 37'].unique()[0]))
                st.metric("**تحت التشييد**",
                          "{:,}".format(e_supervisor['Unnamed: 34'].unique()[0]))
    "---"

    st.markdown("""
                       <h2 style="text-align: center">مستوى المساعد</h2>

                       """, unsafe_allow_html=True)

    e_assoss = df[df['منطقة العمل'] == 'مساعد مشرف']

    long = len(e_assoss['Unnamed: 5'])

    e_assoss_list = []
    for i in sorted(e_assoss['Unnamed: 5'].unique()):
        e_assoss_temp = e_assoss[e_assoss['Unnamed: 5'] == i]
        e_assoss_list.append({
            "إستيفاء ذاتي" : e_assoss_temp['Unnamed: 18'].unique()[0],
            "أعطت بعض البيانات" : e_assoss_temp['Unnamed: 12'].unique()[0],
            "أعطت كامل البيانات" : e_assoss_temp['حالة جمع البيانات'].unique()[0],
            "الإنتاجية %" : "{}".format(e_assoss_temp['نسبة الاكتمال'].unique()[0]),
            "المساعد" : e_assoss_temp['Unnamed: 5'].unique()[0],
            "المشرف": e_assoss_temp['Unnamed: 2'].unique()[0],



        })
    e_assoss_data = pd.DataFrame(e_assoss_list)

    col1,col2 = st.columns(2)
    with col1:
        with st.expander(" ",expanded=True):
            st.markdown("""
                       <h4 style="text-align: center">جمع البيانات</h4>

                       """, unsafe_allow_html=True)
            st.dataframe(e_assoss_data[['إستيفاء ذاتي','أعطت بعض البيانات','أعطت كامل البيانات','المساعد']],use_container_width=True,hide_index=True)


    with col2:
        with st.expander("  ",expanded=True):
            st.markdown("""
                       <h4 style="text-align: center">الإنتاجية</h4>

                       """, unsafe_allow_html=True)
            st.data_editor(e_assoss_data[['الإنتاجية %','المساعد']],use_container_width=True,hide_index=True,column_config={
                'الإنتاجية %' : st.column_config.ProgressColumn("الإنتاجية %",min_value=0,max_value=100,format='%i',width='medium')
            })

    "---"
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
            df = df[df['منطقة العمل'] == "مساعد مشرف"]
            worker_type = st.selectbox('نوع المشتغل', sorted(df['منطقة العمل'].unique()),disabled=True)
            if len(df['منطقة العمل'].unique()) > 1:
                df = df[df['منطقة العمل'] == worker_type]


    with col2:
            supervisor_no = st.selectbox('مشرف', sorted(df['Unnamed: 2'].unique()))
            if len(df['Unnamed: 2'].unique()) > 1:
                if st.checkbox("تفعيل فلتر المشرف"):
                    
                    df = df[df['Unnamed: 4'] == supervisor_no]

    with col3:
            mvice_no = st.selectbox('م نواب', sorted(df['Unnamed: 3'].unique()))
            if len(e_assoss['Unnamed: 3'].unique()) > 1:
                if st.checkbox("تفعيل فلتر م نواب"):
                    st.caption( ":white_check_mark:"+ "فلتر م النائب مفعل")
                    df = df[df['Unnamed: 3'] == mvice_no]

    with col4:
            vice_no = st.selectbox('نائب', sorted(df['Unnamed: 4'].unique()))
            if len(df['Unnamed: 4'].unique()) > 1:
                if st.checkbox("تفعيل فلتر النائب"):
                    df = df[df['Unnamed: 4'] == vice_no]
    with col5:
            associate_no = st.selectbox('مساعد', sorted(df['Unnamed: 5'].unique()),index=0)
            df = df[df['Unnamed: 5'] == associate_no]
            st.caption( ":white_check_mark:"+ "فلتر م المساعد مفعل")






    col1,col2 = st.columns(2)
    with col1:
        st.metric("**:green[الإنتاجية]**", "{:,}%".format
                (df['نسبة الاكتمال'].unique()[0]))


        st.success("**:green[مكتملة]   {:,}**".format
                (df['Unnamed: 27'].unique()[0]))

        st.info("**:blue[غير مكتملة]   {:,}**".format
                (df['Unnamed: 26'].unique()[0]))


        st.error("**:red[جديدة]   {:,}**".format
                (df['حالة الإكتمال'].unique()[0]))


        colmplate = df['Unnamed: 27'].unique()[0]
        uncomplate = df['Unnamed: 26'].unique()[0]
        new = df['حالة الإكتمال'].unique()[0]
        colors = ['green', 'blue', 'red']

        fig = px.pie(df, values=[colmplate, uncomplate, new], names=['المكتملة', 'غير مكتملة', 'جديد'],
                     height=350)
        fig.update_traces(
                      marker=dict(colors=colors, ))

        with col2:
            st.subheader("مساعد {}".format(associate_no))
            st.plotly_chart(fig, use_container_width=True)
            

    co1 , co2 = st.columns(2)
    with co1:
        with st.expander("**مـساعد {}**".format(associate_no), expanded=True):
            full = df['حالة جمع البيانات'].unique()[0]
            part = df['Unnamed: 12'].unique()[0]
            refuse = df['Unnamed: 13'].unique()[0]
            not_found = df['Unnamed: 21'].unique()[0]
            st.markdown("""
                       <h2 style="text-align: center">جمع البيانات</h2>

                       """, unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                st.metric("**أعطت كامل البيانات**", "{:,}✅".format(full))
                st.metric("**أعطت بعض البيانات**", "{:,}⌛".format(part))


            with col2:
                st.metric("**رفض إعطاء البيانات**", "{:,}⛔".format(refuse))
                st.metric("**المدلي غير متواجد حالياً**", "{:,}📆".format(not_found))



        with st.expander("**المزيد ➕**"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("**مغلقة نهائياً**",
                          "{:,}".format(df['Unnamed: 14'].unique()[0]))
                st.metric("**مغلقة مؤقتاً**",
                          "{:,}".format(df['Unnamed: 15'].unique()[0]))
                st.metric("**يطلب الزيارة مرة أخرى وقت آخر**",
                          "{:,}".format(df['Unnamed: 16'].unique()[0]))
            with col2:
            
                st.metric(
                    "**أخرى**", "{:,}".format(df['Unnamed: 17'].unique()[0]))
                st.metric("**إستيفاء ذاتي**",
                          "{:,}".format(df['Unnamed: 18'].unique()[0]))
                st.metric("**تحت التأسيس**",
                          "{:,}".format(df['Unnamed: 19'].unique()[0]))

            with col3:
                st.metric(
                    "**خالية**", "{:,}".format(df['Unnamed: 20'].unique()[0]))
                st.metric("**ليست منشأة**",
                          "{:,}".format(df['Unnamed: 22'].unique()[0]))

    with co2:
        with st.expander("**مـساعد {}**".format(associate_no), expanded=True):
            st.markdown("""
                      <h2 style="text-align: center">حالة الإشغال</h2>

                      """, unsafe_allow_html=True)
            col1, col2= st.columns(2)
            with col1:
                st.metric("**للعمل فقط 🏢**"
                         , "{:,}".format(df['Unnamed: 32'].unique()[0]))
                st.metric("**للسكن والعمل**",
                          "{:,}".format(df['حالة الاشغال'].unique()[0]))
            with col2:
                st.metric("**خالي ومعد للعمل**",
                          "{:,}".format(df['Unnamed: 33'].unique()[0]))

                st.metric("**منشأة حكومية 🏛**"
                         , "{:,}".format(df['Unnamed: 39'].unique()[0]))





        with st.expander("**المزيد ➕ -**"):
            col1, col2, col3 = st.columns(3)
            with col1:

                st.metric("**معسكر عمل**",
                          "{:,}".format(df['Unnamed: 31'].unique()[0]))
                st.metric("**لم يتم العثور عليها 🔍**"
                         , "{:,}".format(df['Unnamed: 38'].unique()[0]))

            with col2:
            
                st.metric("**تحت التشييد**",
                          "{:,}".format(df['Unnamed: 34'].unique()[0]))
                st.metric("**تابع للوحة العقارية**",
                          "{:,}".format(df['Unnamed: 35'].unique()[0]))

            with col3:
                st.metric("**.ليست منشأة**",
                          "{:,}".format(df['Unnamed: 37'].unique()[0]))
                st.metric(
                    "**اخرى**", "{:,}".format(df['Unnamed: 36'].unique()[0]))





    

