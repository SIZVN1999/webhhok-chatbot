def create(data):
    return {
        "thumbnailImageUrl": data['IMAGE'],
        "title": "          "+data['NAME'],
        "text": data['DETAIL'],
        "actions": [
          {
            "type": "uri",
            "label": "ดูรายละเอียด",
            "uri": "https://www.tohome.com/"
          }
        ],
        "imageBackgroundColor": "#FFFFFF"
    }