import ast

from selenium import webdriver
from twocaptcha import TwoCaptcha

from src.common.captcha_helpers import decode_captcha
from src.common.driver_helpers import request_from_driver


def get_address_data(
    driver: webdriver.Chrome | webdriver.Remote, query_data: dict
) -> tuple[list[dict[str, str]], str]:
    """
    > 取得地址資料
    """
    url = "https://www.ris.gov.tw/info-doorplate/app/doorplate/inquiry/date"
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Referer": "https://www.ris.gov.tw/info-doorplate/app/doorplate/query",
        "X-Requested-With": "XMLHttpRequest",
    }

    result_dict = request_from_driver(
        driver, url, method="POST", headers=headers, data=query_data
    )
    assert isinstance(result_dict, dict)

    address_list = result_dict["rows"]
    error_msg = result_dict["errorMsg"].replace(":true,", ":True,")
    captcha_key = ast.literal_eval(error_msg)["captcha"]

    return address_list, captcha_key


def save_captcha_image(
    driver: webdriver.Chrome | webdriver.Remote,
    img_dir: str,
    captcha_key: str,
) -> None:
    """
    > 儲存驗證碼圖片檔
    """
    time = "1671019121123"
    url = f"https://www.ris.gov.tw/info-doorplate/captcha/image?CAPTCHA_KEY={captcha_key}&time={time}"
    # * 設定接受圖片格式，不加會失敗
    headers = {"Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8"}

    img_data = request_from_driver(driver, url, headers=headers, is_img=True)
    assert isinstance(img_data, bytes)

    img_path = f"{img_dir}/{captcha_key}.jpg"
    with open(img_path, "wb") as f:
        f.write(img_data)


def save_and_decode_captcha_image(
    driver: webdriver.Chrome | webdriver.Remote,
    solver: TwoCaptcha,
    img_dir: str,
    captcha_key: str,
) -> str:
    """
    > 更新下一次 query 的 captchaKey 與解答
    """
    save_captcha_image(driver, img_dir, captcha_key)
    img_path = f"{img_dir}/{captcha_key}.jpg"
    captcha_input = decode_captcha(solver, img_path, min_len=5, max_len=5, numeric=4)

    return captcha_input
