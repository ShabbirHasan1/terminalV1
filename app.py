import asyncio
import schedule
import websockets
from json import dumps
from time import sleep
from requests import get
from flask_cors import CORS
from threading import Thread
from yliveticker import YLiveTicker
from flask import Flask, escape, request

s=["ACC.NS","ADANIENT.NS","ADANIPORTS.NS","ADANIPOWER.NS","AMARAJABAT.NS","AMBUJACEM.NS","APOLLOHOSP.NS","APOLLOTYRE.NS","ASHOKLEY.NS","ASIANPAINT.NS","AUROPHARMA.NS","AXISBANK.NS","BAJAJ-AUTO.NS","BAJAJFINSV.NS","BAJFINANCE.NS","BALKRISIND.NS","BANDHANBNK.NS","BANKBARODA.NS","BATAINDIA.NS","BEL.NS","BERGEPAINT.NS","BHARATFORG.NS","BHARTIARTL.NS","BHEL.NS","BIOCON.NS","BOSCHLTD.NS","BPCL.NS","BRITANNIA.NS","CADILAHC.NS","CANBK.NS","CENTURYTEX.NS","CHOLAFIN.NS","CIPLA.NS","COALINDIA.NS","COLPAL.NS","CONCOR.NS","CUMMINSIND.NS","DABUR.NS","DIVISLAB.NS","DLF.NS","DRREDDY.NS","EICHERMOT.NS","EQUITAS.NS","ESCORTS.NS","EXIDEIND.NS","FEDERALBNK.NS","GAIL.NS","GLENMARK.NS","GMRINFRA.NS","GODREJCP.NS","GODREJPROP.NS","GRASIM.NS","HAVELLS.NS","HCLTECH.NS","HDFC.NS","HDFCBANK.NS","HDFCLIFE.NS","HEROMOTOCO.NS","HINDALCO.NS","HINDPETRO.NS","HINDUNILVR.NS","IBULHSGFIN.NS","ICICIBANK.NS","ICICIPRULI.NS","IDEA.NS","IDFCFIRSTB.NS","IGL.NS","INDIGO.NS","INDUSINDBK.NS","INFRATEL.NS","INFY.NS","IOC.NS","ITC.NS","JINDALSTEL.NS","JSWSTEEL.NS","JUBLFOOD.NS","JUSTDIAL.NS","KOTAKBANK.NS","L&TFH.NS","LICHSGFIN.NS","LT.NS","LUPIN.NS","M&M.NS","M&MFIN.NS","MANAPPURAM.NS","MARICO.NS","MARUTI.NS","MCDOWELL-N.NS","MFSL.NS","MGL.NS","MINDTREE.NS","MOTHERSUMI.NS","MRF.NS","MUTHOOTFIN.NS","NATIONALUM.NS","NAUKRI.NS","NCC.NS","NESTLEIND.NS","COFORGE.NS","NMDC.NS","NTPC.NS","ONGC.NS","PAGEIND.NS","PEL.NS","PETRONET.NS","PFC.NS","PIDILITIND.NS","PNB.NS","POWERGRID.NS","PVR.NS","RAMCOCEM.NS","RBLBANK.NS","RECLTD.NS","RELIANCE.NS","SAIL.NS","SBILIFE.NS","SBIN.NS","SHREECEM.NS","SIEMENS.NS","SRF.NS","SRTRANSFIN.NS","SUNPHARMA.NS","SUNTV.NS","TATACHEM.NS","TATACONSUM.NS","TATAELXSI.NS","TATAMOTORS.NS","TATAPOWER.NS","TATASTEEL.NS","TCS.NS","TECHM.NS","TITAN.NS","TORNTPHARM.NS","TORNTPOWER.NS","TVSMOTOR.NS","UBL.NS","UJJIVAN.NS","ULTRACEMCO.NS","UPL.NS","VEDL.NS","VOLTAS.NS","WIPRO.NS","ZEEL.NS","^NSEI"]
q,pivot={},{}

