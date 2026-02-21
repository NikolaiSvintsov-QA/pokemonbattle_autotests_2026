from config.settings import BASE_URL, TOKEN   # импортируем значения из настроек

def test_env_loaded():
    assert BASE_URL is not None   # проверяем, что BASE_URL вообще загрузился
    assert TOKEN is not None      # проверяем, что TOKEN тоже загрузился