import requests
import logging
import json
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    logging.warning('Hello API!')
    return 'Hello API!'


@app.route('/webhook', methods=['POST', 'GET'])
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
        data = {
            "fulfillmentMessages": [
                {
                    "payload": {
                        "line": {

                            "type": "text",
                            "text": fulfillmentText
                        }
                    }
                }
            ]
        }
        return jsonify(data), 200

    elif(action == 'get.province'):
        url = "http://192.168.3.13:3000/address/province"
        response = requests.request("GET", url)
        data = response.json()

        fulfillmentMessage = "จังหวัดในประเทศไทยมีทั้งหมด " + \
            str(len(data['payload']))+" จังหวัด ได้แก่ \n"

        for index, item in enumerate(data['payload']):
            fulfillmentMessage += "province " + \
                str(index+1) + " : "+item['NAME_TH']+" \n"

        data = {
            "fulfillmentMessages": [
                {
                    "payload": {
                        "line": {

                            "type": "text",
                            "text": fulfillmentMessage
                        }
                    }
                }
            ]
        }

        return jsonify(data), 200

    elif (action == 'get.productbyId'):
        numb1 = str(query_result.get('parameters').get('number'))
        numb1 = numb1.split('.')
        numb1 = numb1[0]

        url = "http://192.168.3.13:3000/Line/product/"+numb1
        response = requests.request("GET", url)
        data = response.json()

        product_name = str(data['Product_Name'])

        data = {
            "fulfillmentMessages": [
                {
                    "payload": {
                        "line": {

                            "type": "text",
                            "text": "สินค้าที่คุณตามหา คือ : \n"+product_name
                        }
                    }
                }
            ]
        }

        return jsonify(data), 200
