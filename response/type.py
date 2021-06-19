from response import carousel

def text(response):
    return {
        "fulfillmentMessages": [
            {
                "payload": {
                    "line": {
                        "type": "text",
                        "text": response
                    }
                }
            }
        ]
    }
    
def carousel_template(response):
    data = []
    for index, item in enumerate(response):
        data.append(carousel.create(response[index]))
        
    return {
        "fulfillmentMessages": [
            {
                "payload": {
                    "line": {
                        "type": "template",
                        "altText": "this is a carousel template",
                        "template": {
                            "type": "carousel",
                            "imageSize": "contain",
                            "columns": data
                        }
                    }
                }
            }
        ]
    }

