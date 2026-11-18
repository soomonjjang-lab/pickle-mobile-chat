# 똘마니 모바일 소통창 (PWA)

`soomonjjang-lab/pickle-pc-control` Issue #1 방을 폰에서 그대로 쓰는 웹 소통창입니다.
PC 소통창(`pickle_chat.pyw`)과 같은 방·같은 형식(`[PC]` 말머리)을 사용합니다.

## 구성

| 파일 | 설명 |
| --- | --- |
| `index.html` | 앱 전체 (말풍선 렌더링, 9초 폴링, 사진 첨부, 토큰 입력) |
| `manifest.json` | PWA 매니페스트 (홈 화면 추가 시 전체화면 실행) |
| `sw.js` | 앱 셸 캐시 서비스워커 |
| `icons/` | 앱 아이콘 (192 / 512 / maskable / apple-touch) |

## 보안

- GitHub 토큰은 **코드·URL·저장소에 없습니다.** 처음 화면에서 한 번 입력하면 브라우저
  `localStorage`에만 저장되고, `api.github.com` 외에는 전송되지 않습니다.
- 저장된 토큰은 ⚙ 설정 → "토큰 삭제" 로 언제든 지울 수 있습니다.

## 사용

1. 배포 주소를 폰 크롬으로 연다.
2. PC 소통창에 쓰던 GitHub 토큰을 붙여넣고 저장한다.
3. 크롬 메뉴 ⋮ → **앱 설치 / 홈 화면에 추가**.

## 동작 방식

- `GET /repos/soomonjjang-lab/pickle-pc-control/issues/1/comments` 를 `per_page=100` 페이지
  루프로 전부 받아오고, 이후에는 `since=` 로 새 글만 가져옵니다(9초 주기, 전체 재조회 10회마다 1번).
- 전송은 `[PC] ` 말머리를 붙여 Issue #1에 댓글로 등록합니다.
- 사진은 `captures/` 에 업로드한 뒤 `📎 사진 첨부: captures/…` 댓글로 남기고, 앱이 토큰으로
  이미지를 받아 표시합니다.
