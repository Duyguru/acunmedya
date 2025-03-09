#pythonda built-in bulunan modüller
#local moduller (kendi proje dosyalarımız)
#3.taraf kütüphaneler
import requests
from inheritance import Car
c1=Car("Porshe")
c1.start()

response = requests.get("https://google.com")
print(response.status_code)