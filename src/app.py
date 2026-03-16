import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import os
import numpy as np

st.set_page_config(page_title="AgriIntel 2026 Pro", layout="wide", page_icon="🌾")

# Load external CSS
if os.path.exists("assets/style.css"):
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 1. LOCALIZED DICTIONARY (Every UI element translated)
LANG_DATA = {
    "English": {
        "title": "AI Market Forecast", "crop": "Select Crop", "market": "Select Market",
        "price": "TODAY'S PRICE", "pred": "EXPECTED PRICE", "dist": "DISTANCE", 
        "sell": "✅ SELL NOW", "wait": "⏳ WAIT", "alert": "⚠️ RAIN ALERT", 
        "msg": "70% Chance of rain!", "voice": "en-US", "wa_btn": "Share on WhatsApp",
        "mandi_h": "Mandi Location", "price_h": "Price", "chart_x": "Days", "chart_y": "Rate",
        "seasonal": "Price Seasonality", "radar": "Market Strength", "vol": "Volume", "trust": "Trust"
    },
    "Telugu (తెలుగు)": {
        "title": "AI మార్కెట్ ధర అంచనా", "crop": "పంటను ఎంచుకోండి", "market": "మార్కెట్",
        "price": "నేటి ధర", "pred": "రేపటి ధర", "dist": "దూరం", 
        "sell": "✅ ఇప్పుడే అమ్మండి", "wait": "⏳ వేచి ఉండండి", "alert": "⚠️ వర్షం హెచ్చరిక", 
        "msg": "70% వర్షం అవకాశం!", "voice": "te-IN", "wa_btn": "వాట్సాప్‌లో పంపండి",
        "mandi_h": "మార్కెట్ ప్రాంతం", "price_h": "ధర", "chart_x": "రోజులు", "chart_y": "ధర స్థాయి",
        "seasonal": "నెలవారీ ధరల ధోరణి", "radar": "మార్కెట్ పోలిక", "vol": "పరిమాణం", "trust": "నమ్మకం"
    },
    "Kannada (ಕನ್ನಡ)": {
        "title": "AI ಮಾರುಕಟ್ಟೆ ಬೆಲೆ ಮುನ್ಸೂಚನೆ", "crop": "ಬೆಳೆ ಆರಿಸಿ", "market": "ಮಾರುಕಟ್ಟೆ",
        "price": "ಇಂದಿನ ಬೆಲೆ", "pred": "ನಾಳೆಯ ಬೆಲೆ", "dist": "ದೂರ", 
        "sell": "✅ ಈಗಲೇ ಮಾರಿ", "wait": "⏳ ಕಾಯಿರಿ", "alert": "⚠️ ಮಳೆ ಮುನ್ನೆಚ್ಚರಿಕೆ", 
        "msg": "70% ಮಳೆ ಸಾಧ್ಯತೆ!", "voice": "kn-IN", "wa_btn": "ವಾಟ್ಸಾಪ್‌ನಲ್ಲಿ ಹಂಚಿಕೊಳ್ಳಿ",
        "mandi_h": "ಮಾರುಕಟ್ಟೆ ಸ್ಥಳ", "price_h": "ಬೆಲೆ", "chart_x": "ದಿನಗಳು", "chart_y": "ದರ",
        "seasonal": "ಋತುಮಾನದ ಬೆಲೆ", "radar": "ಮಾರುಕಟ್ಟೆ ಸಾಮರ್ಥ್ಯ", "vol": "ಗಾತ್ರ", "trust": "ವಿಶ್ವಾಸಾರ್ಹತೆ"
    },
    "Tamil (தமிழ்)": {
        "title": "AI சந்தை விலை முன்னறிவிப்பு", "crop": "பயிர்", "market": "சந்தை",
        "price": "இன்றைய விலை", "pred": "நாளை விலை", "dist": "தூரம்", 
        "sell": "✅ இப்பொழுதே விற்கவும்", "wait": "⏳ காத்திருக்கவும்", "alert": "⚠️ மழை எச்சரிக்கை", 
        "msg": "70% மழை வாய்ப்பு!", "voice": "ta-IN", "wa_btn": "வாட்ஸ்அப்பில் பகிரவும்",
        "mandi_h": "சந்தை இடம்", "price_h": "விலை", "chart_x": "நாட்கள்", "chart_y": "விலை விகிதம்",
        "seasonal": "மாதாந்திர விலை", "radar": "சந்தை ஒப்பீடு", "vol": "அளவு", "trust": "நம்பிக்கை"
    },
    "Malayalam (മലയാളം)": {
        "title": "AI മാർക്കറ്റ് വില പ്രവചനം", "crop": "വിള", "market": "മാർക്കറ്റ്",
        "price": "ഇന്നത്തെ വില", "pred": "നാളത്തെ വില", "dist": "ദൂരം", 
        "sell": "✅ ഇപ്പോൾ വിൽക്കുക", "wait": "⏳ കാത്തിരിക്കുക", "alert": "⚠️ മഴ മുന്നറിയിപ്പ്", 
        "msg": "70% മഴയ്ക്ക് സാധ്യത!", "voice": "ml-IN", "wa_btn": "വാട്സാപ്പിൽ അയക്കുക",
        "mandi_h": "മാർക്കറ്റ് സ്ഥലം", "price_h": "വില", "chart_x": "ദിവസങ്ങൾ", "chart_y": "നിരക്ക്",
        "seasonal": "വില വ്യതിയാനം", "radar": "മാർക്കറ്റ് താരതമ്യം", "vol": "അളവ്", "trust": "വിശ്വാസ്യത"
    }
}

