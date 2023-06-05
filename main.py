from DrissionPage import ChromiumPage
from DrissionPage.configs.chromium_options import ChromiumOptions
from DrissionPage.easy_set import set_paths

chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'  # 你的chrome.exe路径，可选
set_paths(chrome_path=chrome_path)

co = ChromiumOptions().use_system_user_path(False)
page = ChromiumPage(co)
with open('api.txt', 'r') as file:
    urls = file.readlines()
for i, url in enumerate(urls):
    page.get(url)
    # 定位到页面上文字为留电的按钮上并点击
    isdisplay1 = page.wait.ele_display('.contact-item-text', timeout=5)
    if isdisplay1:
        ele = page.ele('.contact-item-text')
        if ele:
            ele.click()
        else:
            continue
        isdisplay2 = page.wait.ele_display('.leavetel-input ', timeout=5)
        if isdisplay2:
            page.ele('.leavetel-input ').input('12345678901')
            page.ele('.leavetel-callback').click()
        else:
            continue
    else:
        continue
