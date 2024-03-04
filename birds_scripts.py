import json
import random
import time
import base64

from ru.travelfood.simple_ui import NoSQL as noClass


def customcards_on_open(hashMap, _files=None, _data=None):
    ncl = noClass("database")

    keys = ncl.getallkeys()
    hashMap.put("toast", str(keys))

    jkeys = json.loads(keys)

    j = {"customcards": {
        "options": {
            "search_enabled": True,
            "save_position": True
        },

        "layout": {
            "type": "LinearLayout",
            "orientation": "vertical",
            "height": "match_parent",
            "width": "match_parent",
            "weight": "0",
            "Elements": [
                {
                    "type": "LinearLayout",
                    "orientation": "horizontal",
                    "height": "wrap_content",
                    "width": "match_parent",
                    "weight": "0",
                    "Elements": [
                        {
                            "type": "Picture",
                            "show_by_condition": "",
                            "Value": "picture",
                            "NoRefresh": False,
                            "document_type": "",
                            "mask": "",
                            "Variable": "",
                            "TextSize": "16",
                            "TextColor": "#DB7093",
                            "TextBold": True,
                            "TextItalic": False,
                            "BackgroundColor": "",
                            "width": "match_parent",
                            "height": "wrap_content",
                            "weight": 2
                        },
                        {
                            "type": "LinearLayout",
                            "orientation": "vertical",
                            "height": "wrap_content",
                            "width": "match_parent",
                            "weight": "1",
                            "Elements": [
                                {
                                    "type": "TextView",
                                    "show_by_condition": "",
                                    "Value": "@string1",
                                    "NoRefresh": False,
                                    "document_type": "",
                                    "mask": "",
                                    "Variable": ""
                                },
                                {
                                    "type": "TextView",
                                    "show_by_condition": "",
                                    "Value": "@string2",
                                    "NoRefresh": False,
                                    "document_type": "",
                                    "mask": "",
                                    "Variable": ""
                                },
                            ]
                        },
                        {
                            "type": "LinearLayout",
                            "orientation": "vertical",
                            "height": "wrap_content",
                            "width": "match_parent",
                            "weight": "1",
                            "Elements": [
                                {
                                    "type": "TextView",
                                    "show_by_condition": "",
                                    "Value": "string1",
                                    "NoRefresh": False,
                                    "document_type": "",
                                    "mask": "",
                                    "Variable": ""
                                },
                                {
                                    "type": "TextView",
                                    "show_by_condition": "",
                                    "Value": "Hehey",
                                    "NoRefresh": False,
                                    "document_type": "",
                                    "mask": "",
                                    "Variable": ""
                                },
                            ]
                        },
                    ]
                },
            ]
        }

    }
    }

    j["customcards"]["cardsdata"] = []

    for i in range(0, 5):
        c = {
            "key": str(i),
            "string1": "Материнская плата ASUS ROG MAXIMUS Z690 APEX",
            "string2": "Гнездо процессора LGA 1700",
        }
        j["customcards"]["cardsdata"].append(c)

    if not hashMap.containsKey("cards"):
        hashMap.put("cards", json.dumps(j, ensure_ascii=False).encode('utf8').decode())

    return hashMap


def custom_card_on_tap(hashMap, _files=None, _data=None):
    # hashMap.put("toast", "res=" + str(
    #     hashMap.get("listener") + "/" + str(hashMap.get("layout_listener")) + "/" + str(
    #         hashMap.get("card_data")) + str(hashMap.get("cardsdata")) + "/" + str(
    #         hashMap.get("cards")
    #     )))
    # cards = json.loads(hashMap.get("cards"))
    # keys = []
    # for rec in cards["customcards"]["cardsdata"]:
    #     keys.append(rec["key"])
    #
    # hashMap.put("toast", "key=" + str(keys))
    # hashMap.put("toast", "selected=" + str(hashMap.get("selected_card_key")))

    hashMap.put("selected", str(hashMap.get("selected_card_key")))
    hashMap.put("ShowScreen", "Карточка птицы")

    return hashMap


def on_add(hashMap, _files=None, _data=None):
    hashMap.put("ShowScreen", "Добавить птицу")

    return hashMap


def save_bird(hashMap, _files=None, _data=None):
    bird_name = hashMap.get("name")
    bird_feathers = hashMap.get("feathers")

    if hashMap.containsKey("gallery_picture"):
        bird_picture = hashMap.get("gallery_picture")
    elif hashMap.containsKey("photo_picture"):
        bird_picture = hashMap.get("photo_picture")

    ncl = noClass("database")


    bird_data = {"name": bird_name, "feathers": bird_feathers, "picture": bird_picture}
    ncl.put(bird_name, json.dumps(bird_data,ensure_ascii=False), True)

    hashMap.put("toast", "Сохранено")

    return hashMap()


def add_bird_back(hashMap, _files=None, _data=None):
    hashMap.put("ShowScreen", "Список птиц")

    return hashMap
