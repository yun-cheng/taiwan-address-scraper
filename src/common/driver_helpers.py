import base64
from typing import Any
from urllib.parse import urlencode

from requests.cookies import RequestsCookieJar
from selenium import webdriver


def start_driver(
    driver_path="",
    chrome_path="",
    headless=True,
) -> webdriver.Chrome | webdriver.Remote:
    options = webdriver.ChromeOptions()
    options.binary_location = chrome_path
    if headless:
        options.add_argument("--headless")
        options.add_argument("--session-timeout 60")

    if driver_path:
        driver = webdriver.Chrome(driver_path, options=options)
    else:
        driver = webdriver.Remote("http://selenium:4444/wd/hub", options=options)

    return driver


def get_cookies(driver: webdriver.Chrome | webdriver.Remote) -> RequestsCookieJar:
    """
    > 提取 driver 的 cookies，之後用在 requests
    * reference: https://www.itread01.com/content/1526830854.html
    """
    cookies = driver.get_cookies()
    jar = RequestsCookieJar()
    for cookie in cookies:
        jar.set(cookie["name"], cookie["value"])

    return jar


def request_from_driver(
    driver: webdriver.Chrome | webdriver.Remote,
    url: str,
    method="GET",
    headers: dict[str, str] = {},
    data: dict[str, str] | None = None,
    is_img=False,
) -> bytes | dict[str, Any]:
    """
    > inject js code，在 driver 傳送 request 並回傳資料
    """
    data_str = None
    if data:
        headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        data_str = urlencode(data)

    result = driver.execute_async_script(
        """
    const [url, method, headers, data, is_img] = arguments;
    const callback = arguments[arguments.length - 1]; // 用來回傳資料
    const toBase64 = function(buffer){for(var r,n=new Uint8Array(buffer),t=n.length,a=new Uint8Array(4*Math.ceil(t/3)),i=new Uint8Array(64),o=0,c=0;64>c;++c)i[c]="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".charCodeAt(c);for(c=0;t-t%3>c;c+=3,o+=4)r=n[c]<<16|n[c+1]<<8|n[c+2],a[o]=i[r>>18],a[o+1]=i[r>>12&63],a[o+2]=i[r>>6&63],a[o+3]=i[63&r];return t%3===1?(r=n[t-1],a[o]=i[r>>2],a[o+1]=i[r<<4&63],a[o+2]=61,a[o+3]=61):t%3===2&&(r=(n[t-2]<<8)+n[t-1],a[o]=i[r>>10],a[o+1]=i[r>>4&63],a[o+2]=i[r<<2&63],a[o+3]=61),new TextDecoder("ascii").decode(a)};
    (async function () {
      let response;
      try {
        response = await fetch(url, {
          method: method,
          headers: headers,
          body: data ? data : null,
        });
        let res;
        if (is_img) {
          res = await response.arrayBuffer();
          callback(toBase64(res));
        } else {
          res = await response.json();
          callback(res);
        }
      } catch (error) {
        callback(response.status);
      }
    })();
    """,
        url,
        method,
        headers,
        data_str,
        is_img,
    )

    if type(result) == int:
        raise Exception(f"Request failed with status {result}")

    if is_img:
        result = base64.b64decode(result)

    return result
