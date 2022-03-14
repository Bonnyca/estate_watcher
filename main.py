import pprint
import requests
import json
import time
from pymongo import MongoClient


class ZillowScraper:
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'zguid=23|%2473e0993e-2f17-4576-a8ef-dfd82a2b18c7; '
                  'zgsession=1|1b940487-b41b-4f5e-9083-d9b401676ae3; DoubleClickSession=true; srpfv=1|_w; '
                  'fbc=fb.1.1573792070592.IwAR2YZtkQ2hLI6heAP3DoyB6v-RSW13VSY564VSRiAgKI-zS7cWIrZc4e0dk; '
                  'ki_t=1568348656142%3B1574381928544%3B1574381987101%3B4%3B7; '
                  'ki_s=199442%3A0.0.0.0.2%3B199444%3A0.0.0.0.2%3B199445%3A0.0.0.0.2; _csrf=Zym5YX1pLrvzP4MqoF-HFsXw; '
                  'zgcus_lbut=; zgcus_aeut=96850472; zgcus_ludi=5e6cf918-b452-11eb-9bfe-be7a7232202f-96850; '
                  'ZG_SW_REGISTERED=true; _pxvid=d37ea973-11da-11ec-8b75-4a4746695a56; '
                  '__stripe_mid=ab5cb61a-ae23-4a09-8374-dd43236983ec94b8fe; '
                  'OptanonConsent=isIABGlobal=false&datestamp=Wed+Sep+15+2021+16%3A32%3A08+GMT-0700+('
                  'Pacific+Daylight+Time)&version=5.11.0&landingPath=https%3A%2F%2Fwww.zillow.com%2Frental-manager%2F'
                  '%3Fsource%3Dtopnav%26itc%3Dpostbutton_sitenav&groups=1%3A1%2C3%3A1%2C4%3A1; G_ENABLED_IDPS=google; '
                  'G_AUTHUSER_H=0; swVersion=0.0.343; g_state={"i_l":1,"i_p":1641870526581}; '
                  'loginmemento=1|0093781a2e86ed847cff5e90c38eb2e02bf5dd795c7a4bd39751430a94bfccf9; '
                  'userid=X|3|74ed3dbc1c02d4d9%7C3%7CnvEaJsGVHLB1zcGwUrkAnVlMv-XmsV_VukTeh8VdAY8%3D; '
                  'JSESSIONID=F999E57AA79CECFF428A99BE00E62F42; '
                  'ZILLOW_SID=1'
                  '|AAAAAVVbFRIBVVsVEit4asD98rtVZufFU3P2o4rpp3myXerqz8J2Re8GuZL1bd60QX71lexN3DHGSZ0i4VG97L%2BkfjK1; '
                  '_px3=7b6e26f07cec6283600ded22e3090c4cbec480b5564bca1b711aef49142da09b'
                  ':HJYdkTIK7Z8HXVnhT5bRUx2n4dXTCVlDHIkImGEFECYumU+xXW24fnmqJZ07uBIoMpYgKy0Y3FM5ufC5zTc93w==:1000'
                  ':xiAK9tFn65xo9QCeFuYHWpjr7ArpDwbU9d2/HM5KrS'
                  '/gQk4pSgApOQgGHLFOA9DljlFmPEe3XFS9mVX1aiCKwk5hhuuDZ3IQFxNQUj1PONhmFWTLlQtt800ix6lv'
                  '/ZL2brMmQ6Sv2ziGwQORfMT/wrR2J7Ffm4b9/qqUbnjqz95/mN7KK73zPZlQ2arOz8pyL8fgsXfG0TiXQLaYaluY8A==; '
                  'AWSALB=k/kVy2'
                  '/7SEO5Zaclsa3q311ZpncmmFgPfbTobZyipMnNIp0bp5J45fOm5f7nVIR3zq8UECaSk5GsGL4xSlFpOazJHuN8'
                  '/isWnDK2ptWHf1WOMihY8CKxoC0Li6K9; '
                  'AWSALBCORS=k/kVy2'
                  '/7SEO5Zaclsa3q311ZpncmmFgPfbTobZyipMnNIp0bp5J45fOm5f7nVIR3zq8UECaSk5GsGL4xSlFpOazJHuN8'
                  '/isWnDK2ptWHf1WOMihY8CKxoC0Li6K9; '
                  'search=6|1648870669720%7Cregion%3Dredwood-shores-redwood-city-ca%26rb%3DRedwood-Shores%252C'
                  '-Redwood-City%252C-CA%26rect%3D37.551247%252C-122.22501%252C37.516487%252C-122.269629%26disp%3Dmap'
                  '%26mdm%3Dauto%26fs%3D1%26fr%3D0%26mmm%3D1%26rs%3D0%26ah%3D0%09%09117610%09%09%09%09%09%09',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }

    def push_to_db(self, data):
        cluster = MongoClient(
            'mongodb+srv://Bonny:VThLjXsncC8lYmFc@cluster0.iwifn.mongodb.net/houses_data?retryWrites=true&w=majority')
        db = cluster['houses_data']
        collection = db['houses_coll']
        # self.db.collection.updateMany()
        # print(data)

    #
    # def page_count(self,response):
    #     content = BeautifulSoup():
    #     total_pages = content.find('span', {'class': 'result - count'})
    #     one_page_capacity = 41
    #     pages_to_parse = math.ceil(total_pages / one_page_capacity)
    #     return pages_to_parse

    def fetch(self, url, params):
        response = requests.get(url, headers=self.headers, params=params)
        json_data = response.json()
        return json_data

    def parse(self, jdata):
        to_db = []
        raw_data = jdata['cat1']['searchResults']['listResults']
        for item in raw_data:
            if 'lotAreaValue' in item['hdpData']['homeInfo']:
                house_item = {}
                house_item['sold_price'] = item['unformattedPrice']
                house_item['address_street'] = item['addressStreet']
                house_item['address_city'] = item['addressCity']
                house_item['address_state'] = item['addressState']
                house_item['address_zipcode'] = item['addressZipcode']
                house_item['beds'] = item['beds']
                house_item['baths'] = item['baths']
                house_item['area'] = item['area']
                house_item['home_type'] = item['hdpData']['homeInfo']['homeType']
                house_item['date_sold'] = int(int(item['hdpData']['homeInfo']['dateSold']) / 1000)
                house_item['lot_area'] = item['hdpData']['homeInfo']['lotAreaValue']
                to_db.append(house_item)
        return to_db

    def run(self):
        url = 'https://www.zillow.com/search/GetSearchPageState.htm'

        for page in range(1, 2):
            params = {
                'searchQueryState': '{"customRegionId":"8952f6220fX1-CR10kcul03sw9ku_11m3tt","mapBounds":{'
                                    '"west":-122.76585589628667,"east":-121.08128547202796,"south":37.22581785915044,'
                                    '"north":37.58882914918624},"isMapVisible":true,"filterState":{"doz":{'
                                    '"value":"30"},"isCondo":{"value":false},"isForSaleForeclosure":{"value":false},'
                                    '"isApartment":{"value":false},"isMultiFamily":{"value":false},"isAllHomes":{'
                                    '"value":true},"sortSelection":{"value":"globalrelevanceex"},"isAuction":{'
                                    '"value":false},"isNewConstruction":{"value":false},"isRecentlySold":{'
                                    '"value":true},"isLotLand":{"value":false},"isManufactured":{"value":false},'
                                    '"isForSaleByOwner":{"value":false},"isComingSoon":{"value":false},'
                                    '"isApartmentOrCondo":{"value":false},"isForSaleByAgent":{"value":false}},'
                                    '"isListVisible":true,"pagination":{"currentPage":%s}}' % page,
                'wants': '{"cat1":["listResults","mapResults"]}',
                'requestId': page,
            }
            json_data = self.fetch(url, params)
            to_upload = self.parse(json_data)
            self.push_to_db(to_upload)
            time.sleep(3)