# 2. DATA LOADER
@st.cache_data
def load_data():
    path = "data/finalcapdata_india_all_districts.csv"
    if os.path.exists(path):
        df = pd.read_csv(path)
        df.columns = [c.strip().lower() for c in df.columns]
        return df
    return pd.DataFrame()

df = load_data()

# 3. SIDEBAR CONFIG
with st.sidebar:
    st.markdown("### 🌐 SETTINGS")
    lang = st.selectbox("Language / భాష / ಭಾಷೆ / மொழி / ഭാഷ", list(LANG_DATA.keys()))
    T = LANG_DATA[lang]
    
    if not df.empty:
        sel_crop = st.selectbox(T["crop"], sorted(df['commodity'].unique()))
        sel_loc = st.selectbox(T["market"], sorted(df[df['commodity'] == sel_crop]['location'].unique()))
    
    wa_num = st.text_input("WhatsApp Number", "91")
    voice_btn = st.button("🔊 Voice Briefing")

# 4. DASHBOARD HEADER
st.markdown(f'<div class="weather-alert">{T["alert"]}: {T["msg"]}</div>', unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align:center;'>{T['title']}</h1>", unsafe_allow_html=True)

if not df.empty:
    filtered = df[(df['commodity'] == sel_crop) & (df['location'] == sel_loc)]
    curr_p = filtered['average'].iloc[-1] if not filtered.empty else 2100
    pred_p = round(curr_p * 1.10, 2)
    sig_color = "#22c55e" if pred_p > curr_p else "#facc15"

    # Action Recommendation Banner
    st.markdown(f'<div style="background:{sig_color}22; border:3px solid {sig_color}; padding:20px; border-radius:20px; text-align:center; margin-bottom:20px;">'
                f'<span style="color:{sig_color}; font-size:2.5rem; font-weight:800;">{T["sell"] if sig_color=="#22c55e" else T["wait"]}</span></div>', unsafe_allow_html=True)

    # Main KPI Cards (Localized Labels)
    c1, c2, c3 = st.columns(3)
    c1.markdown(f'<div class="kpi-card"><div style="color:#facc15;">💰 {T["price"]}</div><div style="font-size:2.1rem; font-weight:800; color:white;">₹{curr_p}</div></div>', unsafe_allow_html=True)
    c2.markdown(f'<div class="kpi-card"><div style="color:#22c55e;">📈 {T["pred"]}</div><div style="font-size:2.1rem; font-weight:800; color:#22c55e;">₹{pred_p}</div></div>', unsafe_allow_html=True)
    c3.markdown(f'<div class="kpi-card"><div style="color:#3b82f6;">📍 {T["dist"]}</div><div style="font-size:2.1rem; font-weight:800; color:#3b82f6;">12 KM</div></div>', unsafe_allow_html=True)

    # 5. NEW VISUALIZATIONS
    st.markdown("---")
    v1, v2 = st.columns(2)

    with v1:
        st.markdown(f"### 📊 {T['seasonal']}")
        # Heatmap Simulation
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        heat_vals = [curr_p + np.random.randint(-300, 300) for _ in range(12)]
        fig_heat = px.imshow([heat_vals], x=months, color_continuous_scale='Greens', aspect="auto")
        fig_heat.update_layout(height=250, margin=dict(l=10, r=10, t=10, b=10), paper_bgcolor='rgba(0,0,0,0)', font=dict(color="white"))
        st.plotly_chart(fig_heat, use_container_width=True)

    with v2:
        st.markdown(f"### 🕸️ {T['radar']}")
        # Radar Chart Simulation
        categories = [T['price_h'], T['dist'], T['vol'], T['trust']]
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(r=[85, 20, 70, 95], theta=categories, fill='toself', name=sel_loc, line_color=sig_color))
        fig_radar.add_trace(go.Scatterpolar(r=[65, 50, 95, 60], theta=categories, fill='toself', name="District Hub", line_color="#3b82f6"))
        fig_radar.update_layout(polar=dict(radialaxis=dict(visible=False)), showlegend=False, height=250, margin=dict(l=40, r=40, t=30, b=30), paper_bgcolor='rgba(0,0,0,0)', font=dict(color="white"))
        st.plotly_chart(fig_radar, use_container_width=True)

    # WhatsApp Integration
    wa_url = f"https://wa.me/{wa_num}?text=AgriIntel%20Update%20for%20{sel_crop}"
    st.markdown(f'<a href="{wa_url}" target="_blank"><button style="width:100%; background:#25D366; color:white; border:none; padding:12px; border-radius:15px; font-weight:bold; cursor:pointer; margin:20px 0;">{T["wa_btn"]}</button></a>', unsafe_allow_html=True)

    # 6. LOCALIZED MANDI TABLE
    st.markdown(f"### 📍 {T['mandi_h']}")
    comp_df = pd.DataFrame({
        T["mandi_h"]: [sel_loc, "District Hub", "State Central"],
        T["price_h"]: [f"₹{curr_p}", f"₹{round(curr_p*0.96)}", f"₹{round(curr_p*1.12)}"]
    })
    st.table(comp_df)

    # Price Trend Chart
    fig_trend = go.Figure(go.Scatter(y=filtered['average'].tail(15), line=dict(color='#22c55e', width=4), fill='tozeroy'))
    fig_trend.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="white"), height=300, xaxis_title=T["chart_x"], yaxis_title=T["chart_y"])
    st.plotly_chart(fig_trend, use_container_width=True)
    
