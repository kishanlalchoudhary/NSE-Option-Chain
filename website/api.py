import requests
import json

url_oc      = "https://www.nseindia.com/option-chain"
url_nf      = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'
url_fnf     = 'https://www.nseindia.com/api/option-chain-indices?symbol=FINNIFTY'
url_bnf     = 'https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36', 'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}

sess = requests.Session()
cookies = dict()

def set_cookie():
    request = sess.get(url_oc, headers=headers)
    cookies = dict(request.cookies)
    print("cookies set successfully")

def get_data(url):
    set_cookie()
    response = sess.get(url, headers=headers, cookies=cookies)
    if(response.status_code==200):
        print("get_data successfully")
        return response.text
    print("error in get_data")

def requiredDataIndex(data, requiredDataIndex, expiryDate):
    for i in range(len(data['records']['data'])) :
        ExpiryDate = data['records']['data'][i]
        if expiryDate == ExpiryDate['expiryDate'] :
            requiredDataIndex.append(i)

def finalRequiredData(requiredDataIndex, requiredData):
    finalDataArray = []
    for i in requiredDataIndex:
        finalDataSubArray = []
        if (requiredData[i].get('CE') != None) and (requiredData[i].get('PE') != None):
            finalDataSubArray.append("%.2f" % round(requiredData[i]['CE']["openInterest"], 2))
            finalDataSubArray.append("%.2f" % round(requiredData[i]['CE']["changeinOpenInterest"], 2))
            finalDataSubArray.append("%.2f" % round(requiredData[i]['CE']["totalTradedVolume"], 2))
            finalDataSubArray.append("%.2f" % round(requiredData[i]['CE']["impliedVolatility"], 2))
            finalDataSubArray.append("%.2f" % round(requiredData[i]['CE']["lastPrice"], 2))
            finalDataSubArray.append("%.2f" % round(requiredData[i]['CE']["change"], 2))
            finalDataSubArray.append("%.2f" % round(requiredData[i]['CE']["bidQty"], 2))
            finalDataSubArray.append("%.2f" % round(requiredData[i]['CE']["bidprice"], 2))
            finalDataSubArray.append("%.2f" % round(requiredData[i]['CE']["askPrice"], 2))
            finalDataSubArray.append("%.2f" % round(requiredData[i]['CE']["askQty"], 2))
            finalDataSubArray.append("%.2f" % round(requiredData[i]['PE']["strikePrice"], 2))
            finalDataSubArray.append("%.2f" % round(requiredData[i]['PE']["bidQty"], 2))
            finalDataSubArray.append("%.2f" % round(requiredData[i]['PE']["bidprice"], 2))
            finalDataSubArray.append("%.2f" % round(requiredData[i]['PE']["askPrice"], 2))
            finalDataSubArray.append("%.2f" % round(requiredData[i]['PE']["askQty"], 2))
            finalDataSubArray.append("%.2f" % round(requiredData[i]['PE']["change"], 2))
            finalDataSubArray.append("%.2f" % round(requiredData[i]['PE']["lastPrice"], 2))
            finalDataSubArray.append("%.2f" % round(requiredData[i]['PE']["impliedVolatility"], 2))
            finalDataSubArray.append("%.2f" % round(requiredData[i]['PE']["totalTradedVolume"], 2))
            finalDataSubArray.append("%.2f" % round(requiredData[i]['PE']["changeinOpenInterest"], 2))
            finalDataSubArray.append("%.2f" % round(requiredData[i]['PE']["openInterest"], 2))
        else:
            if (requiredData[i].get('CE') != None) :
                finalDataSubArray.append("%.2f" % round(requiredData[i]['CE']["openInterest"], 2))
                finalDataSubArray.append("%.2f" % round(requiredData[i]['CE']["changeinOpenInterest"], 2))
                finalDataSubArray.append("%.2f" % round(requiredData[i]['CE']["totalTradedVolume"], 2))
                finalDataSubArray.append("%.2f" % round(requiredData[i]['CE']["impliedVolatility"], 2))
                finalDataSubArray.append("%.2f" % round(requiredData[i]['CE']["lastPrice"], 2))
                finalDataSubArray.append("%.2f" % round(requiredData[i]['CE']["change"], 2))
                finalDataSubArray.append("%.2f" % round(requiredData[i]['CE']["bidQty"], 2))
                finalDataSubArray.append("%.2f" % round(requiredData[i]['CE']["bidprice"], 2))
                finalDataSubArray.append("%.2f" % round(requiredData[i]['CE']["askPrice"], 2))
                finalDataSubArray.append("%.2f" % round(requiredData[i]['CE']["strikePrice"], 2))
                for j in range(10):
                    finalDataSubArray.append("-")
            else:
                for j in range(9):
                    finalDataSubArray.append("-")
                finalDataSubArray.append("%.2f" % round(requiredData[i]['PE']["strikePrice"], 2))
                finalDataSubArray.append("%.2f" % round(requiredData[i]['PE']["bidQty"], 2))
                finalDataSubArray.append("%.2f" % round(requiredData[i]['PE']["bidprice"], 2))
                finalDataSubArray.append("%.2f" % round(requiredData[i]['PE']["askPrice"], 2))
                finalDataSubArray.append("%.2f" % round(requiredData[i]['PE']["askQty"], 2))
                finalDataSubArray.append("%.2f" % round(requiredData[i]['PE']["change"], 2))
                finalDataSubArray.append("%.2f" % round(requiredData[i]['PE']["lastPrice"], 2))
                finalDataSubArray.append("%.2f" % round(requiredData[i]['PE']["impliedVolatility"], 2))
                finalDataSubArray.append("%.2f" % round(requiredData[i]['PE']["totalTradedVolume"], 2))
                finalDataSubArray.append("%.2f" % round(requiredData[i]['PE']["changeinOpenInterest"], 2))
                finalDataSubArray.append("%.2f" % round(requiredData[i]['PE']["openInterest"], 2))
        finalDataArray.append(finalDataSubArray)
    return finalDataArray

get_data(url_nf)
response_text = get_data(url_nf)
data_nf = json.loads(response_text)

get_data(url_fnf)
response_text = get_data(url_fnf)
data_fnf = json.loads(response_text)

get_data(url_bnf)
response_text = get_data(url_bnf)
data_bnf = json.loads(response_text)

nfExpiryDate = data_nf["records"]["expiryDates"][0]
fnfExpiryDate = data_fnf["records"]["expiryDates"][0]
bnfExpiryDate = data_bnf["records"]["expiryDates"][0]

nfRequiredDataIndex = []
fnfRequiredDataIndex = []
bnfRequiredDataIndex = []

requiredDataIndex(data_nf, nfRequiredDataIndex, nfExpiryDate)
requiredDataIndex(data_fnf, fnfRequiredDataIndex, fnfExpiryDate)
requiredDataIndex(data_bnf, bnfRequiredDataIndex, bnfExpiryDate)

nfRequiredData = data_nf['records']['data']
fnfRequiredData = data_fnf['records']['data']
bnfRequiredData = data_bnf['records']['data']

nfRequiredData = finalRequiredData(nfRequiredDataIndex, nfRequiredData)
fnfRequiredData = finalRequiredData(fnfRequiredDataIndex, fnfRequiredData)
bnfRequiredData = finalRequiredData(bnfRequiredDataIndex, bnfRequiredData)