if __name__ == '__main__':
    scraper = ZillowScraper()
    scraper.run()

# from bs4 import BeautifulSoup
#
# # url = 'https://www.silversea.com/destinations/cruises-arctic-greenland/reykjavik-to-kangerlussuaq-wi220721011.html?mi_u=25584706&mi_merged_country_code=USA&cid_email=em_USA_EM2112014149_PROSPECT_EXPEDITION_CON_DEM_LINK&IndividualId=25584706&utm_campaign=USA_EM2112014149_PROSPECT&utm_source=USA&utm_medium=Email&cid=92193&mid=237523708'
# url = 'https://www.zillow.com/homes/for_sale/house,multifamily,townhouse_type/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.31644857159259%2C%22east%22%3A-122.2185062111486%2C%22south%22%3A37.5196893489511%2C%22north%22%3A37.56063722952611%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22doz%22%3A%7B%22value%22%3A%2290%22%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A14%7D'
# r = requests.get(url)
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
# }
#
# print('status code', r.status_code)
# # print(r.text)
#
# soup = BeautifulSoup(r.text, 'html.parser')
# # print(soup.title.text)
# print('text',soup)
#
# price = soup.find('span', {'class': 'price usLocal'})
# print(price)

#
# headers = {'Content-Type': 'application/json',
#            # 'Accept': 'application/json, text/plain, */*',
#            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:86.0) Gecko/20100101 Firefox/86.0',
#            'Host': 'book.cruisequick.com',
#            'Referer': 'https://book.cruisequick.com/swift/cruise/package/1141555--18ngt-norway-intensive---svalbard-voyage?siid=1&lang=1',
#            'Origin': 'https://book.cruisequick.com',
#            }
#
# rr = requests.get('https://book.cruisequick.com/swift/cruise/package/1141555--18ngt-norway-intensive---svalbard-voyage?siid=1&lang=1',
#                   headers=headers)
# # print(rr.text)
# print(rr.cookies)
#
# cookies = rr.cookies
# cookies.update({'odysseus-siid': '1',
#                 'ASP.NET_SessionId': 'o1psaejunxqfstr2e5tdrthf',
#                 'OdysseusCookieSet': 'SessionFix=82d08ec8e2484e5a96734c82d0576752'})
# # payload = {'id': '1141555'}
# payload = {"filters": [{"key":"id", "values":[1141555]}]}
# r = requests.post('https://book.cruisequick.com/nitroapi/v2/cruise?pageSize=12&fetchFacets=false&groupByItineraryId=false',
#                   data=json.dumps(payload), headers=headers, cookies=cookies)
# print(r.text)


# import requests
#
#
# r = requests.get('https://www.zillow.com/homedetails/1307-Chelsea-Way-Redwood-City-CA-94061/2071945744_zpid/')
# print(r.text)
