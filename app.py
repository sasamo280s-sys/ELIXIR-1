import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="Elixir-Lab | إكسير-لاب", page_icon="🧪", layout="centered")

# القائمة الجانبية
st.sidebar.title("إكسير-لاب 🧪")
st.sidebar.write("المساعد الرقمي لسكاشن التحليلية")
page = st.sidebar.radio("اختر القسم:", ["الحاسبة الذكية (H2O2)", "راسم المنحنيات الكهروكيميائية", "دليل الألوان"])

# --- القسم الأول: الحاسبة الذكية ---
if page == "الحاسبة الذكية (H2O2)":
    st.header("🧮 الحاسبة الذكية: تعيين قوة ماء الأكسجين")
    st.write("حساب الـ Volume Strength مباشرة من قراءات السحاحة بناءً على تفاعل الـ KMnO4")
    
    titration_vol = st.number_input("أدخل قراءة السحاحة (حجم KMnO4 بالملي):", min_value=0.0, step=0.1)
    
    if st.button("احسب النتيجة"):
        # Eq: Each 1 ml of 0.1N KMnO4 = 0.001702g H2O2
        weight_in_aliquot = titration_vol * 0.001702
        percent_wv = (weight_in_aliquot * 100) / 10 
        volume_strength = percent_wv * 3.292 
        
        st.success(f"النسبة المئوية: {percent_wv:.4f} %")
        st.info(f"قوة الحجم: {volume_strength:.4f} ml O2")

# --- القسم الثاني: راسم المنحنيات ---
elif page == "راسم المنحنيات الكهروكيميائية":
    st.header("📈 راسم المنحنيات (Potentiometry)")
    st.write("أدخل قيم الحجم والجهد لرسم منحنى المعايرة وتحديد نقطة التكافؤ.")
    
    col1, col2 = st.columns(2)
    with col1:
        volumes = st.text_input("أحجام الـ Titrant بالملي (افصل بينها بفاصلة):", "0, 1, 2, 3, 4, 5")
    with col2:
        potentials = st.text_input("قراءات الجهد بالملي فولت (افصل بينها بفاصلة):", "100, 120, 150, 400, 420, 430")
        
    if st.button("ارسم المنحنى"):
        try:
            vol_list = [float(i.strip()) for i in volumes.split(",")]
            pot_list = [float(i.strip()) for i in potentials.split(",")]
            
            fig, ax = plt.subplots()
            ax.plot(vol_list, pot_list, marker='o', linestyle='-', color='b')
            ax.set_title("Potentiometric Titration Curve")
            ax.set_xlabel("Volume (ml)")
            ax.set_ylabel("Potential (mV)")
            ax.grid(True)
            
            st.pyplot(fig)
            st.success("تم رسم المنحنى بنجاح! نقطة التكافؤ تقع عند أطول قفزة في المنحنى.")
        except:
            st.error("تأكد من إدخال الأرقام بشكل صحيح ومفصولين بفاصلة.")

# --- القسم الثالث: دليل الألوان ---
elif page == "دليل الألوان":
    st.header("🎨 دليل الألوان التفاعلي")
    st.write("دليل سريع لنهايات التفاعل في المعايرة بالتراكب (Complexometry).")
    
    st.markdown("""
    * **دليل Erio-T (مع الزنك والماغنسيوم):**
      * لون البداية: أحمر عنابي (Wine Red) 🍷
      * نقطة النهاية: أزرق (Blue) 🔵
      
    * **دليل Xylenol Orange (مع البزموت في وسط حامضي):**
      * لون البداية: أحمر (Red) 🔴
      * نقطة النهاية: أصفر ليموني (Lemon Yellow) 🍋
      
    * **دليل Murexide (مع الكالسيوم فقط):**
      * لون البداية: وردي (Pink) 🌸
      * نقطة النهاية: بنفسجي (Purple) 🟣
    """)

