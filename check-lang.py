# index.html 속 한글 줄이 lang.json(영문·한자 번역표)에 다 있는지 확인한다.
# index.html을 고친 뒤 실행: python3 check-lang.py  → 빠진 줄을 보여 준다
import json, re
src = open('index.html', encoding='utf-8').read().split('\n')
table = json.load(open('lang.json', encoding='utf-8'))
missing = sorted({l.strip() for l in src if re.search('[가-힣]', l)} - table.keys())
for m in missing: print('번역 없음:', m)
print('OK' if not missing else f'{len(missing)}줄 번역 필요')
