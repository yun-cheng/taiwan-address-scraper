import re


def lines_to_dict(file_path: str) -> dict[str, str]:
    """
    > 將 DevTools 複製的 headers/data 直接存成 txt 檔後，讀取成 dictionary
    """
    f = open(file_path, encoding="utf-8")
    lines = f.readlines()
    lines_dict: dict[str, str] = {}
    for line in lines:
        split_line = line.split(":")
        remain = "".join(line.split(":")[1:])
        lines_dict[split_line[0]] = re.sub("^\\s", "", remain.replace("\n", ""))

    return lines_dict
