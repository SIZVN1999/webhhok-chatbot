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
