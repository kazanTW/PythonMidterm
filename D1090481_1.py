if __name__ == '__main__':

    hotel = {'上雅居': {'score': 9.6, 'price': 3900},
             '冬山驛': {'score': 9.2, 'price': 3300},
             '家家陽光': {'score': 9.6, 'price': 3600},
             '大福謙代': {'score': 9.7, 'price': 4500}}

    print(f'分數高於9.5的住宿')
    print("上雅居", ", 分數:", hotel['上雅居']['score'], ", 價格:TWD ", hotel['上雅居']['price'])
    print("家家陽光", ", 分數:", hotel['家家陽光']['score'], ", 價格:TWD ", hotel['家家陽光']['price'])
    print("大福謙代", ", 分數:", hotel['大福謙代']['score'], ", 價格:TWD ", hotel['大福謙代']['price'])