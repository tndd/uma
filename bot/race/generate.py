def gen_year_month() -> list[str]:
    ym_list = []
    for year in range(1990, 2025):
        for month in range(1, 13):
            month_str = str(month).zfill(2)
            ym_list.append(str(year) + month_str)
    return ym_list


def test_gen_year_month():
    ym_list = gen_year_month()
    assert ym_list[0] == "199001"
    assert ym_list[1] == "199002"
    assert ym_list[-1] == "202412"


if __name__ == "__main__":
    test_gen_year_month()