for i in s:
    print(i)
    r=get('https://query1.finance.yahoo.com/v8/finance/chart/'+i+'?region=IN&lang=en-IN&includePrePost=false&interval=1d&range=1d&corsDomain=in.finance.yahoo.com&.tsrc=finance').json()['chart']['result'][0]['indicators']['quote'][0]
    o,h,l,c=r['open'],r['high'],r['low'],r['close']
    p=round((h[0]+l[0]+c[0])/3,2)
    r1=round(2*p-l[0],2)
    s1=round(2*p-h[0],2)
    r2=round(p+(h[0]-l[0]),2)
    s2=round(p-(h[0]-l[0]),2)
    r3=round(r1+(h[0]-l[0]),2)
    s3=round(s1-(h[0]-l[0]),2)
    r4=round(r2+(h[0]-l[0]),2)
    s4=round(s2-(h[0]-l[0]),2)
    pivot[i]=[r4,round((r4+r3)/2,2),r3,round((r3+r2)/2,2),r2,round((r2+r1)/2,2),r1,round((r1+p)/2,2),p,round((p+s1)/2,2),s1,round((s1+s2)/2,2),s2,round((s2+s3)/2,2),s3,round((s3+s4)/2,2),s4]
    j=0
    q[i]=[]
    for p in o:
        q[i].append({'time':j,'open':o[j],'high':h[j],'low':l[j],'close':c[j]})
        j+=1


html='''<!DOCTYPE HTML><html><head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
                body{background:#25292E;margin:0;width:350px;}
                table{font-family:Arial,Helvetica,sans-serif;width:100%;color:#E58947;}</style></head><body>
                <table border="0"id="myTable">
                        <tr><td>BANK NIFTY</td></tr>
                        <tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr>
                </table></body>
        <!--javascript file-->
        <script src="https://unpkg.com/lightweight-charts/dist/lightweight-charts.standalone.production.js"></script>
        <script>
class Cat{
        constructor(){
                this.q=[];
                this.cs=[];
                this.ls=[];
        }
        sD(chn){
                for(let i=0;i<this.q.length;i++){
                        var n=chn[i][0],c=a[n][l].close,w=0;
                        this.q[i].innerHTML=n;
                        this.cs[i].setData(a[n])
                        while(p[n][w]>c)w++;
                        if(w%2!=0)w--;
                        this.ls[i].setData([{time:0,value:p[n][w]}])
                        this.ls[i].applyOptions({title:np[w]})
                }
        }
}
var ga=new Cat(),lo=new Cat(),nif=new Cat(),p,a,l,np={0:'R4',2:'R3',4:'R2',6:'R1',8:'P',10:'S1',12:'S2',14:'S3',16:'S4'},
ws=new WebSocket('ws://127.0.0.1:7872/');
fetch('http://127.0.0.1:5000/d1').then(response=>response.json()).then(data=>p=data)
ws.onmessage=e=>{
        a=JSON.parse(e.data),l=a['^NSEI'].length-1;
        var ch=Object.entries(a.c);
        nif.sD([['^NSEI',0]])
        lo.sD(ch.sort(([,a],[,b])=>a-b))
        ga.sD(ch.reverse())
}
(()=>{var t=document.getElementById('myTable'),
                chartOption={width:175,height:150,handleScroll:false,
                        priceScale:{position:'none'},
                        timeScale:{visible:false},
                        crosshair:{horzLines:{visible:false},vertLines:{visible:false}},
                        grid:{vertLines:{visible:false},horzLines:{visible:false}},
                        layout:{backgroundColor:'#26292E'}
                },lc={priceLineWidth:1,priceLineStyle:0,priceScaleId:'left'};
        function setD(a,b,c,d){
                var j=0,chart=[];
                for(j;j<c;j++){
                        a.q[j]=t.rows[d].insertCell(b);
                        chart[j]=LightweightCharts.createChart(t.rows[d+1].insertCell(b),chartOption);
                        a.cs[j]=chart[j].addCandlestickSeries();
                        a.ls[j]=chart[j].addLineSeries(lc);
                        d+=2;
                }
        }
        setD(ga,0,7,2)
        setD(lo,1,7,2)
        setD(nif,0,1,0)
})();
        </script>
</html>'''

app = Flask(__name__)
CORS(app)
@app.route('/')
def hello():
    return html

@app.route('/d1')
def dds():
    return dumps(pivot)

def ss():
    app.run()


