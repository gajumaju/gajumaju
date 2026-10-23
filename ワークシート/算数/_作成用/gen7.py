# かけ算(2) 第7時 9のだんの九九をつくろう（第5時 8のだん レベル2 の型を引き継ぐ）
import sys

G = '#2e7d4f'; O = '#e08a00'
CSS = f'''<link href="https://fonts.googleapis.com/css2?family=Zen+Maru+Gothic:wght@500;700&display=swap" rel="stylesheet">
<style>
@page {{ size: 182mm 257mm; margin: 8mm 20mm 8mm 8mm; }}
* {{ box-sizing: border-box; }}
body {{ margin:0; font-family:"Zen Maru Gothic","Hiragino Maru Gothic ProN",sans-serif; font-weight:500; color:#222; font-size:13pt; line-height:1.45; }}
b, .bold {{ font-weight:700; }}
rt {{ font-size:6.5pt; }}
.page {{ height:240mm; display:flex; flex-direction:column; overflow:hidden; padding-right:2.5mm; padding-left:0.5mm; }}
.page + .page {{ break-before: page; }}
.head {{ display:flex; justify-content:space-between; align-items:flex-end; border-bottom:2.5px solid {G}; padding-bottom:2mm; }}
.title {{ font-size:14pt; white-space:nowrap; font-weight:700; }}
.title small {{ font-size:10.5pt; color:{G}; margin-right:2mm; font-weight:700; }}
.pg {{ display:inline-block; font-size:10pt; font-weight:700; color:{G}; border:1.5px solid {G}; border-radius:1.5mm; padding:0 2mm; margin-right:2mm; vertical-align:middle; line-height:1.7; }}
.pg img {{ display:inline-block; height:4mm; vertical-align:-0.6mm; margin-right:1mm; }}
.lv {{ display:inline-block; font-size:10pt; font-weight:700; color:#fff; background:{G}; border-radius:1.5mm; padding:0 2.5mm; vertical-align:middle; line-height:1.8; }}
.name {{ font-size:10.5pt; white-space:nowrap; text-align:right; }}
.name span {{ display:inline-block; border-bottom:1px solid #333; width:30mm; height:7mm; }}
.box {{ border:2px solid {G}; border-radius:3mm; padding:2mm 3mm; display:flex; align-items:center; gap:3mm; margin-top:3mm; }}
.box .t {{ flex:1; }}
.sub {{ font-size:11pt; color:#555; }}
.q {{ font-weight:700; color:{G}; font-size:13.5pt; margin-top:3mm; }}
table.mk {{ border-collapse:collapse; width:100%; margin-top:1mm; }}
table.mk th {{ font-size:10pt; color:#fff; padding:0.8mm; font-weight:700; }}
table.mk td {{ border-bottom:1px solid #ccc; height:11.6mm; vertical-align:middle; }}
table.mk td.r {{ width:24mm; font-size:11.5pt; color:{G}; font-weight:700; line-height:1.15; border-right:1px solid #ccc; }}
table.mk td.r small {{ display:block; font-size:7.5pt; font-weight:500; }}
table.mk td.a {{ border-right:1px solid #ccc; padding-left:2.5mm; font-size:14pt; white-space:nowrap; }}
table.mk td.b {{ padding-left:2.5mm; font-size:14pt; white-space:nowrap; }}
.sq {{ display:inline-block; width:12mm; height:9mm; border:1.8px solid #333; border-radius:1.5mm; vertical-align:middle; }}
.wline {{ display:block; border-bottom:1px solid #999; margin:5mm 4mm 0 0; }}
.ck {{ border:1.5px solid #bbb; border-radius:2mm; padding:1.2mm 3mm; margin-top:1.8mm; font-size:12pt; }}
.ck b {{ margin-right:2.5mm; }}
.ex {{ color:#555; font-size:11pt; }}
.tbl9 {{ border-collapse:collapse; margin:1.5mm 0 0 6mm; }}
.tbl9 td, .tbl9 th {{ border:1px solid {G}; text-align:center; }}
.tbl9 th {{ background:#e7f1ea; color:{G}; font-size:11pt; width:12.5mm; height:6.5mm; }}
.tbl9 td {{ height:12mm; }}
.tbl9 .rh {{ width:16mm; background:#e7f1ea; color:{G}; font-size:10.5pt; font-weight:700; }}
.matome {{ border:2.5px solid {O}; border-radius:3mm; padding:2.5mm 4mm 3mm; background:#fff8ec; font-size:13.5pt; line-height:2.2; display:flex; align-items:center; gap:3mm; margin-top:4mm; }}
.matome .tag {{ background:{O}; color:#fff; font-size:11pt; padding:0 3mm; border-radius:1.5mm; font-weight:700; line-height:1.6; flex:none; }}
.matome .in {{ display:inline-block; width:24mm; height:10mm; border:1.8px solid #333; border-radius:1.5mm; vertical-align:middle; background:#fff; }}
.lines div {{ border-bottom:1.5px solid #999; height:13mm; }}
.spacer {{ flex:1; }}
.furiwrap {{ border-top:1.5px dashed #bbb; padding-top:1.5mm; display:flex; align-items:center; gap:2mm; white-space:nowrap; }}
.furi {{ display:flex; gap:1.2mm; font-size:9.5pt; }}
.furi span {{ border:1.5px solid #bbb; border-radius:2mm; padding:1mm 1.6mm; display:flex; align-items:center; gap:0.8mm; }}
.furi img {{ height:4.2mm; }}
.hanko {{ margin-left:auto; margin-right:1mm; flex:none; width:14mm; height:14mm; border:2px dashed {O}; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:9pt; font-weight:700; color:{O}; background:#fffaf0; }}
</style>'''

