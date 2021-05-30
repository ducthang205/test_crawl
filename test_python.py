# importing necessary packages
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json
import codecs
  
# for holding the resultant list
data = {}
data['cinemas'] = []
class Cinemas:
    def __init__(self, city, location, phone, hotline, images):
        self.city = city
        self.location = location
        self.phone = phone
        self.hotline = hotline
        self.images = images

urls = [
    'https://www.cgv.vn/default/cinox/site/cgv-hung-vuong-plaza',
    'https://www.cgv.vn/default/cinox/site/cgv-vivo-city',
    'https://www.cgv.vn/default/cinox/site/cgv-ct-plaza',
    'https://www.cgv.vn/default/cinox/site/cgv-parkson-dong-khoi',
    'https://www.cgv.vn/default/cinox/site/cgv-ly-chinh-thang',
    'https://www.cgv.vn/default/cinox/site/cgv-crescent-mall',
    'https://www.cgv.vn/default/cinox/site/cgv-pearl-plaza',
    'https://www.cgv.vn/default/cinox/site/cgv-pandora-city',
    'https://www.cgv.vn/default/cinox/site/cgv-hoang-van-thu',
    'https://www.cgv.vn/default/cinox/site/cgv-su-van-hanh',
    'https://www.cgv.vn/default/cinox/site/cgv-thao-dien-pearl',
    'https://www.cgv.vn/default/cinox/site/cgv-liberty-citypoint',
    'https://www.cgv.vn/default/cinox/site/cgv-celadon-tan-phu',
    'https://www.cgv.vn/default/cinox/site/cgv-aeon-binh-tan',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-landmark-81',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-thu-duc',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-dong-khoi',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-go-vap',
    'https://www.cgv.vn/default/cinox/site/saigonres-nguyen-xi',
    'https://www.cgv.vn/default/cinox/site/cgv-satra-cu-chi',
    'https://www.cgv.vn/default/cinox/site/cgv-gigamall-thu-duc',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-center-ba-trieu',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-royal-city',
    'https://www.cgv.vn/default/cinox/site/cgv-truong-dinh-plaza',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-metropolis-lieu-giai',
    'https://www.cgv.vn/default/cinox/site/cgv-aeon-ha-dong',
    'https://www.cgv.vn/default/cinox/site/cgv-mipec-tower',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-nguyen-chi-thanh',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-times-city',
    'https://www.cgv.vn/default/cinox/site/cgv-trang-tien-plaza',
    'https://www.cgv.vn/default/cinox/site/cgv-d-le-roi-soleil',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-ocean-park',
    'https://www.cgv.vn/default/cinox/site/cgv-ho-guom-plaza',
    'https://www.cgv.vn/default/cinox/site/cgv-iph-ha-noi',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-long-bien',
    'https://www.cgv.vn/default/cinox/site/cgv-sun-grand-luong-yen',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-sky-lake',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-tran-duy-hung',
    'https://www.cgv.vn/default/cinox/site/cgv-aeon-long-bien',
    'https://www.cgv.vn/default/cinox/site/cgv-rice-city',
    'https://www.cgv.vn/default/cinox/site/cgv-ha-noi-centerpoint',
    'https://www.cgv.vn/default/cinox/site/cgv-machinco',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-bac-tu-liem',
    'https://www.cgv.vn/default/cinox/site/cgv-thuy-duong-plaza',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-hai-phong',
    'https://www.cgv.vn/default/cinox/site/cgv-buon-me-thuot',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-vi-thanh',
    'https://www.cgv.vn/default/cinox/site/cgv-big-c-nha-trang',
    'https://www.cgv.vn/default/cinox/site/cgv-big-c-nha-trang',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-ha-long',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-mong-cai',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-cam-pha',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-tra-vinh',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-ha-tinh',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-kon-tum',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-son-la',
    'https://www.cgv.vn/default/cinox/site/cgv-vinh-trung-plaza',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-da-nang',
    'https://www.cgv.vn/default/cinox/site/cgv-lam-son-square',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-yen-bai',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-phu-yen',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-lang-son',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-tay-ninh',
    'https://www.cgv.vn/default/cinox/site/cgv-sense-city',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-xuan-khanh',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-hung-vuong',
    'https://www.cgv.vn/default/cinox/site/cgv-kim-cuc-plaza',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-vinh-long',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-cao-lanh',
    'https://www.cgv.vn/default/cinox/site/cgv-vinh-centre',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-thai-nguyen',
    'https://www.cgv.vn/default/cinox/site/cgv-coopmart-bien-hoa',
    'https://www.cgv.vn/default/cinox/site/cgv-big-c-dong-nai',
    'https://www.cgv.vn/default/cinox/site/cgv-binh-duong-square',
    'https://www.cgv.vn/default/cinox/site/cgv-aeon-canary',
    'https://www.cgv.vn/default/cinox/site/cgv-rach-gia',
    'https://www.cgv.vn/default/cinox/site/cgv-ecopark-hung-yen',
    'https://www.cgv.vn/default/cinox/site/cgv-vincom-quang-ngai',
    'https://www.cgv.vn/default/cinox/site/cgv-go-my-tho'
]
  
for page in urls:
    page_url = page
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(page_url)
    name = driver.find_elements_by_css_selector('.current')[1]
    city = driver.find_element_by_class_name("siteactive")
    location = driver.find_element_by_class_name("theater-address")
    phone = driver.find_element_by_css_selector('.fax .fax-input')
    hotline = driver.find_element_by_css_selector('.hotline .fax-input')
    image_elements = driver.find_elements_by_css_selector('.cycle-slide img')
    images = []
    for img in image_elements:
        img_element = img
        images.append(img_element.get_attribute("src"))
    
    data['cinemas'].append({
        "name": name.text,
        "city": city.text,
        "location": location.text,
        "phone": phone.text,
        "hotline": hotline.text,
        "images": images
    })
    driver.quit()

with open('data.json', 'w', encoding='utf8') as outfile:
    json.dump(data, outfile, ensure_ascii=False)
