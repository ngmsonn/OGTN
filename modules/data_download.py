import requests
import json
import os


def STRING_Database(id, species, required_score):
    """
    id: ID của gene được lưu trong biến là danh sách hoặc biến đơn
    species: Mã loài. ví dụ 9606 cho người.
    required_score: Giá trị nằm trong khoảng 0 đến 1000
    """   
    list_id = id
    for i in list_id:
        url = "https://string-db.org/api/tsv/network"
        params = {
            "identifiers": i,
            "species": species,
            "required_score": required_score
        }
        response = requests.get(url, params=params)

        with open('data/network'+i+'.tsv', 'wb') as file:
            file.write(response.content)




id = ["PPARA", 'APBB1']
STRING_Database(id, "9606", 100)