s1=["ACC.NS","ADANIENT.NS","ADANIPORTS.NS","ADANIPOWER.NS","AMARAJABAT.NS","AMBUJACEM.NS","APOLLOHOSP.NS","APOLLOTYRE.NS","ASHOKLEY.NS","ASIANPAINT.NS","AUROPHARMA.NS","AXISBANK.NS","BAJAJ-AUTO.NS","BAJAJFINSV.NS","BAJFINANCE.NS","BALKRISIND.NS","BANDHANBNK.NS","BANKBARODA.NS","BATAINDIA.NS","BEL.NS","BERGEPAINT.NS","BHARATFORG.NS","BHARTIARTL.NS","BHEL.NS","BIOCON.NS","BOSCHLTD.NS","BPCL.NS","BRITANNIA.NS","CADILAHC.NS","CANBK.NS","CENTURYTEX.NS","CHOLAFIN.NS","CIPLA.NS","COALINDIA.NS","COLPAL.NS","CONCOR.NS","CUMMINSIND.NS","DABUR.NS","DIVISLAB.NS","DLF.NS","DRREDDY.NS","EICHERMOT.NS","EQUITAS.NS","ESCORTS.NS","EXIDEIND.NS","FEDERALBNK.NS","GAIL.NS","GLENMARK.NS","GMRINFRA.NS","GODREJCP.NS"]
s2=["GODREJPROP.NS","GRASIM.NS","HAVELLS.NS","HCLTECH.NS","HDFC.NS","HDFCBANK.NS","HDFCLIFE.NS","HEROMOTOCO.NS","HINDALCO.NS","HINDPETRO.NS","HINDUNILVR.NS","IBULHSGFIN.NS","ICICIBANK.NS","ICICIPRULI.NS","IDEA.NS","IDFCFIRSTB.NS","IGL.NS","INDIGO.NS","INDUSINDBK.NS","INFRATEL.NS","INFY.NS","IOC.NS","ITC.NS","JINDALSTEL.NS","JSWSTEEL.NS","JUBLFOOD.NS","JUSTDIAL.NS","KOTAKBANK.NS","L&TFH.NS","LICHSGFIN.NS","LT.NS","LUPIN.NS","M&M.NS","M&MFIN.NS","MANAPPURAM.NS","MARICO.NS","MARUTI.NS","MCDOWELL-N.NS","MFSL.NS","MGL.NS","MINDTREE.NS","MOTHERSUMI.NS","MRF.NS","MUTHOOTFIN.NS","NATIONALUM.NS","NAUKRI.NS","NCC.NS","NESTLEIND.NS","COFORGE.NS","NMDC.NS"]
s3=["NTPC.NS","ONGC.NS","PAGEIND.NS","PEL.NS","PETRONET.NS","PFC.NS","PIDILITIND.NS","PNB.NS","POWERGRID.NS","PVR.NS","RAMCOCEM.NS","RBLBANK.NS","RECLTD.NS","RELIANCE.NS","SAIL.NS","SBILIFE.NS","SBIN.NS","SHREECEM.NS","SIEMENS.NS","SRF.NS","SRTRANSFIN.NS","SUNPHARMA.NS","SUNTV.NS","TATACHEM.NS","TATACONSUM.NS","TATAELXSI.NS","TATAMOTORS.NS","TATAPOWER.NS","TATASTEEL.NS","TCS.NS","TECHM.NS","TITAN.NS","TORNTPHARM.NS","TORNTPOWER.NS","TVSMOTOR.NS","UBL.NS","UJJIVAN.NS","ULTRACEMCO.NS","UPL.NS","VEDL.NS","VOLTAS.NS","WIPRO.NS","ZEEL.NS","^NSEI"]
q['c']={}
i=len(q['^NSEI'])

# this function is called on each ticker update
def m(a):
    p=a['p']
    k=a['id']
    q['c'][k]=a['c']
    try:
        if q[k][i]['high']<p:
            q[k][i]['high']=p
        elif q[k][i]['low']>p:
            q[k][i]['low']=p
        q[k][i]['close']=p
    except:
        q[k].append({'time':i,'open':p,'high':p,'low':p,'close':p})

def y1():
    print('1st Connection Started')
    YLiveTicker(on_ticker=m,on_close=y1,ticker_names=s1)

def y2():
    print('2nd Connection Started')
    YLiveTicker(on_ticker=m,on_close=y2,ticker_names=s2)

def y3():
    print('3rd Connection Started')
    YLiveTicker(on_ticker=m,on_close=y3,ticker_names=s3)

def ci():
    global i
    i+=1

def s():
    schedule.every(5).minutes.do(ci).tag('tick')

def z():
    schedule.clear('tick')

schedule.every().day.at('09:15').do(s)
schedule.every().day.at('03:30').do(z)

def t():
    while 1:
        schedule.run_pending()
        sleep(1)

Thread(target=y1).start()
Thread(target=y2).start()
Thread(target=y3).start()
Thread(target=t).start()
Thread(target=ss).start()

async def time(websocket, path):
    while 1:
        await websocket.send(dumps(q))
        await asyncio.sleep(1)

start_server = websockets.serve(time, "127.0.0.1", 7872)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
