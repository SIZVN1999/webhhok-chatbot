import requests
import json
from flask import Flask, request, abort

app = Flask(__name__)


@app.route('/')
def hello():
    return 'hello sizvn', 200

@app.route('/webhook', methods = ['POST', 'GET'])
def webhook():
    req = request.get_json(silent=True, force=True)
    query_result = req.get('queryResult')
    fulfillmentText = ''
    action = query_result.get('action')
    # print(action)
    
    if (action == 'add.number'):
        
        numb1 = int(query_result.get('parameters').get('numb1'))
        numb2 = int(query_result.get('parameters').get('numb2'))
        result = str(numb1+numb2)
        fulfillmentText = str(numb1)+" + "+str(numb2)+" = "+result
        return {
            "fulfillmentMessages": [
            {
            "payload": {
                "line": {
                    "type": "template",
                    "altText": "this is a confirm template",
                        "template": {
                            "type": "confirm",
                            "actions": [
                                {
                                    "type": "message",
                                    "label": "Yes",
                                    "text": "Yes"
                                },
                                {
                                    "type": "message",
                                    "label": "No",
                                    "text": "No"
                                }
                            ],
                            "text": fulfillmentText+" ใช่หรือไม่ ?"
                        }
                    }
                }
            }
        ]
        }, 200
        
    elif(action == 'get.province'):
        url = "http://192.168.3.13:3000/address/province"
        response = requests.request("GET", url)
        data = response.json()
        
        fulfillmentMessage = "จังหวัดในประเทศไทยมีทั้งหมด "+str(len(data))+" จังหวัด ได้แก่ \n"
        
        for item in data:
            fulfillmentMessage += item['NAME_TH']+" \n"

        return   {
            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            fulfillmentMessage
                        ]
                    }
                }
            ]
        }, 200
        
    elif (action == 'get.productbyId'):
        numb1 = str(query_result.get('parameters').get('number'))
        numb1 = numb1.split('.')
        numb1 = numb1[0]
        
        url = "http://192.168.3.13:3000/Line/product/"+numb1
        response = requests.request("GET", url)
        data = response.json()
        
        product_name = str(data['Product_Name'])
        
        return {
            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            "สินค้าที่คุณค้นหาอยู่ คือ : \n"+product_name
                        ]
                    }
                }
            ]
        },200
        