# app.py
import streamlit as st
from PIL import Image
import base64

st.set_page_config(page_title="Sürpriz Arayüz", layout="centered")

# Modern arka plan rengi ve stiller
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
            text-align: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .stButton>button {
            background-color: #ff4b5c;
            color: white;
            font-size: 24px;
            padding: 15px 50px;
            border-radius: 12px;
            border: none;
            transition: transform 0.2s;
            display: block;
            margin: 30px auto;
        }
        .stButton>button:hover {
            transform: scale(1.1);
            cursor: pointer;
        }
        .centered-container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 80vh;
            width: 100%;
        }
        .centered-image {
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 20px 0;
        }
        .rose {
            position: fixed;
            width: 30px;
            height: 30px;
            background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="%23ff4b5c" d="M12,2C9,7,4,9,4,14c0,3,3,4,8,4s8-1,8-4C20,9,15,7,12,2z"/></svg>');
            background-size: contain;
            opacity: 0.7;
            animation: fall linear forwards;
            pointer-events: none;
            z-index: 9999;
        }
        @keyframes fall {
            0% { transform: translateY(-10px) rotate(0deg); opacity: 0.7; }
            100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
        }
        .title-container {
            margin-bottom: 30px;
        }
        /* Müzik için gizli oynatıcı */
        .hidden-audio {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# Başlık
st.markdown('<div class="title-container">', unsafe_allow_html=True)
st.title("🎉 Sürpriz Zamanı 🎉")
st.write("Sürpriz için butona bas!")
st.markdown('</div>', unsafe_allow_html=True)

# Buton
if st.button("Sürpriz için butona bas"):
    # Müziği otomatik başlat (önce ekleyelim ki resim yüklenirken çalsın)
    try:
        # Base64 ile müzik dosyasını göm
        with open('dunyanin_en_guzel_kizi.mp3', 'rb') as audio_file:
            audio_bytes = audio_file.read()
            audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
            
            st.markdown(f'''
                <audio class="hidden-audio" autoplay loop>
                    <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mpeg">
                </audio>
            ''', unsafe_allow_html=True)
    except:
        st.info("Müzik dosyası bulunamadı")

    # Görseli yükle ve göster (ortalanmış ve biraz büyütülmüş)
    try:
        img = Image.open("resim.jpeg")
        
        # Görseli biraz daha büyüt
        max_size = (500, 500)  # 400'den 500'e büyüttük
        img.thumbnail(max_size, Image.Resampling.LANCZOS)
        
        # Görseli tam ortala
        st.markdown('<div class="centered-container">', unsafe_allow_html=True)
        st.image(img, caption="İşte sürprizin!", width=500)  # Genişliği 500 yaptık
        st.markdown('</div>', unsafe_allow_html=True)
        
    except FileNotFoundError:
        st.error("Görsel dosyası bulunamadı. Lütfen 'resim.jpeg' dosyasının mevcut olduğundan emin olun.")

    # Gül yaprağı düşme efekti
    st.markdown("""
        <script>
            function createRose() {
                const rose = document.createElement('div');
                rose.className = 'rose';
                rose.style.left = Math.random() * 100 + 'vw';
                rose.style.animationDuration = 3 + Math.random() * 3 + 's';
                document.body.appendChild(rose);
                
                // Animasyon bittikten sonra elementi kaldır
                setTimeout(() => {
                    rose.remove();
                }, 6000);
            }
            
            // İlk 3 saniye boyunca sürekli gül yaprağı oluştur
            for(let i = 0; i < 20; i++) {
                setTimeout(() => {
                    createRose();
                }, i * 150);
            }
            
            // Sonrasında daha seyrek oluşturmaya devam et
            setInterval(() => {
                createRose();
            }, 500);
        </script>
    """, unsafe_allow_html=True)
