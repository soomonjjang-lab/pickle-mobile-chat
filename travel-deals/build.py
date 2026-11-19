#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds the three static language pages of the Travel Deals Hub:
    travel-deals/index.html      (Korean, default)
    travel-deals/en/index.html   (English)
    travel-deals/ja/index.html   (Japanese)

One source of truth for the 18 partner links (Travelpayouts, sub_id=nanahub).
Run:  python3 travel-deals/build.py
"""
import os
import html

BASE = "https://soomonjjang-lab.github.io/pickle-mobile-chat/travel-deals/"
ROOT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- links
URLS = {
    "aviasales": "https://tp.media/r?campaign_id=100&marker=808164&p=4114&sub_id=nanahub&trs=603335&u=https%3A%2F%2Faviasales.com",
    "klook":     "https://tp.media/r?campaign_id=137&marker=808164&p=4110&sub_id=nanahub&trs=603335&u=https%3A%2F%2Fklook.com",
    "kkday":     "https://tp.media/r?campaign_id=633&marker=808164&p=9074&sub_id=nanahub&trs=603335&u=https%3A%2F%2Fkkday.com",
    "tiqets":    "https://tp.media/r?campaign_id=89&marker=808164&p=2074&sub_id=nanahub&trs=603335&u=https%3A%2F%2Ftiqets.com",
    "gocity":    "https://tp.media/r?campaign_id=62&marker=808164&p=1942&sub_id=nanahub&trs=603335&u=https%3A%2F%2Fgocity.com",
    "airalo":    "https://tp.media/r?campaign_id=541&marker=808164&p=8310&sub_id=nanahub&trs=603335&u=https%3A%2F%2Fairalo.com",
    "yesim":     "https://tp.media/r?campaign_id=224&marker=808164&p=5998&sub_id=nanahub&trs=603335&u=https%3A%2F%2Fyesim.tech",
    "kiwitaxi":  "https://tp.media/r?campaign_id=1&marker=808164&p=647&sub_id=nanahub&trs=603335&u=https%3A%2F%2Fkiwitaxi.com",
    "gettransfer": "https://tp.media/r?campaign_id=147&marker=808164&p=4439&sub_id=nanahub&trs=603335&u=https%3A%2F%2Fgettransfer.com",
    "radicalstorage": "https://tp.media/r?campaign_id=209&marker=808164&p=5867&sub_id=nanahub&trs=603335&u=https%3A%2F%2Fradicalstorage.com",
    # 2026-11-19 newly activated Travelpayouts programs (short links, 302 verified)
    "kiwi":      "https://kiwi.tpx.gr/XdqVyHlW?sub_id=nanahub",
    "saily":     "https://saily.tpx.gr/Jgzg2FGA?sub_id=nanahub",
    "gigsky":    "https://gigsky.tpx.gr/oBferp8i?sub_id=nanahub",
    # 2026-11-19 second batch (tp.media direct 302 URLs, campaign_id/p from 똥구리)
    "welcomepickups": "https://tp.media/r?campaign_id=627&marker=808164&p=8919&sub_id=nanahub&trs=603335&u=https%3A%2F%2Fwelcomepickups.com",
    "wegotrip":  "https://tp.media/r?campaign_id=150&marker=808164&p=4487&sub_id=nanahub&trs=603335&u=https%3A%2F%2Fwegotrip.com",
    "qeeq":      "https://tp.media/r?campaign_id=172&marker=808164&p=4845&sub_id=nanahub&trs=603335&u=https%3A%2F%2Fqeeq.com",
    "autoeurope": "https://tp.media/r?campaign_id=143&marker=808164&p=4354&sub_id=nanahub&trs=603335&u=https%3A%2F%2Fautoeurope.eu",
    "localrent": "https://tp.media/r?campaign_id=87&marker=808164&p=2043&sub_id=nanahub&trs=603335&u=https%3A%2F%2Flocalrent.com%2Fen",
}

CATEGORIES = [
    {"key": "flights", "glyph": "✈️"},
    {"key": "esim", "glyph": "📶"},
    {"key": "transfer", "glyph": "🚐"},
    {"key": "carrental", "glyph": "🚗"},
    {"key": "tours", "glyph": "🎟️"},
    {"key": "luggage", "glyph": "🧳"},
]

# ---------------------------------------------------------------- services
SERVICES = [
    {
        "id": "aviasales", "cat": "flights", "name": "Aviasales",
        "ko": {
            "purpose": "항공사와 판매 대행사의 항공권 값을 한 화면에서 비교합니다.",
            "points": [
                "출발지·도착지·날짜만 넣으면 여러 판매처의 값을 나란히 보여 줍니다.",
                "날짜가 유연하면 한 달 단위로 값이 싼 날을 비교할 수 있습니다.",
                "가장 싼 표는 대개 조건이 가장 빡빡한 표입니다 — 경유가 길거나, 변경·환불이 안 됩니다.",
            ],
            "check": "결제 전에 발권 주체(항공사 직접인지 판매 대행사인지), 위탁 수하물 포함 여부, 변경·환불 규정을 확인하세요. 대행사 발권이면 운항이 흐트러졌을 때 연락할 곳도 그 대행사입니다.",
            "cta": "항공권 최저가 보기",
        },
        "en": {
            "purpose": "Compares airline and ticket-agency fares for the same route on one screen.",
            "points": [
                "Enter an origin, a destination and dates; fares from several sellers appear side by side.",
                "If your dates are flexible, the month view shows which days around the trip are cheaper.",
                "The cheapest fare is usually the least flexible one — long layovers, no changes, no refund.",
            ],
            "check": "Before paying, check who issues the ticket (the airline itself or an agency), whether checked bags are included, and the change and refund rules. With an agency-issued ticket, that agency is who you call when a flight is disrupted.",
            "cta": "Search flights",
        },
        "ja": {
            "purpose": "航空会社と販売代理店の運賃を1つの画面で比べます。",
            "points": [
                "出発地・目的地・日付を入れると、複数の販売店の価格が並びます。",
                "日程に余裕があるときは、1か月表示で前後の安い日を比べられます。",
                "いちばん安い運賃は、たいてい条件がいちばん厳しい運賃です。乗り継ぎが長く、変更・払い戻しができません。",
            ],
            "check": "支払う前に、発券するのが誰か(航空会社か販売代理店か)、受託手荷物の有無、変更・払い戻しの条件を確認してください。代理店発券なら、運航が乱れたときの連絡先もその代理店です。",
            "cta": "航空券を検索",
        },
    },
    {
        "id": "airalo", "cat": "esim", "name": "Airalo",
        "ko": {
            "purpose": "여행지에서 쓸 데이터 eSIM을 앱에서 사서 바로 설치합니다.",
            "points": [
                "국가별·지역별·글로벌 플랜이 있어 한 나라 여행과 여러 나라 여행 모두 맞출 수 있습니다.",
                "설치는 QR 코드나 앱에서 몇 분이면 끝납니다.",
                "플랜 대부분이 데이터 전용이라, 전화번호가 필요한 일은 따로 챙겨야 합니다.",
            ],
            "check": "휴대폰이 eSIM을 지원하고 통신사 잠금이 풀려 있어야 합니다. 플랜의 데이터 용량과 사용 기간, 핫스팟(테더링)이 되는지를 확인하세요.",
            "cta": "eSIM 플랜 보기",
        },
        "en": {
            "purpose": "Buys and installs a travel data eSIM from an app, before or after landing.",
            "points": [
                "Country, regional and global plans, so a single-country trip and a multi-country one both fit.",
                "Installation takes a few minutes, by QR code or inside the app.",
                "Most plans are data-only, so anything that needs a phone number has to be handled separately.",
            ],
            "check": "Your phone must support eSIM and be carrier-unlocked. Check the data amount, the validity period, and whether hotspot/tethering works on that plan.",
            "cta": "See eSIM plans",
        },
        "ja": {
            "purpose": "旅行先で使うデータeSIMをアプリで購入し、そのまま設定します。",
            "points": [
                "国別・地域別・グローバルのプランがあり、1か国の旅にも周遊にも合います。",
                "設定はQRコードかアプリから数分で終わります。",
                "プランの多くはデータ専用なので、電話番号が要る用事は別に用意します。",
            ],
            "check": "端末がeSIMに対応し、SIMロックが解除されている必要があります。データ容量・有効期間・テザリング可否を確認してください。",
            "cta": "eSIMプランを見る",
        },
    },
    {
        "id": "yesim", "cat": "esim", "name": "Yesim",
        "ko": {
            "purpose": "데이터와 통화를 함께 고를 수 있는 eSIM, 두 번째 선택지입니다.",
            "points": [
                "국가별·지역별 eSIM에 더해, 통화가 되는 플랜도 있습니다.",
                "장기 체류나 출장처럼 기간이 긴 여행에서 하루 비용을 비교하기 좋습니다.",
                "사고·설치·관리를 모두 앱 안에서 합니다.",
            ],
            "check": "구매 전에 지원 기기 목록과 잠금 해제 상태를 확인하세요. 같은 나라 플랜이라도 용량·기간·속도 제한 조건이 다릅니다.",
            "cta": "Yesim 플랜 보기",
        },
        "en": {
            "purpose": "A second eSIM option, with data and voice plans in the same app.",
            "points": [
                "Country and regional eSIMs, plus plans that include calls when you need a number.",
                "Worth comparing on long stays and business trips, where the cost per day matters more.",
                "Buying, installing and managing all happen in the app.",
            ],
            "check": "Check the supported device list and that your phone is unlocked before buying. Two plans for the same country can differ in data, duration and speed limits.",
            "cta": "See Yesim plans",
        },
        "ja": {
            "purpose": "データと通話を一緒に選べるeSIM、もう1つの選択肢です。",
            "points": [
                "国別・地域別のeSIMに加えて、通話が付いたプランもあります。",
                "長期滞在や出張など、日割りで比べたい旅に向いています。",
                "購入・設定・管理はすべてアプリ内で行います。",
            ],
            "check": "購入前に対応端末の一覧とSIMロック解除を確認してください。同じ国のプランでも容量・期間・速度制限の条件が違います。",
            "cta": "Yesimプランを見る",
        },
    },
    {
        "id": "kiwitaxi", "cat": "transfer", "name": "Kiwitaxi",
        "ko": {
            "purpose": "공항 도착 시각에 맞춰 기사가 기다리는 픽업을 미리 예약합니다.",
            "points": [
                "예약할 때 항공편 번호를 넣으면 도착 정보에 맞춰 픽업 시간을 잡습니다.",
                "요금이 예약 시점에 정해지고, 목적지까지 미터기로 올라가지 않습니다.",
                "인원과 짐 수에 맞춰 차량 등급을 고릅니다.",
            ],
            "check": "착륙 후 무료 대기 시간이 얼마인지, 기사가 입국장에서 이름판을 들고 마중하는지, 취소 가능 기한이 언제까지인지 확인하세요.",
            "cta": "공항 픽업 예약",
        },
        "en": {
            "purpose": "Pre-books an airport pickup with a driver waiting at your arrival time.",
            "points": [
                "You enter the flight number, and the pickup is timed to the arrival.",
                "The price is set when you book, rather than running on a meter to the door.",
                "Choose the vehicle class to match passengers and luggage.",
            ],
            "check": "Check the free waiting time after landing, whether the driver meets you inside with a name sign, and the cancellation deadline.",
            "cta": "Book a transfer",
        },
        "ja": {
            "purpose": "空港到着の時刻にドライバーが待つ送迎を事前に予約します。",
            "points": [
                "予約時にフライト番号を入れると、到着情報に合わせて迎えの時間を組みます。",
                "料金は予約時に決まり、目的地までメーターで上がることはありません。",
                "人数と荷物に合わせて車種を選びます。",
            ],
            "check": "着陸後の無料待機時間、ドライバーが到着ロビーで名前の札を持って待つか、キャンセル期限を確認してください。",
            "cta": "空港送迎を予約",
        },
    },
    {
        "id": "gettransfer", "cat": "transfer", "name": "GetTransfer",
        "ko": {
            "purpose": "여러 기사의 견적을 비교해 공항 픽업과 도시 간 이동을 예약합니다.",
            "points": [
                "경로와 시간을 올리면 기사들이 값을 제시하고, 그중에서 고릅니다.",
                "공항 픽업도 도시 간 장거리도 같은 방식으로 예약합니다.",
                "차량 사진과 기사 평가를 보고 결정할 수 있습니다.",
            ],
            "check": "제시된 요금에 통행료·주차비·야간 할증이 포함인지 확인하고, 포함 항목을 예약 채팅에 한 번 더 남겨 두세요.",
            "cta": "이동 견적 비교",
        },
        "en": {
            "purpose": "Compares driver quotes for airport pickups and city-to-city rides.",
            "points": [
                "Post the route and the time; drivers offer prices; you pick one.",
                "Airport pickups and longer intercity runs are booked the same way.",
                "Vehicle photos and driver ratings are shown before you choose.",
            ],
            "check": "Check whether tolls, parking and night surcharges sit inside the quoted price, and keep the inclusions in writing in the booking chat.",
            "cta": "Compare transfer quotes",
        },
        "ja": {
            "purpose": "複数のドライバーの見積もりを比べて、空港送迎や都市間移動を予約します。",
            "points": [
                "経路と時間を登録するとドライバーが料金を提示し、その中から選びます。",
                "空港送迎も都市間の長距離も同じ流れで予約できます。",
                "車両の写真とドライバーの評価を見て決められます。",
            ],
            "check": "提示額に通行料・駐車料・夜間割増が含まれるか確認し、含まれる内容を予約チャットに残しておいてください。",
            "cta": "送迎の見積もりを比較",
        },
    },
    {
        "id": "welcomepickups", "cat": "transfer", "name": "Welcome Pickups",
        "ko": {
            "purpose": "예약한 기사가 도착 게이트에서 이름 팻말을 들고 기다리는 공항 픽업 서비스입니다.",
            "points": [
                "예약할 때 정한 요금이 그대로 청구되고, 기사가 명패를 들고 나와 차까지 안내합니다.",
                "374개 도시에서 영어가 되는 기사를 직접 심사해 배정하고, 항공편 지연은 편명으로 확인합니다.",
                "공항 픽업 말고도 시내 이동, 기사와 함께 반나절 도는 관광 라이드도 같은 앱에서 예약합니다.",
            ],
            "check": "요금에 통행료·주차비가 포함인지, 무료 대기 시간이 몇 분인지, 취소 마감 시각을 확인하세요. 인원과 짐에 맞는 차종(세단·밴)을 고르고, 유아 카시트가 필요하면 예약할 때 요청해야 합니다.",
            "cta": "공항 픽업 예약",
        },
        "en": {
            "purpose": "An airport pickup where the driver you booked waits at arrivals with a name sign.",
            "points": [
                "The fare is fixed when you book; the driver meets you with a name board and walks you to the car.",
                "Handpicked, English-speaking drivers in 374 destinations, and your flight number is tracked so a delay does not cost you the ride.",
                "The same app books in-city rides and sightseeing rides with a driver for part of a day.",
            ],
            "check": "Check whether tolls and parking sit inside the fare, how long the free waiting time is, and the cancellation deadline. Pick the vehicle size for your group and bags, and ask for a child seat when booking if you need one.",
            "cta": "Book airport pickup",
        },
        "ja": {
            "purpose": "予約したドライバーが到着ゲートで名前のボードを持って待つ空港送迎です。",
            "points": [
                "予約時に決めた料金がそのまま請求され、ドライバーが名前のボードを持って車まで案内します。",
                "374都市で英語対応のドライバーを直接選考して手配し、フライトの遅延は便名で確認しています。",
                "市内の移動や、ドライバーと半日回る観光ライドも同じアプリで予約できます。",
            ],
            "check": "料金に通行料・駐車場代が含まれるか、無料の待ち時間が何分か、キャンセルの締め切りを確認してください。人数と荷物に合う車種(セダン・バン)を選び、チャイルドシートが必要なら予約時に依頼します。",
            "cta": "空港送迎を予約",
        },
    },
    {
        "id": "klook", "cat": "tours", "name": "Klook",
        "ko": {
            "purpose": "도시별 투어, 입장권, 교통 패스를 한 앱에서 예약합니다.",
            "points": [
                "아시아 주요 도시의 테마파크·전망대·투어 상품이 특히 많고, 다른 지역 도시도 다룹니다.",
                "예약 후 받은 모바일 바우처를 현장에서 보여 주는 방식이 많습니다.",
                "상품마다 이용일 지정 여부와 취소 마감이 다릅니다.",
            ],
            "check": "이용 날짜와 시간대를 먼저 확인하고, 바로 확정되는 상품인지 확인 후 확정인지, 취소 가능 기한이 언제까지인지 상품 페이지에서 보세요.",
            "cta": "투어·티켓 보기",
        },
        "en": {
            "purpose": "Books tours, attraction tickets and transport passes for a city in one app.",
            "points": [
                "Deepest in major Asian cities — theme parks, observation decks, day tours — and covers other regions too.",
                "Many bookings arrive as a mobile voucher you show at the gate.",
                "Each product sets its own date rules and cancellation deadline, so read the page.",
            ],
            "check": "Check whether your date and time slot are fixed, whether the booking is confirmed instantly or after review, and the cancellation deadline for that specific product.",
            "cta": "Browse tours & tickets",
        },
        "ja": {
            "purpose": "都市ごとのツアー、入場券、交通パスを1つのアプリで予約します。",
            "points": [
                "アジア主要都市のテーマパーク・展望台・ツアーが特に多く、他の地域の都市も扱います。",
                "予約後に届くモバイルバウチャーを現地で見せる形式が一般的です。",
                "商品ごとに日付指定の有無とキャンセル期限が異なります。",
            ],
            "check": "利用日と時間帯を先に確認し、即時確定か確認後の確定か、その商品のキャンセル期限を商品ページで確認してください。",
            "cta": "ツアー・チケットを見る",
        },
    },
    {
        "id": "kkday", "cat": "tours", "name": "KKday",
        "ko": {
            "purpose": "현지 투어·액티비티·공항 픽업을 함께 예약하는 아시아계 플랫폼입니다.",
            "points": [
                "아시아·오세아니아 도시의 소규모 투어와 교통 상품이 많습니다.",
                "가이드가 동행하는 투어와 자유 이용권을 함께 판매합니다.",
                "상품 페이지의 후기와 사진으로 당일 진행 방식을 가늠할 수 있습니다.",
            ],
            "check": "집결 장소와 시간이 상품마다 다릅니다. 최소 인원이 차지 않으면 취소되는 상품인지, 픽업이 포함인지 별도인지 확인하세요.",
            "cta": "KKday 상품 보기",
        },
        "en": {
            "purpose": "An Asia-based booking platform for local tours, activities and airport pickups.",
            "points": [
                "Lots of small-group tours and transport products across Asian and Pacific cities.",
                "Sells guided tours and self-guided passes in the same catalogue.",
                "Reviews and photos on each product page show how the day actually runs.",
            ],
            "check": "Meeting points and times differ by product. Check whether the tour needs a minimum number of guests to run, and whether pickup is included or extra.",
            "cta": "Browse KKday",
        },
        "ja": {
            "purpose": "現地ツアー・アクティビティ・空港送迎をまとめて予約できるアジア発のプラットフォームです。",
            "points": [
                "アジア・オセアニア各都市の少人数ツアーや交通商品が充実しています。",
                "ガイド付きツアーとフリーパスを同じカタログで扱っています。",
                "商品ページのレビューと写真で、当日の流れを確認できます。",
            ],
            "check": "集合場所と時間は商品ごとに異なります。最少催行人数があるか、送迎が含まれるか別料金かを確認してください。",
            "cta": "KKdayを見る",
        },
    },
    {
        "id": "tiqets", "cat": "tours", "name": "Tiqets",
        "ko": {
            "purpose": "박물관·미술관·전시 입장권을 날짜를 정해 예약합니다.",
            "points": [
                "유럽 주요 도시의 박물관과 미술관이 중심이고, 다른 지역도 다룹니다.",
                "예약 후 받은 QR 코드를 입구에서 보여 주고 들어가는 방식이 많습니다.",
                "명소에 따라 날짜만이 아니라 입장 시간대까지 정해야 합니다.",
            ],
            "check": "명소 공식 판매처가 더 싼 경우도 있으니 결제 전에 한 번 비교하세요. 바로 입장인지 시간대 예약인지, 취소 조건과 수수료도 확인하세요.",
            "cta": "입장권 보기",
        },
        "en": {
            "purpose": "Reserves museum, gallery and exhibition tickets for a chosen date.",
            "points": [
                "Centred on museums and galleries in major European cities, with more elsewhere.",
                "Most tickets arrive as a QR code you show at the entrance.",
                "Some venues require a time slot, not just a date.",
            ],
            "check": "The venue's own ticket is sometimes cheaper, so compare before paying. Check whether entry is immediate or time-slotted, and the cancellation terms on that ticket.",
            "cta": "See tickets",
        },
        "ja": {
            "purpose": "博物館・美術館・展覧会の入場券を日付を決めて予約します。",
            "points": [
                "ヨーロッパ主要都市の美術館・博物館が中心で、他の地域も扱っています。",
                "予約後に届くQRコードを入口で見せて入る形式が一般的です。",
                "施設によっては日付だけでなく入場時間帯の指定も必要です。",
            ],
            "check": "施設の公式券のほうが安い場合もあるので、支払う前に一度比べてください。即時入場か時間帯指定か、キャンセル条件と手数料も確認を。",
            "cta": "チケットを見る",
        },
    },
    {
        "id": "gocity", "cat": "tours", "name": "Go City",
        "ko": {
            "purpose": "여러 명소를 묶은 시티패스로 입장권을 한 번에 해결합니다.",
            "points": [
                "일수로 고르는 패스와 명소 개수로 고르는 패스, 두 가지가 있습니다.",
                "패스에 들어 있는 명소 목록이 도시마다 다릅니다.",
                "많이 다닐수록 개별 입장권보다 유리해지는 구조입니다.",
            ],
            "check": "가려는 명소가 그 도시 패스 목록에 있는지, 예약이 필요한 명소인지 먼저 확인하세요. 유효기간이 언제부터 세어지는지도 패스마다 다릅니다.",
            "cta": "시티패스 보기",
        },
        "en": {
            "purpose": "A multi-attraction city pass that covers several sights with one purchase.",
            "points": [
                "Two shapes: a pass counted in days, and a pass counted in attractions.",
                "The list of included sights differs by city.",
                "The more you visit, the better it does against buying tickets one by one.",
            ],
            "check": "Check that the sights you want are on that city's list, and whether any of them need a reservation. Passes start counting at first use, but the rule differs by pass.",
            "cta": "See city passes",
        },
        "ja": {
            "purpose": "複数の観光施設をまとめたシティパスで、入場券を一度に済ませます。",
            "points": [
                "日数で選ぶパスと、施設数で選ぶパスの2種類があります。",
                "対象施設の一覧は都市ごとに異なります。",
                "多く回るほど、個別購入より割安になる仕組みです。",
            ],
            "check": "行きたい施設がその都市のパスに入っているか、予約が必要な施設かを先に確認してください。有効期間がいつから数えられるかもパスによって違います。",
            "cta": "シティパスを見る",
        },
    },
    {
        "id": "wegotrip", "cat": "tours", "name": "WeGoTrip",
        "ko": {
            "purpose": "명소 입장권에 오디오 가이드를 붙여, 정해진 시간 없이 자기 속도로 도는 투어입니다.",
            "points": [
                "가이드를 따라다니는 대신 앱이나 링크로 들으며 움직여서, 시작과 일시정지, 재개를 원하는 대로 합니다.",
                "입장권이 포함된 상품과 오디오만 있는 상품이 섞여 있으니, 고른 상품의 포함 항목을 봐야 합니다.",
                "투어를 미리 내려받으면 현지 데이터 없이도 들을 수 있습니다.",
            ],
            "check": "오디오 언어와 입장권 포함 여부, 유효기간(날짜 지정 여부)을 확인하세요. 이어폰과 보조배터리를 챙기고, 박물관별 개장시간과 휴관일은 예약 전에 한 번 더 봅니다.",
            "cta": "오디오 투어 보기",
        },
        "en": {
            "purpose": "An entry ticket with an audio guide attached, walked at your own pace instead of on a fixed schedule.",
            "points": [
                "No guide to keep up with: you listen in the app or from a link, starting, pausing and resuming as you like.",
                "Some products include the admission ticket and some are the audio alone, so read what the specific tour includes.",
                "Download the tour before you go and it plays without local data.",
            ],
            "check": "Check the audio language, whether admission is included, and the validity (a fixed date or not). Bring earphones and a power bank, and re-check each museum's opening hours and closing day before booking.",
            "cta": "See audio tours",
        },
        "ja": {
            "purpose": "入場券に音声ガイドが付き、決まった時間ではなく自分のペースで回るツアーです。",
            "points": [
                "ガイドに付いていく代わりにアプリやリンクで聞きながら動くので、開始・一時停止・再開を自由にします。",
                "入場券込みの商品と音声だけの商品が混ざっているので、選んだ商品の含まれる内容を確認します。",
                "事前にダウンロードしておけば、現地のデータ通信なしでも聞けます。",
            ],
            "check": "音声の言語、入場券の有無、有効期限(日付指定かどうか)を確認してください。イヤホンとモバイルバッテリーを用意し、施設の開館時間と休館日は予約前にもう一度見ます。",
            "cta": "音声ツアーを見る",
        },
    },
    {
        "id": "qeeq", "cat": "carrental", "name": "QEEQ",
        "ko": {
            "purpose": "여러 렌터카 회사의 같은 기간 요금을 한 화면에서 비교해 예약하는 사이트입니다.",
            "points": [
                "공항 카운터와 시내 지점의 차를 함께 보여 주고, 보험 옵션까지 고른 뒤의 총액을 비교하게 합니다.",
                "국제 브랜드와 현지 업체가 섞여 있어, 같은 차종이라도 보증금·연식·반납 조건이 다릅니다.",
                "무료 취소 표시는 상품마다 다르니 결제 화면에 들어가기 전에 한 번 더 확인해야 합니다.",
            ],
            "check": "표시 요금이 보험(자기부담금 포함)까지인지, 주행거리 무제한인지, 연료 정책과 반납 시간을 확인하세요. 국제운전면허증과 보증금용 신용카드가 필요한지, 차가 건널 수 있는 국경도 미리 봅니다.",
            "cta": "렌터카 요금 비교",
        },
        "en": {
            "purpose": "A booking site that puts the same dates at many rental companies on one screen.",
            "points": [
                "Airport counters and city offices appear together, and the total after insurance options is what you compare.",
                "International brands and local operators sit side by side, so the deposit, the car's age and the return terms differ for the same class.",
                "A free-cancellation label varies by product, so read it again before the payment screen.",
            ],
            "check": "Check whether the shown rate includes insurance and the excess, whether mileage is unlimited, the fuel policy and the return time. Look up whether an international driving permit and a credit card for the deposit are needed, and which borders the car may cross.",
            "cta": "Compare car rental rates",
        },
        "ja": {
            "purpose": "同じ日程で複数のレンタカー会社の料金を1画面で比べて予約するサイトです。",
            "points": [
                "空港カウンターと市内営業所の車を一緒に表示し、保険オプションまで選んだ後の総額で比べます。",
                "国際ブランドと現地業者が混在しているので、同じ車種でもデポジット・年式・返却条件が違います。",
                "無料キャンセルの表示は商品ごとに違うため、支払い画面の前にもう一度確認します。",
            ],
            "check": "表示料金に保険(自己負担額を含む)が含まれるか、走行距離無制限か、燃料ポリシーと返却時間を確認してください。国際運転免許証とデポジット用クレジットカードの要否、越えられる国境も先に見ます。",
            "cta": "レンタカー料金を比較",
        },
    },
    {
        "id": "autoeurope", "cat": "carrental", "name": "Auto Europe",
        "ko": {
            "purpose": "1954년부터 유럽 렌터카를 중개해 온 예약 대행사로, 국제 브랜드와 현지 업체를 같은 조건으로 비교합니다.",
            "points": [
                "Avis·Budget·Europcar·Hertz 같은 국제 브랜드와 지역 업체를 같은 조건으로 놓고 값을 비교합니다.",
                "예약은 대행사에서 받고 차는 현지 지점에서 받는 구조라, 문제가 생겼을 때 연락할 곳이 둘로 나뉩니다.",
                "렌터카 말고도 캠핑카, 기사 포함 차량도 같은 창구에서 예약합니다.",
            ],
            "check": "바우처에 적힌 인수 지점이 공항 카운터인지 셔틀로 이동하는 외곽 지점인지, 영업시간은 몇 시까지인지 확인하세요. 겨울용 타이어나 스노체인, 통행료·비네트, 추가 운전자 등록비가 요금에 들어 있는지도 결제 전에 봅니다.",
            "cta": "Auto Europe 요금 보기",
        },
        "en": {
            "purpose": "A booking agent for European car hire since 1954, comparing major brands with local suppliers on the same terms.",
            "points": [
                "Avis, Budget, Europcar and Hertz sit next to regional companies on the same terms, so the price is what separates them.",
                "The booking is with the agent and the car is collected from the local office, so a problem has two places to call.",
                "Motorhomes and cars with a driver are booked through the same desk.",
            ],
            "check": "Check whether the pick-up on the voucher is an airport counter or an off-site office reached by shuttle, and how late it is open. Check whether winter tyres or chains, tolls and vignettes, and an extra-driver fee are inside the rate before you pay.",
            "cta": "See Auto Europe rates",
        },
        "ja": {
            "purpose": "1954年からヨーロッパのレンタカーを仲介してきた予約代理店で、主要ブランドと現地業者を同じ条件で比べます。",
            "points": [
                "Avis・Budget・Europcar・Hertzなどの国際ブランドと地域業者を同じ条件で並べ、価格を比べます。",
                "予約は代理店、車の受け取りは現地営業所なので、トラブル時の連絡先が二つに分かれます。",
                "レンタカー以外にキャンピングカーやドライバー付き車両も同じ窓口で予約できます。",
            ],
            "check": "バウチャーに書かれた受け取り場所が空港カウンターか、シャトルで向かう郊外営業所か、営業時間は何時までかを確認してください。冬用タイヤ・チェーン、通行料・ビネット、追加ドライバー料金が料金に含まれるかも支払い前に見ます。",
            "cta": "Auto Europeの料金を見る",
        },
    },
    {
        "id": "localrent", "cat": "carrental", "name": "Localrent",
        "ko": {
            "purpose": "현지 렌터카 업체의 차를 모아 중개하는 사이트로, 대형 브랜드가 적은 곳에서 선택지가 많습니다.",
            "points": [
                "국제 브랜드 대신 그 나라 업체의 차를 보여 줘서, 같은 기간에 더 싼 차가 자주 나옵니다.",
                "현지 업체는 공항 카운터 대신 차를 숙소나 공항으로 가져다 주는 방식이 많습니다.",
                "보증금이 낮은 대신 차량 연식과 보험 보장 범위가 업체마다 크게 다릅니다.",
            ],
            "check": "맡은 업체의 후기와 보증금 액수(현금인지 카드 블록인지), 자기부담금 한도, 주행거리 제한을 확인하세요. 인수 장소와 시간을 메시지로 확정하고, 차를 받을 때 상태를 사진과 영상으로 남겨 두면 반납 때 말이 줄어듭니다.",
            "cta": "Localrent 차량 보기",
        },
        "en": {
            "purpose": "A marketplace of local rental companies, with the most choice where the big brands are thin.",
            "points": [
                "Instead of an international brand you see the country's own operators, which often means a cheaper car for the same days.",
                "Many local operators have no airport counter; they bring the car to your hotel or the airport instead.",
                "The deposit is often low, but the car's age and what the insurance actually covers differ sharply between operators.",
            ],
            "check": "Read the reviews for that operator and check the deposit (cash or a card hold), the excess limit and any mileage cap. Confirm the pick-up place and time in a message, and photograph and film the car at handover so the return is not an argument.",
            "cta": "See Localrent cars",
        },
        "ja": {
            "purpose": "現地のレンタカー業者の車を集めて仲介するサイトで、大手ブランドが少ない場所ほど選択肢があります。",
            "points": [
                "国際ブランドの代わりにその国の業者の車が並ぶので、同じ日程でも安い車が出やすいです。",
                "現地業者は空港カウンターではなく、ホテルや空港まで車を持ってくる方式が多くあります。",
                "デポジットは低めな代わりに、車の年式と保険の補償範囲は業者ごとに大きく違います。",
            ],
            "check": "担当業者の口コミとデポジットの額(現金かカードの与信か)、自己負担の上限、走行距離の制限を確認してください。受け取り場所と時間はメッセージで確定し、受け取り時に車の状態を写真と動画で残すと返却時のトラブルが減ります。",
            "cta": "Localrentの車を見る",
        },
    },
    {
        "id": "radicalstorage", "cat": "luggage", "name": "Radical Storage",
        "ko": {
            "purpose": "가게와 호텔에 짐을 맡기는 보관소를 지도에서 찾아 예약합니다.",
            "points": [
                "역과 관광지 근처의 제휴 매장에서 시간·일 단위로 짐을 맡깁니다.",
                "체크아웃 후 비행기까지, 또는 체크인 전 몇 시간을 비울 때 씁니다.",
                "예약 내역을 매장에서 보여 주고 맡기고 찾습니다.",
            ],
            "check": "매장 영업시간과 맡길 수 있는 크기(캐리어·자전거 등)를 확인하세요. 보증 범위와 귀중품 규정은 그 매장의 약관을 따릅니다.",
            "cta": "짐 보관소 찾기",
        },
        "en": {
            "purpose": "Finds and books luggage storage in shops and hotels, on a map.",
            "points": [
                "Partner shops near stations and sights take bags by the hour or by the day.",
                "For the gap between checkout and a flight, or the hours before check-in.",
                "Book, then show the booking at the shop when you drop the bags.",
            ],
            "check": "Check the shop's opening hours and what it will take — suitcase size, bikes, awkward items. Insurance and the rules for valuables follow that partner shop's terms.",
            "cta": "Find luggage storage",
        },
        "ja": {
            "purpose": "店舗やホテルに荷物を預ける場所を地図から探して予約します。",
            "points": [
                "駅や観光地の近くの提携店で、時間単位・日単位で荷物を預けられます。",
                "チェックアウトからフライトまで、またはチェックイン前の数時間に使います。",
                "予約画面を店舗で見せて預け、同じ画面で受け取ります。",
            ],
            "check": "店舗の営業時間と、預けられるサイズ(スーツケース・自転車など)を確認してください。保証や貴重品の扱いは提携店の規約に従います。",
            "cta": "荷物預かりを探す",
        },
    },
    {
        "id": "kiwi", "cat": "flights", "name": "Kiwi.com",
        "ko": {
            "purpose": "여러 항공사의 표를 조합해 한 번에 예약하는 항공권 검색·판매 사이트입니다.",
            "points": [
                "서로 다른 항공사를 이어 붙인 '셀프 환승' 일정을 만들어, 직항이나 정식 연결편보다 싼 값을 찾습니다.",
                "저가 항공사를 섞을 수 있어 유럽 안 단거리 여행에서 값이 크게 낮아지는 경우가 있습니다.",
                "연결편 보호는 따로 사는 상품이라, 그냥 예약하면 환승이 어긋났을 때의 책임이 항공사가 아니라 본인에게 있습니다.",
            ],
            "check": "환승이 셀프 환승인지, 수하물을 다시 찾아 부쳐야 하는지 확인하세요. 환승 시간이 짧으면 위탁 수하물이 아예 안 팔리기도 하고, 앞 편이 지연되면 다음 편은 본인 부담입니다. 연결 보호(Connection Protection)는 예약할 때 함께 사야 합니다.",
            "cta": "항공권 조합 검색",
        },
        "en": {
            "purpose": "Searches and sells itineraries that stitch several airlines into one trip.",
            "points": [
                "Builds 'self-transfer' itineraries out of separate airlines, which often costs less than a direct flight or an official connection.",
                "Mixing low-cost carriers in makes short-haul trips, especially within Europe, noticeably cheaper.",
                "Connection protection is an add-on: without it, a missed connection is yours to solve, not the airline's.",
            ],
            "check": "Check whether the connection is a self-transfer and whether you have to collect and re-check your bags. On tight connections checked bags may not be offered at all, and if an earlier flight is late the next leg is your cost. Add connection protection at booking if you want cover.",
            "cta": "Search combined flights",
        },
        "ja": {
            "purpose": "複数の航空会社の航空券を組み合わせて一度に予約する検索・販売サイトです。",
            "points": [
                "別々の航空会社をつなぐ「セルフ乗り継ぎ」の旅程を組み、直行便や正規の乗り継ぎより安い運賃を探します。",
                "LCCを混ぜられるため、欧州内の短距離では安くなる場合があります。",
                "乗り継ぎ保護は別売りの商品で、付けずに予約すると乗り継ぎが崩れたときの責任は航空会社ではなく利用者にあります。",
            ],
            "check": "セルフ乗り継ぎかどうか、荷物を一度受け取って積み直す必要があるかを確認してください。乗り継ぎ時間が短いと受託手荷物自体が買えないことがあり、前の便が遅れると次の便は自己負担です。乗り継ぎ保護は予約時に一緒に購入する必要があります。",
            "cta": "組み合わせ航空券を検索",
        },
    },
    {
        "id": "saily", "cat": "esim", "name": "Saily",
        "ko": {
            "purpose": "NordVPN을 만든 Nord Security의 여행용 eSIM으로, 앱에서 데이터 요금제를 사서 설치합니다.",
            "points": [
                "200개 넘는 국가·지역에 단일 국가·지역·글로벌 요금제가 있습니다.",
                "앱에서 바로 설치하고, 현지에 도착해 요금제를 켠 때부터 기간이 시작됩니다.",
                "통화가 필요하면 미국(+1) 번호를 월 추가 요금으로 붙일 수 있습니다.",
            ],
            "check": "기기가 eSIM을 지원하고 통신사 잠금이 풀려 있어야 합니다. 요금제마다 데이터 양과 기간이 다릅니다. 설치는 출발 전에 해 두어도 되지만, 켜기 전까지는 기간이 흐르지 않으니 현지 도착 후에 켜세요.",
            "cta": "Saily 요금제 보기",
        },
        "en": {
            "purpose": "A travel eSIM from Nord Security, the company behind NordVPN; you buy and install the plan in the app.",
            "points": [
                "Country, regional and global plans across 200+ destinations.",
                "Install from the app, then switch the plan on after landing — the validity starts when you activate it.",
                "If you need a number for calls, a US (+1) line is an optional monthly add-on.",
            ],
            "check": "Your phone must support eSIM and be carrier-unlocked. Data amount and validity differ per plan; installing early is fine, because the clock starts only when you turn it on at your destination.",
            "cta": "See Saily plans",
        },
        "ja": {
            "purpose": "NordVPNを作ったNord Securityの旅行用eSIM。アプリでデータプランを購入して設定します。",
            "points": [
                "200以上の国・地域で、単一国・地域・グローバルのプランがあります。",
                "アプリからそのまま設定でき、現地でプランをオンにした時点から有効期間が始まります。",
                "通話が必要なら米国(+1)番号を月額の追加オプションで付けられます。",
            ],
            "check": "端末がeSIMに対応し、SIMロックが解除されている必要があります。プランごとにデータ量と期間が異なります。設定は出発前に済ませても、目的地でオンにするまで期間は進みません。",
            "cta": "Sailyのプランを見る",
        },
    },
    {
        "id": "gigsky", "cat": "esim", "name": "GigSky",
        "ko": {
            "purpose": "땅 위는 물론 배 위·비행기 안까지 잡는 여행용 eSIM입니다.",
            "points": [
                "국가·지역 플랜 외에 크루즈 선박, 항공기, 해상 근무용 플랜을 따로 팝니다.",
                "크루즈 플랜은 배가 육지에서 약 22km 떨어져 선내 통신망에 붙을 때부터 작동합니다.",
                "기내 플랜은 지원 항공사에서 고도 2만 피트 위로 올라가면 켜집니다.",
            ],
            "check": "크루즈·기내 플랜은 모든 배와 항공사에서 되지 않으니 지원 목록을 먼저 확인하세요. 배 안에서는 선내 와이파이를 꺼야 eSIM 데이터가 쓰입니다. 기기가 eSIM을 지원하고 잠금이 풀려 있어야 합니다.",
            "cta": "GigSky 요금제 보기",
        },
        "en": {
            "purpose": "A travel eSIM that also covers cruise ships and in-flight data, not only land networks.",
            "points": [
                "Alongside country and regional plans, it sells separate cruise, inflight and offshore plans.",
                "A cruise plan starts once the ship is about 14 miles (22 km) offshore and connects to the maritime network.",
                "An inflight plan switches on above 20,000 feet on participating airlines.",
            ],
            "check": "Cruise and inflight plans work only on supported ships and airlines, so check those lists first. At sea, turn the ship's Wi-Fi off or the eSIM data is not used. The phone must support eSIM and be carrier-unlocked.",
            "cta": "See GigSky plans",
        },
        "ja": {
            "purpose": "陸上だけでなく船内・機内でも使える旅行用eSIMです。",
            "points": [
                "国・地域プランに加えて、クルーズ船・機内・洋上向けのプランを別に販売しています。",
                "クルーズプランは船が陸から約22km離れ、船内通信網につながった時点から作動します。",
                "機内プランは対応航空会社で高度2万フィートを超えるとオンになります。",
            ],
            "check": "クルーズ・機内プランはすべての船と航空会社で使えるわけではないので、対応リストを先に確認してください。船内では船のWi-Fiを切らないとeSIMのデータは使われません。端末がeSIMに対応し、SIMロックが解除されている必要があります。",
            "cta": "GigSkyのプランを見る",
        },
    },
]

# ---------------------------------------------------------------- copy
COPY = {
    "ko": {
        "html_lang": "ko",
        "og_locale": "ko_KR",
        "title": "여행딜 허브 — 항공권·eSIM·공항 픽업·렌터카·투어 패스·짐 보관 18곳",
        "desc": "여행 준비에 실제로 여는 서비스 18곳을 한 페이지에. Aviasales·Kiwi.com 항공권 검색, Airalo·Yesim·Saily·GigSky eSIM, Kiwitaxi·GetTransfer·Welcome Pickups 공항 픽업, QEEQ·Auto Europe·Localrent 렌터카, Klook·KKday·Tiqets·Go City·WeGoTrip 투어·패스, Radical Storage 짐 보관. 가격 대신 결제 전에 확인할 것을 적었습니다.",
        "skip": "본문으로 건너뛰기",
        "disc": "이 페이지의 링크는 제휴 링크입니다. 링크를 통해 예약이 이루어지면 파트너사에서 수수료를 받을 수 있으며, 결제 금액은 달라지지 않습니다.",
        "kicker": "TRAVEL DEALS · 2026",
        "h1": "항공권부터 eSIM, 공항 픽업, 렌터카까지 — 여행 준비에 쓰는 링크 18개",
        "lede": "여행을 준비할 때 실제로 여는 사이트를 한 페이지에 모았습니다. 항공권 검색, eSIM, 공항 이동, 투어와 패스, 짐 보관. 각 서비스가 무엇에 맞는지, 결제 전에 무엇을 확인해야 하는지만 적었습니다. 가격은 적지 않습니다 — 검색하는 순간의 값이 정답이기 때문입니다.",
        "meta_updated": "2026년 11월 19일 갱신",
        "meta_count": "파트너 18곳",
        "meta_cats": "6개 카테고리",
        "lang_label": "언어",
        "nav_label": "카테고리",
        "cats": {
            "flights": {"name": "항공권", "intro": "가장 먼저 정하는 건 날짜와 항공권입니다. 검색은 무료이고, 결제는 항공사나 판매처 사이트에서 이루어집니다."},
            "esim": {"name": "eSIM · 데이터", "intro": "도착해서 유심을 사러 줄 서는 대신, 출발 전에 설치해 두세요. 휴대폰이 eSIM을 지원하고 잠금이 풀려 있어야 합니다."},
            "transfer": {"name": "공항 픽업 · 이동", "intro": "밤에 도착하거나 짐이 많을 때, 미리 예약된 기사만큼 편한 이동은 없습니다."},
            "carrental": {"name": "렌터카", "intro": "공항에서 차를 받아 직접 몰고 다니는 여행. 예약은 대개 무료로 취소되지만, 보증금은 픽업할 때 카드로 잡히는 경우가 많습니다."},            "tours": {"name": "투어 · 패스 · 입장권", "intro": "입장권, 투어, 시티패스를 한자리에서. 인기 명소는 당일 현장에 표가 없는 경우가 있어 미리 예약하는 편이 안전합니다."},
            "luggage": {"name": "짐 보관", "intro": "마지막 날, 체크아웃과 비행기 사이의 빈 시간을 짐 없이 보냅니다."},
        },
        "check_label": "확인",
        "order_title": "여행 준비 순서",
        "order_intro": "위에서 아래로 가면 준비가 끝납니다. 각 단계는 해당 카드로 이어집니다.",
        "order": [
            ("날짜와 항공권", "하루이틀만 날짜를 옮겨도 값이 크게 달라지는 경우가 많습니다. 한 달 보기로 주변 날짜를 먼저 비교해 보세요.", "#flights"),
            ("eSIM", "출발 하루이틀 전에 설치하고, 도착하면 로밍 대신 eSIM을 켭니다.", "#esim"),
            ("공항 픽업", "야간 도착이거나 숙소까지 길이 복잡하면 미리 예약합니다.", "#transfer"),
            ("렌터카", "차를 빌릴 거라면 픽업·반납 시간을 먼저 정하고, 보증금이 잡힐 카드를 준비합니다.", "#carrental"),
            ("투어와 패스", "가고 싶은 곳이 세 곳 이상이면 시티패스와 개별 입장권을 견줘 보세요.", "#tours"),
            ("짐 보관", "마지막 날 비행기가 늦으면 마지막 코스 근처에서 보관소를 잡아 둡니다.", "#luggage"),
        ],
        "notes": [
            ("가격을 적지 않은 이유", "항공권과 투어 요금은 매일 바뀝니다. 페이지에 적어 둔 숫자는 다음 날 틀린 정보가 됩니다. 링크를 눌러 그 순간의 가격을 보세요."),
            ("링크가 여는 곳", "모든 링크는 해당 서비스의 사이트로 열립니다. 이 페이지는 예약을 대신하지 않고, 결제·취소·환불은 각 서비스에서 이루어집니다."),
            ("어떻게 골랐나", "2026년 11월 기준, 여행 준비에서 실제로 쓰는 서비스 18곳을 여섯 카테고리로 정리했습니다. 카드에 적은 것은 그 서비스가 하는 일과, 결제 전에 확인할 항목입니다."),
        ],
        "footer": "© 2026 Travel Deals · 정적 페이지입니다. 이 페이지 자체에는 계정도 추적 스크립트도 없습니다. 서비스 이름과 설명은 2026년 11월 각 사 공개 페이지를 참고해 정리했고, 각 사의 조건과 요금은 바뀔 수 있습니다.",
    },
    "en": {
        "html_lang": "en",
        "og_locale": "en_US",
        "title": "Travel Deals Hub — flights, eSIM, airport transfers, car rental, city passes & luggage storage",
        "desc": "Eighteen services worth opening before a trip, on one page: Aviasales and Kiwi.com flight search, Airalo, Yesim, Saily and GigSky eSIMs, Kiwitaxi, GetTransfer and Welcome Pickups airport pickups, QEEQ, Auto Europe and Localrent car hire, Klook, KKday, Tiqets, Go City and WeGoTrip tours and passes, Radical Storage luggage storage.",
        "skip": "Skip to the list",
        "disc": "Links on this page are affiliate links. If you book through one, we may earn a commission from the partner; the price you pay does not change.",
        "kicker": "TRAVEL DEALS · 2026",
        "h1": "Flights, eSIM, airport pickups, car rental — eighteen links that do the work before a trip",
        "lede": "The sites we actually open when planning a trip, in one page: flight search, travel eSIM data, airport transfers, tours and city passes, luggage storage. For each one, what it is for and what to check before you pay. No prices — the number that matters is the one you see when you search.",
        "meta_updated": "Updated 19 November 2026",
        "meta_count": "18 partners",
        "meta_cats": "6 categories",
        "lang_label": "Language",
        "nav_label": "Categories",
        "cats": {
            "flights": {"name": "Flights", "intro": "Dates and flights come first. Searching is free; the payment happens on the airline's or the seller's own site."},
            "esim": {"name": "eSIM · Data", "intro": "Install before you fly, so you are not queueing for a SIM after landing. Your phone needs eSIM support and no carrier lock."},
            "transfer": {"name": "Airport transfer", "intro": "For a late arrival or too many bags, a driver already booked is the least tiring way in."},
            "carrental": {"name": "Car rental", "intro": "For the trips where you take the car at the airport and drive yourself. Bookings are usually free to cancel; the deposit is often held on a card at the counter."},            "tours": {"name": "Tours · Passes · Tickets", "intro": "Tickets, tours and city passes in one place. Popular sights run out at the gate, so booking ahead is the safer plan."},
            "luggage": {"name": "Luggage storage", "intro": "On the last day, the hours between checkout and the flight go better without the bags."},
        },
        "check_label": "Check",
        "order_title": "The order to book in",
        "order_intro": "Top to bottom is the whole preparation. Each step jumps to its card.",
        "order": [
            ("Dates and flights", "Moving a date by a day or two often changes the fare noticeably — compare the days either side first.", "#flights"),
            ("eSIM", "Install a day or two before you fly, and switch it on at landing instead of roaming.", "#esim"),
            ("Airport transfer", "Book ahead for a late arrival, or when the route to your stay is complicated.", "#transfer"),
            ("Car rental", "If you are hiring a car, fix the pick-up and return times first, and bring the card the deposit will be held on.", "#carrental"),
            ("Tours and passes", "Three or more sights? Put a city pass against single tickets before you buy.", "#tours"),
            ("Luggage", "On a late flight, book storage near your last stop before the airport.", "#luggage"),
        ],
        "notes": [
            ("Why there are no prices", "Flight and tour prices move daily, and a number printed on a page is wrong by tomorrow. Press the link and see the price at that moment."),
            ("Where each link goes", "Every link opens the service's own site. This page does not book anything; payment, cancellation and refunds happen with the service."),
            ("How the list was chosen", "Eighteen services actually used to plan a trip, sorted into six categories, as of November 2026. Each card says what the service does and what to check before paying."),
        ],
        "footer": "© 2026 Travel Deals · A static page. No accounts and no tracking scripts on this page itself. Service names and descriptions follow each company's public pages in November 2026; their terms and prices can change.",
    },
    "ja": {
        "html_lang": "ja",
        "og_locale": "ja_JP",
        "title": "旅行ディールハブ — 航空券・eSIM・空港送迎・レンタカー・観光パス・荷物預かりの18サイト",
        "desc": "旅の準備で実際に開く18のサービスを1ページに。Aviasales・Kiwi.comの航空券検索、Airalo・Yesim・Saily・GigSkyのeSIM、Kiwitaxi・GetTransfer・Welcome Pickupsの空港送迎、QEEQ・Auto Europe・Localrentのレンタカー、Klook・KKday・Tiqets・Go City・WeGoTripのツアーとパス、Radical Storageの荷物預かり。価格の代わりに、支払う前に確認することを書いています。",
        "skip": "一覧へ進む",
        "disc": "このページのリンクはアフィリエイトリンクです。リンク経由で予約が成立すると提携先から報酬を受け取ることがありますが、お支払い金額は変わりません。",
        "kicker": "TRAVEL DEALS · 2026",
        "h1": "航空券からeSIM、空港送迎、レンタカーまで — 旅の準備で開く18のリンク",
        "lede": "旅の準備で実際に開くサイトを1ページにまとめました。航空券検索、eSIM、空港送迎、ツアーとパス、荷物預かり。それぞれ何に向いているか、支払う前に何を確認するかだけを書いています。価格は載せていません — 検索したその瞬間の金額が正しいからです。",
        "meta_updated": "2026年11月19日更新",
        "meta_count": "提携先18社",
        "meta_cats": "6カテゴリ",
        "lang_label": "言語",
        "nav_label": "カテゴリ",
        "cats": {
            "flights": {"name": "航空券", "intro": "最初に決めるのは日程と航空券です。検索は無料で、支払いは航空会社または販売店のサイトで行います。"},
            "esim": {"name": "eSIM・データ", "intro": "到着後にSIMを買う列に並ばずに済むよう、出発前に設定します。端末がeSIMに対応し、SIMロックが解除されている必要があります。"},
            "transfer": {"name": "空港送迎", "intro": "夜の到着や荷物が多い旅では、予約済みのドライバーが一番楽な移動手段です。"},
            "carrental": {"name": "レンタカー", "intro": "空港で車を受け取って自分で運転する旅。予約は多くが無料キャンセル可能で、デポジットは受け取り時にカードで押さえられるのが普通です。"},            "tours": {"name": "ツアー・パス・入場券", "intro": "入場券、ツアー、シティパスをまとめて。人気の施設は当日券がないこともあるので、事前予約が安全です。"},
            "luggage": {"name": "荷物預かり", "intro": "最終日、チェックアウトからフライトまでの数時間を手ぶらで過ごします。"},
        },
        "check_label": "確認",
        "order_title": "予約する順番",
        "order_intro": "上から順に進めれば準備は終わります。各項目はカードに移動します。",
        "order": [
            ("日程と航空券", "1〜2日ずらすだけで運賃が大きく変わることもあります。前後の日を先に比べてみてください。", "#flights"),
            ("eSIM", "出発の1〜2日前に設定し、到着したらローミングの代わりにオンにします。", "#esim"),
            ("空港送迎", "夜の到着や、宿までの道のりが複雑なときは事前予約を。", "#transfer"),
            ("レンタカー", "車を借りるなら、受け取り・返却の時間を先に決め、デポジットが押さえられるカードを用意します。", "#carrental"),
            ("ツアーとパス", "行きたい場所が3か所以上なら、シティパスと個別券を比べてから買います。", "#tours"),
            ("荷物預かり", "フライトが遅い日は、最後の立ち寄り先の近くで預け先を押さえます。", "#luggage"),
        ],
        "notes": [
            ("価格を載せない理由", "航空券やツアーの料金は毎日動きます。ページに書いた数字は翌日には間違いになります。リンクを開いて、その時点の金額を見てください。"),
            ("リンクの行き先", "すべてのリンクは各サービスのサイトへ直接開きます。このページは予約を行わず、支払い・キャンセル・返金は各サービスで行われます。"),
            ("選び方", "2026年11月時点で、旅の準備に実際に使う18のサービスを6つのカテゴリに整理しました。カードに書いたのは、そのサービスが何をするかと、支払う前に確認する項目です。"),
        ],
        "footer": "© 2026 Travel Deals · 静的ページです。このページ自体にアカウントも計測スクリプトもありません。サービス名と説明は2026年11月時点の各社公開ページに基づき、各社の条件と料金は変わりえます。",
    },
}

CSS = """
  *,*::before,*::after{box-sizing:border-box}
  :root{
    --bg:#f2f6f7; --card:#ffffff; --ink:#0f2730; --soft:#33505a; --muted:#5f7a83;
    --line:#dce6e8; --accent:#0d6472; --accent-ink:#ffffff; --hero1:#0d3641; --hero2:#124d5a;
    --radius:16px; --maxw:940px;
    --sans:system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue","Apple SD Gothic Neo","Malgun Gothic","Hiragino Sans","Noto Sans JP","Noto Sans KR",sans-serif;
    color-scheme:light;
  }
  html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
  body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);font-size:16px;line-height:1.62;
       -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
  :focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:4px}
  .skip{position:absolute;left:12px;top:-64px;background:var(--ink);color:#fff;padding:10px 16px;
        border-radius:8px;z-index:60;text-decoration:none;font-size:14px}
  .skip:focus{top:12px}
  .wrap{max-width:var(--maxw);margin:0 auto;padding:0 16px}

  .disc{background:#e6eef0;border-bottom:1px solid var(--line);color:var(--soft);
        font-size:12px;line-height:1.5;text-align:center;padding:9px 16px}
  .disc strong{color:var(--ink);font-weight:600}

  .hero{background:linear-gradient(160deg,var(--hero1) 0%,var(--hero2) 100%);color:#eef6f7;
        padding:clamp(26px,6vw,54px) 0 clamp(22px,4vw,34px)}
  .hero .wrap{max-width:var(--maxw)}
  .kicker{margin:0 0 12px;font-size:11px;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:#8fd3da}
  .hero h1{margin:0 0 14px;font-size:clamp(25px,6.4vw,40px);line-height:1.18;letter-spacing:-.02em;
           font-weight:650;max-width:30ch;text-wrap:balance;color:#fff;overflow-wrap:break-word}
  html[lang="ko"] body{word-break:keep-all}
  html[lang="ko"] .hero h1{max-width:26ch}
  html[lang="ja"] .hero h1,html[lang="ja"] .sec-head h2,html[lang="ja"] .card h3{word-break:auto-phrase}
  .lede{margin:0;max-width:60ch;font-size:clamp(14.5px,3.3vw,16.5px);line-height:1.7;color:#d3e6e9}
  .hero-meta{display:flex;flex-wrap:wrap;gap:6px 0;margin:18px 0 0;padding:0;list-style:none;
             font-size:11.5px;letter-spacing:.06em;color:#9ec6cc;text-transform:uppercase}
  .hero-meta li+li::before{content:"·";margin:0 9px;color:#5d8b93}

  .langs{display:flex;flex-wrap:wrap;gap:8px;margin:20px 0 0;padding:0;list-style:none}
  .langs a{display:inline-block;padding:7px 14px;border:1px solid rgba(255,255,255,.3);border-radius:999px;
           color:#dceff2;text-decoration:none;font-size:13px;line-height:1.3;min-height:34px}
  .langs a:hover{border-color:rgba(255,255,255,.6)}
  .langs a[aria-current="page"]{background:#eef6f7;color:var(--hero1);border-color:#eef6f7;font-weight:600}

  .cats{position:sticky;top:0;z-index:30;background:rgba(242,246,247,.95);
        -webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);
        border-bottom:1px solid var(--line)}
  .cats__inner{max-width:var(--maxw);margin:0 auto;display:flex;gap:7px;overflow-x:auto;
               padding:10px 14px;scrollbar-width:none;-webkit-overflow-scrolling:touch}
  .cats__inner::-webkit-scrollbar{display:none}
  .cats a{flex:0 0 auto;display:inline-flex;align-items:center;gap:6px;padding:8px 12px;
          border:1px solid var(--line);border-radius:999px;background:var(--card);color:var(--soft);
          text-decoration:none;font-size:13px;white-space:nowrap}
  .cats a:hover{border-color:#b9ccd0;color:var(--ink)}
  .cats .n{font-size:11px;color:var(--muted);font-variant-numeric:tabular-nums}

  main{max-width:var(--maxw);margin:0 auto;padding:8px 16px 0}
  section.cat{padding-top:26px;scroll-margin-top:64px}
  .sec-head{margin:0 0 14px}
  .sec-head h2{margin:0 0 6px;font-size:19px;line-height:1.3;letter-spacing:-.01em;font-weight:650;
               display:flex;align-items:center;gap:9px}
  .sec-head h2 .glyph{font-size:17px;line-height:1}
  .sec-head p{margin:0;color:var(--muted);font-size:13.5px;line-height:1.6;max-width:62ch}

  .cards{list-style:none;margin:0;padding:0;display:grid;gap:12px;grid-template-columns:1fr}
  @media (min-width:660px){.cards{grid-template-columns:1fr 1fr;gap:14px}}
  @media (min-width:660px){section.cat .cards:has(>li:only-child){grid-template-columns:1fr}}

  .card{display:flex;flex-direction:column;height:100%;background:var(--card);border:1px solid var(--line);
        border-radius:var(--radius);padding:16px 16px 18px}
  @media (hover:hover){.card:hover{border-color:#c2d4d8}}
  .card h3{margin:0 0 4px;font-size:18px;line-height:1.3;font-weight:650;letter-spacing:-.01em}
  .card__purpose{margin:0 0 10px;color:var(--soft);font-size:14px;line-height:1.55}
  .card ul{margin:0;padding:0;list-style:none;display:grid;gap:7px;font-size:13.5px;line-height:1.55;color:var(--soft)}
  .card ul li{display:grid;grid-template-columns:11px 1fr;gap:6px}
  .card ul li::before{content:"";width:4px;height:4px;margin-top:.68em;border-radius:50%;background:var(--accent);opacity:.6}
  .card__check{margin:12px 0 14px;padding:9px 11px;background:#f3f8f9;border-left:2px solid var(--accent);
               border-radius:0 8px 8px 0;font-size:12.5px;line-height:1.55;color:var(--soft)}
  .card__check b{display:inline-block;margin-right:5px;font-size:11px;letter-spacing:.08em;
                 text-transform:uppercase;color:var(--accent)}
  .btn{margin-top:14px;display:block;text-align:center;text-decoration:none;
       background:var(--accent);color:var(--accent-ink);border-radius:11px;
       font-size:14.5px;font-weight:600;min-height:46px;line-height:46px;padding:0 14px;letter-spacing:.005em}
  .btn:hover{background:#0a5160}
  .btn .arrow{margin-left:6px;opacity:.8}
  .card .btn{margin-top:auto}

  .order{margin:34px 0 0;padding:24px 0 4px;border-top:1px solid var(--line)}
  .order h2{margin:0 0 4px;font-size:17px;font-weight:650;letter-spacing:-.005em}
  .order p.intro{margin:0 0 14px;color:var(--muted);font-size:13px}
  .order ol{list-style:none;margin:0;padding:0;display:grid;gap:10px;counter-reset:step}
  @media (min-width:760px){.order ol{grid-template-columns:1fr 1fr}}
  .order li{counter-increment:step;display:grid;grid-template-columns:26px 1fr;gap:9px;
            background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 14px}
  .order li::before{content:counter(step);grid-row:1/3;width:22px;height:22px;border-radius:50%;
                    background:var(--accent);color:#fff;font-size:12px;font-weight:600;
                    display:grid;place-items:center;margin-top:2px}
  .order a{font-size:14px;font-weight:600;color:var(--ink);text-decoration:none;border-bottom:1px solid #b9d3d7}
  .order a:hover{color:var(--accent)}
  .order span{grid-column:2;font-size:13px;color:var(--muted);line-height:1.55}

  .notes{margin:32px 0 0;padding:24px 0 0;border-top:1px solid var(--line);
         display:grid;gap:18px}
  @media (min-width:760px){.notes{grid-template-columns:repeat(3,1fr);gap:24px}}
  .notes h2{margin:0 0 6px;font-size:14px;font-weight:650}
  .notes p{margin:0;font-size:12.5px;line-height:1.65;color:var(--muted)}

  footer{margin-top:34px;background:#e7eff1;border-top:1px solid var(--line)}
  footer .wrap{padding:22px 16px 34px}
  footer strong{display:block;font-size:12.5px;margin-bottom:6px;color:var(--soft)}
  footer p{margin:0;font-size:11.5px;line-height:1.65;color:var(--muted);max-width:80ch}

  @media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{transition:none!important;animation:none!important}}
  @media print{.cats,.langs,.btn,.skip{display:none!important}.card{break-inside:avoid}}
"""

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
           "%3Crect width='64' height='64' rx='14' fill='%230d3641'/%3E"
           "%3Cpath d='M32 11l4 17 15 6v4l-15-2-3 11 5 4v3l-6-2-6 2v-3l5-4-3-11-15 2v-4l15-6z' "
           "fill='%23eef6f7'/%3E%3C/svg%3E")

LANGS = [
    ("ko", "", "한국어", "ko"),
    ("en", "en/", "English", "en"),
    ("ja", "ja/", "日本語", "ja"),
]


def e(s):
    return html.escape(s, quote=True)


def page_url(lang):
    return BASE if lang == "ko" else BASE + lang + "/"


def rel_prefix(lang):
    return "" if lang == "ko" else "../"


def render_service(s, lang):
    c = s[lang]
    pts = "\n".join("            <li>%s</li>" % e(p) for p in c["points"])
    return """
          <li class="card">
            <h3>{name}</h3>
            <p class="card__purpose">{purpose}</p>
            <ul>
{points}
            </ul>
            <p class="card__check"><b>{label}</b>{check}</p>
            <a class="btn" href="{url}" target="_blank" rel="sponsored noopener"
               aria-label="{name} — {cta}">{cta}<span class="arrow" aria-hidden="true">↗</span></a>
          </li>""".format(
        name=e(s["name"]), purpose=e(c["purpose"]), points=pts,
        label=e(COPY[lang]["check_label"]), check=e(c["check"]),
        url=e(URLS[s["id"]]), cta=e(c["cta"]),
    )


# relative hrefs between the three pages, keyed (active page, target page)
LANG_HREF = {
    ("ko", "ko"): "./", ("ko", "en"): "en/", ("ko", "ja"): "ja/",
    ("en", "ko"): "../", ("en", "en"): "./", ("en", "ja"): "../ja/",
    ("ja", "ko"): "../", ("ja", "en"): "../en/", ("ja", "ja"): "./",
}


def render_langs(active):
    out = []
    for code, _path, label, hreflang in LANGS:
        cur = ' aria-current="page"' if code == active else ""
        out.append('      <li><a href="%s" hreflang="%s" lang="%s"%s>%s</a></li>'
                   % (LANG_HREF[(active, code)], hreflang, hreflang, cur, e(label)))
    return "\n".join(out)


def render_cats(lang):
    out = []
    count = {c["key"]: sum(1 for s in SERVICES if s["cat"] == c["key"]) for c in CATEGORIES}
    for c in CATEGORIES:
        info = COPY[lang]["cats"][c["key"]]
        out.append('      <a href="#%s"><span aria-hidden="true">%s</span>%s<span class="n">%d</span></a>'
                   % (c["key"], c["glyph"], e(info["name"]), count[c["key"]]))
    return "\n".join(out)


def render_sections(lang):
    blocks = []
    for c in CATEGORIES:
        cards = [render_service(s, lang) for s in SERVICES if s["cat"] == c["key"]]
        info = COPY[lang]["cats"][c["key"]]
        blocks.append("""
    <section class="cat" id="{key}" aria-labelledby="{key}-h">
      <div class="sec-head">
        <h2 id="{key}-h"><span class="glyph" aria-hidden="true">{glyph}</span>{name}</h2>
        <p>{intro}</p>
      </div>
      <ul class="cards">{cards}
      </ul>
    </section>""".format(key=c["key"], glyph=c["glyph"], name=e(info["name"]),
                          intro=e(info["intro"]), cards="".join(cards)))
    return "".join(blocks)


def render_order(lang):
    cp = COPY[lang]
    items = "\n".join(
        '      <li><a href="%s">%s</a><span>%s</span></li>' % (href, e(t), e(d))
        for t, d, href in cp["order"])
    return """  <section class="order" aria-labelledby="order-h">
      <h2 id="order-h">%s</h2>
      <p class="intro">%s</p>
      <ol>
%s
      </ol>
  </section>""" % (e(cp["order_title"]), e(cp["order_intro"]), items)


def render_notes(lang):
    boxes = "\n".join('      <div><h2>%s</h2><p>%s</p></div>' % (e(t), e(d))
                      for t, d in COPY[lang]["notes"])
    return """  <section class="notes">
%s
  </section>""" % boxes


def render_jsonld(lang):
    items = []
    for i, s in enumerate(SERVICES, 1):
        items.append(
            '      {"@type":"ListItem","position":%d,"name":"%s","description":"%s","url":"%s"}'
            % (i, s["name"], json_escape(s[lang]["purpose"]), json_escape(URLS[s["id"]])))
    return """{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "%s",
  "url": "%s",
  "inLanguage": "%s",
  "isPartOf": {"@type": "WebSite", "url": "https://soomonjjang-lab.github.io/pickle-mobile-chat/"},
  "description": "%s",
  "mainEntity": {
    "@type": "ItemList",
    "numberOfItems": %d,
    "itemListOrder": "https://schema.org/ItemListOrderAscending",
    "itemListElement": [
%s
    ]
  }
}""" % (json_escape(COPY[lang]["title"]), page_url(lang), COPY[lang]["html_lang"],
         json_escape(COPY[lang]["desc"]), len(SERVICES), ",\n".join(items))


def json_escape(s):
    import json
    return json.dumps(s, ensure_ascii=False)[1:-1]


def build(lang):
    cp = COPY[lang]
    pre = rel_prefix(lang)
    alt = "\n".join(
        '<link rel="alternate" hreflang="%s" href="%s">' % (code if code != "ko" else "ko", page_url(code))
        for code, _, _, _ in LANGS)
    alt += '\n<link rel="alternate" hreflang="x-default" href="%s">' % BASE

    body = """<!doctype html>
<html lang="{hl}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index,follow">
<meta name="theme-color" content="#0d3641">
<link rel="icon" href="{favicon}">

<meta property="og:type" content="website">
<meta property="og:site_name" content="Travel Deals">
<meta property="og:locale" content="{oglocale}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<link rel="canonical" href="{url}">
{alts}
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">

<script type="application/ld+json">
{jsonld}
</script>

<style>{css}</style>
</head>
<body>

<a class="skip" href="#catalog">{skip}</a>

<div class="disc" role="note"><strong>{disc}</strong></div>

<header class="hero">
  <div class="wrap">
    <p class="kicker">{kicker}</p>
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
    <ul class="hero-meta">
      <li>{mcount}</li>
      <li>{mcats}</li>
      <li>{mupdated}</li>
    </ul>
    <nav aria-label="{langlabel}">
      <ul class="langs">
{langs}
      </ul>
    </nav>
  </div>
</header>

<nav class="cats" aria-label="{navlabel}">
  <div class="cats__inner">
{cats}
  </div>
</nav>

<main id="catalog">
{sections}
{order}
{notes}
</main>

<footer>
  <div class="wrap">
    <p>{footer}</p>
  </div>
</footer>

</body>
</html>
""".format(
        hl=cp["html_lang"], title=e(cp["title"]), desc=e(cp["desc"]),
        favicon=FAVICON, oglocale=cp["og_locale"], url=page_url(lang), alts=alt,
        jsonld=render_jsonld(lang), css=CSS, skip=e(cp["skip"]), disc=e(cp["disc"]),
        kicker=e(cp["kicker"]), h1=e(cp["h1"]), lede=e(cp["lede"]),
        mcount=e(cp["meta_count"]), mcats=e(cp["meta_cats"]), mupdated=e(cp["meta_updated"]),
        langlabel=e(cp["lang_label"]), langs=render_langs(lang),
        navlabel=e(cp["nav_label"]), cats=render_cats(lang),
        sections=render_sections(lang), order=render_order(lang), notes=render_notes(lang),
        footer=e(cp["footer"]),
    )

    outdir = ROOT if lang == "ko" else os.path.join(ROOT, lang)
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "index.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(body)
    return path


if __name__ == "__main__":
    for lg in ("ko", "en", "ja"):
        print("wrote", build(lg))