def head(lv):
    return f'''<div class="head">
  <div class="title"><small>かけ<ruby>算<rt>ざん</rt></ruby>（2）⑦</small><span class="pg"><img src="img/book.png"><ruby>教科書<rt>きょうかしょ</rt></ruby> 33ページ</span><span class="lv">レベル{lv}</span><br>9の だんの <ruby>九九<rt>くく</rt></ruby>を つくろう</div>
  <div class="name"><ruby>月<rt>がつ</rt></ruby>　　<ruby>日<rt>にち</rt></ruby><br><ruby>名前<rt>なまえ</rt></ruby> <span></span></div>
</div>'''

def dots():
    cw, rh, x0, y0 = 5.2, 4.6, 0, 5.2
    o = [f'<svg width="{9*cw+1}mm" height="{y0+9*rh+1}mm" viewBox="0 0 {9*cw+1} {y0+9*rh+1}">']
    for j in range(9):
        o.append(f'<rect x="{j*cw+0.5}" y="0.5" width="{cw}" height="4.2" fill="#e7f1ea" stroke="{G}" stroke-width="0.25"/>'
                 f'<text x="{j*cw+0.5+cw/2}" y="3.8" font-size="3.3" text-anchor="middle" fill="{G}">{j+1}</text>')
        for i in range(9):
            o.append(f'<circle cx="{j*cw+0.5+cw/2}" cy="{y0+i*rh+rh/2+0.3}" r="1.85" fill="none" stroke="{O}" stroke-width="0.4"/>')
    o.append('</svg>')
    return ''.join(o)

def furikaeri():
    return '''<div class="spacer"></div>
<div class="furiwrap"><b style="font-size:12pt">ふりかえり</b>
  <div class="furi"><span><img src="img/tree.png"><img src="img/tree.png"> ひとりで できた</span><span><img src="img/tree.png"> ヒントで できた</span><span><img src="img/sprout.png"> もう すこし</span></div>
  <div class="hanko">ハンコ</div></div>'''

SQ = '<span class="sq"></span>'

def rows(lv):
    out = []
    for n in range(1, 10):
        r = f'<td class="r">{n}れつめ<small>9こずつ {n}つ<ruby>分<rt>ぶん</rt></ruby></small></td>'
        if lv == 2 and n >= 7:
            a = b = '<span class="wline"></span>'
        elif lv == 2:
            a = '9' if n == 1 else f'{SQ} ＋ 9 ＝ {SQ}'
            b = f'{SQ} × {SQ} ＝ {SQ}'
        else:
            a = '9' if n == 1 else f'{SQ} ＋ 9 ＝ {SQ}'
            b = f'9 × {n} ＝ {SQ}'
        out.append(f'<tr>{r}<td class="a">{a}</td><td class="b">{b}</td></tr>')
    return ''.join(out)

