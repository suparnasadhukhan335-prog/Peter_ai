from flask import Flask, request, jsonify, render_template_string
from datetime import datetime
import pytz
import os
import requests
app = Flask(__name__)
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1"><title>PETER AI</title><style>body{background:#0a0a0a;color:white;font-family:Arial;padding:20px}#chat{height:70vh;overflow-y:auto;border:1px solid #333;padding:10px;border-radius:10px}.msg{margin:10px 0;padding:10px;border-radius:10px}.user{background:#1a73e8;text-align:right}.bot{background:#222}input{width:75%;padding:12px;border-radius:20px;border:none}button{padding:12px 20px;border-radius:20px;border:none;background:#1a73e8;color:white}</style></head><body><h2>🤖 PETER AI</h2><div id="chat"></div><br><input id="inp" placeholder="Bolo Boss..."><button onclick="send()">Send</button><script>async function send(){let i=document.getElementById('inp');let t=i.value;if(!t)return;let c=document.getElementById('chat');c.innerHTML+=`<div class='msg user'>${t}</div>`;i.value='';let r=await fetch('/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:t})});let d=await r.json();c.innerHTML+=`<div class='msg bot'>${d.reply}</div>`;c.scrollTop=c.scrollHeight;}document.getElementById('inp').addEventListener('keypress',function(e){if(e.key==='Enter')send()});</script></body></html>"""
@app.route('/')
def home(): return render_template_string(HTML)
@app.route('/chat', methods=['POST'])
def chat():
    data=request.get_json(); user_msg=data.get('message','')
    ist=pytz.timezone('Asia/Kolkata'); now=datetime.now(ist)
    if 'time' in user_msg.lower() or 'somoy' in user_msg.lower(): return jsonify({'reply': f"Boss somoy {now.strftime('%I:%M %p')} ⏰"})
    try:
        url="https://api.groq.com/openai/v1/chat/completions"; headers={"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}; payload={"model": "llama-3.1-8b-instant", "messages": [{"role": "system", "content": "Tumi PETER, Suparna Boss er assistant, Boss bole dakbe"}, {"role": "user", "content": user_msg}]}
        r=requests.post(url, headers=headers, json=payload); ai_reply=r.json()['choices'][0]['message']['content']; return jsonify({'reply': ai_reply})
    except Exception as e: return jsonify({'reply': f"Boss Render e API Key bosate hobe! {str(e)[:100]}"})
if __name__ == '__main__': app.run(host='0.0.0.0', port=10000)
