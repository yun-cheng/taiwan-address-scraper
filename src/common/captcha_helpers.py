from twocaptcha import TwoCaptcha


def decode_captcha(solver: TwoCaptcha, img_path: str, **kwargs) -> str:
    """
    > 從圖片檔解開驗證碼
    * https://2captcha.com/2captcha-api#solving_normal_captcha
    * 成功率 368/440 ~= 83%
    * 成功率 368/425 ~= 86%
    """
    try:
        result = solver.normal(img_path, **kwargs)
    except:
        return "99999"
    return result["code"]
