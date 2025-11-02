from django.shortcuts import render
from django.conf import settings
import requests


# Create your views here.
def get_dogs(request):
    """
    GET-запрос для получения данных о собачках

    :param request: содержание запроса
    :return: отображение данных
    """
    # Сначала отобразим список пород breeds
    breeds = []
    url_to_breeds = "https://dog.ceo/api/breeds/list"
    breeds_response = requests.get(url_to_breeds, timeout=5)
    if breeds_response.status_code == 200:
        breeds = breeds_response.json()["message"]
    # Затем проверим, ввёл ли пользователь что-то в формочку
    entered_breeds = request.GET.get("input_field")
    if entered_breeds is not None:
        entered_breeds = entered_breeds.replace(" ", "").split(",")
        # А теперь подгрузим изображения
        for breed in entered_breeds:
            # Сначала в виде ссылки
            url_to_image_url = f"https://dog.ceo/api/breed/{breed}/images/random"
            image_url_response = requests.get(url_to_image_url, timeout=5)
            if image_url_response.status_code == 200:
                try:
                    url_to_image = image_url_response.json()["message"]
                    # Затем - само изображение
                    # stream = True, потому что файлы гигантские
                    image_response = requests.get(url_to_image, stream=True, timeout=10)
                    if image_response.status_code == 200:
                        # Разгружаем большой файл по чанкам
                        with open(f"./media/{breed}.jpg", "wb") as f:
                            for chunk in image_response.iter_content(
                                chunk_size=8192
                            ):
                                if chunk:
                                    f.write(chunk)
                except Exception as e:
                    print(e)
    # Используем MEDIA для подгрузки изображений
    return render(
        request,
        "photos/dog_photos.html",
        {
            "breeds": breeds,
            "entered_breeds": entered_breeds,
            "MEDIA_URL": settings.MEDIA_URL,
        },
    )