def p1(lv):
    note = ('7・8・9れつめは、しきを <ruby>自分<rt>じぶん</rt></ruby>で <ruby>書<rt>か</rt></ruby>こう。' if lv == 2
            else 'まえの <ruby>答<rt>こた</rt></ruby>えに 9を たすと、つぎの <ruby>答<rt>こた</rt></ruby>えに なるよ。')
    return f'''<div class="page">
{head(lv)}
<div class="box"><div class="t"><b>9の だんの <ruby>九九<rt>くく</rt></ruby>を つくりましょう。</b><br>
<span class="sub">これまでに <ruby>見<rt>み</rt></ruby>つけた <ruby>九九<rt>くく</rt></ruby>の きまりが つかえないかな。</span></div>
<img src="img/tri.png" style="height:17mm"></div>
<div style="display:flex;align-items:center;gap:4mm;margin:2mm 0 0 14mm">{dots()}
<div class="sub" style="line-height:1.7">1れつに ○が 9こ。<br>れつを ふやして いこう。<br><ruby>色<rt>いろ</rt></ruby>を ぬっても いいよ。</div></div>
<div class="q">？ 9の だんの <ruby>九九<rt>くく</rt></ruby>の つくり<ruby>方<rt>かた</rt></ruby>を くふうして <ruby>考<rt>かんが</rt></ruby>えよう。</div>
<div style="font-size:12pt">○の <ruby>数<rt>かず</rt></ruby>を、たしざんと かけ<ruby>算<rt>ざん</rt></ruby>の しきに しよう。</div>
<table class="mk"><tr><th></th>
<th style="background:{O}">たしざん（<ruby>前<rt>まえ</rt></ruby>の <ruby>答<rt>こた</rt></ruby>え ＋ 9）</th>
<th style="background:{G}">かけ<ruby>算<rt>ざん</rt></ruby>（1つ<ruby>分<rt>ぶん</rt></ruby>の <ruby>数<rt>かず</rt></ruby> × いくつ<ruby>分<rt>ぶん</rt></ruby>）</th></tr>
{rows(lv)}</table>
<div style="font-size:10.5pt;margin-top:1.5mm">{note}</div>
</div>'''

def p2(lv):
    def ck(t, ex):
        return f'<div class="ck"><b>□</b>{t} <span class="ex">（{ex}）</span></div>'
    return f'''<div class="page">
{head(lv)}
<div class="q">どのように <ruby>考<rt>かんが</rt></ruby>えたかな。<span style="font-size:10pt;color:#444;font-weight:500">つかった ものに ✓</span></div>
{ck('かける<ruby>数<rt>かず</rt></ruby>が 1 ふえると、<ruby>答<rt>こた</rt></ruby>えは 9 ふえる', '9×5＝45 → 9×6＝54')}
{ck('かけられる<ruby>数<rt>かず</rt></ruby>と かける<ruby>数<rt>かず</rt></ruby>を <ruby>入<rt>い</rt></ruby>れかえた', '9×3＝3×9')}
{ck('2つに わけて たした', '9×6 → 5×6 と 4×6')}
<div style="font-size:11pt;color:#444;margin-top:1.5mm">そのほかの <ruby>考<rt>かんが</rt></ruby>え<ruby>方<rt>かた</rt></ruby></div>
<div class="lines"><div></div></div>
<div style="margin-top:4mm"><span style="color:{G};font-size:14pt;font-weight:700">①</span> 23ページの ひょうに、9の だんの <ruby>九九<rt>くく</rt></ruby>の <ruby>答<rt>こた</rt></ruby>えを <ruby>書<rt>か</rt></ruby>きましょう。</div>
<table class="tbl9"><tr><th style="background:none;border:0"></th>{''.join(f'<th>{i}</th>' for i in range(1,10))}</tr>
<tr><td class="rh">9の だん</td>{'<td></td>'*9}</tr></table>
<div class="matome"><span class="tag">まとめ</span>
<div style="flex:1">これまでに <ruby>見<rt>み</rt></ruby>つけた いろいろな<br><span class="in"></span> を つかって、9の だんの <ruby>九九<rt>くく</rt></ruby>も<br>つくる ことが できた。</div>
<img src="img/witch.png" style="height:20mm"></div>
<div style="font-size:11pt;color:#444;margin-top:3mm">きづいた こと</div>
<div class="lines"><div></div><div></div></div>
{furikaeri()}
</div>'''

lv = int(sys.argv[1])
html = f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>かけ算2 第7時 レベル{lv}</title>{CSS}</head><body>{p1(lv)}{p2(lv)}</body></html>'
open(f'ws7_lv{lv}.html', 'w').write(html)
