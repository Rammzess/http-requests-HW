import requests
import os


class YaUploader:
    def __init__(self, token):
        self.token = token
    
 
    def _get_link(self, path_to_file):
        # Получение ссылки на загрузку
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"   
        params = {"path": path_to_file, "overwrite": "true"}
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
            }
        response = requests.get(upload_url, headers=headers, params=params)
        # print(response.json())
        return response.json()

    def _upload_file(self, path_on_disk: str, file_path_pc):
        """Метод загружает файл на яндекс диск"""  
        response_dict = self._get_link(path_to_file=path_on_disk)
        href = response_dict.get("href", "")   # возвращает пустую строку если нет ключа Хреф
        #заливка
        response = requests.put(href, data=open(file_path_pc, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Успешно загружено!")
        return

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = os.path.join(os.getcwd(), "aloha.txt") 
    token = 'AQAAAABPGYUbAADLW2W-eByeo0S-hA_wWEkKj24'
    uploader = YaUploader(token)
    result = uploader._upload_file("disk:/test/aloha.txt", path_to_file)   # сработало только когда прописал полный путь к файлу disk: и название

    
    
    
 

   