# 7. FIXED VOICE ENGINE (Removed 'key' to fix TypeError)
if voice_btn:
    voice_text = f"{T['title']}. {sel_crop} {T['price']} {curr_p}."
    
    voice_script = f"""
        <script>
            window.speechSynthesis.cancel();
            var utterance = new SpeechSynthesisUtterance("{voice_text}");
            utterance.lang = "{T['voice']}";
            utterance.rate = 0.9;
            
            // Search for local voice
            var voices = window.speechSynthesis.getVoices();
            var foundVoice = false;
            for(var i=0; i<voices.length; i++) {{
                if(voices[i].lang.includes("{T['voice']}")) {{
                    utterance.voice = voices[i];
                    foundVoice = true;
                    break;
                }}
            }}
            window.speechSynthesis.speak(utterance);
        </script>
    """
    # Create a container to hold the component
    voice_container = st.empty()
    with voice_container:
        st.components.v1.html(voice_script, height=0)

   
# 8. NEWS TICKER
news = ["Mysuru Kisan Expo 2026", "New MSP Guidelines Issued", "Fertilizer Subsidy Active"]
news_html = "".join([f'<span style="margin-right:50px;">🌾 {item}</span>' for item in news])
st.markdown(f'<div class="ticker-wrap"><div class="ticker">{news_html} {news_html}</div></div>', unsafe_allow_html=True)
