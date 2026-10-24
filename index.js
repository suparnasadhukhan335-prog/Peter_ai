const express = require('express');
const cors = require('cors');
const app = express();
app.use(cors());
app.use(express.json());
const PORT = process.env.PORT || 3000;
app.get('/', (req,res)=>{
res.send(`<html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>PETER AI</title><style>body{margin:0;font-family:sans-serif;background:#0a0a0a;color:white;display:flex;justify-content:center;padding:20px}.box{width:100%;max-width:500px;background:#1a1a1a;border-radius:16px;padding:16px}h2{text-align:center;color:#4a7cff}.chat{height:400px;overflow-y:auto;background:#111;border-radius:12px;padding:10px;margin:10px 0}.user{background:#2a5bd7;padding:8px 12px;border-radius:12px;margin:6px 0;text-align:right;margin-left:40px}.ai{background:#333;padding:8px 12px;border-radius:12px;margin:6px 0;margin-right:40px}.row{display:flex}input{flex:1;padding:12px;border-radius:20px;border:none;background:#222;color:white}button{padding:12px 18px;border-radius:20px;border:none;background:#2a5bd7;color:white;margin-left:8px}</style></head><body><div class="box"><h2>🔥 PETER AI - LIVE</h2><div class="chat" id="chat"></div><div class="row"><input id="inp" placeholder="Bolo Boss..."><button onclick="send()">Send</button></div></div><script>const chat=document.getElementById('chat');async function send(){const i=document.getElementById('inp');const t=i.value;if(!t)return;chat.innerHTML+='<div class=user>'+t+'</div>';i.value='';const r=await fetch('/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:t})});const d=await r.json();chat.innerHTML+='<div class=ai>'+d.reply+'</div>';chat.scrollTop=chat.scrollHeight;}</script></body></html>`);
});
app.post('/chat',(req,res)=>{
const m=(req.body.message||'').toLowerCase();let reply='';
if(m.includes('ke tumi')||m.includes('who'))reply="Ami PETER Boss! 😎 Suparna amake baniyeche tomar jonno!";
else if(m.includes('kemon'))reply="Bindass achi Boss! Tumi bolo kemon acho? 😊";
else if(m.includes('love'))reply="Arey love matter? Mon khule bolo Boss, Peter ache! 😏";
else{const a=["Haan Boss bolo! 😎","Ekdom Boss! 🔥 Bolo?","Wah interesting! 😍","Suparna Boss er choice best! 💯","Bolo ki korte hobe Boss!"];reply=a[Math.floor(Math.random()*a.length)]+" (Tumi: "+req.body.message+")";}
res.json({reply});
});
app.listen(PORT,()=>console.log('PETER Live '+PORT));
