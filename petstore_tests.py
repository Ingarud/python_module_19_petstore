import requests
import json
from config import url, info, info2, info_new, status, petId, petId2

# Создаем новых питомцев
res_newpet = requests.post(f'{url}', headers={'accept':'application/json', 'Content-Type': 'application/json'}, data=json.dumps(info, ensure_ascii=False))
print(res_newpet.status_code)
print(res_newpet.json())
print(res_newpet.text)

res_newpet2 = requests.post(f'{url}', headers={'accept':'application/json', 'Content-Type': 'application/json'}, data=json.dumps(info2, ensure_ascii=False))
print(res_newpet2.status_code)
print(res_newpet2.json())
print(res_newpet2.text)

# Ищем питомцев по статусу
res_status = requests.get(f'{url}/findByStatus?status={status}', headers={'accept':'application/json'})
print(res_status.status_code)
print(res_status.text)
print(res_status.json())
print(type(res_status.json()))

# Ищем питомцев по Id
res_id = requests.get(f'{url}/{petId}', headers={'accept':'application/json', 'Content-Type': 'application/json'})
print(res_id.status_code)
print(res_id.json())
print(res_id.text)

res_id2 = requests.get(f'{url}/{petId2}', headers={'accept':'application/json', 'Content-Type': 'application/json'})
print(res_id2.status_code)
print(res_id2.json())
print(res_id2.text)

# Вносим изменения в данные питомца
res_change = requests.put(f'{url}', headers={'accept':'application/json', 'Content-Type': 'application/json'}, data=json.dumps(info_new, ensure_ascii=False))
print(res_change.status_code)
print(res_change.json())
print(res_change.text)

# Удаляем питомца
res_delete = requests.delete(f'{url}/{petId}', headers={'accept':'application/json', 'Content-Type': 'application/json'})
print(res_delete.status_code)
print(res_delete.json())
print(res_delete.text)

# Проверяем удален ли питомец
res_sum = requests.get(f'{url}/{petId}', headers={'accept':'application/json', 'Content-Type': 'application/json'})
print(res_sum.status_code)
print(res_sum.json())
print(res_sum.text)