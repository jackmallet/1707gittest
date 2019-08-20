import redis,os
import requests, re, time, csv, random
from selenium import webdriver
from R_file import Insert_data
from lxml import etree
# from proxies_ip_api import Ip_manager_Spider


class Qianlima_Spider:
    def __init__(self):
        # 建立redis连接池 11为剑鱼 12为千里马
        pool = redis.ConnectionPool(host='120.77.159.174', port=6379, db=14)
        self.r = redis.Redis(connection_pool=pool)
        # self.ip_cont = 1

    def crawl_list(self):
        # 用户名(13711773487
        usernamepassword = [[18925125930, 'jinghongpenhui92']]
        # usernamepassword = [[18925125930,'jinghongpenhui92'],[13711773487,13711773487],['wuyaobin', 123456]]
        # 18675961789 961789   18925125930 jinghongpenhui92 ['wuyaobin', 123456],
        # usernamepassword = [[18675961789,961789]]
        count = -13
        for x in usernamepassword:
            user_name = x[0]
            user_password = x[1]
            count = count + 13
            chromeOptions = webdriver.ChromeOptions()
            # 设置代理
            # self.ip_cont = self.ip_cont + 1
            # print(self.ip_cont)
            # if self.ip_cont % 2 == 0:
            #     Ip = Ip_manager_Spider().get_ip()
            #     chromeOptions.add_argument("--proxy-server=" + Ip['http'])
            # else:
            #     Ip1 = Ip_manager_Spider().get_ip1()
            #     chromeOptions.add_argument("--proxy-server=" + Ip1['http'])
            # self.ip_cont += 0
            # 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
            # 模拟浏览器chrome
            driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe', chrome_options = chromeOptions)
            # 查看本机ip，查看代理是否起作用
            # driver.get("http://httpbin.org/ip")
            # print(driver.page_source)
            time.sleep(3)

            # time.sleep(2)
            driver.get('http://center.qianlima.com/login.jsp')
            # 刷新
            # counter = 1
            # while(counter<3):
            #     driver.refresh()
            #     time.sleep(2)
            #     counter=counter+1
            #     print(counter)

            # 鼠标左键点击用户名输入框(去除开始有的字)
            # driver.set_page_load_timeout(5)
            driver.find_element_by_xpath('//*[ @ id = "abc"]').click()
            # item = driver.find_element_by_xpath('//div[@class="ZD_main_biaoR"]//input[@name="username"]').click()
            print('断点调试')
            # 输入用户名
            driver.find_element_by_xpath('//div[@class="ZD_main_biaoR"]//input[@name="username"]').send_keys(user_name)
            # 输入密码
            driver.find_element_by_xpath('//div[@class="ZD_main_biaoR"]//input[@name="password"]').send_keys(user_password)
            # 点击登录按钮
            driver.find_element_by_xpath('//input[@id="deng"]').click()
            time.sleep(1)
        # 点击招标中心
            driver.find_element_by_xpath('//a[@id="num3"]').click()
            time.sleep(1)
        # 鼠标左键点击输入框(同上去除字)
            driver.find_element_by_xpath('//input[@class="hui"]').click()
            # 输入要搜索的内容
            driver.find_element_by_xpath('//input[@class="hei"]').send_keys('广告')
            # 点击查找按钮
            driver.find_element_by_xpath('//input[@id="fsubmit"]').click()
            # 跟随页面跳转到新页面
            driver.switch_to_window(driver.window_handles[1])
            # 隐性等待
            time.sleep(10)
            # 点击需要选择的地区,6是广东，16是江苏,31是浙江
            driver.find_element_by_xpath('//dl[@id="select1"]/dd/a[6]').click()
            # // *[ @ id = "select1"] / dd / a[31]
            # 选取招标公告内容明天26
            driver.find_element_by_xpath('//dl[@id="select2"]/dd[2]/a').click()
            # 选取标题作为搜索项目
            # driver.find_element_by_xpath('//dl[@id="select5"]/dd[2]/a').click()
            # 拉到最底端
            js = "var q=document.documentElement.scrollTop=10000"
            driver.execute_script(js)
            time.sleep(1)
            # 从多少页开始
            for y in range(count):
                # 拉到最底端
                js = "var q=document.documentElement.scrollTop=10000"
                driver.execute_script(js)
                time.sleep(1)
                driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[4]/div/a[8]').click()
                js = "var q=document.documentElement.scrollTop=10000"
                driver.execute_script(js)
                time.sleep(1)
            #循环遍历前13页
            for x in range(13):
                surffix = []
                list_content = driver.page_source
                list_content = etree.HTML(list_content)
                list_url = list_content.xpath('//*[@id="list"]/tbody/tr/td[2]/a/@title')
                list2 = []
                for x in list_url:
                    if '移动' in x or '联通' in x or '中国联合网络通信' in x or '中国邮政' in x or '中国石油' in x or '中国石化' in x or '电信' in x:
                        list2.append(x)
                for x in list2:
                    list_url.remove(x)
                # print(list_url)
                for i in list_url:
                    js = "var q=document.documentElement.scrollTop=10000"
                    driver.execute_script(js)
                    time.sleep(1)

                    driver.find_element_by_xpath('//a[@title="' + i + '"]').click()

                # for yy in range(2,22):
                #     driver.find_element_by_xpath('//*[@id="list"]/tbody/tr['+str(yy)+']/td[@class="matter"]/a').click()


                    driver.switch_to_window(driver.window_handles[2])
                    # 拉到最底端
                    time.sleep(2)
                    js = "var q=document.documentElement.scrollTop=100000"
                    driver.execute_script(js)
                    time.sleep(2)
                    #响应内容
                    req = driver.page_source

                    try:
                        click_yn = False
                        # 当详情页当中存在附件、则通过该正则获取到附件链接、当点击该链接首先会跳转到千里马的确定窗口、可以从改窗口获取到该附件的原网页链接
                        try:
                            driver.find_element_by_xpath('//*[@id="wen"]//a[@class="l8"][1] | //*[@id="wen"]//a[@target="_blank"][1]').click()
                            driver.switch_to_window(driver.window_handles[3])
                            # //*[@id="wen"]/table/tbody/tr[2]/td[2]/a
                            # //*[@id="wen"]/div/div[2]/a
                            click_yn = True
                        except:
                            pass

                        if click_yn == False:
                            try :
                                driver.find_element_by_xpath('//*[@id="wen"]/div/div/div/div[1]/div[4]/p/a').click()
                                driver.switch_to_window(driver.window_handles[3])
                                click_yn = True
                            except:
                                pass
                        if click_yn == True:
                            driver.switch_to_window(driver.window_handles[2])
                            driver.close()
                            driver.switch_to_window(driver.window_handles[2])
                        contents = driver.page_source
                        link_url = re.search(r'<a target="_blank" class="l8" href="(.*?)">', contents, re.S).group(1)
                        try:
                            if 'http://' in link_url:
                                original_link_prefix = link_url.split('://')[0]
                                original_link_url = link_url.split('://')[1].split('/', 1)[0]
                            else:
                                pass

                            # 判断是http还是https
                            if original_link_prefix == 'http':
                                surffix += ['http://' + original_link_url]
                            elif original_link_prefix == 'https':
                                surffix += ['https://' + original_link_url]
                            else:
                                pass
                        except:
                            pass
                    except:
                        pass

                    if surffix == []:
                        try:
                            content = re.search(r'<div id="wen".*?>(.*?)<div class="contentLB".*?>', req, re.S).group(1)
                            # data = re.findall(r'(http.*?://.*?)[）|（|/|)|”|“|<|>|%|?|:]', content, re.S)
                            # for z in data:
                            #     if z not in surffix:
                            #         if 'qianlima' not in z:
                            #             surffix.append(z)

                            data1 = re.findall(r'(www.*?)[）|（|/|)|”|“|<|>|%|?|:]', content, re.S)
                            for y in data1:
                                if y not in surffix:
                                    if 'qianlima' not in y:
                                        surffix.append(y)
                        except:
                            pass
                    time.sleep(2)
                    driver.close()
                    time.sleep(2)
                    driver.switch_to_window(driver.window_handles[1])
                    # 拉到最底端
                    js = "var q=document.documentElement.scrollTop=10000"
                    driver.execute_script(js)
                    time.sleep(1)

                    if surffix != []:
                        List_end = []
                        try:
                            for s in surffix:
                                c = ''
                                for b in s:
                                    # 判断是不是错误例如__
                                    if u'\u4e00' <= b <= u'\u9fff' or b in '____':
                                        pass
                                    else:
                                        c += b
                                List_end.append(c)
                            for g in List_end:
                                self.r.sadd('source_link', g)
                        except:
                            pass

                #点击下一页
                driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[4]/div/a[8]').click()

            driver.quit()

    def run(self):
        # for page in range(3, 5):
        self.crawl_list()
        Insert_data().inset_data()

if __name__ == '__main__':
    qs = Qianlima_Spider()
    qs.run()
#