## FontBakery report

fontbakery version: 0.10.2

<details><summary><b>[23] Danfo-Bold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 fsType does not impose restrictions. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fstype">com.google.fonts/check/fstype</a>)</summary><div>


* 🔥 **FAIL** In this font fsType is set to 8 meaning that:
The font may be embedded but must only be installed temporarily on other systems.

No such DRM restrictions can be enabled on the Google Fonts collection, so the fsType field must be set to zero (Installable Embedding) instead. [code: drm]
</div></details><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0034 (DIGIT FOUR)


	- 0x0035 (DIGIT FIVE)


	- 0x0036 (DIGIT SIX)


	- 0x0037 (DIGIT SEVEN)


	- 0x0100 (LATIN CAPITAL LETTER A WITH MACRON)


	- 0x0112 (LATIN CAPITAL LETTER E WITH MACRON)


	- 0x012A (LATIN CAPITAL LETTER I WITH MACRON)


	- 0x014C (LATIN CAPITAL LETTER O WITH MACRON)


	- 0x016A (LATIN CAPITAL LETTER U WITH MACRON)


	- 0x0101 (LATIN SMALL LETTER A WITH MACRON)


	- 0x0113 (LATIN SMALL LETTER E WITH MACRON)


	- 0x012B (LATIN SMALL LETTER I WITH MACRON)


	- 0x014D (LATIN SMALL LETTER O WITH MACRON)


	- 0x016B (LATIN SMALL LETTER U WITH MACRON)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font names are correct (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_names">com.google.fonts/check/font_names</a>)</summary><div>


* 🔥 **FAIL** Font names are incorrect:

| nameID | current | expected |
| :--- | :--- | :--- |
| Family Name | **Danfo Bold** | **Danfo** |
| Subfamily Name | **Regular** | **Bold** |
| Full Name | Danfo Bold | Danfo Bold |
| Postscript Name | Danfo-Bold | Danfo-Bold |
| Typographic Family Name | **Danfo** | **N/A** |
| Typographic Subfamily Name | **Bold** | **N/A** | [code: bad-names]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.sTypoLineGap is "200" it should be 0 [code: bad-OS/2.sTypoLineGap]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1150, but got 1100 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 917, but got 100 instead [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (900) and hhea ascent (1100) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current FontBakery version is 0.10.2, while a newer 0.10.3 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Font contains '.notdef' as its first glyph? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/mandatory_glyphs">com.google.fonts/check/mandatory_glyphs</a>)</summary><div>


* 🔥 **FAIL** The '.notdef' glyph should contain a drawing, but it is blank. [code: notdef-is-blank]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* 🔥 **FAIL** The following glyphs have no contours even though they were expected to have some:

	- Glyph name: dollar	Expected: 1, 3 or 5

	- Glyph name: percent	Expected: 5

	- Glyph name: ampersand	Expected: 1, 2 or 3

	- Glyph name: plus	Expected: 1

	- Glyph name: less	Expected: 1

	- Glyph name: equal	Expected: 2

	- Glyph name: greater	Expected: 1

	- Glyph name: at	Expected: 2

	- Glyph name: asciicircum	Expected: 1

	- Glyph name: k	Expected: 1 or 2

	- Glyph name: n	Expected: 1

	- Glyph name: p	Expected: 2

	- Glyph name: q	Expected: 2

	- Glyph name: bar	Expected: 1

	- Glyph name: asciitilde	Expected: 1

	- Glyph name: cent	Expected: 1 or 2

	- Glyph name: sterling	Expected: 1 or 2

	- Glyph name: yen	Expected: 1 or 2

	- Glyph name: section	Expected: 2

	- Glyph name: copyright	Expected: 3

	- Glyph name: registered	Expected: 3 or 4

	- Glyph name: degree	Expected: 2

	- Glyph name: paragraph	Expected: 1, 2 or 3

	- Glyph name: AE	Expected: 2

	- Glyph name: Eth	Expected: 2

	- Glyph name: multiply	Expected: 1

	- Glyph name: Oslash	Expected: 2 or 3

	- Glyph name: Thorn	Expected: 1 or 2

	- Glyph name: germandbls	Expected: 1

	- Glyph name: ae	Expected: 3

	- Glyph name: eth	Expected: 2

	- Glyph name: divide	Expected: 3

	- Glyph name: oslash	Expected: 3

	- Glyph name: thorn	Expected: 2

	- Glyph name: Dcroat	Expected: 2

	- Glyph name: dcroat	Expected: 2

	- Glyph name: Hbar	Expected: 2

	- Glyph name: hbar	Expected: 1

	- Glyph name: Lslash	Expected: 1

	- Glyph name: lslash	Expected: 1

	- Glyph name: Eng	Expected: 1

	- Glyph name: eng	Expected: 1

	- Glyph name: OE	Expected: 2

	- Glyph name: oe	Expected: 3

	- Glyph name: uni0180	Expected: 2

	- Glyph name: uni0181	Expected: 3

	- Glyph name: uni0186	Expected: 1

	- Glyph name: uni0187	Expected: 1

	- Glyph name: uni0188	Expected: 1

	- Glyph name: Dtail	Expected: 2

	- Glyph name: uni018A	Expected: 2

	- Glyph name: uni018E	Expected: 1

	- Glyph name: uni018F	Expected: 2

	- Glyph name: uni0190	Expected: 1

	- Glyph name: uni0191	Expected: 1

	- Glyph name: florin	Expected: 1

	- Glyph name: uni0193	Expected: 1

	- Glyph name: Gammalatin	Expected: 2

	- Glyph name: Iotalatin	Expected: 1

	- Glyph name: uni0197	Expected: 1

	- Glyph name: uni0198	Expected: 1

	- Glyph name: uni0199	Expected: 1

	- Glyph name: uni019A	Expected: 1

	- Glyph name: uni019B	Expected: 1

	- Glyph name: uni019D	Expected: 1

	- Glyph name: uni019E	Expected: 1

	- Glyph name: uni019F	Expected: 3

	- Glyph name: uni01A4	Expected: 2

	- Glyph name: uni01A5	Expected: 2

	- Glyph name: uni01A9	Expected: 1

	- Glyph name: uni01AC	Expected: 1

	- Glyph name: uni01AD	Expected: 1

	- Glyph name: uni01AE	Expected: 1

	- Glyph name: Upsilonlatin	Expected: 1

	- Glyph name: uni01B2	Expected: 1

	- Glyph name: uni01B3	Expected: 1

	- Glyph name: uni01B4	Expected: 1

	- Glyph name: uni01B5	Expected: 1

	- Glyph name: uni01B6	Expected: 1

	- Glyph name: uni01B7	Expected: 1

	- Glyph name: uni01B8	Expected: 1

	- Glyph name: uni01B9	Expected: 1

	- Glyph name: uni01C0	Expected: 1

	- Glyph name: uni01C1	Expected: 2

	- Glyph name: uni01C2	Expected: 1

	- Glyph name: uni01C3	Expected: 2

	- Glyph name: uni01DD	Expected: 2

	- Glyph name: uni01E4	Expected: 1

	- Glyph name: uni01E5	Expected: 2

	- Glyph name: uni0220	Expected: 1

	- Glyph name: uni0222	Expected: 2

	- Glyph name: uni0223	Expected: 2

	- Glyph name: uni0237	Expected: 1

	- Glyph name: uni023A	Expected: 3

	- Glyph name: uni023B	Expected: 2

	- Glyph name: uni023C	Expected: 2

	- Glyph name: uni023D	Expected: 1

	- Glyph name: uni023E	Expected: 2

	- Glyph name: uni0241	Expected: 1

	- Glyph name: uni0242	Expected: 1

	- Glyph name: uni0243	Expected: 3

	- Glyph name: uni0244	Expected: 2

	- Glyph name: uni0245	Expected: 1

	- Glyph name: uni0246	Expected: 3

	- Glyph name: uni0247	Expected: 4

	- Glyph name: uni0248	Expected: 1

	- Glyph name: uni0249	Expected: 2

	- Glyph name: uni024A	Expected: 2

	- Glyph name: uni024B	Expected: 2

	- Glyph name: uni024C	Expected: 2

	- Glyph name: uni024D	Expected: 1

	- Glyph name: uni024E	Expected: 2

	- Glyph name: uni024F	Expected: 2

	- Glyph name: uni0251	Expected: 2

	- Glyph name: uni0259	Expected: 2

	- Glyph name: uni0272	Expected: 1

	- Glyph name: uni0292	Expected: 1

	- Glyph name: uni02BB	Expected: 1

	- Glyph name: uni02BE	Expected: 1

	- Glyph name: uni02BF	Expected: 1

	- Glyph name: uni02CA	Expected: 1

	- Glyph name: uni02CB	Expected: 1

	- Glyph name: hookabovecomb	Expected: 1

	- Glyph name: uni031B	Expected: 1

	- Glyph name: uni1E2A	Expected: 2

	- Glyph name: uni1E2B	Expected: 2

	- Glyph name: uni1E9E	Expected: 1

	- Glyph name: uni207F	Expected: 1

	- Glyph name: Euro	Expected: 1 or 2

	- Glyph name: uni20AD	Expected: 1

	- Glyph name: minus	Expected: 1

	- Glyph name: uniA78B	Expected: 1

	- Glyph name: uniA78C	Expected: 1

	- Glyph name: AE	Expected: 2

	- Glyph name: Dcroat	Expected: 2

	- Glyph name: Eng	Expected: 1

	- Glyph name: Eth	Expected: 2

	- Glyph name: Euro	Expected: 1 or 2

	- Glyph name: Hbar	Expected: 2

	- Glyph name: Lslash	Expected: 1

	- Glyph name: OE	Expected: 2

	- Glyph name: Oslash	Expected: 2 or 3

	- Glyph name: Thorn	Expected: 1 or 2

	- Glyph name: ae	Expected: 3

	- Glyph name: ampersand	Expected: 1, 2 or 3

	- Glyph name: asciicircum	Expected: 1

	- Glyph name: asciitilde	Expected: 1

	- Glyph name: at	Expected: 2

	- Glyph name: bar	Expected: 1

	- Glyph name: cent	Expected: 1 or 2

	- Glyph name: copyright	Expected: 3

	- Glyph name: dcroat	Expected: 2

	- Glyph name: degree	Expected: 2

	- Glyph name: divide	Expected: 3

	- Glyph name: dollar	Expected: 1, 3 or 5

	- Glyph name: eng	Expected: 1

	- Glyph name: equal	Expected: 2

	- Glyph name: eth	Expected: 2

	- Glyph name: germandbls	Expected: 1

	- Glyph name: greater	Expected: 1

	- Glyph name: hbar	Expected: 1

	- Glyph name: k	Expected: 1 or 2

	- Glyph name: less	Expected: 1

	- Glyph name: lslash	Expected: 1

	- Glyph name: minus	Expected: 1

	- Glyph name: multiply	Expected: 1

	- Glyph name: n	Expected: 1

	- Glyph name: oe	Expected: 3

	- Glyph name: oslash	Expected: 3

	- Glyph name: p	Expected: 2

	- Glyph name: paragraph	Expected: 1, 2 or 3

	- Glyph name: percent	Expected: 5

	- Glyph name: plus	Expected: 1

	- Glyph name: q	Expected: 2

	- Glyph name: registered	Expected: 3 or 4

	- Glyph name: section	Expected: 2

	- Glyph name: sterling	Expected: 1 or 2

	- Glyph name: thorn	Expected: 2

	- Glyph name: uni0180	Expected: 2

	- Glyph name: uni0181	Expected: 3

	- Glyph name: uni0186	Expected: 1

	- Glyph name: uni0187	Expected: 1

	- Glyph name: uni0188	Expected: 1

	- Glyph name: uni018A	Expected: 2

	- Glyph name: uni018E	Expected: 1

	- Glyph name: uni018F	Expected: 2

	- Glyph name: uni0190	Expected: 1

	- Glyph name: uni0191	Expected: 1

	- Glyph name: uni0193	Expected: 1

	- Glyph name: uni0197	Expected: 1

	- Glyph name: uni0198	Expected: 1

	- Glyph name: uni0199	Expected: 1

	- Glyph name: uni019A	Expected: 1

	- Glyph name: uni019B	Expected: 1

	- Glyph name: uni019D	Expected: 1

	- Glyph name: uni019E	Expected: 1

	- Glyph name: uni019F	Expected: 3

	- Glyph name: uni01A4	Expected: 2

	- Glyph name: uni01A5	Expected: 2

	- Glyph name: uni01A9	Expected: 1

	- Glyph name: uni01AC	Expected: 1

	- Glyph name: uni01AD	Expected: 1

	- Glyph name: uni01AE	Expected: 1

	- Glyph name: uni01B2	Expected: 1

	- Glyph name: uni01B3	Expected: 1

	- Glyph name: uni01B4	Expected: 1

	- Glyph name: uni01B5	Expected: 1

	- Glyph name: uni01B6	Expected: 1

	- Glyph name: uni01B7	Expected: 1

	- Glyph name: uni01B8	Expected: 1

	- Glyph name: uni01B9	Expected: 1

	- Glyph name: uni01C0	Expected: 1

	- Glyph name: uni01C1	Expected: 2

	- Glyph name: uni01C2	Expected: 1

	- Glyph name: uni01C3	Expected: 2

	- Glyph name: uni01DD	Expected: 2

	- Glyph name: uni01E4	Expected: 1

	- Glyph name: uni01E5	Expected: 2

	- Glyph name: uni0220	Expected: 1

	- Glyph name: uni0222	Expected: 2

	- Glyph name: uni0223	Expected: 2

	- Glyph name: uni0237	Expected: 1

	- Glyph name: uni023A	Expected: 3

	- Glyph name: uni023B	Expected: 2

	- Glyph name: uni023C	Expected: 2

	- Glyph name: uni023D	Expected: 1

	- Glyph name: uni023E	Expected: 2

	- Glyph name: uni0241	Expected: 1

	- Glyph name: uni0242	Expected: 1

	- Glyph name: uni0243	Expected: 3

	- Glyph name: uni0244	Expected: 2

	- Glyph name: uni0245	Expected: 1

	- Glyph name: uni0246	Expected: 3

	- Glyph name: uni0247	Expected: 4

	- Glyph name: uni0248	Expected: 1

	- Glyph name: uni0249	Expected: 2

	- Glyph name: uni024A	Expected: 2

	- Glyph name: uni024B	Expected: 2

	- Glyph name: uni024C	Expected: 2

	- Glyph name: uni024D	Expected: 1

	- Glyph name: uni024E	Expected: 2

	- Glyph name: uni024F	Expected: 2

	- Glyph name: uni0251	Expected: 2

	- Glyph name: uni0259	Expected: 2

	- Glyph name: uni0272	Expected: 1

	- Glyph name: uni0292	Expected: 1

	- Glyph name: uni02BB	Expected: 1

	- Glyph name: uni02BE	Expected: 1

	- Glyph name: uni02BF	Expected: 1

	- Glyph name: uni02CA	Expected: 1

	- Glyph name: uni02CB	Expected: 1

	- Glyph name: uni031B	Expected: 1

	- Glyph name: uni1E2A	Expected: 2

	- Glyph name: uni1E2B	Expected: 2

	- Glyph name: uni1E9E	Expected: 1

	- Glyph name: uni20AD	Expected: 1

	- Glyph name: uniA78B	Expected: 1

	- Glyph name: uniA78C	Expected: 1

	- Glyph name: yen	Expected: 1 or 2
 [code: no-contour]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: H	Contours detected: 3	Expected: 1

	- Glyph name: b	Contours detected: 3	Expected: 2

	- Glyph name: e	Contours detected: 1	Expected: 2

	- Glyph name: g	Contours detected: 1	Expected: 2 or 3

	- Glyph name: h	Contours detected: 3	Expected: 1

	- Glyph name: j	Contours detected: 1	Expected: 2

	- Glyph name: r	Contours detected: 2	Expected: 1

	- Glyph name: egrave	Contours detected: 2	Expected: 3

	- Glyph name: eacute	Contours detected: 2	Expected: 3

	- Glyph name: ecircumflex	Contours detected: 2	Expected: 3

	- Glyph name: edieresis	Contours detected: 3	Expected: 4

	- Glyph name: ntilde	Contours detected: 1	Expected: 2

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: edotaccent	Contours detected: 2	Expected: 3

	- Glyph name: ecaron	Contours detected: 2	Expected: 3

	- Glyph name: gbreve	Contours detected: 2	Expected: 3 or 4

	- Glyph name: gdotaccent	Contours detected: 2	Expected: 3 or 4

	- Glyph name: uni0123	Contours detected: 2	Expected: 3 or 4

	- Glyph name: uni0137	Contours detected: 1	Expected: 2 or 3

	- Glyph name: nacute	Contours detected: 1	Expected: 2

	- Glyph name: uni0146	Contours detected: 1	Expected: 2

	- Glyph name: ncaron	Contours detected: 1	Expected: 2

	- Glyph name: racute	Contours detected: 3	Expected: 2

	- Glyph name: uni0157	Contours detected: 3	Expected: 2

	- Glyph name: rcaron	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: gcaron	Contours detected: 2	Expected: 3 or 4

	- Glyph name: uni01E9	Contours detected: 1	Expected: 2

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni01EE	Contours detected: 1	Expected: 2

	- Glyph name: uni01EF	Contours detected: 1	Expected: 2

	- Glyph name: uni01F5	Contours detected: 2	Expected: 3

	- Glyph name: uni01F9	Contours detected: 1	Expected: 2

	- Glyph name: Oslashacute	Contours detected: 1	Expected: 4

	- Glyph name: oslashacute	Contours detected: 1	Expected: 4

	- Glyph name: uni0205	Contours detected: 3	Expected: 4

	- Glyph name: uni0207	Contours detected: 2	Expected: 3

	- Glyph name: uni0211	Contours detected: 4	Expected: 3

	- Glyph name: uni0213	Contours detected: 3	Expected: 2

	- Glyph name: uni021E	Contours detected: 4	Expected: 2

	- Glyph name: uni021F	Contours detected: 4	Expected: 2

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni02B0	Contours detected: 3	Expected: 1

	- Glyph name: uni1E03	Contours detected: 4	Expected: 3

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E15	Contours detected: 3	Expected: 4

	- Glyph name: uni1E16	Contours detected: 1	Expected: 3

	- Glyph name: uni1E17	Contours detected: 1	Expected: 4

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E21	Contours detected: 2	Expected: 3 or 4

	- Glyph name: uni1E24	Contours detected: 4	Expected: 2

	- Glyph name: uni1E25	Contours detected: 4	Expected: 2

	- Glyph name: uni1E45	Contours detected: 1	Expected: 2

	- Glyph name: uni1E47	Contours detected: 1	Expected: 2

	- Glyph name: nmacronbelow	Contours detected: 1	Expected: 2

	- Glyph name: uni1E52	Contours detected: 2	Expected: 4

	- Glyph name: uni1E53	Contours detected: 2	Expected: 4

	- Glyph name: uni1E57	Contours detected: 1	Expected: 3

	- Glyph name: uni1E5B	Contours detected: 3	Expected: 2

	- Glyph name: uni1E5D	Contours detected: 4	Expected: 3

	- Glyph name: rmacronbelow	Contours detected: 3	Expected: 2

	- Glyph name: uni1EA2	Contours detected: 2	Expected: 3

	- Glyph name: uni1EA3	Contours detected: 2	Expected: 3

	- Glyph name: uni1EA8	Contours detected: 3	Expected: 4

	- Glyph name: uni1EA9	Contours detected: 3	Expected: 4

	- Glyph name: uni1EB2	Contours detected: 3	Expected: 4

	- Glyph name: uni1EB3	Contours detected: 3	Expected: 4

	- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

	- Glyph name: uni1EBA	Contours detected: 1	Expected: 2

	- Glyph name: uni1EBB	Contours detected: 1	Expected: 3

	- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

	- Glyph name: uni1EBF	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC1	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC2	Contours detected: 2	Expected: 3

	- Glyph name: uni1EC3	Contours detected: 2	Expected: 4

	- Glyph name: uni1EC5	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC7	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC8	Contours detected: 1	Expected: 2

	- Glyph name: uni1EC9	Contours detected: 1	Expected: 2

	- Glyph name: uni1ECE	Contours detected: 2	Expected: 3

	- Glyph name: uni1ECF	Contours detected: 2	Expected: 3

	- Glyph name: uni1ED4	Contours detected: 3	Expected: 4

	- Glyph name: uni1ED5	Contours detected: 3	Expected: 4

	- Glyph name: uni1EDE	Contours detected: 2	Expected: 3 or 4

	- Glyph name: uni1EDF	Contours detected: 2	Expected: 3

	- Glyph name: uni1EE6	Contours detected: 1	Expected: 2

	- Glyph name: uni1EE7	Contours detected: 1	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 1	Expected: 2

	- Glyph name: uni1EED	Contours detected: 1	Expected: 2

	- Glyph name: uni1EF6	Contours detected: 1	Expected: 2

	- Glyph name: uni1EF7	Contours detected: 1	Expected: 2

	- Glyph name: H	Contours detected: 3	Expected: 1

	- Glyph name: Oslashacute	Contours detected: 1	Expected: 4

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: b	Contours detected: 3	Expected: 2

	- Glyph name: e	Contours detected: 1	Expected: 2

	- Glyph name: eacute	Contours detected: 2	Expected: 3

	- Glyph name: ecaron	Contours detected: 2	Expected: 3

	- Glyph name: ecircumflex	Contours detected: 2	Expected: 3

	- Glyph name: edieresis	Contours detected: 3	Expected: 4

	- Glyph name: edotaccent	Contours detected: 2	Expected: 3

	- Glyph name: egrave	Contours detected: 2	Expected: 3

	- Glyph name: g	Contours detected: 1	Expected: 2 or 3

	- Glyph name: gbreve	Contours detected: 2	Expected: 3 or 4

	- Glyph name: gcaron	Contours detected: 2	Expected: 3 or 4

	- Glyph name: gdotaccent	Contours detected: 2	Expected: 3 or 4

	- Glyph name: h	Contours detected: 3	Expected: 1

	- Glyph name: j	Contours detected: 1	Expected: 2

	- Glyph name: nacute	Contours detected: 1	Expected: 2

	- Glyph name: ncaron	Contours detected: 1	Expected: 2

	- Glyph name: ntilde	Contours detected: 1	Expected: 2

	- Glyph name: oslashacute	Contours detected: 1	Expected: 4

	- Glyph name: r	Contours detected: 2	Expected: 1

	- Glyph name: racute	Contours detected: 3	Expected: 2

	- Glyph name: rcaron	Contours detected: 3	Expected: 2

	- Glyph name: uni0123	Contours detected: 2	Expected: 3 or 4

	- Glyph name: uni0137	Contours detected: 1	Expected: 2 or 3

	- Glyph name: uni0146	Contours detected: 1	Expected: 2

	- Glyph name: uni0157	Contours detected: 3	Expected: 2

	- Glyph name: uni01E9	Contours detected: 1	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni01EE	Contours detected: 1	Expected: 2

	- Glyph name: uni01EF	Contours detected: 1	Expected: 2

	- Glyph name: uni01F9	Contours detected: 1	Expected: 2

	- Glyph name: uni021E	Contours detected: 4	Expected: 2

	- Glyph name: uni021F	Contours detected: 4	Expected: 2

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni1E03	Contours detected: 4	Expected: 3

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E15	Contours detected: 3	Expected: 4

	- Glyph name: uni1E16	Contours detected: 1	Expected: 3

	- Glyph name: uni1E17	Contours detected: 1	Expected: 4

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E21	Contours detected: 2	Expected: 3 or 4

	- Glyph name: uni1E24	Contours detected: 4	Expected: 2

	- Glyph name: uni1E25	Contours detected: 4	Expected: 2

	- Glyph name: uni1E45	Contours detected: 1	Expected: 2

	- Glyph name: uni1E47	Contours detected: 1	Expected: 2

	- Glyph name: uni1E52	Contours detected: 2	Expected: 4

	- Glyph name: uni1E53	Contours detected: 2	Expected: 4

	- Glyph name: uni1E57	Contours detected: 1	Expected: 3

	- Glyph name: uni1E5B	Contours detected: 3	Expected: 2

	- Glyph name: uni1E5D	Contours detected: 4	Expected: 3

	- Glyph name: uni1EA2	Contours detected: 2	Expected: 3

	- Glyph name: uni1EA3	Contours detected: 2	Expected: 3

	- Glyph name: uni1EA8	Contours detected: 3	Expected: 4

	- Glyph name: uni1EA9	Contours detected: 3	Expected: 4

	- Glyph name: uni1EB2	Contours detected: 3	Expected: 4

	- Glyph name: uni1EB3	Contours detected: 3	Expected: 4

	- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

	- Glyph name: uni1EBA	Contours detected: 1	Expected: 2

	- Glyph name: uni1EBB	Contours detected: 1	Expected: 3

	- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

	- Glyph name: uni1EBF	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC1	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC2	Contours detected: 2	Expected: 3

	- Glyph name: uni1EC3	Contours detected: 2	Expected: 4

	- Glyph name: uni1EC5	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC7	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC8	Contours detected: 1	Expected: 2

	- Glyph name: uni1EC9	Contours detected: 1	Expected: 2

	- Glyph name: uni1ECE	Contours detected: 2	Expected: 3

	- Glyph name: uni1ECF	Contours detected: 2	Expected: 3

	- Glyph name: uni1ED4	Contours detected: 3	Expected: 4

	- Glyph name: uni1ED5	Contours detected: 3	Expected: 4

	- Glyph name: uni1EDE	Contours detected: 2	Expected: 3 or 4

	- Glyph name: uni1EDF	Contours detected: 2	Expected: 3

	- Glyph name: uni1EE6	Contours detected: 1	Expected: 2

	- Glyph name: uni1EE7	Contours detected: 1	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 1	Expected: 2

	- Glyph name: uni1EED	Contours detected: 1	Expected: 2

	- Glyph name: uni1EF6	Contours detected: 1	Expected: 2

	- Glyph name: uni1EF7	Contours detected: 1	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking head.macStyle value. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/head.html#com.google.fonts/check/mac_style">com.google.fonts/check/mac_style</a>)</summary><div>


* 🔥 **FAIL** head macStyle BOLD bit should be set. [code: bad-BOLD]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 fsSelection value. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/fsselection">com.google.fonts/check/fsselection</a>)</summary><div>


* 🔥 **FAIL** OS/2 fsSelection REGULAR bit should be unset. [code: bad-REGULAR]
* 🔥 **FAIL** OS/2 fsSelection BOLD bit should be set. [code: bad-BOLD]
</div></details><details><summary>🔥 <b>FAIL:</b> Check glyphs do not have duplicate components which have the same x,y coordinates. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/glyf.html#com.google.fonts/check/glyf_non_transformed_duplicate_components">com.google.fonts/check/glyf_non_transformed_duplicate_components</a>)</summary><div>


* 🔥 **FAIL** The following glyphs have duplicate components which have the same x,y coordinates:
	* {'glyph': 'ellipsis', 'component': 'period', 'x': 0, 'y': 0}
	* {'glyph': 'ellipsis', 'component': 'period', 'x': 0, 'y': 0}
	* {'glyph': 'quotedblbase', 'component': 'comma', 'x': 0, 'y': 0}
	* {'glyph': 'quotedblright', 'component': 'quoteright', 'x': 0, 'y': 0} and {'glyph': 'guillemotleft', 'component': 'guilsinglleft', 'x': 0, 'y': 0} [code: found-duplicates]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Check for codepoints not covered by METADATA subsets. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/unreachable_subsetting">com.google.fonts/check/metadata/unreachable_subsetting</a>)</summary><div>


* ⚠ **WARN** The following codepoints supported by the font are not covered by
    any subsets defined in the font's metadata file, and will never
    be served. You can solve this by either manually adding additional
    subset declarations to METADATA.pb, or by editing the glyphset
    definitions.

 * U+02B0 MODIFIER LETTER SMALL H: not included in any glyphset definition
 * U+02B7 MODIFIER LETTER SMALL W: not included in any glyphset definition
 * U+02BE MODIFIER LETTER RIGHT HALF RING: not included in any glyphset definition
 * U+02BF MODIFIER LETTER LEFT HALF RING: not included in any glyphset definition
 * U+02C0 MODIFIER LETTER GLOTTAL STOP: not included in any glyphset definition
 * U+02C7 CARON: try adding one of: canadian-aboriginal, yi, tifinagh
 * U+02CA MODIFIER LETTER ACUTE ACCENT: not included in any glyphset definition
 * U+02CB MODIFIER LETTER GRAVE ACCENT: not included in any glyphset definition
 * U+02D7 MODIFIER LETTER MINUS SIGN: not included in any glyphset definition
 * U+02D8 BREVE: try adding one of: canadian-aboriginal, yi
 * U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi
 * U+02DB OGONEK: try adding one of: canadian-aboriginal, yi
 * U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition
 * U+02EE MODIFIER LETTER DOUBLE APOSTROPHE: not included in any glyphset definition
 * U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, cherokee, coptic, tifinagh
 * U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh
 * U+0307 COMBINING DOT ABOVE: try adding one of: math, canadian-aboriginal, coptic, syriac, malayalam, tifinagh, tai-le, old-permic
 * U+030A COMBINING RING ABOVE: try adding syriac
 * U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee
 * U+030C COMBINING CARON: try adding one of: tai-le, cherokee
 * U+030D COMBINING VERTICAL LINE ABOVE: not included in any glyphset definition
 * U+030F COMBINING DOUBLE GRAVE ACCENT: not included in any glyphset definition
 * U+0310 COMBINING CANDRABINDU: not included in any glyphset definition
 * U+0311 COMBINING INVERTED BREVE: try adding coptic
 * U+0312 COMBINING TURNED COMMA ABOVE: not included in any glyphset definition
 * U+0313 COMBINING COMMA ABOVE: try adding old-permic
 * U+031B COMBINING HORN: not included in any glyphset definition
 * U+0325 COMBINING RING BELOW: try adding syriac
 * U+0326 COMBINING COMMA BELOW: not included in any glyphset definition
 * U+0327 COMBINING CEDILLA: not included in any glyphset definition
 * U+0328 COMBINING OGONEK: not included in any glyphset definition
 * U+032D COMBINING CIRCUMFLEX ACCENT BELOW: try adding syriac
 * U+032F COMBINING INVERTED BREVE BELOW: not included in any glyphset definition
 * U+0330 COMBINING TILDE BELOW: try adding one of: math, cherokee, syriac
 * U+0331 COMBINING MACRON BELOW: try adding one of: cherokee, syriac, gothic, caucasian-albanian, tifinagh
 * U+0332 COMBINING LOW LINE: not included in any glyphset definition
 * U+0334 COMBINING TILDE OVERLAY: not included in any glyphset definition
 * U+0358 COMBINING DOT ABOVE RIGHT: try adding osage
 * U+1D58 MODIFIER LETTER SMALL U: not included in any glyphset definition
 * U+1D5B MODIFIER LETTER SMALL V: not included in any glyphset definition
 * U+1D7D LATIN SMALL LETTER P WITH STROKE: not included in any glyphset definition
 * U+1DBB MODIFIER LETTER SMALL Z: not included in any glyphset definition
 * U+1DC4 COMBINING MACRON-ACUTE: not included in any glyphset definition
 * U+1DC5 COMBINING GRAVE-MACRON: not included in any glyphset definition
 * U+1DC6 COMBINING MACRON-GRAVE: not included in any glyphset definition
 * U+1DC7 COMBINING ACUTE-MACRON: not included in any glyphset definition
 * U+1DCA COMBINING LATIN SMALL LETTER R BELOW: not included in any glyphset definition
 * U+207F SUPERSCRIPT LATIN SMALL LETTER N: not included in any glyphset definition
 * U+AB53 LATIN SMALL LETTER CHI: not included in any glyphset definition

Or you can add the above codepoints to one of the subsets supported by the font: `latin`, `latin-ext`, `vietnamese` [code: unreachable-subsetting]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- J.ss01

	- N.ss02

	- R.ss01

	- U.ss01

	- V.ss01

	- X.ss01

	- Y.ss01

	- Y.ss02

	- comma.ss01

	- four.ss01

	- four.ss02

	- i.loclTRK

	- one.ss01

	- periodcentered.loclCAT

	- periodcentered.loclCAT.case

	- pixel

	- uni03000304

	- uni03010304

	- uni03040300

	- zero.ss01
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** OS/2 sTypoLineGap is not equal to 0. [code: OS/2]
</div></details><details><summary>⚠ <b>WARN:</b> Checking post.italicAngle value. (derived from com.google.fonts/check/italic_angle) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/post.html#com.google.fonts/check/italic_angle">com.google.fonts/check/italic_angle</a>)</summary><div>


* ⚠ **WARN** The following glyphs were present but did not contain any outlines: bar [code: empty-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* B (U+0042): B<<598.0,573.0>-<581.0,547.0>-<533.0,544.0>>/B<<533.0,544.0>-<601.0,544.0>-<629.0,501.5>> = 3.576334374997269

	* Bmacronbelow (U+1E06): B<<598.0,573.0>-<581.0,547.0>-<533.0,544.0>>/B<<533.0,544.0>-<601.0,544.0>-<629.0,501.5>> = 3.576334374997269

	* b (U+0062): B<<598.0,573.0>-<581.0,547.0>-<533.0,544.0>>/B<<533.0,544.0>-<601.0,544.0>-<629.0,501.5>> = 3.576334374997269

	* bmacronbelow (U+1E07): B<<598.0,573.0>-<581.0,547.0>-<533.0,544.0>>/B<<533.0,544.0>-<601.0,544.0>-<629.0,501.5>> = 3.576334374997269

	* three (U+0033): B<<466.5,544.5>-<441.0,533.0>-<414.0,531.0>>/B<<414.0,531.0>-<433.0,530.0>-<459.0,523.5>> = 7.249182303242161

	* uni1E02 (U+1E02): B<<598.0,573.0>-<581.0,547.0>-<533.0,544.0>>/B<<533.0,544.0>-<601.0,544.0>-<629.0,501.5>> = 3.576334374997269

	* uni1E03 (U+1E03): B<<598.0,573.0>-<581.0,547.0>-<533.0,544.0>>/B<<533.0,544.0>-<601.0,544.0>-<629.0,501.5>> = 3.576334374997269

	* uni1E04 (U+1E04): B<<598.0,573.0>-<581.0,547.0>-<533.0,544.0>>/B<<533.0,544.0>-<601.0,544.0>-<629.0,501.5>> = 3.576334374997269

	* uni1E05 (U+1E05): B<<598.0,573.0>-<581.0,547.0>-<533.0,544.0>>/B<<533.0,544.0>-<601.0,544.0>-<629.0,501.5>> = 3.576334374997269 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* A (U+0041): L<<305.0,434.0>--<303.0,0.0>>

	* Aacute (U+00C1): L<<305.0,434.0>--<303.0,0.0>>

	* Abreve (U+0102): L<<305.0,434.0>--<303.0,0.0>>

	* Acircumflex (U+00C2): L<<305.0,434.0>--<303.0,0.0>>

	* Adieresis (U+00C4): L<<305.0,434.0>--<303.0,0.0>>

	* Agrave (U+00C0): L<<305.0,434.0>--<303.0,0.0>>

	* Aogonek (U+0104): L<<305.0,434.0>--<303.0,0.0>>

	* Aring (U+00C5): L<<305.0,434.0>--<303.0,0.0>>

	* Atilde (U+00C3): L<<305.0,434.0>--<303.0,0.0>>

	* B (U+0042): L<<400.0,512.0>--<273.0,513.0>>

	* B (U+0042): L<<472.0,1.0>--<46.0,0.0>>

	* Bmacronbelow (U+1E06): L<<400.0,512.0>--<273.0,513.0>>

	* Bmacronbelow (U+1E06): L<<472.0,1.0>--<46.0,0.0>>

	* D (U+0044): L<<47.0,0.0>--<46.0,437.0>>

	* Dcaron (U+010E): L<<47.0,0.0>--<46.0,437.0>>

	* Dmacronbelow (U+1E0E): L<<47.0,0.0>--<46.0,437.0>>

	* E (U+0045): L<<549.0,497.0>--<552.0,0.0>>

	* Eacute (U+00C9): L<<549.0,497.0>--<552.0,0.0>>

	* Ecaron (U+011A): L<<549.0,497.0>--<552.0,0.0>>

	* Ecircumflex (U+00CA): L<<549.0,497.0>--<552.0,0.0>>

	* Edieresis (U+00CB): L<<549.0,497.0>--<552.0,0.0>>

	* Edotaccent (U+0116): L<<549.0,497.0>--<552.0,0.0>>

	* Egrave (U+00C8): L<<549.0,497.0>--<552.0,0.0>>

	* Eogonek (U+0118): L<<549.0,497.0>--<552.0,0.0>>

	* F (U+0046): L<<414.0,433.0>--<417.0,0.0>>

	* G (U+0047): L<<441.0,497.0>--<629.0,498.0>>

	* Gbreve (U+011E): L<<441.0,497.0>--<629.0,498.0>>

	* Gcaron (U+01E6): L<<441.0,497.0>--<629.0,498.0>>

	* Gdotaccent (U+0120): L<<441.0,497.0>--<629.0,498.0>>

	* P (U+0050): L<<431.0,490.0>--<273.0,489.0>>

	* R (U+0052): L<<396.0,185.0>--<395.0,434.0>>

	* Racute (U+0154): L<<396.0,185.0>--<395.0,434.0>>

	* Rcaron (U+0158): L<<396.0,185.0>--<395.0,434.0>>

	* Rmacronbelow (U+1E5E): L<<396.0,185.0>--<395.0,434.0>>

	* T (U+0054): L<<481.0,434.0>--<482.0,-2.0>>

	* T (U+0054): L<<482.0,-2.0>--<87.0,0.0>>

	* Tcaron (U+0164): L<<481.0,434.0>--<482.0,-2.0>>

	* Tcaron (U+0164): L<<482.0,-2.0>--<87.0,0.0>>

	* Tmacronbelow (U+1E6E): L<<481.0,434.0>--<482.0,-2.0>>

	* Tmacronbelow (U+1E6E): L<<482.0,-2.0>--<87.0,0.0>>

	* Z (U+005A): L<<214.0,439.0>--<399.0,440.0>>

	* Zacute (U+0179): L<<214.0,439.0>--<399.0,440.0>>

	* Zcaron (U+017D): L<<214.0,439.0>--<399.0,440.0>>

	* Zdotaccent (U+017B): L<<214.0,439.0>--<399.0,440.0>>

	* Zmacronbelow (U+1E94): L<<214.0,439.0>--<399.0,440.0>>

	* a (U+0061): L<<305.0,434.0>--<303.0,0.0>>

	* aacute (U+00E1): L<<305.0,434.0>--<303.0,0.0>>

	* abreve (U+0103): L<<305.0,434.0>--<303.0,0.0>>

	* acircumflex (U+00E2): L<<305.0,434.0>--<303.0,0.0>>

	* adieresis (U+00E4): L<<305.0,434.0>--<303.0,0.0>>

	* agrave (U+00E0): L<<305.0,434.0>--<303.0,0.0>>

	* aogonek (U+0105): L<<305.0,434.0>--<303.0,0.0>>

	* aring (U+00E5): L<<305.0,434.0>--<303.0,0.0>>

	* atilde (U+00E3): L<<305.0,434.0>--<303.0,0.0>>

	* b (U+0062): L<<400.0,512.0>--<273.0,513.0>>

	* b (U+0062): L<<472.0,1.0>--<46.0,0.0>>

	* bmacronbelow (U+1E07): L<<400.0,512.0>--<273.0,513.0>>

	* bmacronbelow (U+1E07): L<<472.0,1.0>--<46.0,0.0>>

	* bracketleft (U+005B): L<<152.0,735.0>--<150.0,20.0>>

	* bracketleft (U+005B): L<<24.0,-76.0>--<27.0,816.0>>

	* bracketleft (U+005B): L<<384.0,-77.0>--<24.0,-76.0>>

	* bracketright (U+005D): L<<24.0,820.0>--<384.0,819.0>>

	* bracketright (U+005D): L<<256.0,8.0>--<258.0,723.0>>

	* bracketright (U+005D): L<<384.0,819.0>--<381.0,-73.0>>

	* d (U+0064): L<<47.0,0.0>--<46.0,437.0>>

	* dcaron (U+010F): L<<47.0,0.0>--<46.0,437.0>>

	* dmacronbelow (U+1E0F): L<<47.0,0.0>--<46.0,437.0>>

	* e (U+0065): L<<549.0,497.0>--<552.0,0.0>>

	* eacute (U+00E9): L<<549.0,497.0>--<552.0,0.0>>

	* ecaron (U+011B): L<<549.0,497.0>--<552.0,0.0>>

	* ecircumflex (U+00EA): L<<549.0,497.0>--<552.0,0.0>>

	* edieresis (U+00EB): L<<549.0,497.0>--<552.0,0.0>>

	* edotaccent (U+0117): L<<549.0,497.0>--<552.0,0.0>>

	* egrave (U+00E8): L<<549.0,497.0>--<552.0,0.0>>

	* eogonek (U+0119): L<<549.0,497.0>--<552.0,0.0>>

	* f (U+0066): L<<414.0,433.0>--<417.0,0.0>>

	* g (U+0067): L<<441.0,497.0>--<629.0,498.0>>

	* gbreve (U+011F): L<<441.0,497.0>--<629.0,498.0>>

	* gcaron (U+01E7): L<<441.0,497.0>--<629.0,498.0>>

	* gdotaccent (U+0121): L<<441.0,497.0>--<629.0,498.0>>

	* macron (U+00AF): L<<25.0,678.0>--<325.0,679.0>>

	* ordfeminine (U+00AA): L<<305.0,434.0>--<303.0,0.0>>

	* r (U+0072): L<<396.0,185.0>--<395.0,434.0>>

	* racute (U+0155): L<<396.0,185.0>--<395.0,434.0>>

	* rcaron (U+0159): L<<396.0,185.0>--<395.0,434.0>>

	* rmacronbelow (U+1E5F): L<<396.0,185.0>--<395.0,434.0>>

	* t (U+0074): L<<481.0,434.0>--<482.0,-2.0>>

	* t (U+0074): L<<482.0,-2.0>--<87.0,0.0>>

	* tcaron (U+0165): L<<481.0,434.0>--<482.0,-2.0>>

	* tcaron (U+0165): L<<482.0,-2.0>--<87.0,0.0>>

	* tmacronbelow (U+1E6F): L<<481.0,434.0>--<482.0,-2.0>>

	* tmacronbelow (U+1E6F): L<<482.0,-2.0>--<87.0,0.0>>

	* trademark (U+2122): L<<481.0,434.0>--<482.0,-2.0>>

	* trademark (U+2122): L<<482.0,-2.0>--<87.0,0.0>>

	* two (U+0032): L<<541.0,-1.0>--<24.0,0.0>>

	* two (U+0032): L<<543.0,498.0>--<541.0,-1.0>>

	* uni0122 (U+0122): L<<441.0,497.0>--<629.0,498.0>>

	* uni0123 (U+0123): L<<441.0,497.0>--<629.0,498.0>>

	* uni0156 (U+0156): L<<396.0,185.0>--<395.0,434.0>>

	* uni0157 (U+0157): L<<396.0,185.0>--<395.0,434.0>>

	* uni01CD (U+01CD): L<<305.0,434.0>--<303.0,0.0>>

	* uni01CE (U+01CE): L<<305.0,434.0>--<303.0,0.0>>

	* uni01D5 (U+01D5): L<<-149.0,77.0>--<151.0,78.0>>

	* uni01D6 (U+01D6): L<<47.0,77.0>--<347.0,78.0>>

	* uni01DE (U+01DE): L<<305.0,434.0>--<303.0,0.0>>

	* uni01DE (U+01DE): L<<74.0,77.0>--<374.0,78.0>>

	* uni01DF (U+01DF): L<<305.0,434.0>--<303.0,0.0>>

	* uni01DF (U+01DF): L<<84.0,77.0>--<384.0,78.0>>

	* uni01E0 (U+01E0): L<<305.0,434.0>--<303.0,0.0>>

	* uni01E0 (U+01E0): L<<75.0,77.0>--<375.0,78.0>>

	* uni01E1 (U+01E1): L<<305.0,434.0>--<303.0,0.0>>

	* uni01E1 (U+01E1): L<<85.0,77.0>--<385.0,78.0>>

	* uni01EC (U+01EC): L<<190.0,793.0>--<490.0,794.0>>

	* uni01ED (U+01ED): L<<208.0,793.0>--<508.0,794.0>>

	* uni01F4 (U+01F4): L<<441.0,497.0>--<629.0,498.0>>

	* uni01F5 (U+01F5): L<<441.0,497.0>--<629.0,498.0>>

	* uni0200 (U+0200): L<<305.0,434.0>--<303.0,0.0>>

	* uni0201 (U+0201): L<<305.0,434.0>--<303.0,0.0>>

	* uni0202 (U+0202): L<<305.0,434.0>--<303.0,0.0>>

	* uni0203 (U+0203): L<<305.0,434.0>--<303.0,0.0>>

	* uni0204 (U+0204): L<<549.0,497.0>--<552.0,0.0>>

	* uni0205 (U+0205): L<<549.0,497.0>--<552.0,0.0>>

	* uni0206 (U+0206): L<<549.0,497.0>--<552.0,0.0>>

	* uni0207 (U+0207): L<<549.0,497.0>--<552.0,0.0>>

	* uni0210 (U+0210): L<<396.0,185.0>--<395.0,434.0>>

	* uni0211 (U+0211): L<<396.0,185.0>--<395.0,434.0>>

	* uni0212 (U+0212): L<<396.0,185.0>--<395.0,434.0>>

	* uni0213 (U+0213): L<<396.0,185.0>--<395.0,434.0>>

	* uni021A (U+021A): L<<481.0,434.0>--<482.0,-2.0>>

	* uni021A (U+021A): L<<482.0,-2.0>--<87.0,0.0>>

	* uni021B (U+021B): L<<481.0,434.0>--<482.0,-2.0>>

	* uni021B (U+021B): L<<482.0,-2.0>--<87.0,0.0>>

	* uni0226 (U+0226): L<<305.0,434.0>--<303.0,0.0>>

	* uni0227 (U+0227): L<<305.0,434.0>--<303.0,0.0>>

	* uni0228 (U+0228): L<<549.0,497.0>--<552.0,0.0>>

	* uni0229 (U+0229): L<<549.0,497.0>--<552.0,0.0>>

	* uni022A (U+022A): L<<68.0,77.0>--<368.0,78.0>>

	* uni022B (U+022B): L<<86.0,77.0>--<386.0,78.0>>

	* uni022C (U+022C): L<<193.0,935.0>--<493.0,936.0>>

	* uni022D (U+022D): L<<211.0,935.0>--<511.0,936.0>>

	* uni0230 (U+0230): L<<69.0,77.0>--<369.0,78.0>>

	* uni0231 (U+0231): L<<87.0,77.0>--<387.0,78.0>>

	* uni0232 (U+0232): L<<25.0,678.0>--<325.0,679.0>>

	* uni0233 (U+0233): L<<182.0,793.0>--<482.0,794.0>>

	* uni0304 (U+0304): L<<25.0,678.0>--<325.0,679.0>>

	* uni1DBB (U+1DBB): L<<214.0,439.0>--<399.0,440.0>>

	* uni1E00 (U+1E00): L<<305.0,434.0>--<303.0,0.0>>

	* uni1E01 (U+1E01): L<<305.0,434.0>--<303.0,0.0>>

	* uni1E02 (U+1E02): L<<400.0,512.0>--<273.0,513.0>>

	* uni1E02 (U+1E02): L<<472.0,1.0>--<46.0,0.0>>

	* uni1E03 (U+1E03): L<<400.0,512.0>--<273.0,513.0>>

	* uni1E03 (U+1E03): L<<472.0,1.0>--<46.0,0.0>>

	* uni1E04 (U+1E04): L<<400.0,512.0>--<273.0,513.0>>

	* uni1E04 (U+1E04): L<<472.0,1.0>--<46.0,0.0>>

	* uni1E05 (U+1E05): L<<400.0,512.0>--<273.0,513.0>>

	* uni1E05 (U+1E05): L<<472.0,1.0>--<46.0,0.0>>

	* uni1E0A (U+1E0A): L<<47.0,0.0>--<46.0,437.0>>

	* uni1E0B (U+1E0B): L<<47.0,0.0>--<46.0,437.0>>

	* uni1E0C (U+1E0C): L<<47.0,0.0>--<46.0,437.0>>

	* uni1E0D (U+1E0D): L<<47.0,0.0>--<46.0,437.0>>

	* uni1E10 (U+1E10): L<<47.0,0.0>--<46.0,437.0>>

	* uni1E11 (U+1E11): L<<47.0,0.0>--<46.0,437.0>>

	* uni1E12 (U+1E12): L<<47.0,0.0>--<46.0,437.0>>

	* uni1E13 (U+1E13): L<<47.0,0.0>--<46.0,437.0>>

	* uni1E14 (U+1E14): L<<357.0,494.0>--<657.0,495.0>>

	* uni1E14 (U+1E14): L<<549.0,497.0>--<552.0,0.0>>

	* uni1E15 (U+1E15): L<<346.0,494.0>--<646.0,495.0>>

	* uni1E15 (U+1E15): L<<549.0,497.0>--<552.0,0.0>>

	* uni1E16 (U+1E16): L<<549.0,439.0>--<552.0,0.0>>

	* uni1E17 (U+1E17): L<<549.0,439.0>--<552.0,0.0>>

	* uni1E18 (U+1E18): L<<549.0,497.0>--<552.0,0.0>>

	* uni1E19 (U+1E19): L<<549.0,497.0>--<552.0,0.0>>

	* uni1E1A (U+1E1A): L<<549.0,497.0>--<552.0,0.0>>

	* uni1E1B (U+1E1B): L<<549.0,497.0>--<552.0,0.0>>

	* uni1E1C (U+1E1C): L<<549.0,497.0>--<552.0,0.0>>

	* uni1E1D (U+1E1D): L<<549.0,497.0>--<552.0,0.0>>

	* uni1E1E (U+1E1E): L<<414.0,433.0>--<417.0,0.0>>

	* uni1E1F (U+1E1F): L<<414.0,433.0>--<417.0,0.0>>

	* uni1E20 (U+1E20): L<<184.0,793.0>--<484.0,794.0>>

	* uni1E20 (U+1E20): L<<441.0,497.0>--<629.0,498.0>>

	* uni1E21 (U+1E21): L<<151.0,977.0>--<451.0,978.0>>

	* uni1E21 (U+1E21): L<<441.0,497.0>--<629.0,498.0>>

	* uni1E38 (U+1E38): L<<87.0,77.0>--<387.0,78.0>>

	* uni1E39 (U+1E39): L<<73.0,261.0>--<373.0,262.0>>

	* uni1E50 (U+1E50): L<<364.0,494.0>--<664.0,495.0>>

	* uni1E51 (U+1E51): L<<382.0,494.0>--<682.0,495.0>>

	* uni1E54 (U+1E54): L<<431.0,490.0>--<273.0,489.0>>

	* uni1E56 (U+1E56): L<<431.0,490.0>--<273.0,489.0>>

	* uni1E58 (U+1E58): L<<396.0,185.0>--<395.0,434.0>>

	* uni1E59 (U+1E59): L<<396.0,185.0>--<395.0,434.0>>

	* uni1E5A (U+1E5A): L<<396.0,185.0>--<395.0,434.0>>

	* uni1E5B (U+1E5B): L<<396.0,185.0>--<395.0,434.0>>

	* uni1E5C (U+1E5C): L<<-153.0,-860.0>--<147.0,-859.0>>

	* uni1E5C (U+1E5C): L<<396.0,185.0>--<395.0,434.0>>

	* uni1E5D (U+1E5D): L<<30.0,77.0>--<330.0,78.0>>

	* uni1E5D (U+1E5D): L<<396.0,185.0>--<395.0,434.0>>

	* uni1E6A (U+1E6A): L<<481.0,434.0>--<482.0,-2.0>>

	* uni1E6A (U+1E6A): L<<482.0,-2.0>--<87.0,0.0>>

	* uni1E6B (U+1E6B): L<<481.0,434.0>--<482.0,-2.0>>

	* uni1E6B (U+1E6B): L<<482.0,-2.0>--<87.0,0.0>>

	* uni1E6C (U+1E6C): L<<481.0,434.0>--<482.0,-2.0>>

	* uni1E6C (U+1E6C): L<<482.0,-2.0>--<87.0,0.0>>

	* uni1E6D (U+1E6D): L<<481.0,434.0>--<482.0,-2.0>>

	* uni1E6D (U+1E6D): L<<482.0,-2.0>--<87.0,0.0>>

	* uni1E70 (U+1E70): L<<481.0,434.0>--<482.0,-2.0>>

	* uni1E70 (U+1E70): L<<482.0,-2.0>--<87.0,0.0>>

	* uni1E71 (U+1E71): L<<481.0,434.0>--<482.0,-2.0>>

	* uni1E71 (U+1E71): L<<482.0,-2.0>--<87.0,0.0>>

	* uni1E7A (U+1E7A): L<<25.0,678.0>--<325.0,679.0>>

	* uni1E7B (U+1E7B): L<<169.0,793.0>--<469.0,794.0>>

	* uni1E90 (U+1E90): L<<214.0,439.0>--<399.0,440.0>>

	* uni1E91 (U+1E91): L<<214.0,439.0>--<399.0,440.0>>

	* uni1E92 (U+1E92): L<<214.0,439.0>--<399.0,440.0>>

	* uni1E93 (U+1E93): L<<214.0,439.0>--<399.0,440.0>>

	* uni1EA0 (U+1EA0): L<<305.0,434.0>--<303.0,0.0>>

	* uni1EA1 (U+1EA1): L<<305.0,434.0>--<303.0,0.0>>

	* uni1EA2 (U+1EA2): L<<305.0,434.0>--<303.0,0.0>>

	* uni1EA3 (U+1EA3): L<<305.0,434.0>--<303.0,0.0>>

	* uni1EA4 (U+1EA4): L<<305.0,434.0>--<303.0,0.0>>

	* uni1EA5 (U+1EA5): L<<305.0,434.0>--<303.0,0.0>>

	* uni1EA6 (U+1EA6): L<<305.0,434.0>--<303.0,0.0>>

	* uni1EA7 (U+1EA7): L<<305.0,434.0>--<303.0,0.0>>

	* uni1EA8 (U+1EA8): L<<305.0,434.0>--<303.0,0.0>>

	* uni1EA9 (U+1EA9): L<<305.0,434.0>--<303.0,0.0>>

	* uni1EAA (U+1EAA): L<<305.0,434.0>--<303.0,0.0>>

	* uni1EAB (U+1EAB): L<<305.0,434.0>--<303.0,0.0>>

	* uni1EAC (U+1EAC): L<<305.0,434.0>--<303.0,0.0>>

	* uni1EAD (U+1EAD): L<<305.0,434.0>--<303.0,0.0>>

	* uni1EAE (U+1EAE): L<<305.0,434.0>--<303.0,0.0>>

	* uni1EAF (U+1EAF): L<<305.0,434.0>--<303.0,0.0>>

	* uni1EB0 (U+1EB0): L<<305.0,434.0>--<303.0,0.0>>

	* uni1EB1 (U+1EB1): L<<305.0,434.0>--<303.0,0.0>>

	* uni1EB2 (U+1EB2): L<<305.0,434.0>--<303.0,0.0>>

	* uni1EB3 (U+1EB3): L<<305.0,434.0>--<303.0,0.0>>

	* uni1EB4 (U+1EB4): L<<305.0,434.0>--<303.0,0.0>>

	* uni1EB5 (U+1EB5): L<<305.0,434.0>--<303.0,0.0>>

	* uni1EB6 (U+1EB6): L<<305.0,434.0>--<303.0,0.0>>

	* uni1EB7 (U+1EB7): L<<305.0,434.0>--<303.0,0.0>>

	* uni1EB8 (U+1EB8): L<<549.0,497.0>--<552.0,0.0>>

	* uni1EB9 (U+1EB9): L<<549.0,497.0>--<552.0,0.0>>

	* uni1EBA (U+1EBA): L<<549.0,497.0>--<552.0,0.0>>

	* uni1EBB (U+1EBB): L<<549.0,497.0>--<552.0,0.0>>

	* uni1EBC (U+1EBC): L<<549.0,497.0>--<552.0,0.0>>

	* uni1EBD (U+1EBD): L<<549.0,497.0>--<552.0,0.0>>

	* uni1EBE (U+1EBE): L<<549.0,497.0>--<552.0,0.0>>

	* uni1EBF (U+1EBF): L<<549.0,497.0>--<552.0,0.0>>

	* uni1EC0 (U+1EC0): L<<549.0,497.0>--<552.0,0.0>>

	* uni1EC1 (U+1EC1): L<<549.0,497.0>--<552.0,0.0>>

	* uni1EC2 (U+1EC2): L<<549.0,497.0>--<552.0,0.0>>

	* uni1EC3 (U+1EC3): L<<549.0,497.0>--<552.0,0.0>>

	* uni1EC4 (U+1EC4): L<<549.0,497.0>--<552.0,0.0>>

	* uni1EC5 (U+1EC5): L<<549.0,497.0>--<552.0,0.0>>

	* uni1EC6 (U+1EC6): L<<549.0,497.0>--<552.0,0.0>>

	* uni1EC7 (U+1EC7): L<<549.0,497.0>--<552.0,0.0>>

	* z (U+007A): L<<214.0,439.0>--<399.0,440.0>>

	* zacute (U+017A): L<<214.0,439.0>--<399.0,440.0>>

	* zcaron (U+017E): L<<214.0,439.0>--<399.0,440.0>>

	* zdotaccent (U+017C): L<<214.0,439.0>--<399.0,440.0>>

	* zmacronbelow (U+1E95): L<<214.0,439.0>--<399.0,440.0>> [code: found-semi-vertical]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* ⚠ **WARN** The dot of soft dotted characters used in orthographies _must_ disappear in the following strings: i̊ i̋ i̍ i̐ i̓ i᷆ i᷇ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ ɨ̀ ɨ́ ɨ̂ ɨ̃ ɨ̄ ɨ̈ ɨ̋ ɨ̌ ɨ̏ ɨ̧̀ ɨ̧́ ɨ̧̂ ɨ̧̌ ɨ̱̀ ɨ̱́ ɨ̱̈ ḭ̀ ḭ́ ḭ̄ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters _should_ disappear in other cases, for example: ī ĭ i̇ i̒ i᷄ i᷅ ī̛ ĭ̛ i̛̇ i̛̊ i̛̋ i̛̍ i̛̐ i̛̒ i̛̓ i̛᷄ i̛᷅ i̛᷆ i̛᷇ ī̥

Your font fully covers the following languages that require the soft-dotted feature: Lithuanian (Latn, 2,357,094 speakers), Dutch (Latn, 31,709,104 speakers), Navajo (Latn, 166,319 speakers), Avokaya (Latn, 100,000 speakers). 

Your font does *not* cover the following languages that require the soft-dotted feature: Koonzime (Latn, 40,000 speakers), Belarusian (Cyrl, 10,064,517 speakers), Kom (Latn, 360,685 speakers), Igbo (Latn, 27,823,640 speakers), Lugbara (Latn, 2,200,000 speakers), Dan (Latn, 1,099,244 speakers), Basaa (Latn, 332,940 speakers), Nateni (Latn, 100,000 speakers), Aghem (Latn, 38,843 speakers), Ejagham (Latn, 120,000 speakers), Ebira (Latn, 2,200,000 speakers), Ma’di (Latn, 584,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers). [code: soft-dotted]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 12 | 11 | 123 | 7 | 101 | 0 |
| 0% | 5% | 4% | 48% | 3% | 40% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
