from selenium import webdriver
import time
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import threading
from selenium.webdriver.common.action_chains import ActionChains

class ZaloCL:
    def __init__(self):
        self.wbitono = webdriver.Firefox(executable_path='geckodriver.exe')  # options=options,firefox_profile=profile,
        self.wbitono.get("https://id.zalo.me/account?continue=https://chat.zalo.me")
        time.sleep(2)
        phone = self.wbitono.find_element_by_id("input-phone")
        str_phone = "989133891"
        for i in str_phone:
            phone.send_keys(i)
            time.sleep(0.2)

        time.sleep(1)
        passw = self.wbitono.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/input')
        str_pass = "anhngoc123321"
        for i in str_pass:
            passw.send_keys(i)
            time.sleep(0.2)

        time.sleep(1.2)
        btnlog = self.wbitono.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div[4]/a')
        if btnlog.is_enabled():
            btnlog.click()

        self.thread1 = threading.Thread(name="ThreadPost", target=self.Thread_Post,args=())
        self.thread1.start()

    def Thread_Post(self):
        try:
            #while True:
            #    lst_avatar = self.wbitono.find_elements_by_id("list-avatar")

            while True:
                findall = self.wbitono.find_elements_by_id("contact-search-input")
                if len(findall) > 0:
                    break
                time.sleep(1)

            time.sleep(10)
            findG = self.wbitono.find_element_by_id("contact-search-input")
            str_chonoi=["Truyền File"] #,"Phố đồ ăn: sáng-trưa-chiều","Chợ Nội Khu Hope"
            while True:
                for i in str_chonoi:
                    for j in i:
                        findG.send_keys(j)
                        time.sleep(0.1)

                    timthay = self.wbitono.find_elements_by_class_name("list-friend-conctact__avatar")
                    if len(timthay) > 0:
                        timthay[0].click()
                        time.sleep(2)
                        input = self.wbitono.find_element_by_id("richInput")
                        str_mess ="RUỐC TÉP HẠ LONG 70/Túi (200g) \n" \
                                      "- Nguyên liệu chính để tạo nên món Ruốc Tép Hạ Long là Thịt nạc, tôm nõn và tép biển.\n" \
                                      "- Ruốc tép: có hương vị đậm đà, bùi bùi béo ngậy của thịt heo, vị ngọt của tép biển, tôm nõn\n" \
                                      "- Ruốc tép có thể kèm với bánh mỳ, xôi, cháo… nhưng ngon nhất vẫn là dùng chung với cơm nóng.\n" \
                                      "- Ruốc Tép phù hợp với tất cả mọi người đặc biệt là các em nhỏ.\n" \
                                      "H1-1512a - Zalo: 0989.133.891"
                            #banner-noti-browser__group-btn
                        spt = str_mess.split("\n")
                        for x in spt:
                            input.send_keys(x)
                            # actions = ActionChains(self.wbitono)
                            # actions.key_down(Keys.ALT)
                            # actions.send_keys(Keys.ENTER)
                            # actions.key_up(Keys.ALT)
                            # actions.perform()
                            time.sleep(0.2)
                        input.send_keys(Keys.ENTER)
                        #btn_send = self.wbitono.find_element_by_class_name("send-btn-chatbar")
                        #btn_send.click()

                time.sleep(10)
        except:
            self.wbitono.refresh()

if __name__=='__main__':
    zalo = ZaloCL()
