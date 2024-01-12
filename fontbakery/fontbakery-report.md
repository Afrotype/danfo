## FontBakery report

fontbakery version: 0.10.8

<details><summary><b>[21] Danfo-Regular50.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 fsType does not impose restrictions. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fstype">com.google.fonts/check/fstype</a>)</summary><div>


* 🔥 **FAIL** In this font fsType is set to 8 meaning that:
The font may be embedded but must only be installed temporarily on other systems.

No such DRM restrictions can be enabled on the Google Fonts collection, so the fsType field must be set to zero (Installable Embedding) instead. [code: drm]
</div></details><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0060 (GRAVE ACCENT)


	- 0x00A0 (NO-BREAK SPACE)


	- 0x00A8 (DIAERESIS)


	- 0x00AA (FEMININE ORDINAL INDICATOR)


	- 0x00AF (MACRON)


	- 0x00B4 (ACUTE ACCENT)


	- 0x00B8 (CEDILLA)


	- 0x00BA (MASCULINE ORDINAL INDICATOR)


	- 0x02C6 (MODIFIER LETTER CIRCUMFLEX ACCENT)


	- 0x02C7 (CARON)


	- 0x02D8 (BREVE)


	- 0x02D9 (DOT ABOVE)


	- 0x02DA (RING ABOVE)


	- 0x02DB (OGONEK)


	- 0x02DC (SMALL TILDE)


	- 0x02DD (DOUBLE ACUTE ACCENT)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font names are correct (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_names">com.google.fonts/check/font_names</a>)</summary><div>


* 🔥 **FAIL** Font names are incorrect:

| nameID | current | expected |
| :--- | :--- | :--- |
| Family Name | Danfo 50 | Danfo 50 |
| Subfamily Name | Regular | Regular |
| Full Name | **Danfo Regular 50** | **Danfo 50 Regular** |
| Postscript Name | **Danfo-Regular50** | **Danfo50-Regular** |
| Typographic Family Name | **Danfo** | **N/A** |
| Typographic Subfamily Name | **Regular 50** | **N/A** | [code: bad-names]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.sTypoLineGap is "200" it should be 0 [code: bad-OS/2.sTypoLineGap]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 219, but got 100 instead [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (900) and hhea ascent (1100) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Font contains glyphs for whitespace characters? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphs">com.google.fonts/check/whitespace_glyphs</a>)</summary><div>


* 🔥 **FAIL** Whitespace glyph missing for codepoint 0x00A0. [code: missing-whitespace-glyph-0x00A0]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* 🔥 **FAIL** The following glyphs have no contours even though they were expected to have some:

	- Glyph name: onequarter	Expected: 3 or 4

	- Glyph name: onehalf	Expected: 3

	- Glyph name: threequarters	Expected: 3 or 4

	- Glyph name: uni0312	Expected: 1

	- Glyph name: uni0334	Expected: 1

	- Glyph name: fraction	Expected: 1

	- Glyph name: uni2153	Expected: 3

	- Glyph name: uni2154	Expected: 1 or 3

	- Glyph name: fraction	Expected: 1

	- Glyph name: onehalf	Expected: 3

	- Glyph name: onequarter	Expected: 3 or 4

	- Glyph name: threequarters	Expected: 3 or 4

	- Glyph name: uni0312	Expected: 1
 [code: no-contour]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: B	Contours detected: 4	Expected: 2 or 3

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 3	Expected: 2

	- Glyph name: G	Contours detected: 2	Expected: 1

	- Glyph name: J	Contours detected: 3	Expected: 1

	- Glyph name: O	Contours detected: 4	Expected: 2

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: S	Contours detected: 3	Expected: 1

	- Glyph name: U	Contours detected: 2	Expected: 1

	- Glyph name: W	Contours detected: 5	Expected: 1 or 2

	- Glyph name: Y	Contours detected: 2	Expected: 1

	- Glyph name: b	Contours detected: 4	Expected: 2

	- Glyph name: c	Contours detected: 3	Expected: 1

	- Glyph name: d	Contours detected: 3	Expected: 2

	- Glyph name: e	Contours detected: 1	Expected: 2

	- Glyph name: i	Contours detected: 1	Expected: 2

	- Glyph name: j	Contours detected: 3	Expected: 2

	- Glyph name: o	Contours detected: 4	Expected: 2

	- Glyph name: q	Contours detected: 3	Expected: 2

	- Glyph name: r	Contours detected: 2	Expected: 1

	- Glyph name: s	Contours detected: 3	Expected: 1

	- Glyph name: u	Contours detected: 2	Expected: 1

	- Glyph name: w	Contours detected: 5	Expected: 1

	- Glyph name: y	Contours detected: 2	Expected: 1

	- Glyph name: Ccedilla	Contours detected: 4	Expected: 1 or 2

	- Glyph name: Ograve	Contours detected: 5	Expected: 3

	- Glyph name: Oacute	Contours detected: 5	Expected: 3

	- Glyph name: Ocircumflex	Contours detected: 5	Expected: 3

	- Glyph name: Otilde	Contours detected: 5	Expected: 3

	- Glyph name: Odieresis	Contours detected: 6	Expected: 4

	- Glyph name: Oslash	Contours detected: 4	Expected: 2 or 3

	- Glyph name: Ugrave	Contours detected: 3	Expected: 2

	- Glyph name: Uacute	Contours detected: 3	Expected: 2

	- Glyph name: Ucircumflex	Contours detected: 3	Expected: 2

	- Glyph name: Udieresis	Contours detected: 4	Expected: 3

	- Glyph name: Yacute	Contours detected: 3	Expected: 2

	- Glyph name: ae	Contours detected: 2	Expected: 3

	- Glyph name: ccedilla	Contours detected: 4	Expected: 1 or 2

	- Glyph name: egrave	Contours detected: 2	Expected: 3

	- Glyph name: eacute	Contours detected: 2	Expected: 3

	- Glyph name: edieresis	Contours detected: 3	Expected: 4

	- Glyph name: ograve	Contours detected: 5	Expected: 3

	- Glyph name: oacute	Contours detected: 5	Expected: 3

	- Glyph name: ocircumflex	Contours detected: 5	Expected: 3

	- Glyph name: otilde	Contours detected: 5	Expected: 3

	- Glyph name: odieresis	Contours detected: 6	Expected: 4

	- Glyph name: oslash	Contours detected: 4	Expected: 3

	- Glyph name: ugrave	Contours detected: 3	Expected: 2

	- Glyph name: uacute	Contours detected: 3	Expected: 2

	- Glyph name: ucircumflex	Contours detected: 3	Expected: 2

	- Glyph name: udieresis	Contours detected: 4	Expected: 3

	- Glyph name: yacute	Contours detected: 3	Expected: 2

	- Glyph name: ydieresis	Contours detected: 4	Expected: 3

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Cacute	Contours detected: 4	Expected: 2

	- Glyph name: cacute	Contours detected: 4	Expected: 2

	- Glyph name: Cdotaccent	Contours detected: 4	Expected: 2

	- Glyph name: cdotaccent	Contours detected: 4	Expected: 2

	- Glyph name: Ccaron	Contours detected: 4	Expected: 2

	- Glyph name: ccaron	Contours detected: 4	Expected: 2

	- Glyph name: Dcaron	Contours detected: 4	Expected: 3

	- Glyph name: dcaron	Contours detected: 4	Expected: 3

	- Glyph name: emacron	Contours detected: 2	Expected: 3

	- Glyph name: edotaccent	Contours detected: 2	Expected: 3

	- Glyph name: ecaron	Contours detected: 2	Expected: 3

	- Glyph name: Gbreve	Contours detected: 3	Expected: 2

	- Glyph name: Gdotaccent	Contours detected: 3	Expected: 2

	- Glyph name: uni0122	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: IJ	Contours detected: 4	Expected: 1 or 2

	- Glyph name: Jcircumflex	Contours detected: 4	Expected: 2

	- Glyph name: Omacron	Contours detected: 5	Expected: 3

	- Glyph name: omacron	Contours detected: 5	Expected: 3

	- Glyph name: Ohungarumlaut	Contours detected: 6	Expected: 4

	- Glyph name: ohungarumlaut	Contours detected: 6	Expected: 4

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: racute	Contours detected: 3	Expected: 2

	- Glyph name: uni0157	Contours detected: 3	Expected: 2

	- Glyph name: rcaron	Contours detected: 3	Expected: 2

	- Glyph name: Sacute	Contours detected: 4	Expected: 2

	- Glyph name: sacute	Contours detected: 4	Expected: 2

	- Glyph name: Scedilla	Contours detected: 4	Expected: 1 or 2

	- Glyph name: scedilla	Contours detected: 4	Expected: 1 or 2

	- Glyph name: Scaron	Contours detected: 4	Expected: 2

	- Glyph name: scaron	Contours detected: 4	Expected: 2

	- Glyph name: Utilde	Contours detected: 3	Expected: 2

	- Glyph name: utilde	Contours detected: 3	Expected: 2

	- Glyph name: Umacron	Contours detected: 3	Expected: 2

	- Glyph name: umacron	Contours detected: 3	Expected: 2

	- Glyph name: Ubreve	Contours detected: 3	Expected: 2

	- Glyph name: ubreve	Contours detected: 3	Expected: 2

	- Glyph name: Uring	Contours detected: 4	Expected: 3

	- Glyph name: uring	Contours detected: 4	Expected: 3

	- Glyph name: Uhungarumlaut	Contours detected: 4	Expected: 3

	- Glyph name: uhungarumlaut	Contours detected: 4	Expected: 3

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: Wcircumflex	Contours detected: 6	Expected: 2

	- Glyph name: wcircumflex	Contours detected: 6	Expected: 2

	- Glyph name: Ycircumflex	Contours detected: 3	Expected: 2

	- Glyph name: ycircumflex	Contours detected: 3	Expected: 2

	- Glyph name: Ydieresis	Contours detected: 4	Expected: 3

	- Glyph name: uni0180	Contours detected: 4	Expected: 2

	- Glyph name: uni0181	Contours detected: 5	Expected: 3

	- Glyph name: uni0186	Contours detected: 3	Expected: 1

	- Glyph name: uni0187	Contours detected: 4	Expected: 1

	- Glyph name: uni0188	Contours detected: 4	Expected: 1

	- Glyph name: uni018A	Contours detected: 4	Expected: 2

	- Glyph name: uni018F	Contours detected: 6	Expected: 2

	- Glyph name: uni0190	Contours detected: 3	Expected: 1

	- Glyph name: uni0191	Contours detected: 2	Expected: 1

	- Glyph name: uni0193	Contours detected: 2	Expected: 1

	- Glyph name: uni0197	Contours detected: 2	Expected: 1

	- Glyph name: uni0198	Contours detected: 2	Expected: 1

	- Glyph name: uni0199	Contours detected: 2	Expected: 1

	- Glyph name: uni019A	Contours detected: 2	Expected: 1

	- Glyph name: uni019B	Contours detected: 2	Expected: 1

	- Glyph name: Obarred	Contours detected: 5	Expected: 3

	- Glyph name: Ohorn	Contours detected: 5	Expected: 2 or 3

	- Glyph name: ohorn	Contours detected: 5	Expected: 2

	- Glyph name: uni01A4	Contours detected: 3	Expected: 2

	- Glyph name: uni01A5	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 3	Expected: 1

	- Glyph name: uhorn	Contours detected: 3	Expected: 1

	- Glyph name: uni01B2	Contours detected: 2	Expected: 1

	- Glyph name: uni01B3	Contours detected: 3	Expected: 1

	- Glyph name: uni01B4	Contours detected: 3	Expected: 1

	- Glyph name: uni01B7	Contours detected: 3	Expected: 1

	- Glyph name: uni01B8	Contours detected: 3	Expected: 1

	- Glyph name: uni01B9	Contours detected: 3	Expected: 1

	- Glyph name: uni01D1	Contours detected: 5	Expected: 3

	- Glyph name: uni01D2	Contours detected: 5	Expected: 3

	- Glyph name: uni01D3	Contours detected: 3	Expected: 2

	- Glyph name: uni01D4	Contours detected: 3	Expected: 2

	- Glyph name: uni01D5	Contours detected: 5	Expected: 4

	- Glyph name: uni01D6	Contours detected: 5	Expected: 4

	- Glyph name: uni01D7	Contours detected: 5	Expected: 4

	- Glyph name: uni01D8	Contours detected: 5	Expected: 4

	- Glyph name: uni01D9	Contours detected: 5	Expected: 4

	- Glyph name: uni01DA	Contours detected: 5	Expected: 4

	- Glyph name: uni01DB	Contours detected: 5	Expected: 4

	- Glyph name: uni01DC	Contours detected: 5	Expected: 4

	- Glyph name: uni01DD	Contours detected: 1	Expected: 2

	- Glyph name: uni01E3	Contours detected: 3	Expected: 4

	- Glyph name: uni01E4	Contours detected: 2	Expected: 1

	- Glyph name: Gcaron	Contours detected: 3	Expected: 2

	- Glyph name: uni01EA	Contours detected: 5	Expected: 2

	- Glyph name: uni01EB	Contours detected: 5	Expected: 2

	- Glyph name: uni01EC	Contours detected: 6	Expected: 3

	- Glyph name: uni01ED	Contours detected: 6	Expected: 3

	- Glyph name: uni01EE	Contours detected: 4	Expected: 2

	- Glyph name: uni01EF	Contours detected: 4	Expected: 2

	- Glyph name: uni01F4	Contours detected: 3	Expected: 2

	- Glyph name: Oslashacute	Contours detected: 5	Expected: 4

	- Glyph name: oslashacute	Contours detected: 5	Expected: 4

	- Glyph name: uni0205	Contours detected: 3	Expected: 4

	- Glyph name: uni0207	Contours detected: 2	Expected: 3

	- Glyph name: uni020C	Contours detected: 6	Expected: 4

	- Glyph name: uni020D	Contours detected: 6	Expected: 4

	- Glyph name: uni020E	Contours detected: 5	Expected: 3

	- Glyph name: uni020F	Contours detected: 5	Expected: 3

	- Glyph name: uni0211	Contours detected: 4	Expected: 3

	- Glyph name: uni0213	Contours detected: 3	Expected: 2

	- Glyph name: uni0214	Contours detected: 4	Expected: 3

	- Glyph name: uni0215	Contours detected: 4	Expected: 3

	- Glyph name: uni0216	Contours detected: 3	Expected: 2

	- Glyph name: uni0217	Contours detected: 3	Expected: 2

	- Glyph name: uni0218	Contours detected: 4	Expected: 2

	- Glyph name: uni0219	Contours detected: 4	Expected: 2

	- Glyph name: uni0222	Contours detected: 4	Expected: 2

	- Glyph name: uni0223	Contours detected: 4	Expected: 2

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni022A	Contours detected: 7	Expected: 5

	- Glyph name: uni022B	Contours detected: 7	Expected: 5

	- Glyph name: uni022C	Contours detected: 6	Expected: 4

	- Glyph name: uni022D	Contours detected: 6	Expected: 4

	- Glyph name: uni022E	Contours detected: 5	Expected: 3

	- Glyph name: uni022F	Contours detected: 5	Expected: 3

	- Glyph name: uni0230	Contours detected: 6	Expected: 4

	- Glyph name: uni0231	Contours detected: 6	Expected: 4

	- Glyph name: uni0232	Contours detected: 3	Expected: 2

	- Glyph name: uni0233	Contours detected: 3	Expected: 2

	- Glyph name: uni0237	Contours detected: 3	Expected: 1

	- Glyph name: uni023A	Contours detected: 2	Expected: 3

	- Glyph name: uni023B	Contours detected: 3	Expected: 2

	- Glyph name: uni023C	Contours detected: 3	Expected: 2

	- Glyph name: uni023D	Contours detected: 2	Expected: 1

	- Glyph name: uni023E	Contours detected: 1	Expected: 2

	- Glyph name: uni0243	Contours detected: 4	Expected: 3

	- Glyph name: uni0244	Contours detected: 3	Expected: 2

	- Glyph name: uni0247	Contours detected: 3	Expected: 4

	- Glyph name: uni0248	Contours detected: 4	Expected: 1

	- Glyph name: uni0249	Contours detected: 4	Expected: 2

	- Glyph name: uni024A	Contours detected: 3	Expected: 2

	- Glyph name: uni024B	Contours detected: 3	Expected: 2

	- Glyph name: uni024D	Contours detected: 2	Expected: 1

	- Glyph name: uni0251	Contours detected: 4	Expected: 2

	- Glyph name: uni0259	Contours detected: 6	Expected: 2

	- Glyph name: uni0292	Contours detected: 3	Expected: 1

	- Glyph name: uni1E02	Contours detected: 5	Expected: 4

	- Glyph name: uni1E03	Contours detected: 5	Expected: 3

	- Glyph name: uni1E08	Contours detected: 5	Expected: 2

	- Glyph name: uni1E09	Contours detected: 5	Expected: 2

	- Glyph name: uni1E0A	Contours detected: 4	Expected: 3

	- Glyph name: uni1E0B	Contours detected: 4	Expected: 3

	- Glyph name: uni1E0C	Contours detected: 4	Expected: 3

	- Glyph name: uni1E0D	Contours detected: 4	Expected: 3

	- Glyph name: Dmacronbelow	Contours detected: 4	Expected: 3

	- Glyph name: dmacronbelow	Contours detected: 4	Expected: 3

	- Glyph name: uni1E15	Contours detected: 3	Expected: 4

	- Glyph name: uni1E17	Contours detected: 3	Expected: 4

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E20	Contours detected: 3	Expected: 2

	- Glyph name: uni1E4C	Contours detected: 6	Expected: 4

	- Glyph name: uni1E4D	Contours detected: 6	Expected: 4

	- Glyph name: uni1E4E	Contours detected: 7	Expected: 5

	- Glyph name: uni1E4F	Contours detected: 7	Expected: 5

	- Glyph name: uni1E50	Contours detected: 6	Expected: 4

	- Glyph name: uni1E51	Contours detected: 6	Expected: 4

	- Glyph name: uni1E52	Contours detected: 6	Expected: 4

	- Glyph name: uni1E53	Contours detected: 6	Expected: 4

	- Glyph name: uni1E5B	Contours detected: 3	Expected: 2

	- Glyph name: uni1E5D	Contours detected: 4	Expected: 3

	- Glyph name: rmacronbelow	Contours detected: 3	Expected: 2

	- Glyph name: uni1E60	Contours detected: 4	Expected: 2

	- Glyph name: uni1E61	Contours detected: 4	Expected: 2

	- Glyph name: uni1E62	Contours detected: 4	Expected: 2

	- Glyph name: uni1E63	Contours detected: 4	Expected: 2

	- Glyph name: uni1E64	Contours detected: 5	Expected: 3

	- Glyph name: uni1E65	Contours detected: 5	Expected: 3

	- Glyph name: uni1E66	Contours detected: 5	Expected: 3

	- Glyph name: uni1E67	Contours detected: 5	Expected: 3

	- Glyph name: uni1E68	Contours detected: 5	Expected: 3

	- Glyph name: uni1E69	Contours detected: 5	Expected: 3

	- Glyph name: uni1E78	Contours detected: 4	Expected: 3

	- Glyph name: uni1E79	Contours detected: 4	Expected: 3

	- Glyph name: uni1E7A	Contours detected: 5	Expected: 4

	- Glyph name: uni1E7B	Contours detected: 5	Expected: 4

	- Glyph name: Wgrave	Contours detected: 6	Expected: 2

	- Glyph name: wgrave	Contours detected: 6	Expected: 2

	- Glyph name: Wacute	Contours detected: 6	Expected: 2

	- Glyph name: wacute	Contours detected: 6	Expected: 2

	- Glyph name: Wdieresis	Contours detected: 7	Expected: 3

	- Glyph name: wdieresis	Contours detected: 7	Expected: 3

	- Glyph name: uni1E8E	Contours detected: 3	Expected: 2

	- Glyph name: uni1E8F	Contours detected: 3	Expected: 2

	- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

	- Glyph name: uni1EBB	Contours detected: 2	Expected: 3

	- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

	- Glyph name: uni1EBF	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC1	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC3	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC5	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC7	Contours detected: 3	Expected: 4

	- Glyph name: uni1ECB	Contours detected: 2	Expected: 3

	- Glyph name: uni1ECC	Contours detected: 5	Expected: 3

	- Glyph name: uni1ECD	Contours detected: 5	Expected: 3

	- Glyph name: uni1ECE	Contours detected: 5	Expected: 3

	- Glyph name: uni1ECF	Contours detected: 5	Expected: 3

	- Glyph name: uni1ED0	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED1	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED2	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED3	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED4	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED5	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED6	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED7	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED8	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED9	Contours detected: 6	Expected: 4

	- Glyph name: uni1EDA	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EDB	Contours detected: 6	Expected: 3

	- Glyph name: uni1EDC	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EDD	Contours detected: 6	Expected: 3

	- Glyph name: uni1EDE	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EDF	Contours detected: 6	Expected: 3

	- Glyph name: uni1EE0	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EE1	Contours detected: 6	Expected: 3

	- Glyph name: uni1EE2	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EE3	Contours detected: 6	Expected: 3

	- Glyph name: uni1EE4	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE5	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE6	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE7	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE8	Contours detected: 4	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 4	Expected: 2

	- Glyph name: uni1EED	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 4	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 4	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 4	Expected: 2

	- Glyph name: Ygrave	Contours detected: 3	Expected: 2

	- Glyph name: ygrave	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF4	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF5	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF6	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF7	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF9	Contours detected: 3	Expected: 2

	- Glyph name: B	Contours detected: 4	Expected: 2 or 3

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: Cacute	Contours detected: 4	Expected: 2

	- Glyph name: Ccaron	Contours detected: 4	Expected: 2

	- Glyph name: Ccedilla	Contours detected: 4	Expected: 1 or 2

	- Glyph name: Cdotaccent	Contours detected: 4	Expected: 2

	- Glyph name: D	Contours detected: 3	Expected: 2

	- Glyph name: Dcaron	Contours detected: 4	Expected: 3

	- Glyph name: G	Contours detected: 2	Expected: 1

	- Glyph name: Gbreve	Contours detected: 3	Expected: 2

	- Glyph name: Gcaron	Contours detected: 3	Expected: 2

	- Glyph name: Gdotaccent	Contours detected: 3	Expected: 2

	- Glyph name: IJ	Contours detected: 4	Expected: 1 or 2

	- Glyph name: J	Contours detected: 3	Expected: 1

	- Glyph name: Jcircumflex	Contours detected: 4	Expected: 2

	- Glyph name: O	Contours detected: 4	Expected: 2

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: Oacute	Contours detected: 5	Expected: 3

	- Glyph name: Ocircumflex	Contours detected: 5	Expected: 3

	- Glyph name: Odieresis	Contours detected: 6	Expected: 4

	- Glyph name: Ograve	Contours detected: 5	Expected: 3

	- Glyph name: Ohorn	Contours detected: 5	Expected: 2 or 3

	- Glyph name: Ohungarumlaut	Contours detected: 6	Expected: 4

	- Glyph name: Omacron	Contours detected: 5	Expected: 3

	- Glyph name: Oslash	Contours detected: 4	Expected: 2 or 3

	- Glyph name: Oslashacute	Contours detected: 5	Expected: 4

	- Glyph name: Otilde	Contours detected: 5	Expected: 3

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: S	Contours detected: 3	Expected: 1

	- Glyph name: Sacute	Contours detected: 4	Expected: 2

	- Glyph name: Scaron	Contours detected: 4	Expected: 2

	- Glyph name: U	Contours detected: 2	Expected: 1

	- Glyph name: Uacute	Contours detected: 3	Expected: 2

	- Glyph name: Ubreve	Contours detected: 3	Expected: 2

	- Glyph name: Ucircumflex	Contours detected: 3	Expected: 2

	- Glyph name: Udieresis	Contours detected: 4	Expected: 3

	- Glyph name: Ugrave	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 3	Expected: 1

	- Glyph name: Uhungarumlaut	Contours detected: 4	Expected: 3

	- Glyph name: Umacron	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: Uring	Contours detected: 4	Expected: 3

	- Glyph name: Utilde	Contours detected: 3	Expected: 2

	- Glyph name: W	Contours detected: 5	Expected: 1 or 2

	- Glyph name: Wacute	Contours detected: 6	Expected: 2

	- Glyph name: Wcircumflex	Contours detected: 6	Expected: 2

	- Glyph name: Wdieresis	Contours detected: 7	Expected: 3

	- Glyph name: Wgrave	Contours detected: 6	Expected: 2

	- Glyph name: Y	Contours detected: 2	Expected: 1

	- Glyph name: Yacute	Contours detected: 3	Expected: 2

	- Glyph name: Ycircumflex	Contours detected: 3	Expected: 2

	- Glyph name: Ydieresis	Contours detected: 4	Expected: 3

	- Glyph name: Ygrave	Contours detected: 3	Expected: 2

	- Glyph name: ae	Contours detected: 2	Expected: 3

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: b	Contours detected: 4	Expected: 2

	- Glyph name: c	Contours detected: 3	Expected: 1

	- Glyph name: cacute	Contours detected: 4	Expected: 2

	- Glyph name: ccaron	Contours detected: 4	Expected: 2

	- Glyph name: ccedilla	Contours detected: 4	Expected: 1 or 2

	- Glyph name: cdotaccent	Contours detected: 4	Expected: 2

	- Glyph name: d	Contours detected: 3	Expected: 2

	- Glyph name: dcaron	Contours detected: 4	Expected: 3

	- Glyph name: e	Contours detected: 1	Expected: 2

	- Glyph name: eacute	Contours detected: 2	Expected: 3

	- Glyph name: ecaron	Contours detected: 2	Expected: 3

	- Glyph name: edieresis	Contours detected: 3	Expected: 4

	- Glyph name: edotaccent	Contours detected: 2	Expected: 3

	- Glyph name: egrave	Contours detected: 2	Expected: 3

	- Glyph name: emacron	Contours detected: 2	Expected: 3

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: i	Contours detected: 1	Expected: 2

	- Glyph name: j	Contours detected: 3	Expected: 2

	- Glyph name: o	Contours detected: 4	Expected: 2

	- Glyph name: oacute	Contours detected: 5	Expected: 3

	- Glyph name: ocircumflex	Contours detected: 5	Expected: 3

	- Glyph name: odieresis	Contours detected: 6	Expected: 4

	- Glyph name: ograve	Contours detected: 5	Expected: 3

	- Glyph name: ohorn	Contours detected: 5	Expected: 2

	- Glyph name: ohungarumlaut	Contours detected: 6	Expected: 4

	- Glyph name: omacron	Contours detected: 5	Expected: 3

	- Glyph name: oslash	Contours detected: 4	Expected: 3

	- Glyph name: oslashacute	Contours detected: 5	Expected: 4

	- Glyph name: otilde	Contours detected: 5	Expected: 3

	- Glyph name: q	Contours detected: 3	Expected: 2

	- Glyph name: r	Contours detected: 2	Expected: 1

	- Glyph name: racute	Contours detected: 3	Expected: 2

	- Glyph name: rcaron	Contours detected: 3	Expected: 2

	- Glyph name: s	Contours detected: 3	Expected: 1

	- Glyph name: sacute	Contours detected: 4	Expected: 2

	- Glyph name: scaron	Contours detected: 4	Expected: 2

	- Glyph name: u	Contours detected: 2	Expected: 1

	- Glyph name: uacute	Contours detected: 3	Expected: 2

	- Glyph name: ubreve	Contours detected: 3	Expected: 2

	- Glyph name: ucircumflex	Contours detected: 3	Expected: 2

	- Glyph name: udieresis	Contours detected: 4	Expected: 3

	- Glyph name: ugrave	Contours detected: 3	Expected: 2

	- Glyph name: uhorn	Contours detected: 3	Expected: 1

	- Glyph name: uhungarumlaut	Contours detected: 4	Expected: 3

	- Glyph name: umacron	Contours detected: 3	Expected: 2

	- Glyph name: uni0122	Contours detected: 3	Expected: 2

	- Glyph name: uni0157	Contours detected: 3	Expected: 2

	- Glyph name: uni0180	Contours detected: 4	Expected: 2

	- Glyph name: uni0181	Contours detected: 5	Expected: 3

	- Glyph name: uni0186	Contours detected: 3	Expected: 1

	- Glyph name: uni0187	Contours detected: 4	Expected: 1

	- Glyph name: uni0188	Contours detected: 4	Expected: 1

	- Glyph name: uni018A	Contours detected: 4	Expected: 2

	- Glyph name: uni018F	Contours detected: 6	Expected: 2

	- Glyph name: uni0190	Contours detected: 3	Expected: 1

	- Glyph name: uni0191	Contours detected: 2	Expected: 1

	- Glyph name: uni0193	Contours detected: 2	Expected: 1

	- Glyph name: uni0197	Contours detected: 2	Expected: 1

	- Glyph name: uni0198	Contours detected: 2	Expected: 1

	- Glyph name: uni0199	Contours detected: 2	Expected: 1

	- Glyph name: uni019A	Contours detected: 2	Expected: 1

	- Glyph name: uni019B	Contours detected: 2	Expected: 1

	- Glyph name: uni01A4	Contours detected: 3	Expected: 2

	- Glyph name: uni01A5	Contours detected: 3	Expected: 2

	- Glyph name: uni01B2	Contours detected: 2	Expected: 1

	- Glyph name: uni01B3	Contours detected: 3	Expected: 1

	- Glyph name: uni01B4	Contours detected: 3	Expected: 1

	- Glyph name: uni01B7	Contours detected: 3	Expected: 1

	- Glyph name: uni01B8	Contours detected: 3	Expected: 1

	- Glyph name: uni01B9	Contours detected: 3	Expected: 1

	- Glyph name: uni01D1	Contours detected: 5	Expected: 3

	- Glyph name: uni01D2	Contours detected: 5	Expected: 3

	- Glyph name: uni01D3	Contours detected: 3	Expected: 2

	- Glyph name: uni01D4	Contours detected: 3	Expected: 2

	- Glyph name: uni01D5	Contours detected: 5	Expected: 4

	- Glyph name: uni01D6	Contours detected: 5	Expected: 4

	- Glyph name: uni01D7	Contours detected: 5	Expected: 4

	- Glyph name: uni01D8	Contours detected: 5	Expected: 4

	- Glyph name: uni01D9	Contours detected: 5	Expected: 4

	- Glyph name: uni01DA	Contours detected: 5	Expected: 4

	- Glyph name: uni01DB	Contours detected: 5	Expected: 4

	- Glyph name: uni01DC	Contours detected: 5	Expected: 4

	- Glyph name: uni01DD	Contours detected: 1	Expected: 2

	- Glyph name: uni01E3	Contours detected: 3	Expected: 4

	- Glyph name: uni01E4	Contours detected: 2	Expected: 1

	- Glyph name: uni01EC	Contours detected: 6	Expected: 3

	- Glyph name: uni01ED	Contours detected: 6	Expected: 3

	- Glyph name: uni01EE	Contours detected: 4	Expected: 2

	- Glyph name: uni01EF	Contours detected: 4	Expected: 2

	- Glyph name: uni0218	Contours detected: 4	Expected: 2

	- Glyph name: uni0219	Contours detected: 4	Expected: 2

	- Glyph name: uni0222	Contours detected: 4	Expected: 2

	- Glyph name: uni0223	Contours detected: 4	Expected: 2

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni022A	Contours detected: 7	Expected: 5

	- Glyph name: uni022B	Contours detected: 7	Expected: 5

	- Glyph name: uni022C	Contours detected: 6	Expected: 4

	- Glyph name: uni022D	Contours detected: 6	Expected: 4

	- Glyph name: uni022E	Contours detected: 5	Expected: 3

	- Glyph name: uni022F	Contours detected: 5	Expected: 3

	- Glyph name: uni0230	Contours detected: 6	Expected: 4

	- Glyph name: uni0231	Contours detected: 6	Expected: 4

	- Glyph name: uni0232	Contours detected: 3	Expected: 2

	- Glyph name: uni0233	Contours detected: 3	Expected: 2

	- Glyph name: uni0237	Contours detected: 3	Expected: 1

	- Glyph name: uni023A	Contours detected: 2	Expected: 3

	- Glyph name: uni023B	Contours detected: 3	Expected: 2

	- Glyph name: uni023C	Contours detected: 3	Expected: 2

	- Glyph name: uni023D	Contours detected: 2	Expected: 1

	- Glyph name: uni023E	Contours detected: 1	Expected: 2

	- Glyph name: uni0243	Contours detected: 4	Expected: 3

	- Glyph name: uni0244	Contours detected: 3	Expected: 2

	- Glyph name: uni0247	Contours detected: 3	Expected: 4

	- Glyph name: uni0248	Contours detected: 4	Expected: 1

	- Glyph name: uni0249	Contours detected: 4	Expected: 2

	- Glyph name: uni024A	Contours detected: 3	Expected: 2

	- Glyph name: uni024B	Contours detected: 3	Expected: 2

	- Glyph name: uni024D	Contours detected: 2	Expected: 1

	- Glyph name: uni0251	Contours detected: 4	Expected: 2

	- Glyph name: uni0259	Contours detected: 6	Expected: 2

	- Glyph name: uni0292	Contours detected: 3	Expected: 1

	- Glyph name: uni1E02	Contours detected: 5	Expected: 4

	- Glyph name: uni1E03	Contours detected: 5	Expected: 3

	- Glyph name: uni1E08	Contours detected: 5	Expected: 2

	- Glyph name: uni1E09	Contours detected: 5	Expected: 2

	- Glyph name: uni1E0A	Contours detected: 4	Expected: 3

	- Glyph name: uni1E0B	Contours detected: 4	Expected: 3

	- Glyph name: uni1E0C	Contours detected: 4	Expected: 3

	- Glyph name: uni1E0D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E15	Contours detected: 3	Expected: 4

	- Glyph name: uni1E17	Contours detected: 3	Expected: 4

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E20	Contours detected: 3	Expected: 2

	- Glyph name: uni1E4C	Contours detected: 6	Expected: 4

	- Glyph name: uni1E4D	Contours detected: 6	Expected: 4

	- Glyph name: uni1E4E	Contours detected: 7	Expected: 5

	- Glyph name: uni1E4F	Contours detected: 7	Expected: 5

	- Glyph name: uni1E50	Contours detected: 6	Expected: 4

	- Glyph name: uni1E51	Contours detected: 6	Expected: 4

	- Glyph name: uni1E52	Contours detected: 6	Expected: 4

	- Glyph name: uni1E53	Contours detected: 6	Expected: 4

	- Glyph name: uni1E5B	Contours detected: 3	Expected: 2

	- Glyph name: uni1E5D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E60	Contours detected: 4	Expected: 2

	- Glyph name: uni1E61	Contours detected: 4	Expected: 2

	- Glyph name: uni1E62	Contours detected: 4	Expected: 2

	- Glyph name: uni1E63	Contours detected: 4	Expected: 2

	- Glyph name: uni1E64	Contours detected: 5	Expected: 3

	- Glyph name: uni1E65	Contours detected: 5	Expected: 3

	- Glyph name: uni1E66	Contours detected: 5	Expected: 3

	- Glyph name: uni1E67	Contours detected: 5	Expected: 3

	- Glyph name: uni1E68	Contours detected: 5	Expected: 3

	- Glyph name: uni1E69	Contours detected: 5	Expected: 3

	- Glyph name: uni1E78	Contours detected: 4	Expected: 3

	- Glyph name: uni1E79	Contours detected: 4	Expected: 3

	- Glyph name: uni1E7A	Contours detected: 5	Expected: 4

	- Glyph name: uni1E7B	Contours detected: 5	Expected: 4

	- Glyph name: uni1E8E	Contours detected: 3	Expected: 2

	- Glyph name: uni1E8F	Contours detected: 3	Expected: 2

	- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

	- Glyph name: uni1EBB	Contours detected: 2	Expected: 3

	- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

	- Glyph name: uni1EBF	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC1	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC3	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC5	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC7	Contours detected: 3	Expected: 4

	- Glyph name: uni1ECB	Contours detected: 2	Expected: 3

	- Glyph name: uni1ECC	Contours detected: 5	Expected: 3

	- Glyph name: uni1ECD	Contours detected: 5	Expected: 3

	- Glyph name: uni1ECE	Contours detected: 5	Expected: 3

	- Glyph name: uni1ECF	Contours detected: 5	Expected: 3

	- Glyph name: uni1ED0	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED1	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED2	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED3	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED4	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED5	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED6	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED7	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED8	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED9	Contours detected: 6	Expected: 4

	- Glyph name: uni1EDA	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EDB	Contours detected: 6	Expected: 3

	- Glyph name: uni1EDC	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EDD	Contours detected: 6	Expected: 3

	- Glyph name: uni1EDE	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EDF	Contours detected: 6	Expected: 3

	- Glyph name: uni1EE0	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EE1	Contours detected: 6	Expected: 3

	- Glyph name: uni1EE2	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EE3	Contours detected: 6	Expected: 3

	- Glyph name: uni1EE4	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE5	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE6	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE7	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE8	Contours detected: 4	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 4	Expected: 2

	- Glyph name: uni1EED	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 4	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 4	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 4	Expected: 2

	- Glyph name: uni1EF4	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF5	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF6	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF7	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF9	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uring	Contours detected: 4	Expected: 3

	- Glyph name: utilde	Contours detected: 3	Expected: 2

	- Glyph name: w	Contours detected: 5	Expected: 1

	- Glyph name: wacute	Contours detected: 6	Expected: 2

	- Glyph name: wcircumflex	Contours detected: 6	Expected: 2

	- Glyph name: wdieresis	Contours detected: 7	Expected: 3

	- Glyph name: wgrave	Contours detected: 6	Expected: 2

	- Glyph name: y	Contours detected: 2	Expected: 1

	- Glyph name: yacute	Contours detected: 3	Expected: 2

	- Glyph name: ycircumflex	Contours detected: 3	Expected: 2

	- Glyph name: ydieresis	Contours detected: 4	Expected: 3

	- Glyph name: ygrave	Contours detected: 3	Expected: 2
 [code: contour-count]
</div></details><details><summary>🔥 <b>FAIL:</b> Check accent of Lcaron, dcaron, lcaron, tcaron (derived from com.google.fonts/check/alt_caron) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/alt_caron">com.google.fonts/check/alt_caron</a>)</summary><div>


* 🔥 **FAIL** Lcaron uses component uni030C. [code: wrong-mark]
* 🔥 **FAIL** dcaron uses component uni030C. [code: wrong-mark]
* 🔥 **FAIL** lcaron uses component uni030C. [code: wrong-mark]
* 🔥 **FAIL** tcaron uses component uni030C. [code: wrong-mark]
</div></details><details><summary>🔥 <b>FAIL:</b> Does full font name begin with the font family name? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/name/match_familyname_fullfont">com.google.fonts/check/name/match_familyname_fullfont</a>)</summary><div>


* 🔥 **FAIL** On the 'name' table, the full font name 'Danfo Regular 50' does not begin with the font family name 'Danfo 50' in platformID 3, encodingID 1, languageID 1033(0409), and nameID 1. [code: mismatch-font-names]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Check for codepoints not covered by METADATA subsets. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/unreachable_subsetting">com.google.fonts/check/metadata/unreachable_subsetting</a>)</summary><div>


* ⚠ **WARN** The following codepoints supported by the font are not covered by
    any subsets defined in the font's metadata file, and will never
    be served. You can solve this by either manually adding additional
    subset declarations to METADATA.pb, or by editing the glyphset
    definitions.

 * U+02D7 MODIFIER LETTER MINUS SIGN: not included in any glyphset definition
 * U+02EE MODIFIER LETTER DOUBLE APOSTROPHE: not included in any glyphset definition
 * U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, math, tifinagh, cherokee
 * U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic
 * U+0307 COMBINING DOT ABOVE: try adding one of: math, tai-le, malayalam, syriac, canadian-aboriginal, old-permic, coptic, tifinagh
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
 * U+0324 COMBINING DIAERESIS BELOW: try adding one of: syriac, cherokee
 * U+0325 COMBINING RING BELOW: try adding syriac
 * U+0326 COMBINING COMMA BELOW: not included in any glyphset definition
 * U+0327 COMBINING CEDILLA: not included in any glyphset definition
 * U+0328 COMBINING OGONEK: not included in any glyphset definition
 * U+032D COMBINING CIRCUMFLEX ACCENT BELOW: try adding syriac
 * U+032E COMBINING BREVE BELOW: try adding syriac
 * U+032F COMBINING INVERTED BREVE BELOW: not included in any glyphset definition
 * U+0330 COMBINING TILDE BELOW: try adding one of: math, syriac, cherokee
 * U+0331 COMBINING MACRON BELOW: try adding one of: syriac, cherokee, gothic, caucasian-albanian, tifinagh
 * U+0332 COMBINING LOW LINE: not included in any glyphset definition
 * U+0334 COMBINING TILDE OVERLAY: not included in any glyphset definition
 * U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition
 * U+0358 COMBINING DOT ABOVE RIGHT: try adding osage
 * U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai
 * U+1D7D LATIN SMALL LETTER P WITH STROKE: not included in any glyphset definition
 * U+1DC4 COMBINING MACRON-ACUTE: not included in any glyphset definition
 * U+1DC5 COMBINING GRAVE-MACRON: not included in any glyphset definition
 * U+1DC6 COMBINING MACRON-GRAVE: not included in any glyphset definition
 * U+1DC7 COMBINING ACUTE-MACRON: not included in any glyphset definition
 * U+1DCA COMBINING LATIN SMALL LETTER R BELOW: not included in any glyphset definition
 * U+2016 DOUBLE VERTICAL LINE: not included in any glyphset definition
 * U+2021 DOUBLE DAGGER: try adding adlam
 * U+2030 PER MILLE SIGN: try adding adlam
 * U+2075 SUPERSCRIPT FIVE: not included in any glyphset definition
 * U+2076 SUPERSCRIPT SIX: not included in any glyphset definition
 * U+2077 SUPERSCRIPT SEVEN: not included in any glyphset definition
 * U+2078 SUPERSCRIPT EIGHT: not included in any glyphset definition
 * U+2079 SUPERSCRIPT NINE: not included in any glyphset definition
 * U+2081 SUBSCRIPT ONE: not included in any glyphset definition
 * U+2082 SUBSCRIPT TWO: not included in any glyphset definition
 * U+2083 SUBSCRIPT THREE: not included in any glyphset definition
 * U+2084 SUBSCRIPT FOUR: not included in any glyphset definition
 * U+2085 SUBSCRIPT FIVE: not included in any glyphset definition
 * U+2086 SUBSCRIPT SIX: not included in any glyphset definition
 * U+2087 SUBSCRIPT SEVEN: not included in any glyphset definition
 * U+2088 SUBSCRIPT EIGHT: not included in any glyphset definition
 * U+2089 SUBSCRIPT NINE: not included in any glyphset definition
 * U+2126 OHM SIGN: not included in any glyphset definition
 * U+212E ESTIMATED SYMBOL: not included in any glyphset definition
 * U+2153 VULGAR FRACTION ONE THIRD: not included in any glyphset definition
 * U+2154 VULGAR FRACTION TWO THIRDS: not included in any glyphset definition
 * U+2190 LEFTWARDS ARROW: try adding one of: math, symbols
 * U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols
 * U+2194 LEFT RIGHT ARROW: try adding one of: math, emoji, symbols
 * U+2195 UP DOWN ARROW: try adding one of: math, emoji, symbols
 * U+2196 NORTH WEST ARROW: try adding one of: math, emoji, symbols
 * U+2197 NORTH EAST ARROW: try adding one of: math, emoji, symbols
 * U+2198 SOUTH EAST ARROW: try adding one of: math, emoji, symbols
 * U+2199 SOUTH WEST ARROW: try adding one of: math, emoji, symbols
 * U+2202 PARTIAL DIFFERENTIAL: try adding math
 * U+2205 EMPTY SET: try adding math
 * U+2206 INCREMENT: try adding math
 * U+220F N-ARY PRODUCT: try adding math
 * U+2211 N-ARY SUMMATION: try adding math
 * U+221A SQUARE ROOT: try adding math
 * U+221E INFINITY: try adding math
 * U+222B INTEGRAL: try adding math
 * U+2248 ALMOST EQUAL TO: try adding math
 * U+2260 NOT EQUAL TO: try adding math
 * U+2264 LESS-THAN OR EQUAL TO: try adding math
 * U+2265 GREATER-THAN OR EQUAL TO: try adding math
 * U+25A0 BLACK SQUARE: try adding symbols
 * U+25A1 WHITE SQUARE: try adding symbols
 * U+25AA BLACK SMALL SQUARE: try adding one of: emoji, symbols
 * U+25AB WHITE SMALL SQUARE: try adding one of: emoji, symbols
 * U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols
 * U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: math, symbols
 * U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols
 * U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols
 * U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding one of: emoji, symbols
 * U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: math, symbols
 * U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols
 * U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols
 * U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols
 * U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: math, symbols
 * U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols
 * U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols
 * U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding one of: emoji, symbols
 * U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: math, symbols
 * U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols
 * U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols
 * U+25C6 BLACK DIAMOND: try adding symbols
 * U+25C7 WHITE DIAMOND: try adding symbols
 * U+25CA LOZENGE: try adding one of: math, symbols
 * U+25CB WHITE CIRCLE: try adding symbols
 * U+25CF BLACK CIRCLE: try adding symbols
 * U+25E6 WHITE BULLET: try adding symbols
 * U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math
 * U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math
 * U+3008 LEFT ANGLE BRACKET: try adding one of: tai-le, japanese, yi, chinese-traditional, phags-pa, chinese-hongkong, chinese-simplified
 * U+3009 RIGHT ANGLE BRACKET: try adding one of: tai-le, japanese, yi, chinese-traditional, phags-pa, chinese-hongkong, chinese-simplified
 * U+AB53 LATIN SMALL LETTER CHI: not included in any glyphset definition
 * U+FF0D FULLWIDTH HYPHEN-MINUS: try adding chinese-simplified

Or you can add the above codepoints to one of the subsets supported by the font: `cyrillic-ext`, `latin`, `latin-ext`, `vietnamese` [code: unreachable-subsetting]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- _part.cut

	- hook.part
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 298 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 279:
less, greater

Width = 326:
equal

Width = 306:
logicalnot

Width = 284:
multiply

Width = 316:
divide

Width = 286:
minus

Width = 330:
approxequal

Width = 339:
notequal

Width = 287:
lessequal, greaterequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** OS/2 sTypoLineGap is not equal to 0. [code: OS/2]
</div></details><details><summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Euro (U+20AC): L<<231.0,550.0>--<231.0,547.0>> -> L<<231.0,547.0>--<231.0,519.0>>

	* Gammalatin (U+0194): L<<166.0,334.0>--<166.0,261.0>> -> L<<166.0,261.0>--<166.0,260.0>>

	* paragraph (U+00B6): L<<182.0,715.0>--<491.0,716.0>> -> L<<491.0,716.0>--<648.0,716.0>>

	* section (U+00A7): L<<268.0,464.0>--<326.0,459.0>> -> L<<326.0,459.0>--<344.0,457.0>>

	* uni0222 (U+0222): L<<275.0,430.0>--<332.0,429.0>> -> L<<332.0,429.0>--<369.0,430.0>>

	* uni0223 (U+0223): L<<275.0,430.0>--<332.0,429.0>> -> L<<332.0,429.0>--<369.0,430.0>>

	* uni024E (U+024E): L<<421.0,491.0>--<110.0,517.0>> -> L<<110.0,517.0>--<27.0,517.0>>

	* uni024F (U+024F): L<<421.0,491.0>--<110.0,517.0>> -> L<<110.0,517.0>--<27.0,517.0>>

	* uni0263 (U+0263): L<<166.0,334.0>--<166.0,261.0>> -> L<<166.0,261.0>--<166.0,260.0>>

	* uniA7B8 (U+A7B8): L<<337.0,-6.0>--<225.0,-6.0>> -> L<<225.0,-6.0>--<223.0,-6.0>>

	* uniA7B9 (U+A7B9): L<<337.0,-6.0>--<225.0,-6.0>> -> L<<225.0,-6.0>--<223.0,-6.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* Euro (U+20AC): L<<218.0,722.0>--<426.0,721.0>>

	* G (U+0047): L<<218.0,722.0>--<426.0,721.0>>

	* Gbreve (U+011E): L<<218.0,722.0>--<426.0,721.0>>

	* Gcaron (U+01E6): L<<218.0,722.0>--<426.0,721.0>>

	* Gdotaccent (U+0120): L<<218.0,722.0>--<426.0,721.0>>

	* Glottalstopsmall (U+0241): L<<161.0,721.0>--<334.0,722.0>>

	* M (U+004D): L<<354.0,0.0>--<29.0,-1.0>>

	* M (U+004D): L<<739.0,-1.0>--<414.0,0.0>>

	* Ohungarumlaut (U+0150): L<<393.0,877.0>--<511.0,878.0>>

	* Thorn (U+00DE): L<<267.0,588.0>--<470.0,587.0>>

	* Thorn (U+00DE): L<<29.0,716.0>--<331.0,715.0>>

	* Thorn (U+00DE): L<<331.0,-1.0>--<29.0,0.0>>

	* Thorn (U+00DE): L<<484.0,368.0>--<266.0,369.0>>

	* Uhungarumlaut (U+0170): L<<422.0,877.0>--<540.0,878.0>>

	* ampersand (U+0026): L<<408.0,540.0>--<676.0,538.0>>

	* arrowboth (U+2194): L<<300.0,324.0>--<299.0,103.0>>

	* arrowboth (U+2194): L<<301.0,644.0>--<300.0,424.0>>

	* arrowboth (U+2194): L<<478.0,424.0>--<477.0,644.0>>

	* arrowboth (U+2194): L<<479.0,103.0>--<478.0,324.0>>

	* arrowdown (U+2193): L<<18.0,397.0>--<238.0,396.0>>

	* arrowdown (U+2193): L<<337.0,396.0>--<559.0,395.0>>

	* arrowdown (U+2193): L<<338.0,704.0>--<337.0,396.0>>

	* arrowleft (U+2190): L<<299.0,691.0>--<300.0,469.0>>

	* arrowleft (U+2190): L<<300.0,370.0>--<301.0,150.0>>

	* arrowleft (U+2190): L<<300.0,469.0>--<608.0,470.0>>

	* arrowright (U+2192): L<<337.0,342.0>--<29.0,341.0>>

	* arrowright (U+2192): L<<337.0,441.0>--<336.0,661.0>>

	* arrowright (U+2192): L<<338.0,120.0>--<337.0,342.0>>

	* arrowup (U+2191): L<<239.0,433.0>--<19.0,432.0>>

	* arrowup (U+2191): L<<338.0,433.0>--<339.0,125.0>>

	* arrowup (U+2191): L<<560.0,434.0>--<338.0,433.0>>

	* arrowupdn (U+2195): L<<10.0,287.0>--<231.0,288.0>>

	* arrowupdn (U+2195): L<<231.0,466.0>--<10.0,467.0>>

	* arrowupdn (U+2195): L<<331.0,288.0>--<551.0,289.0>>

	* arrowupdn (U+2195): L<<551.0,465.0>--<331.0,466.0>>

	* bracketleft (U+005B): L<<190.0,757.0>--<188.0,-44.0>>

	* bracketleft (U+005B): L<<29.0,-125.0>--<32.0,837.0>>

	* bracketright (U+005D): L<<166.0,-40.0>--<168.0,761.0>>

	* bracketright (U+005D): L<<327.0,842.0>--<324.0,-120.0>>

	* eight (U+0038): L<<189.0,716.0>--<451.0,715.0>>

	* eight (U+0038): L<<431.0,-8.0>--<209.0,-7.0>>

	* exclam (U+0021): L<<30.0,723.0>--<252.0,724.0>>

	* exclamdown (U+00A1): L<<260.0,-140.0>--<38.0,-141.0>>

	* five (U+0035): L<<27.0,179.0>--<28.0,470.0>>

	* five (U+0035): L<<592.0,410.0>--<591.0,178.0>>

	* florin (U+0192): L<<29.0,0.0>--<30.0,434.0>>

	* four (U+0034): L<<581.0,-1.0>--<31.0,-3.0>>

	* g (U+0067): L<<218.0,722.0>--<426.0,721.0>>

	* gbreve (U+011F): L<<218.0,722.0>--<426.0,721.0>>

	* gcaron (U+01E7): L<<218.0,722.0>--<426.0,721.0>>

	* gdotaccent (U+0121): L<<218.0,722.0>--<426.0,721.0>>

	* m (U+006D): L<<354.0,0.0>--<29.0,-1.0>>

	* m (U+006D): L<<739.0,-1.0>--<414.0,0.0>>

	* minute (U+2032): L<<60.0,717.0>--<287.0,716.0>>

	* nine (U+0039): L<<24.0,180.0>--<25.0,470.0>>

	* nine (U+0039): L<<399.0,-7.0>--<213.0,-6.0>>

	* nine (U+0039): L<<589.0,550.0>--<588.0,179.0>>

	* nlongrightleg (U+019E): L<<667.0,-139.0>--<375.0,-138.0>>

	* ohungarumlaut (U+0151): L<<393.0,877.0>--<511.0,878.0>>

	* one (U+0031): L<<210.0,715.0>--<397.0,716.0>>

	* one (U+0031): L<<397.0,716.0>--<398.0,495.0>>

	* paragraph (U+00B6): L<<182.0,715.0>--<491.0,716.0>>

	* percent (U+0025): L<<481.0,722.0>--<599.0,721.0>>

	* perthousand (U+2030): L<<481.0,722.0>--<599.0,721.0>>

	* radical (U+221A): L<<376.0,-101.0>--<181.0,-100.0>>

	* radical (U+221A): L<<512.0,899.0>--<636.0,898.0>>

	* second (U+2033): L<<316.0,717.0>--<543.0,716.0>>

	* second (U+2033): L<<60.0,717.0>--<287.0,716.0>>

	* seven (U+0037): L<<26.0,0.0>--<27.0,434.0>>

	* seven (U+0037): L<<27.0,716.0>--<534.0,714.0>>

	* seven (U+0037): L<<534.0,-1.0>--<26.0,0.0>>

	* six (U+0036): L<<430.0,-6.0>--<216.0,-5.0>>

	* sterling (U+00A3): L<<564.0,589.0>--<393.0,590.0>>

	* thorn (U+00FE): L<<267.0,588.0>--<470.0,587.0>>

	* thorn (U+00FE): L<<29.0,716.0>--<331.0,715.0>>

	* thorn (U+00FE): L<<331.0,-1.0>--<29.0,0.0>>

	* thorn (U+00FE): L<<484.0,368.0>--<266.0,369.0>>

	* triagdn (U+25BC): L<<29.0,731.0>--<733.0,728.0>>

	* triagup (U+25B2): L<<733.0,141.0>--<29.0,144.0>>

	* uhungarumlaut (U+0171): L<<422.0,877.0>--<540.0,878.0>>

	* uni00B9 (U+00B9): L<<210.0,715.0>--<397.0,716.0>>

	* uni00B9 (U+00B9): L<<397.0,716.0>--<398.0,495.0>>

	* uni0122 (U+0122): L<<218.0,722.0>--<426.0,721.0>>

	* uni0123 (U+0123): L<<218.0,722.0>--<426.0,721.0>>

	* uni0190 (U+0190): L<<189.0,716.0>--<416.0,715.0>>

	* uni0190 (U+0190): L<<403.0,-8.0>--<209.0,-7.0>>

	* uni0193 (U+0193): L<<218.0,722.0>--<426.0,721.0>>

	* uni019C (U+019C): L<<29.0,717.0>--<354.0,716.0>>

	* uni019C (U+019C): L<<414.0,716.0>--<739.0,717.0>>

	* uni01A9 (U+01A9): L<<27.0,716.0>--<540.0,714.0>>

	* uni01A9 (U+01A9): L<<541.0,-2.0>--<27.0,0.0>>

	* uni01B7 (U+01B7): L<<44.0,715.0>--<557.0,716.0>>

	* uni01B8 (U+01B8): L<<53.0,716.0>--<566.0,715.0>>

	* uni01B9 (U+01B9): L<<53.0,716.0>--<566.0,715.0>>

	* uni01E4 (U+01E4): L<<218.0,722.0>--<426.0,721.0>>

	* uni01E5 (U+01E5): L<<218.0,722.0>--<426.0,721.0>>

	* uni01EE (U+01EE): L<<44.0,715.0>--<557.0,716.0>>

	* uni01EF (U+01EF): L<<44.0,715.0>--<557.0,716.0>>

	* uni01F4 (U+01F4): L<<218.0,722.0>--<426.0,721.0>>

	* uni01F5 (U+01F5): L<<218.0,722.0>--<426.0,721.0>>

	* uni0220 (U+0220): L<<667.0,-139.0>--<375.0,-138.0>>

	* uni0242 (U+0242): L<<161.0,558.0>--<334.0,559.0>>

	* uni025B (U+025B): L<<189.0,716.0>--<416.0,715.0>>

	* uni025B (U+025B): L<<403.0,-8.0>--<209.0,-7.0>>

	* uni0260 (U+0260): L<<218.0,722.0>--<426.0,721.0>>

	* uni0265 (U+0265): L<<642.0,0.0>--<330.0,-1.0>>

	* uni026F (U+026F): L<<29.0,717.0>--<354.0,716.0>>

	* uni026F (U+026F): L<<414.0,716.0>--<739.0,717.0>>

	* uni0292 (U+0292): L<<44.0,715.0>--<557.0,716.0>>

	* uni0294 (U+0294): L<<161.0,721.0>--<334.0,722.0>>

	* uni0295 (U+0295): L<<219.0,722.0>--<392.0,721.0>>

	* uni030B (U+030B): L<<202.0,768.0>--<320.0,769.0>>

	* uni1E20 (U+1E20): L<<218.0,722.0>--<426.0,721.0>>

	* uni1E21 (U+1E21): L<<218.0,722.0>--<426.0,721.0>>

	* uni1E3E (U+1E3E): L<<354.0,0.0>--<29.0,-1.0>>

	* uni1E3E (U+1E3E): L<<739.0,-1.0>--<414.0,0.0>>

	* uni1E3F (U+1E3F): L<<354.0,0.0>--<29.0,-1.0>>

	* uni1E3F (U+1E3F): L<<739.0,-1.0>--<414.0,0.0>>

	* uni1E40 (U+1E40): L<<354.0,0.0>--<29.0,-1.0>>

	* uni1E40 (U+1E40): L<<739.0,-1.0>--<414.0,0.0>>

	* uni1E41 (U+1E41): L<<354.0,0.0>--<29.0,-1.0>>

	* uni1E41 (U+1E41): L<<739.0,-1.0>--<414.0,0.0>>

	* uni1E42 (U+1E42): L<<354.0,0.0>--<29.0,-1.0>>

	* uni1E42 (U+1E42): L<<739.0,-1.0>--<414.0,0.0>>

	* uni1E43 (U+1E43): L<<354.0,0.0>--<29.0,-1.0>>

	* uni1E43 (U+1E43): L<<739.0,-1.0>--<414.0,0.0>>

	* uni2074 (U+2074): L<<581.0,-1.0>--<31.0,-3.0>>

	* uni2075 (U+2075): L<<27.0,179.0>--<28.0,470.0>>

	* uni2075 (U+2075): L<<592.0,410.0>--<591.0,178.0>>

	* uni2076 (U+2076): L<<430.0,-6.0>--<216.0,-5.0>>

	* uni2077 (U+2077): L<<26.0,0.0>--<27.0,434.0>>

	* uni2077 (U+2077): L<<27.0,716.0>--<534.0,714.0>>

	* uni2077 (U+2077): L<<534.0,-1.0>--<26.0,0.0>>

	* uni2078 (U+2078): L<<189.0,716.0>--<451.0,715.0>>

	* uni2078 (U+2078): L<<431.0,-8.0>--<209.0,-7.0>>

	* uni2079 (U+2079): L<<24.0,180.0>--<25.0,470.0>>

	* uni2079 (U+2079): L<<399.0,-7.0>--<213.0,-6.0>>

	* uni2079 (U+2079): L<<589.0,550.0>--<588.0,179.0>>

	* uni2081 (U+2081): L<<210.0,715.0>--<397.0,716.0>>

	* uni2081 (U+2081): L<<397.0,716.0>--<398.0,495.0>>

	* uni2084 (U+2084): L<<581.0,-1.0>--<31.0,-3.0>>

	* uni2085 (U+2085): L<<27.0,179.0>--<28.0,470.0>>

	* uni2085 (U+2085): L<<592.0,410.0>--<591.0,178.0>>

	* uni2086 (U+2086): L<<430.0,-6.0>--<216.0,-5.0>>

	* uni2087 (U+2087): L<<26.0,0.0>--<27.0,434.0>>

	* uni2087 (U+2087): L<<27.0,716.0>--<534.0,714.0>>

	* uni2087 (U+2087): L<<534.0,-1.0>--<26.0,0.0>>

	* uni2088 (U+2088): L<<189.0,716.0>--<451.0,715.0>>

	* uni2088 (U+2088): L<<431.0,-8.0>--<209.0,-7.0>>

	* uni2089 (U+2089): L<<24.0,180.0>--<25.0,470.0>>

	* uni2089 (U+2089): L<<399.0,-7.0>--<213.0,-6.0>>

	* uni2089 (U+2089): L<<589.0,550.0>--<588.0,179.0>>

	* uni20AA (U+20AA): L<<179.0,-2.0>--<29.0,-3.0>>

	* uni20AA (U+20AA): L<<237.0,574.0>--<387.0,573.0>>

	* uni20AA (U+20AA): L<<29.0,719.0>--<444.0,717.0>>

	* uni20AA (U+20AA): L<<595.0,142.0>--<445.0,143.0>>

	* uni20AA (U+20AA): L<<653.0,718.0>--<803.0,719.0>>

	* uni20AA (U+20AA): L<<803.0,-3.0>--<388.0,-1.0>>

	* uni20BA (U+20BA): L<<238.0,-1.0>--<42.0,0.0>>

	* uni20BA (U+20BA): L<<42.0,0.0>--<43.0,434.0>>

	* uni20BC (U+20BC): L<<701.0,-2.0>--<394.0,-1.0>>

	* uni2126 (U+2126): L<<329.0,439.0>--<330.0,0.0>>

	* uni2126 (U+2126): L<<388.0,0.0>--<387.0,439.0>>

	* uni2196 (U+2196): L<<35.0,637.0>--<416.0,636.0>>

	* uni2197 (U+2197): L<<482.0,629.0>--<481.0,248.0>>

	* uni2198 (U+2198): L<<466.0,174.0>--<85.0,175.0>>

	* uni2199 (U+2199): L<<22.0,210.0>--<23.0,591.0>>

	* uni25B3 (U+25B3): L<<154.0,205.0>--<604.0,204.0>>

	* uni25B3 (U+25B3): L<<733.0,132.0>--<29.0,135.0>>

	* uni25B4 (U+25B4): L<<377.0,143.0>--<19.0,144.0>>

	* uni25B5 (U+25B5): L<<377.0,143.0>--<19.0,144.0>>

	* uni25B6 (U+25B6): L<<29.0,3.0>--<32.0,707.0>>

	* uni25B8 (U+25B8): L<<29.0,68.0>--<30.0,426.0>>

	* uni25B9 (U+25B9): L<<29.0,68.0>--<30.0,426.0>>

	* uni25BD (U+25BD): L<<29.0,728.0>--<733.0,725.0>>

	* uni25BD (U+25BD): L<<608.0,655.0>--<158.0,656.0>>

	* uni25BE (U+25BE): L<<10.0,434.0>--<368.0,433.0>>

	* uni25BF (U+25BF): L<<19.0,434.0>--<377.0,433.0>>

	* uni25C0 (U+25C0): L<<601.0,707.0>--<604.0,3.0>>

	* uni25C1 (U+25C1): L<<531.0,228.0>--<532.0,678.0>>

	* uni25C1 (U+25C1): L<<604.0,807.0>--<601.0,103.0>>

	* uni25C2 (U+25C2): L<<320.0,426.0>--<321.0,68.0>>

	* uni25C3 (U+25C3): L<<321.0,429.0>--<320.0,71.0>>

	* uniA78D (U+A78D): L<<642.0,0.0>--<330.0,-1.0>> [code: found-semi-vertical]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><br></div></details><details><summary><b>[20] Danfo-Regular0.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 fsType does not impose restrictions. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fstype">com.google.fonts/check/fstype</a>)</summary><div>


* 🔥 **FAIL** In this font fsType is set to 8 meaning that:
The font may be embedded but must only be installed temporarily on other systems.

No such DRM restrictions can be enabled on the Google Fonts collection, so the fsType field must be set to zero (Installable Embedding) instead. [code: drm]
</div></details><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0060 (GRAVE ACCENT)


	- 0x00A0 (NO-BREAK SPACE)


	- 0x00A8 (DIAERESIS)


	- 0x00AA (FEMININE ORDINAL INDICATOR)


	- 0x00AF (MACRON)


	- 0x00B4 (ACUTE ACCENT)


	- 0x00B8 (CEDILLA)


	- 0x00BA (MASCULINE ORDINAL INDICATOR)


	- 0x02C6 (MODIFIER LETTER CIRCUMFLEX ACCENT)


	- 0x02C7 (CARON)


	- 0x02D8 (BREVE)


	- 0x02D9 (DOT ABOVE)


	- 0x02DA (RING ABOVE)


	- 0x02DB (OGONEK)


	- 0x02DC (SMALL TILDE)


	- 0x02DD (DOUBLE ACUTE ACCENT)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font names are correct (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_names">com.google.fonts/check/font_names</a>)</summary><div>


* 🔥 **FAIL** Font names are incorrect:

| nameID | current | expected |
| :--- | :--- | :--- |
| Family Name | Danfo 0 | Danfo 0 |
| Subfamily Name | Regular | Regular |
| Full Name | **Danfo Regular 0** | **Danfo 0 Regular** |
| Postscript Name | **Danfo-Regular0** | **Danfo0-Regular** |
| Typographic Family Name | **Danfo** | **N/A** |
| Typographic Subfamily Name | **Regular 0** | **N/A** | [code: bad-names]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.sTypoLineGap is "200" it should be 0 [code: bad-OS/2.sTypoLineGap]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 219, but got 100 instead [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (900) and hhea ascent (1100) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Font contains glyphs for whitespace characters? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphs">com.google.fonts/check/whitespace_glyphs</a>)</summary><div>


* 🔥 **FAIL** Whitespace glyph missing for codepoint 0x00A0. [code: missing-whitespace-glyph-0x00A0]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* 🔥 **FAIL** The following glyphs have no contours even though they were expected to have some:

	- Glyph name: onequarter	Expected: 3 or 4

	- Glyph name: onehalf	Expected: 3

	- Glyph name: threequarters	Expected: 3 or 4

	- Glyph name: uni0312	Expected: 1

	- Glyph name: uni0334	Expected: 1

	- Glyph name: fraction	Expected: 1

	- Glyph name: uni2153	Expected: 3

	- Glyph name: uni2154	Expected: 1 or 3

	- Glyph name: fraction	Expected: 1

	- Glyph name: onehalf	Expected: 3

	- Glyph name: onequarter	Expected: 3 or 4

	- Glyph name: threequarters	Expected: 3 or 4

	- Glyph name: uni0312	Expected: 1
 [code: no-contour]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: B	Contours detected: 4	Expected: 2 or 3

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 3	Expected: 2

	- Glyph name: G	Contours detected: 2	Expected: 1

	- Glyph name: J	Contours detected: 3	Expected: 1

	- Glyph name: O	Contours detected: 4	Expected: 2

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: S	Contours detected: 3	Expected: 1

	- Glyph name: U	Contours detected: 2	Expected: 1

	- Glyph name: W	Contours detected: 5	Expected: 1 or 2

	- Glyph name: Y	Contours detected: 2	Expected: 1

	- Glyph name: b	Contours detected: 4	Expected: 2

	- Glyph name: c	Contours detected: 3	Expected: 1

	- Glyph name: d	Contours detected: 3	Expected: 2

	- Glyph name: e	Contours detected: 1	Expected: 2

	- Glyph name: i	Contours detected: 1	Expected: 2

	- Glyph name: j	Contours detected: 3	Expected: 2

	- Glyph name: o	Contours detected: 4	Expected: 2

	- Glyph name: q	Contours detected: 3	Expected: 2

	- Glyph name: r	Contours detected: 2	Expected: 1

	- Glyph name: s	Contours detected: 3	Expected: 1

	- Glyph name: u	Contours detected: 2	Expected: 1

	- Glyph name: w	Contours detected: 5	Expected: 1

	- Glyph name: y	Contours detected: 2	Expected: 1

	- Glyph name: Ccedilla	Contours detected: 4	Expected: 1 or 2

	- Glyph name: Ograve	Contours detected: 5	Expected: 3

	- Glyph name: Oacute	Contours detected: 5	Expected: 3

	- Glyph name: Ocircumflex	Contours detected: 5	Expected: 3

	- Glyph name: Otilde	Contours detected: 5	Expected: 3

	- Glyph name: Odieresis	Contours detected: 6	Expected: 4

	- Glyph name: Oslash	Contours detected: 4	Expected: 2 or 3

	- Glyph name: Ugrave	Contours detected: 3	Expected: 2

	- Glyph name: Uacute	Contours detected: 3	Expected: 2

	- Glyph name: Ucircumflex	Contours detected: 3	Expected: 2

	- Glyph name: Udieresis	Contours detected: 4	Expected: 3

	- Glyph name: Yacute	Contours detected: 3	Expected: 2

	- Glyph name: ae	Contours detected: 2	Expected: 3

	- Glyph name: ccedilla	Contours detected: 4	Expected: 1 or 2

	- Glyph name: egrave	Contours detected: 2	Expected: 3

	- Glyph name: eacute	Contours detected: 2	Expected: 3

	- Glyph name: edieresis	Contours detected: 3	Expected: 4

	- Glyph name: ograve	Contours detected: 5	Expected: 3

	- Glyph name: oacute	Contours detected: 5	Expected: 3

	- Glyph name: ocircumflex	Contours detected: 5	Expected: 3

	- Glyph name: otilde	Contours detected: 5	Expected: 3

	- Glyph name: odieresis	Contours detected: 6	Expected: 4

	- Glyph name: oslash	Contours detected: 4	Expected: 3

	- Glyph name: ugrave	Contours detected: 3	Expected: 2

	- Glyph name: uacute	Contours detected: 3	Expected: 2

	- Glyph name: ucircumflex	Contours detected: 3	Expected: 2

	- Glyph name: udieresis	Contours detected: 4	Expected: 3

	- Glyph name: yacute	Contours detected: 3	Expected: 2

	- Glyph name: ydieresis	Contours detected: 4	Expected: 3

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Cacute	Contours detected: 4	Expected: 2

	- Glyph name: cacute	Contours detected: 4	Expected: 2

	- Glyph name: Cdotaccent	Contours detected: 4	Expected: 2

	- Glyph name: cdotaccent	Contours detected: 4	Expected: 2

	- Glyph name: Ccaron	Contours detected: 4	Expected: 2

	- Glyph name: ccaron	Contours detected: 4	Expected: 2

	- Glyph name: Dcaron	Contours detected: 4	Expected: 3

	- Glyph name: dcaron	Contours detected: 4	Expected: 3

	- Glyph name: emacron	Contours detected: 2	Expected: 3

	- Glyph name: edotaccent	Contours detected: 2	Expected: 3

	- Glyph name: ecaron	Contours detected: 2	Expected: 3

	- Glyph name: Gbreve	Contours detected: 3	Expected: 2

	- Glyph name: Gdotaccent	Contours detected: 3	Expected: 2

	- Glyph name: uni0122	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: IJ	Contours detected: 4	Expected: 1 or 2

	- Glyph name: Jcircumflex	Contours detected: 4	Expected: 2

	- Glyph name: Omacron	Contours detected: 5	Expected: 3

	- Glyph name: omacron	Contours detected: 5	Expected: 3

	- Glyph name: Ohungarumlaut	Contours detected: 6	Expected: 4

	- Glyph name: ohungarumlaut	Contours detected: 6	Expected: 4

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: racute	Contours detected: 3	Expected: 2

	- Glyph name: uni0157	Contours detected: 3	Expected: 2

	- Glyph name: rcaron	Contours detected: 3	Expected: 2

	- Glyph name: Sacute	Contours detected: 4	Expected: 2

	- Glyph name: sacute	Contours detected: 4	Expected: 2

	- Glyph name: Scedilla	Contours detected: 4	Expected: 1 or 2

	- Glyph name: scedilla	Contours detected: 4	Expected: 1 or 2

	- Glyph name: Scaron	Contours detected: 4	Expected: 2

	- Glyph name: scaron	Contours detected: 4	Expected: 2

	- Glyph name: Utilde	Contours detected: 3	Expected: 2

	- Glyph name: utilde	Contours detected: 3	Expected: 2

	- Glyph name: Umacron	Contours detected: 3	Expected: 2

	- Glyph name: umacron	Contours detected: 3	Expected: 2

	- Glyph name: Ubreve	Contours detected: 3	Expected: 2

	- Glyph name: ubreve	Contours detected: 3	Expected: 2

	- Glyph name: Uring	Contours detected: 4	Expected: 3

	- Glyph name: uring	Contours detected: 4	Expected: 3

	- Glyph name: Uhungarumlaut	Contours detected: 4	Expected: 3

	- Glyph name: uhungarumlaut	Contours detected: 4	Expected: 3

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: Wcircumflex	Contours detected: 6	Expected: 2

	- Glyph name: wcircumflex	Contours detected: 6	Expected: 2

	- Glyph name: Ycircumflex	Contours detected: 3	Expected: 2

	- Glyph name: ycircumflex	Contours detected: 3	Expected: 2

	- Glyph name: Ydieresis	Contours detected: 4	Expected: 3

	- Glyph name: uni0180	Contours detected: 4	Expected: 2

	- Glyph name: uni0181	Contours detected: 5	Expected: 3

	- Glyph name: uni0186	Contours detected: 3	Expected: 1

	- Glyph name: uni0187	Contours detected: 4	Expected: 1

	- Glyph name: uni0188	Contours detected: 4	Expected: 1

	- Glyph name: uni018A	Contours detected: 4	Expected: 2

	- Glyph name: uni018F	Contours detected: 6	Expected: 2

	- Glyph name: uni0190	Contours detected: 3	Expected: 1

	- Glyph name: uni0191	Contours detected: 2	Expected: 1

	- Glyph name: uni0193	Contours detected: 2	Expected: 1

	- Glyph name: uni0197	Contours detected: 2	Expected: 1

	- Glyph name: uni0198	Contours detected: 2	Expected: 1

	- Glyph name: uni0199	Contours detected: 2	Expected: 1

	- Glyph name: uni019A	Contours detected: 2	Expected: 1

	- Glyph name: uni019B	Contours detected: 2	Expected: 1

	- Glyph name: Obarred	Contours detected: 5	Expected: 3

	- Glyph name: Ohorn	Contours detected: 5	Expected: 2 or 3

	- Glyph name: ohorn	Contours detected: 5	Expected: 2

	- Glyph name: uni01A4	Contours detected: 3	Expected: 2

	- Glyph name: uni01A5	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 3	Expected: 1

	- Glyph name: uhorn	Contours detected: 3	Expected: 1

	- Glyph name: uni01B2	Contours detected: 2	Expected: 1

	- Glyph name: uni01B3	Contours detected: 3	Expected: 1

	- Glyph name: uni01B4	Contours detected: 3	Expected: 1

	- Glyph name: uni01B7	Contours detected: 3	Expected: 1

	- Glyph name: uni01B8	Contours detected: 3	Expected: 1

	- Glyph name: uni01B9	Contours detected: 3	Expected: 1

	- Glyph name: uni01D1	Contours detected: 5	Expected: 3

	- Glyph name: uni01D2	Contours detected: 5	Expected: 3

	- Glyph name: uni01D3	Contours detected: 3	Expected: 2

	- Glyph name: uni01D4	Contours detected: 3	Expected: 2

	- Glyph name: uni01D5	Contours detected: 5	Expected: 4

	- Glyph name: uni01D6	Contours detected: 5	Expected: 4

	- Glyph name: uni01D7	Contours detected: 5	Expected: 4

	- Glyph name: uni01D8	Contours detected: 5	Expected: 4

	- Glyph name: uni01D9	Contours detected: 5	Expected: 4

	- Glyph name: uni01DA	Contours detected: 5	Expected: 4

	- Glyph name: uni01DB	Contours detected: 5	Expected: 4

	- Glyph name: uni01DC	Contours detected: 5	Expected: 4

	- Glyph name: uni01DD	Contours detected: 1	Expected: 2

	- Glyph name: uni01E3	Contours detected: 3	Expected: 4

	- Glyph name: uni01E4	Contours detected: 2	Expected: 1

	- Glyph name: Gcaron	Contours detected: 3	Expected: 2

	- Glyph name: uni01EA	Contours detected: 5	Expected: 2

	- Glyph name: uni01EB	Contours detected: 5	Expected: 2

	- Glyph name: uni01EC	Contours detected: 6	Expected: 3

	- Glyph name: uni01ED	Contours detected: 6	Expected: 3

	- Glyph name: uni01EE	Contours detected: 4	Expected: 2

	- Glyph name: uni01EF	Contours detected: 4	Expected: 2

	- Glyph name: uni01F4	Contours detected: 3	Expected: 2

	- Glyph name: Oslashacute	Contours detected: 5	Expected: 4

	- Glyph name: oslashacute	Contours detected: 5	Expected: 4

	- Glyph name: uni0205	Contours detected: 3	Expected: 4

	- Glyph name: uni0207	Contours detected: 2	Expected: 3

	- Glyph name: uni020C	Contours detected: 6	Expected: 4

	- Glyph name: uni020D	Contours detected: 6	Expected: 4

	- Glyph name: uni020E	Contours detected: 5	Expected: 3

	- Glyph name: uni020F	Contours detected: 5	Expected: 3

	- Glyph name: uni0211	Contours detected: 4	Expected: 3

	- Glyph name: uni0213	Contours detected: 3	Expected: 2

	- Glyph name: uni0214	Contours detected: 4	Expected: 3

	- Glyph name: uni0215	Contours detected: 4	Expected: 3

	- Glyph name: uni0216	Contours detected: 3	Expected: 2

	- Glyph name: uni0217	Contours detected: 3	Expected: 2

	- Glyph name: uni0218	Contours detected: 4	Expected: 2

	- Glyph name: uni0219	Contours detected: 4	Expected: 2

	- Glyph name: uni0222	Contours detected: 4	Expected: 2

	- Glyph name: uni0223	Contours detected: 4	Expected: 2

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni022A	Contours detected: 7	Expected: 5

	- Glyph name: uni022B	Contours detected: 7	Expected: 5

	- Glyph name: uni022C	Contours detected: 6	Expected: 4

	- Glyph name: uni022D	Contours detected: 6	Expected: 4

	- Glyph name: uni022E	Contours detected: 5	Expected: 3

	- Glyph name: uni022F	Contours detected: 5	Expected: 3

	- Glyph name: uni0230	Contours detected: 6	Expected: 4

	- Glyph name: uni0231	Contours detected: 6	Expected: 4

	- Glyph name: uni0232	Contours detected: 3	Expected: 2

	- Glyph name: uni0233	Contours detected: 3	Expected: 2

	- Glyph name: uni0237	Contours detected: 3	Expected: 1

	- Glyph name: uni023A	Contours detected: 2	Expected: 3

	- Glyph name: uni023B	Contours detected: 3	Expected: 2

	- Glyph name: uni023C	Contours detected: 3	Expected: 2

	- Glyph name: uni023D	Contours detected: 2	Expected: 1

	- Glyph name: uni023E	Contours detected: 1	Expected: 2

	- Glyph name: uni0243	Contours detected: 4	Expected: 3

	- Glyph name: uni0244	Contours detected: 3	Expected: 2

	- Glyph name: uni0247	Contours detected: 3	Expected: 4

	- Glyph name: uni0248	Contours detected: 4	Expected: 1

	- Glyph name: uni0249	Contours detected: 4	Expected: 2

	- Glyph name: uni024A	Contours detected: 3	Expected: 2

	- Glyph name: uni024B	Contours detected: 3	Expected: 2

	- Glyph name: uni024D	Contours detected: 2	Expected: 1

	- Glyph name: uni0251	Contours detected: 4	Expected: 2

	- Glyph name: uni0259	Contours detected: 6	Expected: 2

	- Glyph name: uni0292	Contours detected: 3	Expected: 1

	- Glyph name: uni1E02	Contours detected: 5	Expected: 4

	- Glyph name: uni1E03	Contours detected: 5	Expected: 3

	- Glyph name: uni1E08	Contours detected: 5	Expected: 2

	- Glyph name: uni1E09	Contours detected: 5	Expected: 2

	- Glyph name: uni1E0A	Contours detected: 4	Expected: 3

	- Glyph name: uni1E0B	Contours detected: 4	Expected: 3

	- Glyph name: uni1E0C	Contours detected: 4	Expected: 3

	- Glyph name: uni1E0D	Contours detected: 4	Expected: 3

	- Glyph name: Dmacronbelow	Contours detected: 4	Expected: 3

	- Glyph name: dmacronbelow	Contours detected: 4	Expected: 3

	- Glyph name: uni1E15	Contours detected: 3	Expected: 4

	- Glyph name: uni1E17	Contours detected: 3	Expected: 4

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E20	Contours detected: 3	Expected: 2

	- Glyph name: uni1E4C	Contours detected: 6	Expected: 4

	- Glyph name: uni1E4D	Contours detected: 6	Expected: 4

	- Glyph name: uni1E4E	Contours detected: 7	Expected: 5

	- Glyph name: uni1E4F	Contours detected: 7	Expected: 5

	- Glyph name: uni1E50	Contours detected: 6	Expected: 4

	- Glyph name: uni1E51	Contours detected: 6	Expected: 4

	- Glyph name: uni1E52	Contours detected: 6	Expected: 4

	- Glyph name: uni1E53	Contours detected: 6	Expected: 4

	- Glyph name: uni1E5B	Contours detected: 3	Expected: 2

	- Glyph name: uni1E5D	Contours detected: 4	Expected: 3

	- Glyph name: rmacronbelow	Contours detected: 3	Expected: 2

	- Glyph name: uni1E60	Contours detected: 4	Expected: 2

	- Glyph name: uni1E61	Contours detected: 4	Expected: 2

	- Glyph name: uni1E62	Contours detected: 4	Expected: 2

	- Glyph name: uni1E63	Contours detected: 4	Expected: 2

	- Glyph name: uni1E64	Contours detected: 5	Expected: 3

	- Glyph name: uni1E65	Contours detected: 5	Expected: 3

	- Glyph name: uni1E66	Contours detected: 5	Expected: 3

	- Glyph name: uni1E67	Contours detected: 5	Expected: 3

	- Glyph name: uni1E68	Contours detected: 5	Expected: 3

	- Glyph name: uni1E69	Contours detected: 5	Expected: 3

	- Glyph name: uni1E78	Contours detected: 4	Expected: 3

	- Glyph name: uni1E79	Contours detected: 4	Expected: 3

	- Glyph name: uni1E7A	Contours detected: 5	Expected: 4

	- Glyph name: uni1E7B	Contours detected: 5	Expected: 4

	- Glyph name: Wgrave	Contours detected: 6	Expected: 2

	- Glyph name: wgrave	Contours detected: 6	Expected: 2

	- Glyph name: Wacute	Contours detected: 6	Expected: 2

	- Glyph name: wacute	Contours detected: 6	Expected: 2

	- Glyph name: Wdieresis	Contours detected: 7	Expected: 3

	- Glyph name: wdieresis	Contours detected: 7	Expected: 3

	- Glyph name: uni1E8E	Contours detected: 3	Expected: 2

	- Glyph name: uni1E8F	Contours detected: 3	Expected: 2

	- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

	- Glyph name: uni1EBB	Contours detected: 2	Expected: 3

	- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

	- Glyph name: uni1EBF	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC1	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC3	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC5	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC7	Contours detected: 3	Expected: 4

	- Glyph name: uni1ECB	Contours detected: 2	Expected: 3

	- Glyph name: uni1ECC	Contours detected: 5	Expected: 3

	- Glyph name: uni1ECD	Contours detected: 5	Expected: 3

	- Glyph name: uni1ECE	Contours detected: 5	Expected: 3

	- Glyph name: uni1ECF	Contours detected: 5	Expected: 3

	- Glyph name: uni1ED0	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED1	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED2	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED3	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED4	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED5	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED6	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED7	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED8	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED9	Contours detected: 6	Expected: 4

	- Glyph name: uni1EDA	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EDB	Contours detected: 6	Expected: 3

	- Glyph name: uni1EDC	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EDD	Contours detected: 6	Expected: 3

	- Glyph name: uni1EDE	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EDF	Contours detected: 6	Expected: 3

	- Glyph name: uni1EE0	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EE1	Contours detected: 6	Expected: 3

	- Glyph name: uni1EE2	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EE3	Contours detected: 6	Expected: 3

	- Glyph name: uni1EE4	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE5	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE6	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE7	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE8	Contours detected: 4	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 4	Expected: 2

	- Glyph name: uni1EED	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 4	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 4	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 4	Expected: 2

	- Glyph name: Ygrave	Contours detected: 3	Expected: 2

	- Glyph name: ygrave	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF4	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF5	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF6	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF7	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF9	Contours detected: 3	Expected: 2

	- Glyph name: B	Contours detected: 4	Expected: 2 or 3

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: Cacute	Contours detected: 4	Expected: 2

	- Glyph name: Ccaron	Contours detected: 4	Expected: 2

	- Glyph name: Ccedilla	Contours detected: 4	Expected: 1 or 2

	- Glyph name: Cdotaccent	Contours detected: 4	Expected: 2

	- Glyph name: D	Contours detected: 3	Expected: 2

	- Glyph name: Dcaron	Contours detected: 4	Expected: 3

	- Glyph name: G	Contours detected: 2	Expected: 1

	- Glyph name: Gbreve	Contours detected: 3	Expected: 2

	- Glyph name: Gcaron	Contours detected: 3	Expected: 2

	- Glyph name: Gdotaccent	Contours detected: 3	Expected: 2

	- Glyph name: IJ	Contours detected: 4	Expected: 1 or 2

	- Glyph name: J	Contours detected: 3	Expected: 1

	- Glyph name: Jcircumflex	Contours detected: 4	Expected: 2

	- Glyph name: O	Contours detected: 4	Expected: 2

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: Oacute	Contours detected: 5	Expected: 3

	- Glyph name: Ocircumflex	Contours detected: 5	Expected: 3

	- Glyph name: Odieresis	Contours detected: 6	Expected: 4

	- Glyph name: Ograve	Contours detected: 5	Expected: 3

	- Glyph name: Ohorn	Contours detected: 5	Expected: 2 or 3

	- Glyph name: Ohungarumlaut	Contours detected: 6	Expected: 4

	- Glyph name: Omacron	Contours detected: 5	Expected: 3

	- Glyph name: Oslash	Contours detected: 4	Expected: 2 or 3

	- Glyph name: Oslashacute	Contours detected: 5	Expected: 4

	- Glyph name: Otilde	Contours detected: 5	Expected: 3

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: S	Contours detected: 3	Expected: 1

	- Glyph name: Sacute	Contours detected: 4	Expected: 2

	- Glyph name: Scaron	Contours detected: 4	Expected: 2

	- Glyph name: U	Contours detected: 2	Expected: 1

	- Glyph name: Uacute	Contours detected: 3	Expected: 2

	- Glyph name: Ubreve	Contours detected: 3	Expected: 2

	- Glyph name: Ucircumflex	Contours detected: 3	Expected: 2

	- Glyph name: Udieresis	Contours detected: 4	Expected: 3

	- Glyph name: Ugrave	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 3	Expected: 1

	- Glyph name: Uhungarumlaut	Contours detected: 4	Expected: 3

	- Glyph name: Umacron	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: Uring	Contours detected: 4	Expected: 3

	- Glyph name: Utilde	Contours detected: 3	Expected: 2

	- Glyph name: W	Contours detected: 5	Expected: 1 or 2

	- Glyph name: Wacute	Contours detected: 6	Expected: 2

	- Glyph name: Wcircumflex	Contours detected: 6	Expected: 2

	- Glyph name: Wdieresis	Contours detected: 7	Expected: 3

	- Glyph name: Wgrave	Contours detected: 6	Expected: 2

	- Glyph name: Y	Contours detected: 2	Expected: 1

	- Glyph name: Yacute	Contours detected: 3	Expected: 2

	- Glyph name: Ycircumflex	Contours detected: 3	Expected: 2

	- Glyph name: Ydieresis	Contours detected: 4	Expected: 3

	- Glyph name: Ygrave	Contours detected: 3	Expected: 2

	- Glyph name: ae	Contours detected: 2	Expected: 3

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: b	Contours detected: 4	Expected: 2

	- Glyph name: c	Contours detected: 3	Expected: 1

	- Glyph name: cacute	Contours detected: 4	Expected: 2

	- Glyph name: ccaron	Contours detected: 4	Expected: 2

	- Glyph name: ccedilla	Contours detected: 4	Expected: 1 or 2

	- Glyph name: cdotaccent	Contours detected: 4	Expected: 2

	- Glyph name: d	Contours detected: 3	Expected: 2

	- Glyph name: dcaron	Contours detected: 4	Expected: 3

	- Glyph name: e	Contours detected: 1	Expected: 2

	- Glyph name: eacute	Contours detected: 2	Expected: 3

	- Glyph name: ecaron	Contours detected: 2	Expected: 3

	- Glyph name: edieresis	Contours detected: 3	Expected: 4

	- Glyph name: edotaccent	Contours detected: 2	Expected: 3

	- Glyph name: egrave	Contours detected: 2	Expected: 3

	- Glyph name: emacron	Contours detected: 2	Expected: 3

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: i	Contours detected: 1	Expected: 2

	- Glyph name: j	Contours detected: 3	Expected: 2

	- Glyph name: o	Contours detected: 4	Expected: 2

	- Glyph name: oacute	Contours detected: 5	Expected: 3

	- Glyph name: ocircumflex	Contours detected: 5	Expected: 3

	- Glyph name: odieresis	Contours detected: 6	Expected: 4

	- Glyph name: ograve	Contours detected: 5	Expected: 3

	- Glyph name: ohorn	Contours detected: 5	Expected: 2

	- Glyph name: ohungarumlaut	Contours detected: 6	Expected: 4

	- Glyph name: omacron	Contours detected: 5	Expected: 3

	- Glyph name: oslash	Contours detected: 4	Expected: 3

	- Glyph name: oslashacute	Contours detected: 5	Expected: 4

	- Glyph name: otilde	Contours detected: 5	Expected: 3

	- Glyph name: q	Contours detected: 3	Expected: 2

	- Glyph name: r	Contours detected: 2	Expected: 1

	- Glyph name: racute	Contours detected: 3	Expected: 2

	- Glyph name: rcaron	Contours detected: 3	Expected: 2

	- Glyph name: s	Contours detected: 3	Expected: 1

	- Glyph name: sacute	Contours detected: 4	Expected: 2

	- Glyph name: scaron	Contours detected: 4	Expected: 2

	- Glyph name: u	Contours detected: 2	Expected: 1

	- Glyph name: uacute	Contours detected: 3	Expected: 2

	- Glyph name: ubreve	Contours detected: 3	Expected: 2

	- Glyph name: ucircumflex	Contours detected: 3	Expected: 2

	- Glyph name: udieresis	Contours detected: 4	Expected: 3

	- Glyph name: ugrave	Contours detected: 3	Expected: 2

	- Glyph name: uhorn	Contours detected: 3	Expected: 1

	- Glyph name: uhungarumlaut	Contours detected: 4	Expected: 3

	- Glyph name: umacron	Contours detected: 3	Expected: 2

	- Glyph name: uni0122	Contours detected: 3	Expected: 2

	- Glyph name: uni0157	Contours detected: 3	Expected: 2

	- Glyph name: uni0180	Contours detected: 4	Expected: 2

	- Glyph name: uni0181	Contours detected: 5	Expected: 3

	- Glyph name: uni0186	Contours detected: 3	Expected: 1

	- Glyph name: uni0187	Contours detected: 4	Expected: 1

	- Glyph name: uni0188	Contours detected: 4	Expected: 1

	- Glyph name: uni018A	Contours detected: 4	Expected: 2

	- Glyph name: uni018F	Contours detected: 6	Expected: 2

	- Glyph name: uni0190	Contours detected: 3	Expected: 1

	- Glyph name: uni0191	Contours detected: 2	Expected: 1

	- Glyph name: uni0193	Contours detected: 2	Expected: 1

	- Glyph name: uni0197	Contours detected: 2	Expected: 1

	- Glyph name: uni0198	Contours detected: 2	Expected: 1

	- Glyph name: uni0199	Contours detected: 2	Expected: 1

	- Glyph name: uni019A	Contours detected: 2	Expected: 1

	- Glyph name: uni019B	Contours detected: 2	Expected: 1

	- Glyph name: uni01A4	Contours detected: 3	Expected: 2

	- Glyph name: uni01A5	Contours detected: 3	Expected: 2

	- Glyph name: uni01B2	Contours detected: 2	Expected: 1

	- Glyph name: uni01B3	Contours detected: 3	Expected: 1

	- Glyph name: uni01B4	Contours detected: 3	Expected: 1

	- Glyph name: uni01B7	Contours detected: 3	Expected: 1

	- Glyph name: uni01B8	Contours detected: 3	Expected: 1

	- Glyph name: uni01B9	Contours detected: 3	Expected: 1

	- Glyph name: uni01D1	Contours detected: 5	Expected: 3

	- Glyph name: uni01D2	Contours detected: 5	Expected: 3

	- Glyph name: uni01D3	Contours detected: 3	Expected: 2

	- Glyph name: uni01D4	Contours detected: 3	Expected: 2

	- Glyph name: uni01D5	Contours detected: 5	Expected: 4

	- Glyph name: uni01D6	Contours detected: 5	Expected: 4

	- Glyph name: uni01D7	Contours detected: 5	Expected: 4

	- Glyph name: uni01D8	Contours detected: 5	Expected: 4

	- Glyph name: uni01D9	Contours detected: 5	Expected: 4

	- Glyph name: uni01DA	Contours detected: 5	Expected: 4

	- Glyph name: uni01DB	Contours detected: 5	Expected: 4

	- Glyph name: uni01DC	Contours detected: 5	Expected: 4

	- Glyph name: uni01DD	Contours detected: 1	Expected: 2

	- Glyph name: uni01E3	Contours detected: 3	Expected: 4

	- Glyph name: uni01E4	Contours detected: 2	Expected: 1

	- Glyph name: uni01EC	Contours detected: 6	Expected: 3

	- Glyph name: uni01ED	Contours detected: 6	Expected: 3

	- Glyph name: uni01EE	Contours detected: 4	Expected: 2

	- Glyph name: uni01EF	Contours detected: 4	Expected: 2

	- Glyph name: uni0218	Contours detected: 4	Expected: 2

	- Glyph name: uni0219	Contours detected: 4	Expected: 2

	- Glyph name: uni0222	Contours detected: 4	Expected: 2

	- Glyph name: uni0223	Contours detected: 4	Expected: 2

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni022A	Contours detected: 7	Expected: 5

	- Glyph name: uni022B	Contours detected: 7	Expected: 5

	- Glyph name: uni022C	Contours detected: 6	Expected: 4

	- Glyph name: uni022D	Contours detected: 6	Expected: 4

	- Glyph name: uni022E	Contours detected: 5	Expected: 3

	- Glyph name: uni022F	Contours detected: 5	Expected: 3

	- Glyph name: uni0230	Contours detected: 6	Expected: 4

	- Glyph name: uni0231	Contours detected: 6	Expected: 4

	- Glyph name: uni0232	Contours detected: 3	Expected: 2

	- Glyph name: uni0233	Contours detected: 3	Expected: 2

	- Glyph name: uni0237	Contours detected: 3	Expected: 1

	- Glyph name: uni023A	Contours detected: 2	Expected: 3

	- Glyph name: uni023B	Contours detected: 3	Expected: 2

	- Glyph name: uni023C	Contours detected: 3	Expected: 2

	- Glyph name: uni023D	Contours detected: 2	Expected: 1

	- Glyph name: uni023E	Contours detected: 1	Expected: 2

	- Glyph name: uni0243	Contours detected: 4	Expected: 3

	- Glyph name: uni0244	Contours detected: 3	Expected: 2

	- Glyph name: uni0247	Contours detected: 3	Expected: 4

	- Glyph name: uni0248	Contours detected: 4	Expected: 1

	- Glyph name: uni0249	Contours detected: 4	Expected: 2

	- Glyph name: uni024A	Contours detected: 3	Expected: 2

	- Glyph name: uni024B	Contours detected: 3	Expected: 2

	- Glyph name: uni024D	Contours detected: 2	Expected: 1

	- Glyph name: uni0251	Contours detected: 4	Expected: 2

	- Glyph name: uni0259	Contours detected: 6	Expected: 2

	- Glyph name: uni0292	Contours detected: 3	Expected: 1

	- Glyph name: uni1E02	Contours detected: 5	Expected: 4

	- Glyph name: uni1E03	Contours detected: 5	Expected: 3

	- Glyph name: uni1E08	Contours detected: 5	Expected: 2

	- Glyph name: uni1E09	Contours detected: 5	Expected: 2

	- Glyph name: uni1E0A	Contours detected: 4	Expected: 3

	- Glyph name: uni1E0B	Contours detected: 4	Expected: 3

	- Glyph name: uni1E0C	Contours detected: 4	Expected: 3

	- Glyph name: uni1E0D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E15	Contours detected: 3	Expected: 4

	- Glyph name: uni1E17	Contours detected: 3	Expected: 4

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E20	Contours detected: 3	Expected: 2

	- Glyph name: uni1E4C	Contours detected: 6	Expected: 4

	- Glyph name: uni1E4D	Contours detected: 6	Expected: 4

	- Glyph name: uni1E4E	Contours detected: 7	Expected: 5

	- Glyph name: uni1E4F	Contours detected: 7	Expected: 5

	- Glyph name: uni1E50	Contours detected: 6	Expected: 4

	- Glyph name: uni1E51	Contours detected: 6	Expected: 4

	- Glyph name: uni1E52	Contours detected: 6	Expected: 4

	- Glyph name: uni1E53	Contours detected: 6	Expected: 4

	- Glyph name: uni1E5B	Contours detected: 3	Expected: 2

	- Glyph name: uni1E5D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E60	Contours detected: 4	Expected: 2

	- Glyph name: uni1E61	Contours detected: 4	Expected: 2

	- Glyph name: uni1E62	Contours detected: 4	Expected: 2

	- Glyph name: uni1E63	Contours detected: 4	Expected: 2

	- Glyph name: uni1E64	Contours detected: 5	Expected: 3

	- Glyph name: uni1E65	Contours detected: 5	Expected: 3

	- Glyph name: uni1E66	Contours detected: 5	Expected: 3

	- Glyph name: uni1E67	Contours detected: 5	Expected: 3

	- Glyph name: uni1E68	Contours detected: 5	Expected: 3

	- Glyph name: uni1E69	Contours detected: 5	Expected: 3

	- Glyph name: uni1E78	Contours detected: 4	Expected: 3

	- Glyph name: uni1E79	Contours detected: 4	Expected: 3

	- Glyph name: uni1E7A	Contours detected: 5	Expected: 4

	- Glyph name: uni1E7B	Contours detected: 5	Expected: 4

	- Glyph name: uni1E8E	Contours detected: 3	Expected: 2

	- Glyph name: uni1E8F	Contours detected: 3	Expected: 2

	- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

	- Glyph name: uni1EBB	Contours detected: 2	Expected: 3

	- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

	- Glyph name: uni1EBF	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC1	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC3	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC5	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC7	Contours detected: 3	Expected: 4

	- Glyph name: uni1ECB	Contours detected: 2	Expected: 3

	- Glyph name: uni1ECC	Contours detected: 5	Expected: 3

	- Glyph name: uni1ECD	Contours detected: 5	Expected: 3

	- Glyph name: uni1ECE	Contours detected: 5	Expected: 3

	- Glyph name: uni1ECF	Contours detected: 5	Expected: 3

	- Glyph name: uni1ED0	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED1	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED2	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED3	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED4	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED5	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED6	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED7	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED8	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED9	Contours detected: 6	Expected: 4

	- Glyph name: uni1EDA	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EDB	Contours detected: 6	Expected: 3

	- Glyph name: uni1EDC	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EDD	Contours detected: 6	Expected: 3

	- Glyph name: uni1EDE	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EDF	Contours detected: 6	Expected: 3

	- Glyph name: uni1EE0	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EE1	Contours detected: 6	Expected: 3

	- Glyph name: uni1EE2	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EE3	Contours detected: 6	Expected: 3

	- Glyph name: uni1EE4	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE5	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE6	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE7	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE8	Contours detected: 4	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 4	Expected: 2

	- Glyph name: uni1EED	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 4	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 4	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 4	Expected: 2

	- Glyph name: uni1EF4	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF5	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF6	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF7	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF9	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uring	Contours detected: 4	Expected: 3

	- Glyph name: utilde	Contours detected: 3	Expected: 2

	- Glyph name: w	Contours detected: 5	Expected: 1

	- Glyph name: wacute	Contours detected: 6	Expected: 2

	- Glyph name: wcircumflex	Contours detected: 6	Expected: 2

	- Glyph name: wdieresis	Contours detected: 7	Expected: 3

	- Glyph name: wgrave	Contours detected: 6	Expected: 2

	- Glyph name: y	Contours detected: 2	Expected: 1

	- Glyph name: yacute	Contours detected: 3	Expected: 2

	- Glyph name: ycircumflex	Contours detected: 3	Expected: 2

	- Glyph name: ydieresis	Contours detected: 4	Expected: 3

	- Glyph name: ygrave	Contours detected: 3	Expected: 2
 [code: contour-count]
</div></details><details><summary>🔥 <b>FAIL:</b> Check accent of Lcaron, dcaron, lcaron, tcaron (derived from com.google.fonts/check/alt_caron) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/alt_caron">com.google.fonts/check/alt_caron</a>)</summary><div>


* 🔥 **FAIL** Lcaron uses component uni030C. [code: wrong-mark]
* 🔥 **FAIL** dcaron uses component uni030C. [code: wrong-mark]
* 🔥 **FAIL** lcaron uses component uni030C. [code: wrong-mark]
* 🔥 **FAIL** tcaron uses component uni030C. [code: wrong-mark]
</div></details><details><summary>🔥 <b>FAIL:</b> Does full font name begin with the font family name? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/name/match_familyname_fullfont">com.google.fonts/check/name/match_familyname_fullfont</a>)</summary><div>


* 🔥 **FAIL** On the 'name' table, the full font name 'Danfo Regular 0' does not begin with the font family name 'Danfo 0' in platformID 3, encodingID 1, languageID 1033(0409), and nameID 1. [code: mismatch-font-names]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Check for codepoints not covered by METADATA subsets. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/unreachable_subsetting">com.google.fonts/check/metadata/unreachable_subsetting</a>)</summary><div>


* ⚠ **WARN** The following codepoints supported by the font are not covered by
    any subsets defined in the font's metadata file, and will never
    be served. You can solve this by either manually adding additional
    subset declarations to METADATA.pb, or by editing the glyphset
    definitions.

 * U+02D7 MODIFIER LETTER MINUS SIGN: not included in any glyphset definition
 * U+02EE MODIFIER LETTER DOUBLE APOSTROPHE: not included in any glyphset definition
 * U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, math, tifinagh, cherokee
 * U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic
 * U+0307 COMBINING DOT ABOVE: try adding one of: math, tai-le, malayalam, syriac, canadian-aboriginal, old-permic, coptic, tifinagh
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
 * U+0324 COMBINING DIAERESIS BELOW: try adding one of: syriac, cherokee
 * U+0325 COMBINING RING BELOW: try adding syriac
 * U+0326 COMBINING COMMA BELOW: not included in any glyphset definition
 * U+0327 COMBINING CEDILLA: not included in any glyphset definition
 * U+0328 COMBINING OGONEK: not included in any glyphset definition
 * U+032D COMBINING CIRCUMFLEX ACCENT BELOW: try adding syriac
 * U+032E COMBINING BREVE BELOW: try adding syriac
 * U+032F COMBINING INVERTED BREVE BELOW: not included in any glyphset definition
 * U+0330 COMBINING TILDE BELOW: try adding one of: math, syriac, cherokee
 * U+0331 COMBINING MACRON BELOW: try adding one of: syriac, cherokee, gothic, caucasian-albanian, tifinagh
 * U+0332 COMBINING LOW LINE: not included in any glyphset definition
 * U+0334 COMBINING TILDE OVERLAY: not included in any glyphset definition
 * U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition
 * U+0358 COMBINING DOT ABOVE RIGHT: try adding osage
 * U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai
 * U+1D7D LATIN SMALL LETTER P WITH STROKE: not included in any glyphset definition
 * U+1DC4 COMBINING MACRON-ACUTE: not included in any glyphset definition
 * U+1DC5 COMBINING GRAVE-MACRON: not included in any glyphset definition
 * U+1DC6 COMBINING MACRON-GRAVE: not included in any glyphset definition
 * U+1DC7 COMBINING ACUTE-MACRON: not included in any glyphset definition
 * U+1DCA COMBINING LATIN SMALL LETTER R BELOW: not included in any glyphset definition
 * U+2016 DOUBLE VERTICAL LINE: not included in any glyphset definition
 * U+2021 DOUBLE DAGGER: try adding adlam
 * U+2030 PER MILLE SIGN: try adding adlam
 * U+2075 SUPERSCRIPT FIVE: not included in any glyphset definition
 * U+2076 SUPERSCRIPT SIX: not included in any glyphset definition
 * U+2077 SUPERSCRIPT SEVEN: not included in any glyphset definition
 * U+2078 SUPERSCRIPT EIGHT: not included in any glyphset definition
 * U+2079 SUPERSCRIPT NINE: not included in any glyphset definition
 * U+2081 SUBSCRIPT ONE: not included in any glyphset definition
 * U+2082 SUBSCRIPT TWO: not included in any glyphset definition
 * U+2083 SUBSCRIPT THREE: not included in any glyphset definition
 * U+2084 SUBSCRIPT FOUR: not included in any glyphset definition
 * U+2085 SUBSCRIPT FIVE: not included in any glyphset definition
 * U+2086 SUBSCRIPT SIX: not included in any glyphset definition
 * U+2087 SUBSCRIPT SEVEN: not included in any glyphset definition
 * U+2088 SUBSCRIPT EIGHT: not included in any glyphset definition
 * U+2089 SUBSCRIPT NINE: not included in any glyphset definition
 * U+2126 OHM SIGN: not included in any glyphset definition
 * U+212E ESTIMATED SYMBOL: not included in any glyphset definition
 * U+2153 VULGAR FRACTION ONE THIRD: not included in any glyphset definition
 * U+2154 VULGAR FRACTION TWO THIRDS: not included in any glyphset definition
 * U+2190 LEFTWARDS ARROW: try adding one of: math, symbols
 * U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols
 * U+2194 LEFT RIGHT ARROW: try adding one of: math, emoji, symbols
 * U+2195 UP DOWN ARROW: try adding one of: math, emoji, symbols
 * U+2196 NORTH WEST ARROW: try adding one of: math, emoji, symbols
 * U+2197 NORTH EAST ARROW: try adding one of: math, emoji, symbols
 * U+2198 SOUTH EAST ARROW: try adding one of: math, emoji, symbols
 * U+2199 SOUTH WEST ARROW: try adding one of: math, emoji, symbols
 * U+2202 PARTIAL DIFFERENTIAL: try adding math
 * U+2205 EMPTY SET: try adding math
 * U+2206 INCREMENT: try adding math
 * U+220F N-ARY PRODUCT: try adding math
 * U+2211 N-ARY SUMMATION: try adding math
 * U+221A SQUARE ROOT: try adding math
 * U+221E INFINITY: try adding math
 * U+222B INTEGRAL: try adding math
 * U+2248 ALMOST EQUAL TO: try adding math
 * U+2260 NOT EQUAL TO: try adding math
 * U+2264 LESS-THAN OR EQUAL TO: try adding math
 * U+2265 GREATER-THAN OR EQUAL TO: try adding math
 * U+25A0 BLACK SQUARE: try adding symbols
 * U+25A1 WHITE SQUARE: try adding symbols
 * U+25AA BLACK SMALL SQUARE: try adding one of: emoji, symbols
 * U+25AB WHITE SMALL SQUARE: try adding one of: emoji, symbols
 * U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols
 * U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: math, symbols
 * U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols
 * U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols
 * U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding one of: emoji, symbols
 * U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: math, symbols
 * U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols
 * U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols
 * U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols
 * U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: math, symbols
 * U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols
 * U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols
 * U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding one of: emoji, symbols
 * U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: math, symbols
 * U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols
 * U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols
 * U+25C6 BLACK DIAMOND: try adding symbols
 * U+25C7 WHITE DIAMOND: try adding symbols
 * U+25CA LOZENGE: try adding one of: math, symbols
 * U+25CB WHITE CIRCLE: try adding symbols
 * U+25CF BLACK CIRCLE: try adding symbols
 * U+25E6 WHITE BULLET: try adding symbols
 * U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math
 * U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math
 * U+3008 LEFT ANGLE BRACKET: try adding one of: tai-le, japanese, yi, chinese-traditional, phags-pa, chinese-hongkong, chinese-simplified
 * U+3009 RIGHT ANGLE BRACKET: try adding one of: tai-le, japanese, yi, chinese-traditional, phags-pa, chinese-hongkong, chinese-simplified
 * U+AB53 LATIN SMALL LETTER CHI: not included in any glyphset definition
 * U+FF0D FULLWIDTH HYPHEN-MINUS: try adding chinese-simplified

Or you can add the above codepoints to one of the subsets supported by the font: `cyrillic-ext`, `latin`, `latin-ext`, `vietnamese` [code: unreachable-subsetting]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- _part.cut

	- hook.part
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 298 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 279:
less, greater

Width = 326:
equal

Width = 306:
logicalnot

Width = 284:
multiply

Width = 316:
divide

Width = 286:
minus

Width = 330:
approxequal

Width = 339:
notequal

Width = 287:
lessequal, greaterequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** OS/2 sTypoLineGap is not equal to 0. [code: OS/2]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Euro (U+20AC): L<<231.0,550.0>--<231.0,547.0>> -> L<<231.0,547.0>--<231.0,519.0>>

	* V (U+0056): L<<100.0,210.0>--<100.0,141.0>> -> L<<100.0,141.0>--<100.0,140.0>>

	* V (U+0056): L<<76.0,334.0>--<76.0,267.0>> -> L<<76.0,267.0>--<76.0,265.0>>

	* paragraph (U+00B6): L<<182.0,715.0>--<491.0,716.0>> -> L<<491.0,716.0>--<648.0,716.0>>

	* section (U+00A7): L<<268.0,464.0>--<326.0,459.0>> -> L<<326.0,459.0>--<344.0,457.0>>

	* uni018F (U+018F): L<<19.0,265.0>--<19.0,260.0>> -> L<<19.0,260.0>--<19.0,259.0>>

	* uni0222 (U+0222): L<<275.0,430.0>--<332.0,429.0>> -> L<<332.0,429.0>--<369.0,430.0>>

	* uni0223 (U+0223): L<<275.0,430.0>--<332.0,429.0>> -> L<<332.0,429.0>--<369.0,430.0>>

	* uni024E (U+024E): L<<421.0,491.0>--<110.0,517.0>> -> L<<110.0,517.0>--<27.0,517.0>>

	* uni024F (U+024F): L<<421.0,491.0>--<110.0,517.0>> -> L<<110.0,517.0>--<27.0,517.0>>

	* uni0259 (U+0259): L<<19.0,265.0>--<19.0,260.0>> -> L<<19.0,260.0>--<19.0,259.0>>

	* uni1E7C (U+1E7C): L<<100.0,210.0>--<100.0,141.0>> -> L<<100.0,141.0>--<100.0,140.0>>

	* uni1E7C (U+1E7C): L<<76.0,334.0>--<76.0,267.0>> -> L<<76.0,267.0>--<76.0,265.0>>

	* uni1E7D (U+1E7D): L<<100.0,210.0>--<100.0,141.0>> -> L<<100.0,141.0>--<100.0,140.0>>

	* uni1E7D (U+1E7D): L<<76.0,334.0>--<76.0,267.0>> -> L<<76.0,267.0>--<76.0,265.0>>

	* uni1E7E (U+1E7E): L<<100.0,210.0>--<100.0,141.0>> -> L<<100.0,141.0>--<100.0,140.0>>

	* uni1E7E (U+1E7E): L<<76.0,334.0>--<76.0,267.0>> -> L<<76.0,267.0>--<76.0,265.0>>

	* uni1E7F (U+1E7F): L<<100.0,210.0>--<100.0,141.0>> -> L<<100.0,141.0>--<100.0,140.0>>

	* uni1E7F (U+1E7F): L<<76.0,334.0>--<76.0,267.0>> -> L<<76.0,267.0>--<76.0,265.0>>

	* uni2C60 (U+2C60): L<<29.0,203.0>--<29.0,142.0>> -> L<<29.0,142.0>--<29.0,136.0>>

	* uni2C60 (U+2C60): L<<29.0,210.0>--<29.0,203.0>> -> L<<29.0,203.0>--<29.0,142.0>>

	* uni2C61 (U+2C61): L<<29.0,203.0>--<29.0,142.0>> -> L<<29.0,142.0>--<29.0,136.0>>

	* uni2C61 (U+2C61): L<<29.0,210.0>--<29.0,203.0>> -> L<<29.0,203.0>--<29.0,142.0>>

	* uniA7B8 (U+A7B8): L<<337.0,-6.0>--<225.0,-6.0>> -> L<<225.0,-6.0>--<223.0,-6.0>>

	* uniA7B9 (U+A7B9): L<<337.0,-6.0>--<225.0,-6.0>> -> L<<225.0,-6.0>--<223.0,-6.0>>

	* v (U+0076): L<<100.0,210.0>--<100.0,141.0>> -> L<<100.0,141.0>--<100.0,140.0>>

	* v (U+0076): L<<76.0,334.0>--<76.0,267.0>> -> L<<76.0,267.0>--<76.0,265.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* Euro (U+20AC): L<<218.0,722.0>--<426.0,721.0>>

	* G (U+0047): L<<218.0,722.0>--<426.0,721.0>>

	* Gbreve (U+011E): L<<218.0,722.0>--<426.0,721.0>>

	* Gcaron (U+01E6): L<<218.0,722.0>--<426.0,721.0>>

	* Gdotaccent (U+0120): L<<218.0,722.0>--<426.0,721.0>>

	* Glottalstopsmall (U+0241): L<<161.0,721.0>--<334.0,722.0>>

	* M (U+004D): L<<354.0,0.0>--<29.0,-1.0>>

	* M (U+004D): L<<739.0,-1.0>--<414.0,0.0>>

	* Ohungarumlaut (U+0150): L<<393.0,877.0>--<511.0,878.0>>

	* Thorn (U+00DE): L<<267.0,588.0>--<470.0,587.0>>

	* Thorn (U+00DE): L<<29.0,716.0>--<331.0,715.0>>

	* Thorn (U+00DE): L<<331.0,-1.0>--<29.0,0.0>>

	* Thorn (U+00DE): L<<484.0,368.0>--<266.0,369.0>>

	* Uhungarumlaut (U+0170): L<<422.0,877.0>--<540.0,878.0>>

	* ampersand (U+0026): L<<408.0,540.0>--<676.0,538.0>>

	* arrowboth (U+2194): L<<300.0,324.0>--<299.0,103.0>>

	* arrowboth (U+2194): L<<301.0,644.0>--<300.0,424.0>>

	* arrowboth (U+2194): L<<478.0,424.0>--<477.0,644.0>>

	* arrowboth (U+2194): L<<479.0,103.0>--<478.0,324.0>>

	* arrowdown (U+2193): L<<18.0,397.0>--<238.0,396.0>>

	* arrowdown (U+2193): L<<337.0,396.0>--<559.0,395.0>>

	* arrowdown (U+2193): L<<338.0,704.0>--<337.0,396.0>>

	* arrowleft (U+2190): L<<299.0,691.0>--<300.0,469.0>>

	* arrowleft (U+2190): L<<300.0,370.0>--<301.0,150.0>>

	* arrowleft (U+2190): L<<300.0,469.0>--<608.0,470.0>>

	* arrowright (U+2192): L<<337.0,342.0>--<29.0,341.0>>

	* arrowright (U+2192): L<<337.0,441.0>--<336.0,661.0>>

	* arrowright (U+2192): L<<338.0,120.0>--<337.0,342.0>>

	* arrowup (U+2191): L<<239.0,433.0>--<19.0,432.0>>

	* arrowup (U+2191): L<<338.0,433.0>--<339.0,125.0>>

	* arrowup (U+2191): L<<560.0,434.0>--<338.0,433.0>>

	* arrowupdn (U+2195): L<<10.0,287.0>--<231.0,288.0>>

	* arrowupdn (U+2195): L<<231.0,466.0>--<10.0,467.0>>

	* arrowupdn (U+2195): L<<331.0,288.0>--<551.0,289.0>>

	* arrowupdn (U+2195): L<<551.0,465.0>--<331.0,466.0>>

	* bracketleft (U+005B): L<<190.0,757.0>--<188.0,-44.0>>

	* bracketleft (U+005B): L<<29.0,-125.0>--<32.0,837.0>>

	* bracketright (U+005D): L<<166.0,-40.0>--<168.0,761.0>>

	* bracketright (U+005D): L<<327.0,842.0>--<324.0,-120.0>>

	* eight (U+0038): L<<189.0,716.0>--<451.0,715.0>>

	* eight (U+0038): L<<431.0,-8.0>--<209.0,-7.0>>

	* exclam (U+0021): L<<30.0,723.0>--<252.0,724.0>>

	* exclamdown (U+00A1): L<<260.0,-140.0>--<38.0,-141.0>>

	* five (U+0035): L<<27.0,179.0>--<28.0,470.0>>

	* five (U+0035): L<<592.0,410.0>--<591.0,178.0>>

	* florin (U+0192): L<<29.0,0.0>--<30.0,434.0>>

	* four (U+0034): L<<581.0,-1.0>--<31.0,-3.0>>

	* g (U+0067): L<<218.0,722.0>--<426.0,721.0>>

	* gbreve (U+011F): L<<218.0,722.0>--<426.0,721.0>>

	* gcaron (U+01E7): L<<218.0,722.0>--<426.0,721.0>>

	* gdotaccent (U+0121): L<<218.0,722.0>--<426.0,721.0>>

	* m (U+006D): L<<354.0,0.0>--<29.0,-1.0>>

	* m (U+006D): L<<739.0,-1.0>--<414.0,0.0>>

	* minute (U+2032): L<<60.0,717.0>--<287.0,716.0>>

	* nine (U+0039): L<<24.0,180.0>--<25.0,470.0>>

	* nine (U+0039): L<<399.0,-7.0>--<213.0,-6.0>>

	* nine (U+0039): L<<589.0,550.0>--<588.0,179.0>>

	* nlongrightleg (U+019E): L<<667.0,-139.0>--<375.0,-138.0>>

	* ohungarumlaut (U+0151): L<<393.0,877.0>--<511.0,878.0>>

	* one (U+0031): L<<210.0,715.0>--<397.0,716.0>>

	* one (U+0031): L<<397.0,716.0>--<398.0,495.0>>

	* paragraph (U+00B6): L<<182.0,715.0>--<491.0,716.0>>

	* percent (U+0025): L<<481.0,722.0>--<599.0,721.0>>

	* perthousand (U+2030): L<<481.0,722.0>--<599.0,721.0>>

	* radical (U+221A): L<<376.0,-101.0>--<181.0,-100.0>>

	* radical (U+221A): L<<512.0,899.0>--<636.0,898.0>>

	* second (U+2033): L<<316.0,717.0>--<543.0,716.0>>

	* second (U+2033): L<<60.0,717.0>--<287.0,716.0>>

	* seven (U+0037): L<<26.0,0.0>--<27.0,434.0>>

	* seven (U+0037): L<<27.0,716.0>--<534.0,714.0>>

	* seven (U+0037): L<<534.0,-1.0>--<26.0,0.0>>

	* six (U+0036): L<<430.0,-6.0>--<216.0,-5.0>>

	* sterling (U+00A3): L<<564.0,589.0>--<393.0,590.0>>

	* thorn (U+00FE): L<<267.0,588.0>--<470.0,587.0>>

	* thorn (U+00FE): L<<29.0,716.0>--<331.0,715.0>>

	* thorn (U+00FE): L<<331.0,-1.0>--<29.0,0.0>>

	* thorn (U+00FE): L<<484.0,368.0>--<266.0,369.0>>

	* triagdn (U+25BC): L<<29.0,731.0>--<733.0,728.0>>

	* triagup (U+25B2): L<<733.0,141.0>--<29.0,144.0>>

	* uhungarumlaut (U+0171): L<<422.0,877.0>--<540.0,878.0>>

	* uni00B9 (U+00B9): L<<210.0,715.0>--<397.0,716.0>>

	* uni00B9 (U+00B9): L<<397.0,716.0>--<398.0,495.0>>

	* uni0122 (U+0122): L<<218.0,722.0>--<426.0,721.0>>

	* uni0123 (U+0123): L<<218.0,722.0>--<426.0,721.0>>

	* uni0190 (U+0190): L<<189.0,716.0>--<416.0,715.0>>

	* uni0190 (U+0190): L<<403.0,-8.0>--<209.0,-7.0>>

	* uni0193 (U+0193): L<<218.0,722.0>--<426.0,721.0>>

	* uni019C (U+019C): L<<29.0,717.0>--<354.0,716.0>>

	* uni019C (U+019C): L<<414.0,716.0>--<739.0,717.0>>

	* uni01A9 (U+01A9): L<<27.0,716.0>--<540.0,714.0>>

	* uni01A9 (U+01A9): L<<541.0,-2.0>--<27.0,0.0>>

	* uni01B7 (U+01B7): L<<44.0,715.0>--<557.0,716.0>>

	* uni01B8 (U+01B8): L<<53.0,716.0>--<566.0,715.0>>

	* uni01B9 (U+01B9): L<<53.0,716.0>--<566.0,715.0>>

	* uni01E4 (U+01E4): L<<218.0,722.0>--<426.0,721.0>>

	* uni01E5 (U+01E5): L<<218.0,722.0>--<426.0,721.0>>

	* uni01EE (U+01EE): L<<44.0,715.0>--<557.0,716.0>>

	* uni01EF (U+01EF): L<<44.0,715.0>--<557.0,716.0>>

	* uni01F4 (U+01F4): L<<218.0,722.0>--<426.0,721.0>>

	* uni01F5 (U+01F5): L<<218.0,722.0>--<426.0,721.0>>

	* uni0220 (U+0220): L<<667.0,-139.0>--<375.0,-138.0>>

	* uni0242 (U+0242): L<<161.0,558.0>--<334.0,559.0>>

	* uni025B (U+025B): L<<189.0,716.0>--<416.0,715.0>>

	* uni025B (U+025B): L<<403.0,-8.0>--<209.0,-7.0>>

	* uni0260 (U+0260): L<<218.0,722.0>--<426.0,721.0>>

	* uni0265 (U+0265): L<<642.0,0.0>--<330.0,-1.0>>

	* uni026F (U+026F): L<<29.0,717.0>--<354.0,716.0>>

	* uni026F (U+026F): L<<414.0,716.0>--<739.0,717.0>>

	* uni0292 (U+0292): L<<44.0,715.0>--<557.0,716.0>>

	* uni0294 (U+0294): L<<161.0,721.0>--<334.0,722.0>>

	* uni0295 (U+0295): L<<219.0,722.0>--<392.0,721.0>>

	* uni030B (U+030B): L<<202.0,768.0>--<320.0,769.0>>

	* uni1E20 (U+1E20): L<<218.0,722.0>--<426.0,721.0>>

	* uni1E21 (U+1E21): L<<218.0,722.0>--<426.0,721.0>>

	* uni1E3E (U+1E3E): L<<354.0,0.0>--<29.0,-1.0>>

	* uni1E3E (U+1E3E): L<<739.0,-1.0>--<414.0,0.0>>

	* uni1E3F (U+1E3F): L<<354.0,0.0>--<29.0,-1.0>>

	* uni1E3F (U+1E3F): L<<739.0,-1.0>--<414.0,0.0>>

	* uni1E40 (U+1E40): L<<354.0,0.0>--<29.0,-1.0>>

	* uni1E40 (U+1E40): L<<739.0,-1.0>--<414.0,0.0>>

	* uni1E41 (U+1E41): L<<354.0,0.0>--<29.0,-1.0>>

	* uni1E41 (U+1E41): L<<739.0,-1.0>--<414.0,0.0>>

	* uni1E42 (U+1E42): L<<354.0,0.0>--<29.0,-1.0>>

	* uni1E42 (U+1E42): L<<739.0,-1.0>--<414.0,0.0>>

	* uni1E43 (U+1E43): L<<354.0,0.0>--<29.0,-1.0>>

	* uni1E43 (U+1E43): L<<739.0,-1.0>--<414.0,0.0>>

	* uni2074 (U+2074): L<<581.0,-1.0>--<31.0,-3.0>>

	* uni2075 (U+2075): L<<27.0,179.0>--<28.0,470.0>>

	* uni2075 (U+2075): L<<592.0,410.0>--<591.0,178.0>>

	* uni2076 (U+2076): L<<430.0,-6.0>--<216.0,-5.0>>

	* uni2077 (U+2077): L<<26.0,0.0>--<27.0,434.0>>

	* uni2077 (U+2077): L<<27.0,716.0>--<534.0,714.0>>

	* uni2077 (U+2077): L<<534.0,-1.0>--<26.0,0.0>>

	* uni2078 (U+2078): L<<189.0,716.0>--<451.0,715.0>>

	* uni2078 (U+2078): L<<431.0,-8.0>--<209.0,-7.0>>

	* uni2079 (U+2079): L<<24.0,180.0>--<25.0,470.0>>

	* uni2079 (U+2079): L<<399.0,-7.0>--<213.0,-6.0>>

	* uni2079 (U+2079): L<<589.0,550.0>--<588.0,179.0>>

	* uni2081 (U+2081): L<<210.0,715.0>--<397.0,716.0>>

	* uni2081 (U+2081): L<<397.0,716.0>--<398.0,495.0>>

	* uni2084 (U+2084): L<<581.0,-1.0>--<31.0,-3.0>>

	* uni2085 (U+2085): L<<27.0,179.0>--<28.0,470.0>>

	* uni2085 (U+2085): L<<592.0,410.0>--<591.0,178.0>>

	* uni2086 (U+2086): L<<430.0,-6.0>--<216.0,-5.0>>

	* uni2087 (U+2087): L<<26.0,0.0>--<27.0,434.0>>

	* uni2087 (U+2087): L<<27.0,716.0>--<534.0,714.0>>

	* uni2087 (U+2087): L<<534.0,-1.0>--<26.0,0.0>>

	* uni2088 (U+2088): L<<189.0,716.0>--<451.0,715.0>>

	* uni2088 (U+2088): L<<431.0,-8.0>--<209.0,-7.0>>

	* uni2089 (U+2089): L<<24.0,180.0>--<25.0,470.0>>

	* uni2089 (U+2089): L<<399.0,-7.0>--<213.0,-6.0>>

	* uni2089 (U+2089): L<<589.0,550.0>--<588.0,179.0>>

	* uni20AA (U+20AA): L<<179.0,-2.0>--<29.0,-3.0>>

	* uni20AA (U+20AA): L<<237.0,574.0>--<387.0,573.0>>

	* uni20AA (U+20AA): L<<29.0,719.0>--<444.0,717.0>>

	* uni20AA (U+20AA): L<<595.0,142.0>--<445.0,143.0>>

	* uni20AA (U+20AA): L<<653.0,718.0>--<803.0,719.0>>

	* uni20AA (U+20AA): L<<803.0,-3.0>--<388.0,-1.0>>

	* uni20BA (U+20BA): L<<238.0,-1.0>--<42.0,0.0>>

	* uni20BA (U+20BA): L<<42.0,0.0>--<43.0,434.0>>

	* uni20BC (U+20BC): L<<701.0,-2.0>--<394.0,-1.0>>

	* uni2126 (U+2126): L<<329.0,439.0>--<330.0,0.0>>

	* uni2126 (U+2126): L<<388.0,0.0>--<387.0,439.0>>

	* uni2196 (U+2196): L<<35.0,637.0>--<416.0,636.0>>

	* uni2197 (U+2197): L<<482.0,629.0>--<481.0,248.0>>

	* uni2198 (U+2198): L<<466.0,174.0>--<85.0,175.0>>

	* uni2199 (U+2199): L<<22.0,210.0>--<23.0,591.0>>

	* uni25B3 (U+25B3): L<<154.0,205.0>--<604.0,204.0>>

	* uni25B3 (U+25B3): L<<733.0,132.0>--<29.0,135.0>>

	* uni25B4 (U+25B4): L<<377.0,143.0>--<19.0,144.0>>

	* uni25B5 (U+25B5): L<<377.0,143.0>--<19.0,144.0>>

	* uni25B6 (U+25B6): L<<29.0,3.0>--<32.0,707.0>>

	* uni25B8 (U+25B8): L<<29.0,68.0>--<30.0,426.0>>

	* uni25B9 (U+25B9): L<<29.0,68.0>--<30.0,426.0>>

	* uni25BD (U+25BD): L<<29.0,728.0>--<733.0,725.0>>

	* uni25BD (U+25BD): L<<608.0,655.0>--<158.0,656.0>>

	* uni25BE (U+25BE): L<<10.0,434.0>--<368.0,433.0>>

	* uni25BF (U+25BF): L<<19.0,434.0>--<377.0,433.0>>

	* uni25C0 (U+25C0): L<<601.0,707.0>--<604.0,3.0>>

	* uni25C1 (U+25C1): L<<531.0,228.0>--<532.0,678.0>>

	* uni25C1 (U+25C1): L<<604.0,807.0>--<601.0,103.0>>

	* uni25C2 (U+25C2): L<<320.0,426.0>--<321.0,68.0>>

	* uni25C3 (U+25C3): L<<321.0,429.0>--<320.0,71.0>>

	* uniA78D (U+A78D): L<<642.0,0.0>--<330.0,-1.0>> [code: found-semi-vertical]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><br></div></details><details><summary><b>[21] Danfo-Regular100.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 fsType does not impose restrictions. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fstype">com.google.fonts/check/fstype</a>)</summary><div>


* 🔥 **FAIL** In this font fsType is set to 8 meaning that:
The font may be embedded but must only be installed temporarily on other systems.

No such DRM restrictions can be enabled on the Google Fonts collection, so the fsType field must be set to zero (Installable Embedding) instead. [code: drm]
</div></details><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0060 (GRAVE ACCENT)


	- 0x00A0 (NO-BREAK SPACE)


	- 0x00A8 (DIAERESIS)


	- 0x00AA (FEMININE ORDINAL INDICATOR)


	- 0x00AF (MACRON)


	- 0x00B4 (ACUTE ACCENT)


	- 0x00B8 (CEDILLA)


	- 0x00BA (MASCULINE ORDINAL INDICATOR)


	- 0x02C6 (MODIFIER LETTER CIRCUMFLEX ACCENT)


	- 0x02C7 (CARON)


	- 0x02D8 (BREVE)


	- 0x02D9 (DOT ABOVE)


	- 0x02DA (RING ABOVE)


	- 0x02DB (OGONEK)


	- 0x02DC (SMALL TILDE)


	- 0x02DD (DOUBLE ACUTE ACCENT)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font names are correct (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_names">com.google.fonts/check/font_names</a>)</summary><div>


* 🔥 **FAIL** Font names are incorrect:

| nameID | current | expected |
| :--- | :--- | :--- |
| Family Name | Danfo 100 | Danfo 100 |
| Subfamily Name | Regular | Regular |
| Full Name | **Danfo Regular 100** | **Danfo 100 Regular** |
| Postscript Name | **Danfo-Regular100** | **Danfo100-Regular** |
| Typographic Family Name | **Danfo** | **N/A** |
| Typographic Subfamily Name | **Regular 100** | **N/A** | [code: bad-names]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.sTypoLineGap is "200" it should be 0 [code: bad-OS/2.sTypoLineGap]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 219, but got 100 instead [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (900) and hhea ascent (1100) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Font contains glyphs for whitespace characters? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphs">com.google.fonts/check/whitespace_glyphs</a>)</summary><div>


* 🔥 **FAIL** Whitespace glyph missing for codepoint 0x00A0. [code: missing-whitespace-glyph-0x00A0]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* 🔥 **FAIL** The following glyphs have no contours even though they were expected to have some:

	- Glyph name: onequarter	Expected: 3 or 4

	- Glyph name: onehalf	Expected: 3

	- Glyph name: threequarters	Expected: 3 or 4

	- Glyph name: uni0312	Expected: 1

	- Glyph name: uni0334	Expected: 1

	- Glyph name: fraction	Expected: 1

	- Glyph name: uni2153	Expected: 3

	- Glyph name: uni2154	Expected: 1 or 3

	- Glyph name: fraction	Expected: 1

	- Glyph name: onehalf	Expected: 3

	- Glyph name: onequarter	Expected: 3 or 4

	- Glyph name: threequarters	Expected: 3 or 4

	- Glyph name: uni0312	Expected: 1
 [code: no-contour]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: B	Contours detected: 4	Expected: 2 or 3

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 3	Expected: 2

	- Glyph name: G	Contours detected: 2	Expected: 1

	- Glyph name: J	Contours detected: 3	Expected: 1

	- Glyph name: O	Contours detected: 4	Expected: 2

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: S	Contours detected: 3	Expected: 1

	- Glyph name: U	Contours detected: 2	Expected: 1

	- Glyph name: W	Contours detected: 5	Expected: 1 or 2

	- Glyph name: Y	Contours detected: 2	Expected: 1

	- Glyph name: b	Contours detected: 4	Expected: 2

	- Glyph name: c	Contours detected: 3	Expected: 1

	- Glyph name: d	Contours detected: 3	Expected: 2

	- Glyph name: e	Contours detected: 1	Expected: 2

	- Glyph name: i	Contours detected: 1	Expected: 2

	- Glyph name: j	Contours detected: 3	Expected: 2

	- Glyph name: o	Contours detected: 4	Expected: 2

	- Glyph name: q	Contours detected: 3	Expected: 2

	- Glyph name: r	Contours detected: 2	Expected: 1

	- Glyph name: s	Contours detected: 3	Expected: 1

	- Glyph name: u	Contours detected: 2	Expected: 1

	- Glyph name: w	Contours detected: 5	Expected: 1

	- Glyph name: y	Contours detected: 2	Expected: 1

	- Glyph name: Ccedilla	Contours detected: 4	Expected: 1 or 2

	- Glyph name: Ograve	Contours detected: 5	Expected: 3

	- Glyph name: Oacute	Contours detected: 5	Expected: 3

	- Glyph name: Ocircumflex	Contours detected: 5	Expected: 3

	- Glyph name: Otilde	Contours detected: 5	Expected: 3

	- Glyph name: Odieresis	Contours detected: 6	Expected: 4

	- Glyph name: Oslash	Contours detected: 4	Expected: 2 or 3

	- Glyph name: Ugrave	Contours detected: 3	Expected: 2

	- Glyph name: Uacute	Contours detected: 3	Expected: 2

	- Glyph name: Ucircumflex	Contours detected: 3	Expected: 2

	- Glyph name: Udieresis	Contours detected: 4	Expected: 3

	- Glyph name: Yacute	Contours detected: 3	Expected: 2

	- Glyph name: ae	Contours detected: 2	Expected: 3

	- Glyph name: ccedilla	Contours detected: 4	Expected: 1 or 2

	- Glyph name: egrave	Contours detected: 2	Expected: 3

	- Glyph name: eacute	Contours detected: 2	Expected: 3

	- Glyph name: edieresis	Contours detected: 3	Expected: 4

	- Glyph name: ograve	Contours detected: 5	Expected: 3

	- Glyph name: oacute	Contours detected: 5	Expected: 3

	- Glyph name: ocircumflex	Contours detected: 5	Expected: 3

	- Glyph name: otilde	Contours detected: 5	Expected: 3

	- Glyph name: odieresis	Contours detected: 6	Expected: 4

	- Glyph name: oslash	Contours detected: 4	Expected: 3

	- Glyph name: ugrave	Contours detected: 3	Expected: 2

	- Glyph name: uacute	Contours detected: 3	Expected: 2

	- Glyph name: ucircumflex	Contours detected: 3	Expected: 2

	- Glyph name: udieresis	Contours detected: 4	Expected: 3

	- Glyph name: yacute	Contours detected: 3	Expected: 2

	- Glyph name: ydieresis	Contours detected: 4	Expected: 3

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Cacute	Contours detected: 4	Expected: 2

	- Glyph name: cacute	Contours detected: 4	Expected: 2

	- Glyph name: Cdotaccent	Contours detected: 4	Expected: 2

	- Glyph name: cdotaccent	Contours detected: 4	Expected: 2

	- Glyph name: Ccaron	Contours detected: 4	Expected: 2

	- Glyph name: ccaron	Contours detected: 4	Expected: 2

	- Glyph name: Dcaron	Contours detected: 4	Expected: 3

	- Glyph name: dcaron	Contours detected: 4	Expected: 3

	- Glyph name: emacron	Contours detected: 2	Expected: 3

	- Glyph name: edotaccent	Contours detected: 2	Expected: 3

	- Glyph name: ecaron	Contours detected: 2	Expected: 3

	- Glyph name: Gbreve	Contours detected: 3	Expected: 2

	- Glyph name: Gdotaccent	Contours detected: 3	Expected: 2

	- Glyph name: uni0122	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: IJ	Contours detected: 4	Expected: 1 or 2

	- Glyph name: Jcircumflex	Contours detected: 4	Expected: 2

	- Glyph name: Omacron	Contours detected: 5	Expected: 3

	- Glyph name: omacron	Contours detected: 5	Expected: 3

	- Glyph name: Ohungarumlaut	Contours detected: 6	Expected: 4

	- Glyph name: ohungarumlaut	Contours detected: 6	Expected: 4

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: racute	Contours detected: 3	Expected: 2

	- Glyph name: uni0157	Contours detected: 3	Expected: 2

	- Glyph name: rcaron	Contours detected: 3	Expected: 2

	- Glyph name: Sacute	Contours detected: 4	Expected: 2

	- Glyph name: sacute	Contours detected: 4	Expected: 2

	- Glyph name: Scedilla	Contours detected: 4	Expected: 1 or 2

	- Glyph name: scedilla	Contours detected: 4	Expected: 1 or 2

	- Glyph name: Scaron	Contours detected: 4	Expected: 2

	- Glyph name: scaron	Contours detected: 4	Expected: 2

	- Glyph name: Utilde	Contours detected: 3	Expected: 2

	- Glyph name: utilde	Contours detected: 3	Expected: 2

	- Glyph name: Umacron	Contours detected: 3	Expected: 2

	- Glyph name: umacron	Contours detected: 3	Expected: 2

	- Glyph name: Ubreve	Contours detected: 3	Expected: 2

	- Glyph name: ubreve	Contours detected: 3	Expected: 2

	- Glyph name: Uring	Contours detected: 4	Expected: 3

	- Glyph name: uring	Contours detected: 4	Expected: 3

	- Glyph name: Uhungarumlaut	Contours detected: 4	Expected: 3

	- Glyph name: uhungarumlaut	Contours detected: 4	Expected: 3

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: Wcircumflex	Contours detected: 6	Expected: 2

	- Glyph name: wcircumflex	Contours detected: 6	Expected: 2

	- Glyph name: Ycircumflex	Contours detected: 3	Expected: 2

	- Glyph name: ycircumflex	Contours detected: 3	Expected: 2

	- Glyph name: Ydieresis	Contours detected: 4	Expected: 3

	- Glyph name: uni0180	Contours detected: 4	Expected: 2

	- Glyph name: uni0181	Contours detected: 5	Expected: 3

	- Glyph name: uni0186	Contours detected: 3	Expected: 1

	- Glyph name: uni0187	Contours detected: 4	Expected: 1

	- Glyph name: uni0188	Contours detected: 4	Expected: 1

	- Glyph name: uni018A	Contours detected: 4	Expected: 2

	- Glyph name: uni018F	Contours detected: 4	Expected: 2

	- Glyph name: uni0190	Contours detected: 3	Expected: 1

	- Glyph name: uni0191	Contours detected: 2	Expected: 1

	- Glyph name: uni0193	Contours detected: 2	Expected: 1

	- Glyph name: uni0197	Contours detected: 2	Expected: 1

	- Glyph name: uni0198	Contours detected: 2	Expected: 1

	- Glyph name: uni0199	Contours detected: 2	Expected: 1

	- Glyph name: uni019A	Contours detected: 2	Expected: 1

	- Glyph name: Obarred	Contours detected: 5	Expected: 3

	- Glyph name: Ohorn	Contours detected: 5	Expected: 2 or 3

	- Glyph name: ohorn	Contours detected: 5	Expected: 2

	- Glyph name: uni01A4	Contours detected: 3	Expected: 2

	- Glyph name: uni01A5	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 3	Expected: 1

	- Glyph name: uhorn	Contours detected: 3	Expected: 1

	- Glyph name: uni01B2	Contours detected: 2	Expected: 1

	- Glyph name: uni01B3	Contours detected: 3	Expected: 1

	- Glyph name: uni01B4	Contours detected: 3	Expected: 1

	- Glyph name: uni01B7	Contours detected: 3	Expected: 1

	- Glyph name: uni01B8	Contours detected: 3	Expected: 1

	- Glyph name: uni01B9	Contours detected: 3	Expected: 1

	- Glyph name: uni01D1	Contours detected: 5	Expected: 3

	- Glyph name: uni01D2	Contours detected: 5	Expected: 3

	- Glyph name: uni01D3	Contours detected: 3	Expected: 2

	- Glyph name: uni01D4	Contours detected: 3	Expected: 2

	- Glyph name: uni01D5	Contours detected: 5	Expected: 4

	- Glyph name: uni01D6	Contours detected: 5	Expected: 4

	- Glyph name: uni01D7	Contours detected: 5	Expected: 4

	- Glyph name: uni01D8	Contours detected: 5	Expected: 4

	- Glyph name: uni01D9	Contours detected: 5	Expected: 4

	- Glyph name: uni01DA	Contours detected: 5	Expected: 4

	- Glyph name: uni01DB	Contours detected: 5	Expected: 4

	- Glyph name: uni01DC	Contours detected: 5	Expected: 4

	- Glyph name: uni01DD	Contours detected: 1	Expected: 2

	- Glyph name: uni01E3	Contours detected: 3	Expected: 4

	- Glyph name: uni01E4	Contours detected: 2	Expected: 1

	- Glyph name: Gcaron	Contours detected: 3	Expected: 2

	- Glyph name: uni01EA	Contours detected: 5	Expected: 2

	- Glyph name: uni01EB	Contours detected: 5	Expected: 2

	- Glyph name: uni01EC	Contours detected: 6	Expected: 3

	- Glyph name: uni01ED	Contours detected: 6	Expected: 3

	- Glyph name: uni01EE	Contours detected: 4	Expected: 2

	- Glyph name: uni01EF	Contours detected: 4	Expected: 2

	- Glyph name: uni01F4	Contours detected: 3	Expected: 2

	- Glyph name: Oslashacute	Contours detected: 5	Expected: 4

	- Glyph name: oslashacute	Contours detected: 5	Expected: 4

	- Glyph name: uni0205	Contours detected: 3	Expected: 4

	- Glyph name: uni0207	Contours detected: 2	Expected: 3

	- Glyph name: uni020C	Contours detected: 6	Expected: 4

	- Glyph name: uni020D	Contours detected: 6	Expected: 4

	- Glyph name: uni020E	Contours detected: 5	Expected: 3

	- Glyph name: uni020F	Contours detected: 5	Expected: 3

	- Glyph name: uni0211	Contours detected: 4	Expected: 3

	- Glyph name: uni0213	Contours detected: 3	Expected: 2

	- Glyph name: uni0214	Contours detected: 4	Expected: 3

	- Glyph name: uni0215	Contours detected: 4	Expected: 3

	- Glyph name: uni0216	Contours detected: 3	Expected: 2

	- Glyph name: uni0217	Contours detected: 3	Expected: 2

	- Glyph name: uni0218	Contours detected: 4	Expected: 2

	- Glyph name: uni0219	Contours detected: 4	Expected: 2

	- Glyph name: uni0222	Contours detected: 4	Expected: 2

	- Glyph name: uni0223	Contours detected: 4	Expected: 2

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni022A	Contours detected: 7	Expected: 5

	- Glyph name: uni022B	Contours detected: 7	Expected: 5

	- Glyph name: uni022C	Contours detected: 6	Expected: 4

	- Glyph name: uni022D	Contours detected: 6	Expected: 4

	- Glyph name: uni022E	Contours detected: 5	Expected: 3

	- Glyph name: uni022F	Contours detected: 5	Expected: 3

	- Glyph name: uni0230	Contours detected: 6	Expected: 4

	- Glyph name: uni0231	Contours detected: 6	Expected: 4

	- Glyph name: uni0232	Contours detected: 3	Expected: 2

	- Glyph name: uni0233	Contours detected: 3	Expected: 2

	- Glyph name: uni0237	Contours detected: 3	Expected: 1

	- Glyph name: uni023A	Contours detected: 2	Expected: 3

	- Glyph name: uni023B	Contours detected: 3	Expected: 2

	- Glyph name: uni023C	Contours detected: 3	Expected: 2

	- Glyph name: uni023D	Contours detected: 2	Expected: 1

	- Glyph name: uni023E	Contours detected: 1	Expected: 2

	- Glyph name: uni0243	Contours detected: 4	Expected: 3

	- Glyph name: uni0244	Contours detected: 3	Expected: 2

	- Glyph name: uni0246	Contours detected: 1	Expected: 3

	- Glyph name: uni0247	Contours detected: 1	Expected: 4

	- Glyph name: uni0248	Contours detected: 4	Expected: 1

	- Glyph name: uni0249	Contours detected: 4	Expected: 2

	- Glyph name: uni024A	Contours detected: 3	Expected: 2

	- Glyph name: uni024B	Contours detected: 3	Expected: 2

	- Glyph name: uni024D	Contours detected: 2	Expected: 1

	- Glyph name: uni0251	Contours detected: 3	Expected: 2

	- Glyph name: uni0259	Contours detected: 4	Expected: 2

	- Glyph name: uni0292	Contours detected: 3	Expected: 1

	- Glyph name: uni1E02	Contours detected: 5	Expected: 4

	- Glyph name: uni1E03	Contours detected: 5	Expected: 3

	- Glyph name: uni1E08	Contours detected: 5	Expected: 2

	- Glyph name: uni1E09	Contours detected: 5	Expected: 2

	- Glyph name: uni1E0A	Contours detected: 4	Expected: 3

	- Glyph name: uni1E0B	Contours detected: 4	Expected: 3

	- Glyph name: uni1E0C	Contours detected: 4	Expected: 3

	- Glyph name: uni1E0D	Contours detected: 4	Expected: 3

	- Glyph name: Dmacronbelow	Contours detected: 4	Expected: 3

	- Glyph name: dmacronbelow	Contours detected: 4	Expected: 3

	- Glyph name: uni1E15	Contours detected: 3	Expected: 4

	- Glyph name: uni1E17	Contours detected: 3	Expected: 4

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E20	Contours detected: 3	Expected: 2

	- Glyph name: uni1E4C	Contours detected: 6	Expected: 4

	- Glyph name: uni1E4D	Contours detected: 6	Expected: 4

	- Glyph name: uni1E4E	Contours detected: 7	Expected: 5

	- Glyph name: uni1E4F	Contours detected: 7	Expected: 5

	- Glyph name: uni1E50	Contours detected: 6	Expected: 4

	- Glyph name: uni1E51	Contours detected: 6	Expected: 4

	- Glyph name: uni1E52	Contours detected: 6	Expected: 4

	- Glyph name: uni1E53	Contours detected: 6	Expected: 4

	- Glyph name: uni1E5B	Contours detected: 3	Expected: 2

	- Glyph name: uni1E5D	Contours detected: 4	Expected: 3

	- Glyph name: rmacronbelow	Contours detected: 3	Expected: 2

	- Glyph name: uni1E60	Contours detected: 4	Expected: 2

	- Glyph name: uni1E61	Contours detected: 4	Expected: 2

	- Glyph name: uni1E62	Contours detected: 4	Expected: 2

	- Glyph name: uni1E63	Contours detected: 4	Expected: 2

	- Glyph name: uni1E64	Contours detected: 5	Expected: 3

	- Glyph name: uni1E65	Contours detected: 5	Expected: 3

	- Glyph name: uni1E66	Contours detected: 5	Expected: 3

	- Glyph name: uni1E67	Contours detected: 5	Expected: 3

	- Glyph name: uni1E68	Contours detected: 5	Expected: 3

	- Glyph name: uni1E69	Contours detected: 5	Expected: 3

	- Glyph name: uni1E78	Contours detected: 4	Expected: 3

	- Glyph name: uni1E79	Contours detected: 4	Expected: 3

	- Glyph name: uni1E7A	Contours detected: 5	Expected: 4

	- Glyph name: uni1E7B	Contours detected: 5	Expected: 4

	- Glyph name: Wgrave	Contours detected: 6	Expected: 2

	- Glyph name: wgrave	Contours detected: 6	Expected: 2

	- Glyph name: Wacute	Contours detected: 6	Expected: 2

	- Glyph name: wacute	Contours detected: 6	Expected: 2

	- Glyph name: Wdieresis	Contours detected: 7	Expected: 3

	- Glyph name: wdieresis	Contours detected: 7	Expected: 3

	- Glyph name: uni1E8E	Contours detected: 3	Expected: 2

	- Glyph name: uni1E8F	Contours detected: 3	Expected: 2

	- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

	- Glyph name: uni1EBB	Contours detected: 2	Expected: 3

	- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

	- Glyph name: uni1EBF	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC1	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC3	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC5	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC7	Contours detected: 3	Expected: 4

	- Glyph name: uni1ECB	Contours detected: 2	Expected: 3

	- Glyph name: uni1ECC	Contours detected: 5	Expected: 3

	- Glyph name: uni1ECD	Contours detected: 5	Expected: 3

	- Glyph name: uni1ECE	Contours detected: 5	Expected: 3

	- Glyph name: uni1ECF	Contours detected: 5	Expected: 3

	- Glyph name: uni1ED0	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED1	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED2	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED3	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED4	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED5	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED6	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED7	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED8	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED9	Contours detected: 6	Expected: 4

	- Glyph name: uni1EDA	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EDB	Contours detected: 6	Expected: 3

	- Glyph name: uni1EDC	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EDD	Contours detected: 6	Expected: 3

	- Glyph name: uni1EDE	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EDF	Contours detected: 6	Expected: 3

	- Glyph name: uni1EE0	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EE1	Contours detected: 6	Expected: 3

	- Glyph name: uni1EE2	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EE3	Contours detected: 6	Expected: 3

	- Glyph name: uni1EE4	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE5	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE6	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE7	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE8	Contours detected: 4	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 4	Expected: 2

	- Glyph name: uni1EED	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 4	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 4	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 4	Expected: 2

	- Glyph name: Ygrave	Contours detected: 3	Expected: 2

	- Glyph name: ygrave	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF4	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF5	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF6	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF7	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF9	Contours detected: 3	Expected: 2

	- Glyph name: B	Contours detected: 4	Expected: 2 or 3

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: Cacute	Contours detected: 4	Expected: 2

	- Glyph name: Ccaron	Contours detected: 4	Expected: 2

	- Glyph name: Ccedilla	Contours detected: 4	Expected: 1 or 2

	- Glyph name: Cdotaccent	Contours detected: 4	Expected: 2

	- Glyph name: D	Contours detected: 3	Expected: 2

	- Glyph name: Dcaron	Contours detected: 4	Expected: 3

	- Glyph name: G	Contours detected: 2	Expected: 1

	- Glyph name: Gbreve	Contours detected: 3	Expected: 2

	- Glyph name: Gcaron	Contours detected: 3	Expected: 2

	- Glyph name: Gdotaccent	Contours detected: 3	Expected: 2

	- Glyph name: IJ	Contours detected: 4	Expected: 1 or 2

	- Glyph name: J	Contours detected: 3	Expected: 1

	- Glyph name: Jcircumflex	Contours detected: 4	Expected: 2

	- Glyph name: O	Contours detected: 4	Expected: 2

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: Oacute	Contours detected: 5	Expected: 3

	- Glyph name: Ocircumflex	Contours detected: 5	Expected: 3

	- Glyph name: Odieresis	Contours detected: 6	Expected: 4

	- Glyph name: Ograve	Contours detected: 5	Expected: 3

	- Glyph name: Ohorn	Contours detected: 5	Expected: 2 or 3

	- Glyph name: Ohungarumlaut	Contours detected: 6	Expected: 4

	- Glyph name: Omacron	Contours detected: 5	Expected: 3

	- Glyph name: Oslash	Contours detected: 4	Expected: 2 or 3

	- Glyph name: Oslashacute	Contours detected: 5	Expected: 4

	- Glyph name: Otilde	Contours detected: 5	Expected: 3

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: S	Contours detected: 3	Expected: 1

	- Glyph name: Sacute	Contours detected: 4	Expected: 2

	- Glyph name: Scaron	Contours detected: 4	Expected: 2

	- Glyph name: U	Contours detected: 2	Expected: 1

	- Glyph name: Uacute	Contours detected: 3	Expected: 2

	- Glyph name: Ubreve	Contours detected: 3	Expected: 2

	- Glyph name: Ucircumflex	Contours detected: 3	Expected: 2

	- Glyph name: Udieresis	Contours detected: 4	Expected: 3

	- Glyph name: Ugrave	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 3	Expected: 1

	- Glyph name: Uhungarumlaut	Contours detected: 4	Expected: 3

	- Glyph name: Umacron	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: Uring	Contours detected: 4	Expected: 3

	- Glyph name: Utilde	Contours detected: 3	Expected: 2

	- Glyph name: W	Contours detected: 5	Expected: 1 or 2

	- Glyph name: Wacute	Contours detected: 6	Expected: 2

	- Glyph name: Wcircumflex	Contours detected: 6	Expected: 2

	- Glyph name: Wdieresis	Contours detected: 7	Expected: 3

	- Glyph name: Wgrave	Contours detected: 6	Expected: 2

	- Glyph name: Y	Contours detected: 2	Expected: 1

	- Glyph name: Yacute	Contours detected: 3	Expected: 2

	- Glyph name: Ycircumflex	Contours detected: 3	Expected: 2

	- Glyph name: Ydieresis	Contours detected: 4	Expected: 3

	- Glyph name: Ygrave	Contours detected: 3	Expected: 2

	- Glyph name: ae	Contours detected: 2	Expected: 3

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: b	Contours detected: 4	Expected: 2

	- Glyph name: c	Contours detected: 3	Expected: 1

	- Glyph name: cacute	Contours detected: 4	Expected: 2

	- Glyph name: ccaron	Contours detected: 4	Expected: 2

	- Glyph name: ccedilla	Contours detected: 4	Expected: 1 or 2

	- Glyph name: cdotaccent	Contours detected: 4	Expected: 2

	- Glyph name: d	Contours detected: 3	Expected: 2

	- Glyph name: dcaron	Contours detected: 4	Expected: 3

	- Glyph name: e	Contours detected: 1	Expected: 2

	- Glyph name: eacute	Contours detected: 2	Expected: 3

	- Glyph name: ecaron	Contours detected: 2	Expected: 3

	- Glyph name: edieresis	Contours detected: 3	Expected: 4

	- Glyph name: edotaccent	Contours detected: 2	Expected: 3

	- Glyph name: egrave	Contours detected: 2	Expected: 3

	- Glyph name: emacron	Contours detected: 2	Expected: 3

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: i	Contours detected: 1	Expected: 2

	- Glyph name: j	Contours detected: 3	Expected: 2

	- Glyph name: o	Contours detected: 4	Expected: 2

	- Glyph name: oacute	Contours detected: 5	Expected: 3

	- Glyph name: ocircumflex	Contours detected: 5	Expected: 3

	- Glyph name: odieresis	Contours detected: 6	Expected: 4

	- Glyph name: ograve	Contours detected: 5	Expected: 3

	- Glyph name: ohorn	Contours detected: 5	Expected: 2

	- Glyph name: ohungarumlaut	Contours detected: 6	Expected: 4

	- Glyph name: omacron	Contours detected: 5	Expected: 3

	- Glyph name: oslash	Contours detected: 4	Expected: 3

	- Glyph name: oslashacute	Contours detected: 5	Expected: 4

	- Glyph name: otilde	Contours detected: 5	Expected: 3

	- Glyph name: q	Contours detected: 3	Expected: 2

	- Glyph name: r	Contours detected: 2	Expected: 1

	- Glyph name: racute	Contours detected: 3	Expected: 2

	- Glyph name: rcaron	Contours detected: 3	Expected: 2

	- Glyph name: s	Contours detected: 3	Expected: 1

	- Glyph name: sacute	Contours detected: 4	Expected: 2

	- Glyph name: scaron	Contours detected: 4	Expected: 2

	- Glyph name: u	Contours detected: 2	Expected: 1

	- Glyph name: uacute	Contours detected: 3	Expected: 2

	- Glyph name: ubreve	Contours detected: 3	Expected: 2

	- Glyph name: ucircumflex	Contours detected: 3	Expected: 2

	- Glyph name: udieresis	Contours detected: 4	Expected: 3

	- Glyph name: ugrave	Contours detected: 3	Expected: 2

	- Glyph name: uhorn	Contours detected: 3	Expected: 1

	- Glyph name: uhungarumlaut	Contours detected: 4	Expected: 3

	- Glyph name: umacron	Contours detected: 3	Expected: 2

	- Glyph name: uni0122	Contours detected: 3	Expected: 2

	- Glyph name: uni0157	Contours detected: 3	Expected: 2

	- Glyph name: uni0180	Contours detected: 4	Expected: 2

	- Glyph name: uni0181	Contours detected: 5	Expected: 3

	- Glyph name: uni0186	Contours detected: 3	Expected: 1

	- Glyph name: uni0187	Contours detected: 4	Expected: 1

	- Glyph name: uni0188	Contours detected: 4	Expected: 1

	- Glyph name: uni018A	Contours detected: 4	Expected: 2

	- Glyph name: uni018F	Contours detected: 4	Expected: 2

	- Glyph name: uni0190	Contours detected: 3	Expected: 1

	- Glyph name: uni0191	Contours detected: 2	Expected: 1

	- Glyph name: uni0193	Contours detected: 2	Expected: 1

	- Glyph name: uni0197	Contours detected: 2	Expected: 1

	- Glyph name: uni0198	Contours detected: 2	Expected: 1

	- Glyph name: uni0199	Contours detected: 2	Expected: 1

	- Glyph name: uni019A	Contours detected: 2	Expected: 1

	- Glyph name: uni01A4	Contours detected: 3	Expected: 2

	- Glyph name: uni01A5	Contours detected: 3	Expected: 2

	- Glyph name: uni01B2	Contours detected: 2	Expected: 1

	- Glyph name: uni01B3	Contours detected: 3	Expected: 1

	- Glyph name: uni01B4	Contours detected: 3	Expected: 1

	- Glyph name: uni01B7	Contours detected: 3	Expected: 1

	- Glyph name: uni01B8	Contours detected: 3	Expected: 1

	- Glyph name: uni01B9	Contours detected: 3	Expected: 1

	- Glyph name: uni01D1	Contours detected: 5	Expected: 3

	- Glyph name: uni01D2	Contours detected: 5	Expected: 3

	- Glyph name: uni01D3	Contours detected: 3	Expected: 2

	- Glyph name: uni01D4	Contours detected: 3	Expected: 2

	- Glyph name: uni01D5	Contours detected: 5	Expected: 4

	- Glyph name: uni01D6	Contours detected: 5	Expected: 4

	- Glyph name: uni01D7	Contours detected: 5	Expected: 4

	- Glyph name: uni01D8	Contours detected: 5	Expected: 4

	- Glyph name: uni01D9	Contours detected: 5	Expected: 4

	- Glyph name: uni01DA	Contours detected: 5	Expected: 4

	- Glyph name: uni01DB	Contours detected: 5	Expected: 4

	- Glyph name: uni01DC	Contours detected: 5	Expected: 4

	- Glyph name: uni01DD	Contours detected: 1	Expected: 2

	- Glyph name: uni01E3	Contours detected: 3	Expected: 4

	- Glyph name: uni01E4	Contours detected: 2	Expected: 1

	- Glyph name: uni01EC	Contours detected: 6	Expected: 3

	- Glyph name: uni01ED	Contours detected: 6	Expected: 3

	- Glyph name: uni01EE	Contours detected: 4	Expected: 2

	- Glyph name: uni01EF	Contours detected: 4	Expected: 2

	- Glyph name: uni0218	Contours detected: 4	Expected: 2

	- Glyph name: uni0219	Contours detected: 4	Expected: 2

	- Glyph name: uni0222	Contours detected: 4	Expected: 2

	- Glyph name: uni0223	Contours detected: 4	Expected: 2

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni022A	Contours detected: 7	Expected: 5

	- Glyph name: uni022B	Contours detected: 7	Expected: 5

	- Glyph name: uni022C	Contours detected: 6	Expected: 4

	- Glyph name: uni022D	Contours detected: 6	Expected: 4

	- Glyph name: uni022E	Contours detected: 5	Expected: 3

	- Glyph name: uni022F	Contours detected: 5	Expected: 3

	- Glyph name: uni0230	Contours detected: 6	Expected: 4

	- Glyph name: uni0231	Contours detected: 6	Expected: 4

	- Glyph name: uni0232	Contours detected: 3	Expected: 2

	- Glyph name: uni0233	Contours detected: 3	Expected: 2

	- Glyph name: uni0237	Contours detected: 3	Expected: 1

	- Glyph name: uni023A	Contours detected: 2	Expected: 3

	- Glyph name: uni023B	Contours detected: 3	Expected: 2

	- Glyph name: uni023C	Contours detected: 3	Expected: 2

	- Glyph name: uni023D	Contours detected: 2	Expected: 1

	- Glyph name: uni023E	Contours detected: 1	Expected: 2

	- Glyph name: uni0243	Contours detected: 4	Expected: 3

	- Glyph name: uni0244	Contours detected: 3	Expected: 2

	- Glyph name: uni0246	Contours detected: 1	Expected: 3

	- Glyph name: uni0247	Contours detected: 1	Expected: 4

	- Glyph name: uni0248	Contours detected: 4	Expected: 1

	- Glyph name: uni0249	Contours detected: 4	Expected: 2

	- Glyph name: uni024A	Contours detected: 3	Expected: 2

	- Glyph name: uni024B	Contours detected: 3	Expected: 2

	- Glyph name: uni024D	Contours detected: 2	Expected: 1

	- Glyph name: uni0251	Contours detected: 3	Expected: 2

	- Glyph name: uni0259	Contours detected: 4	Expected: 2

	- Glyph name: uni0292	Contours detected: 3	Expected: 1

	- Glyph name: uni1E02	Contours detected: 5	Expected: 4

	- Glyph name: uni1E03	Contours detected: 5	Expected: 3

	- Glyph name: uni1E08	Contours detected: 5	Expected: 2

	- Glyph name: uni1E09	Contours detected: 5	Expected: 2

	- Glyph name: uni1E0A	Contours detected: 4	Expected: 3

	- Glyph name: uni1E0B	Contours detected: 4	Expected: 3

	- Glyph name: uni1E0C	Contours detected: 4	Expected: 3

	- Glyph name: uni1E0D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E15	Contours detected: 3	Expected: 4

	- Glyph name: uni1E17	Contours detected: 3	Expected: 4

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E20	Contours detected: 3	Expected: 2

	- Glyph name: uni1E4C	Contours detected: 6	Expected: 4

	- Glyph name: uni1E4D	Contours detected: 6	Expected: 4

	- Glyph name: uni1E4E	Contours detected: 7	Expected: 5

	- Glyph name: uni1E4F	Contours detected: 7	Expected: 5

	- Glyph name: uni1E50	Contours detected: 6	Expected: 4

	- Glyph name: uni1E51	Contours detected: 6	Expected: 4

	- Glyph name: uni1E52	Contours detected: 6	Expected: 4

	- Glyph name: uni1E53	Contours detected: 6	Expected: 4

	- Glyph name: uni1E5B	Contours detected: 3	Expected: 2

	- Glyph name: uni1E5D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E60	Contours detected: 4	Expected: 2

	- Glyph name: uni1E61	Contours detected: 4	Expected: 2

	- Glyph name: uni1E62	Contours detected: 4	Expected: 2

	- Glyph name: uni1E63	Contours detected: 4	Expected: 2

	- Glyph name: uni1E64	Contours detected: 5	Expected: 3

	- Glyph name: uni1E65	Contours detected: 5	Expected: 3

	- Glyph name: uni1E66	Contours detected: 5	Expected: 3

	- Glyph name: uni1E67	Contours detected: 5	Expected: 3

	- Glyph name: uni1E68	Contours detected: 5	Expected: 3

	- Glyph name: uni1E69	Contours detected: 5	Expected: 3

	- Glyph name: uni1E78	Contours detected: 4	Expected: 3

	- Glyph name: uni1E79	Contours detected: 4	Expected: 3

	- Glyph name: uni1E7A	Contours detected: 5	Expected: 4

	- Glyph name: uni1E7B	Contours detected: 5	Expected: 4

	- Glyph name: uni1E8E	Contours detected: 3	Expected: 2

	- Glyph name: uni1E8F	Contours detected: 3	Expected: 2

	- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

	- Glyph name: uni1EBB	Contours detected: 2	Expected: 3

	- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

	- Glyph name: uni1EBF	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC1	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC3	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC5	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC7	Contours detected: 3	Expected: 4

	- Glyph name: uni1ECB	Contours detected: 2	Expected: 3

	- Glyph name: uni1ECC	Contours detected: 5	Expected: 3

	- Glyph name: uni1ECD	Contours detected: 5	Expected: 3

	- Glyph name: uni1ECE	Contours detected: 5	Expected: 3

	- Glyph name: uni1ECF	Contours detected: 5	Expected: 3

	- Glyph name: uni1ED0	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED1	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED2	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED3	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED4	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED5	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED6	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED7	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED8	Contours detected: 6	Expected: 4

	- Glyph name: uni1ED9	Contours detected: 6	Expected: 4

	- Glyph name: uni1EDA	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EDB	Contours detected: 6	Expected: 3

	- Glyph name: uni1EDC	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EDD	Contours detected: 6	Expected: 3

	- Glyph name: uni1EDE	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EDF	Contours detected: 6	Expected: 3

	- Glyph name: uni1EE0	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EE1	Contours detected: 6	Expected: 3

	- Glyph name: uni1EE2	Contours detected: 6	Expected: 3 or 4

	- Glyph name: uni1EE3	Contours detected: 6	Expected: 3

	- Glyph name: uni1EE4	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE5	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE6	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE7	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE8	Contours detected: 4	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 4	Expected: 2

	- Glyph name: uni1EED	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 4	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 4	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 4	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 4	Expected: 2

	- Glyph name: uni1EF4	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF5	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF6	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF7	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF9	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uring	Contours detected: 4	Expected: 3

	- Glyph name: utilde	Contours detected: 3	Expected: 2

	- Glyph name: w	Contours detected: 5	Expected: 1

	- Glyph name: wacute	Contours detected: 6	Expected: 2

	- Glyph name: wcircumflex	Contours detected: 6	Expected: 2

	- Glyph name: wdieresis	Contours detected: 7	Expected: 3

	- Glyph name: wgrave	Contours detected: 6	Expected: 2

	- Glyph name: y	Contours detected: 2	Expected: 1

	- Glyph name: yacute	Contours detected: 3	Expected: 2

	- Glyph name: ycircumflex	Contours detected: 3	Expected: 2

	- Glyph name: ydieresis	Contours detected: 4	Expected: 3

	- Glyph name: ygrave	Contours detected: 3	Expected: 2
 [code: contour-count]
</div></details><details><summary>🔥 <b>FAIL:</b> Check accent of Lcaron, dcaron, lcaron, tcaron (derived from com.google.fonts/check/alt_caron) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/alt_caron">com.google.fonts/check/alt_caron</a>)</summary><div>


* 🔥 **FAIL** Lcaron uses component uni030C. [code: wrong-mark]
* 🔥 **FAIL** dcaron uses component uni030C. [code: wrong-mark]
* 🔥 **FAIL** lcaron uses component uni030C. [code: wrong-mark]
* 🔥 **FAIL** tcaron uses component uni030C. [code: wrong-mark]
</div></details><details><summary>🔥 <b>FAIL:</b> Does full font name begin with the font family name? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/name/match_familyname_fullfont">com.google.fonts/check/name/match_familyname_fullfont</a>)</summary><div>


* 🔥 **FAIL** On the 'name' table, the full font name 'Danfo Regular 100' does not begin with the font family name 'Danfo 100' in platformID 3, encodingID 1, languageID 1033(0409), and nameID 1. [code: mismatch-font-names]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Check for codepoints not covered by METADATA subsets. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/unreachable_subsetting">com.google.fonts/check/metadata/unreachable_subsetting</a>)</summary><div>


* ⚠ **WARN** The following codepoints supported by the font are not covered by
    any subsets defined in the font's metadata file, and will never
    be served. You can solve this by either manually adding additional
    subset declarations to METADATA.pb, or by editing the glyphset
    definitions.

 * U+02D7 MODIFIER LETTER MINUS SIGN: not included in any glyphset definition
 * U+02EE MODIFIER LETTER DOUBLE APOSTROPHE: not included in any glyphset definition
 * U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, math, tifinagh, cherokee
 * U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic
 * U+0307 COMBINING DOT ABOVE: try adding one of: math, tai-le, malayalam, syriac, canadian-aboriginal, old-permic, coptic, tifinagh
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
 * U+0324 COMBINING DIAERESIS BELOW: try adding one of: syriac, cherokee
 * U+0325 COMBINING RING BELOW: try adding syriac
 * U+0326 COMBINING COMMA BELOW: not included in any glyphset definition
 * U+0327 COMBINING CEDILLA: not included in any glyphset definition
 * U+0328 COMBINING OGONEK: not included in any glyphset definition
 * U+032D COMBINING CIRCUMFLEX ACCENT BELOW: try adding syriac
 * U+032E COMBINING BREVE BELOW: try adding syriac
 * U+032F COMBINING INVERTED BREVE BELOW: not included in any glyphset definition
 * U+0330 COMBINING TILDE BELOW: try adding one of: math, syriac, cherokee
 * U+0331 COMBINING MACRON BELOW: try adding one of: syriac, cherokee, gothic, caucasian-albanian, tifinagh
 * U+0332 COMBINING LOW LINE: not included in any glyphset definition
 * U+0334 COMBINING TILDE OVERLAY: not included in any glyphset definition
 * U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition
 * U+0358 COMBINING DOT ABOVE RIGHT: try adding osage
 * U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai
 * U+1D7D LATIN SMALL LETTER P WITH STROKE: not included in any glyphset definition
 * U+1DC4 COMBINING MACRON-ACUTE: not included in any glyphset definition
 * U+1DC5 COMBINING GRAVE-MACRON: not included in any glyphset definition
 * U+1DC6 COMBINING MACRON-GRAVE: not included in any glyphset definition
 * U+1DC7 COMBINING ACUTE-MACRON: not included in any glyphset definition
 * U+1DCA COMBINING LATIN SMALL LETTER R BELOW: not included in any glyphset definition
 * U+2016 DOUBLE VERTICAL LINE: not included in any glyphset definition
 * U+2021 DOUBLE DAGGER: try adding adlam
 * U+2030 PER MILLE SIGN: try adding adlam
 * U+2075 SUPERSCRIPT FIVE: not included in any glyphset definition
 * U+2076 SUPERSCRIPT SIX: not included in any glyphset definition
 * U+2077 SUPERSCRIPT SEVEN: not included in any glyphset definition
 * U+2078 SUPERSCRIPT EIGHT: not included in any glyphset definition
 * U+2079 SUPERSCRIPT NINE: not included in any glyphset definition
 * U+2081 SUBSCRIPT ONE: not included in any glyphset definition
 * U+2082 SUBSCRIPT TWO: not included in any glyphset definition
 * U+2083 SUBSCRIPT THREE: not included in any glyphset definition
 * U+2084 SUBSCRIPT FOUR: not included in any glyphset definition
 * U+2085 SUBSCRIPT FIVE: not included in any glyphset definition
 * U+2086 SUBSCRIPT SIX: not included in any glyphset definition
 * U+2087 SUBSCRIPT SEVEN: not included in any glyphset definition
 * U+2088 SUBSCRIPT EIGHT: not included in any glyphset definition
 * U+2089 SUBSCRIPT NINE: not included in any glyphset definition
 * U+2126 OHM SIGN: not included in any glyphset definition
 * U+212E ESTIMATED SYMBOL: not included in any glyphset definition
 * U+2153 VULGAR FRACTION ONE THIRD: not included in any glyphset definition
 * U+2154 VULGAR FRACTION TWO THIRDS: not included in any glyphset definition
 * U+2190 LEFTWARDS ARROW: try adding one of: math, symbols
 * U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols
 * U+2194 LEFT RIGHT ARROW: try adding one of: math, emoji, symbols
 * U+2195 UP DOWN ARROW: try adding one of: math, emoji, symbols
 * U+2196 NORTH WEST ARROW: try adding one of: math, emoji, symbols
 * U+2197 NORTH EAST ARROW: try adding one of: math, emoji, symbols
 * U+2198 SOUTH EAST ARROW: try adding one of: math, emoji, symbols
 * U+2199 SOUTH WEST ARROW: try adding one of: math, emoji, symbols
 * U+2202 PARTIAL DIFFERENTIAL: try adding math
 * U+2205 EMPTY SET: try adding math
 * U+2206 INCREMENT: try adding math
 * U+220F N-ARY PRODUCT: try adding math
 * U+2211 N-ARY SUMMATION: try adding math
 * U+221A SQUARE ROOT: try adding math
 * U+221E INFINITY: try adding math
 * U+222B INTEGRAL: try adding math
 * U+2248 ALMOST EQUAL TO: try adding math
 * U+2260 NOT EQUAL TO: try adding math
 * U+2264 LESS-THAN OR EQUAL TO: try adding math
 * U+2265 GREATER-THAN OR EQUAL TO: try adding math
 * U+25A0 BLACK SQUARE: try adding symbols
 * U+25A1 WHITE SQUARE: try adding symbols
 * U+25AA BLACK SMALL SQUARE: try adding one of: emoji, symbols
 * U+25AB WHITE SMALL SQUARE: try adding one of: emoji, symbols
 * U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols
 * U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: math, symbols
 * U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols
 * U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols
 * U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding one of: emoji, symbols
 * U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: math, symbols
 * U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols
 * U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols
 * U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols
 * U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: math, symbols
 * U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols
 * U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols
 * U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding one of: emoji, symbols
 * U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: math, symbols
 * U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols
 * U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols
 * U+25C6 BLACK DIAMOND: try adding symbols
 * U+25C7 WHITE DIAMOND: try adding symbols
 * U+25CA LOZENGE: try adding one of: math, symbols
 * U+25CB WHITE CIRCLE: try adding symbols
 * U+25CF BLACK CIRCLE: try adding symbols
 * U+25E6 WHITE BULLET: try adding symbols
 * U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math
 * U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math
 * U+3008 LEFT ANGLE BRACKET: try adding one of: tai-le, japanese, yi, chinese-traditional, phags-pa, chinese-hongkong, chinese-simplified
 * U+3009 RIGHT ANGLE BRACKET: try adding one of: tai-le, japanese, yi, chinese-traditional, phags-pa, chinese-hongkong, chinese-simplified
 * U+AB53 LATIN SMALL LETTER CHI: not included in any glyphset definition
 * U+FF0D FULLWIDTH HYPHEN-MINUS: try adding chinese-simplified

Or you can add the above codepoints to one of the subsets supported by the font: `cyrillic-ext`, `latin`, `latin-ext`, `vietnamese` [code: unreachable-subsetting]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- _part.cut

	- hook.part
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 298 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 279:
less, greater

Width = 326:
equal

Width = 306:
logicalnot

Width = 284:
multiply

Width = 316:
divide

Width = 286:
minus

Width = 330:
approxequal

Width = 339:
notequal

Width = 287:
lessequal, greaterequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** OS/2 sTypoLineGap is not equal to 0. [code: OS/2]
</div></details><details><summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Euro (U+20AC): L<<231.0,550.0>--<231.0,547.0>> -> L<<231.0,547.0>--<231.0,519.0>>

	* Gammalatin (U+0194): L<<166.0,334.0>--<166.0,261.0>> -> L<<166.0,261.0>--<166.0,260.0>>

	* paragraph (U+00B6): L<<182.0,715.0>--<491.0,716.0>> -> L<<491.0,716.0>--<648.0,716.0>>

	* section (U+00A7): L<<268.0,464.0>--<326.0,459.0>> -> L<<326.0,459.0>--<344.0,457.0>>

	* uni0222 (U+0222): L<<275.0,430.0>--<332.0,429.0>> -> L<<332.0,429.0>--<369.0,430.0>>

	* uni0223 (U+0223): L<<275.0,430.0>--<332.0,429.0>> -> L<<332.0,429.0>--<369.0,430.0>>

	* uni024E (U+024E): L<<421.0,491.0>--<110.0,517.0>> -> L<<110.0,517.0>--<27.0,517.0>>

	* uni024F (U+024F): L<<421.0,491.0>--<110.0,517.0>> -> L<<110.0,517.0>--<27.0,517.0>>

	* uni0263 (U+0263): L<<166.0,334.0>--<166.0,261.0>> -> L<<166.0,261.0>--<166.0,260.0>>

	* uniA7B8 (U+A7B8): L<<337.0,-6.0>--<225.0,-6.0>> -> L<<225.0,-6.0>--<223.0,-6.0>>

	* uniA7B9 (U+A7B9): L<<337.0,-6.0>--<225.0,-6.0>> -> L<<225.0,-6.0>--<223.0,-6.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* Euro (U+20AC): L<<218.0,722.0>--<426.0,721.0>>

	* G (U+0047): L<<218.0,722.0>--<426.0,721.0>>

	* Gbreve (U+011E): L<<218.0,722.0>--<426.0,721.0>>

	* Gcaron (U+01E6): L<<218.0,722.0>--<426.0,721.0>>

	* Gdotaccent (U+0120): L<<218.0,722.0>--<426.0,721.0>>

	* Glottalstopsmall (U+0241): L<<161.0,721.0>--<334.0,722.0>>

	* M (U+004D): L<<354.0,0.0>--<29.0,-1.0>>

	* M (U+004D): L<<739.0,-1.0>--<414.0,0.0>>

	* Ohungarumlaut (U+0150): L<<393.0,877.0>--<511.0,878.0>>

	* Thorn (U+00DE): L<<267.0,588.0>--<470.0,587.0>>

	* Thorn (U+00DE): L<<29.0,716.0>--<331.0,715.0>>

	* Thorn (U+00DE): L<<331.0,-1.0>--<29.0,0.0>>

	* Thorn (U+00DE): L<<484.0,368.0>--<266.0,369.0>>

	* Uhungarumlaut (U+0170): L<<422.0,877.0>--<540.0,878.0>>

	* ampersand (U+0026): L<<408.0,540.0>--<676.0,538.0>>

	* arrowboth (U+2194): L<<300.0,324.0>--<299.0,103.0>>

	* arrowboth (U+2194): L<<301.0,644.0>--<300.0,424.0>>

	* arrowboth (U+2194): L<<478.0,424.0>--<477.0,644.0>>

	* arrowboth (U+2194): L<<479.0,103.0>--<478.0,324.0>>

	* arrowdown (U+2193): L<<18.0,397.0>--<238.0,396.0>>

	* arrowdown (U+2193): L<<337.0,396.0>--<559.0,395.0>>

	* arrowdown (U+2193): L<<338.0,704.0>--<337.0,396.0>>

	* arrowleft (U+2190): L<<299.0,691.0>--<300.0,469.0>>

	* arrowleft (U+2190): L<<300.0,370.0>--<301.0,150.0>>

	* arrowleft (U+2190): L<<300.0,469.0>--<608.0,470.0>>

	* arrowright (U+2192): L<<337.0,342.0>--<29.0,341.0>>

	* arrowright (U+2192): L<<337.0,441.0>--<336.0,661.0>>

	* arrowright (U+2192): L<<338.0,120.0>--<337.0,342.0>>

	* arrowup (U+2191): L<<239.0,433.0>--<19.0,432.0>>

	* arrowup (U+2191): L<<338.0,433.0>--<339.0,125.0>>

	* arrowup (U+2191): L<<560.0,434.0>--<338.0,433.0>>

	* arrowupdn (U+2195): L<<10.0,287.0>--<231.0,288.0>>

	* arrowupdn (U+2195): L<<231.0,466.0>--<10.0,467.0>>

	* arrowupdn (U+2195): L<<331.0,288.0>--<551.0,289.0>>

	* arrowupdn (U+2195): L<<551.0,465.0>--<331.0,466.0>>

	* bracketleft (U+005B): L<<190.0,757.0>--<188.0,-44.0>>

	* bracketleft (U+005B): L<<29.0,-125.0>--<32.0,837.0>>

	* bracketright (U+005D): L<<166.0,-40.0>--<168.0,761.0>>

	* bracketright (U+005D): L<<327.0,842.0>--<324.0,-120.0>>

	* eight (U+0038): L<<189.0,716.0>--<451.0,715.0>>

	* eight (U+0038): L<<431.0,-8.0>--<209.0,-7.0>>

	* exclam (U+0021): L<<30.0,723.0>--<252.0,724.0>>

	* exclamdown (U+00A1): L<<260.0,-140.0>--<38.0,-141.0>>

	* five (U+0035): L<<27.0,179.0>--<28.0,470.0>>

	* five (U+0035): L<<592.0,410.0>--<591.0,178.0>>

	* florin (U+0192): L<<29.0,0.0>--<30.0,434.0>>

	* four (U+0034): L<<581.0,-1.0>--<31.0,-3.0>>

	* g (U+0067): L<<218.0,722.0>--<426.0,721.0>>

	* gbreve (U+011F): L<<218.0,722.0>--<426.0,721.0>>

	* gcaron (U+01E7): L<<218.0,722.0>--<426.0,721.0>>

	* gdotaccent (U+0121): L<<218.0,722.0>--<426.0,721.0>>

	* m (U+006D): L<<354.0,0.0>--<29.0,-1.0>>

	* m (U+006D): L<<739.0,-1.0>--<414.0,0.0>>

	* minute (U+2032): L<<60.0,717.0>--<287.0,716.0>>

	* nine (U+0039): L<<24.0,180.0>--<25.0,470.0>>

	* nine (U+0039): L<<399.0,-7.0>--<213.0,-6.0>>

	* nine (U+0039): L<<589.0,550.0>--<588.0,179.0>>

	* nlongrightleg (U+019E): L<<667.0,-139.0>--<375.0,-138.0>>

	* ohungarumlaut (U+0151): L<<393.0,877.0>--<511.0,878.0>>

	* one (U+0031): L<<210.0,715.0>--<397.0,716.0>>

	* one (U+0031): L<<397.0,716.0>--<398.0,495.0>>

	* paragraph (U+00B6): L<<182.0,715.0>--<491.0,716.0>>

	* percent (U+0025): L<<481.0,722.0>--<599.0,721.0>>

	* perthousand (U+2030): L<<481.0,722.0>--<599.0,721.0>>

	* radical (U+221A): L<<376.0,-101.0>--<181.0,-100.0>>

	* radical (U+221A): L<<512.0,899.0>--<636.0,898.0>>

	* second (U+2033): L<<316.0,717.0>--<543.0,716.0>>

	* second (U+2033): L<<60.0,717.0>--<287.0,716.0>>

	* seven (U+0037): L<<26.0,0.0>--<27.0,434.0>>

	* seven (U+0037): L<<27.0,716.0>--<534.0,714.0>>

	* seven (U+0037): L<<534.0,-1.0>--<26.0,0.0>>

	* six (U+0036): L<<430.0,-6.0>--<216.0,-5.0>>

	* sterling (U+00A3): L<<564.0,589.0>--<393.0,590.0>>

	* thorn (U+00FE): L<<267.0,588.0>--<470.0,587.0>>

	* thorn (U+00FE): L<<29.0,716.0>--<331.0,715.0>>

	* thorn (U+00FE): L<<331.0,-1.0>--<29.0,0.0>>

	* thorn (U+00FE): L<<484.0,368.0>--<266.0,369.0>>

	* triagdn (U+25BC): L<<29.0,731.0>--<733.0,728.0>>

	* triagup (U+25B2): L<<733.0,141.0>--<29.0,144.0>>

	* uhungarumlaut (U+0171): L<<422.0,877.0>--<540.0,878.0>>

	* uni00B9 (U+00B9): L<<210.0,715.0>--<397.0,716.0>>

	* uni00B9 (U+00B9): L<<397.0,716.0>--<398.0,495.0>>

	* uni0122 (U+0122): L<<218.0,722.0>--<426.0,721.0>>

	* uni0123 (U+0123): L<<218.0,722.0>--<426.0,721.0>>

	* uni0190 (U+0190): L<<189.0,716.0>--<416.0,715.0>>

	* uni0190 (U+0190): L<<403.0,-8.0>--<209.0,-7.0>>

	* uni0193 (U+0193): L<<218.0,722.0>--<426.0,721.0>>

	* uni019C (U+019C): L<<29.0,717.0>--<354.0,716.0>>

	* uni019C (U+019C): L<<414.0,716.0>--<739.0,717.0>>

	* uni01A9 (U+01A9): L<<27.0,716.0>--<540.0,714.0>>

	* uni01A9 (U+01A9): L<<541.0,-2.0>--<27.0,0.0>>

	* uni01B7 (U+01B7): L<<44.0,715.0>--<557.0,716.0>>

	* uni01B8 (U+01B8): L<<53.0,716.0>--<566.0,715.0>>

	* uni01B9 (U+01B9): L<<53.0,716.0>--<566.0,715.0>>

	* uni01E4 (U+01E4): L<<218.0,722.0>--<426.0,721.0>>

	* uni01E5 (U+01E5): L<<218.0,722.0>--<426.0,721.0>>

	* uni01EE (U+01EE): L<<44.0,715.0>--<557.0,716.0>>

	* uni01EF (U+01EF): L<<44.0,715.0>--<557.0,716.0>>

	* uni01F4 (U+01F4): L<<218.0,722.0>--<426.0,721.0>>

	* uni01F5 (U+01F5): L<<218.0,722.0>--<426.0,721.0>>

	* uni0220 (U+0220): L<<667.0,-139.0>--<375.0,-138.0>>

	* uni0242 (U+0242): L<<161.0,558.0>--<334.0,559.0>>

	* uni025B (U+025B): L<<189.0,716.0>--<416.0,715.0>>

	* uni025B (U+025B): L<<403.0,-8.0>--<209.0,-7.0>>

	* uni0260 (U+0260): L<<218.0,722.0>--<426.0,721.0>>

	* uni0265 (U+0265): L<<642.0,0.0>--<330.0,-1.0>>

	* uni026F (U+026F): L<<29.0,717.0>--<354.0,716.0>>

	* uni026F (U+026F): L<<414.0,716.0>--<739.0,717.0>>

	* uni0292 (U+0292): L<<44.0,715.0>--<557.0,716.0>>

	* uni0294 (U+0294): L<<161.0,721.0>--<334.0,722.0>>

	* uni0295 (U+0295): L<<219.0,722.0>--<392.0,721.0>>

	* uni030B (U+030B): L<<202.0,768.0>--<320.0,769.0>>

	* uni1E20 (U+1E20): L<<218.0,722.0>--<426.0,721.0>>

	* uni1E21 (U+1E21): L<<218.0,722.0>--<426.0,721.0>>

	* uni1E3E (U+1E3E): L<<354.0,0.0>--<29.0,-1.0>>

	* uni1E3E (U+1E3E): L<<739.0,-1.0>--<414.0,0.0>>

	* uni1E3F (U+1E3F): L<<354.0,0.0>--<29.0,-1.0>>

	* uni1E3F (U+1E3F): L<<739.0,-1.0>--<414.0,0.0>>

	* uni1E40 (U+1E40): L<<354.0,0.0>--<29.0,-1.0>>

	* uni1E40 (U+1E40): L<<739.0,-1.0>--<414.0,0.0>>

	* uni1E41 (U+1E41): L<<354.0,0.0>--<29.0,-1.0>>

	* uni1E41 (U+1E41): L<<739.0,-1.0>--<414.0,0.0>>

	* uni1E42 (U+1E42): L<<354.0,0.0>--<29.0,-1.0>>

	* uni1E42 (U+1E42): L<<739.0,-1.0>--<414.0,0.0>>

	* uni1E43 (U+1E43): L<<354.0,0.0>--<29.0,-1.0>>

	* uni1E43 (U+1E43): L<<739.0,-1.0>--<414.0,0.0>>

	* uni2074 (U+2074): L<<581.0,-1.0>--<31.0,-3.0>>

	* uni2075 (U+2075): L<<27.0,179.0>--<28.0,470.0>>

	* uni2075 (U+2075): L<<592.0,410.0>--<591.0,178.0>>

	* uni2076 (U+2076): L<<430.0,-6.0>--<216.0,-5.0>>

	* uni2077 (U+2077): L<<26.0,0.0>--<27.0,434.0>>

	* uni2077 (U+2077): L<<27.0,716.0>--<534.0,714.0>>

	* uni2077 (U+2077): L<<534.0,-1.0>--<26.0,0.0>>

	* uni2078 (U+2078): L<<189.0,716.0>--<451.0,715.0>>

	* uni2078 (U+2078): L<<431.0,-8.0>--<209.0,-7.0>>

	* uni2079 (U+2079): L<<24.0,180.0>--<25.0,470.0>>

	* uni2079 (U+2079): L<<399.0,-7.0>--<213.0,-6.0>>

	* uni2079 (U+2079): L<<589.0,550.0>--<588.0,179.0>>

	* uni2081 (U+2081): L<<210.0,715.0>--<397.0,716.0>>

	* uni2081 (U+2081): L<<397.0,716.0>--<398.0,495.0>>

	* uni2084 (U+2084): L<<581.0,-1.0>--<31.0,-3.0>>

	* uni2085 (U+2085): L<<27.0,179.0>--<28.0,470.0>>

	* uni2085 (U+2085): L<<592.0,410.0>--<591.0,178.0>>

	* uni2086 (U+2086): L<<430.0,-6.0>--<216.0,-5.0>>

	* uni2087 (U+2087): L<<26.0,0.0>--<27.0,434.0>>

	* uni2087 (U+2087): L<<27.0,716.0>--<534.0,714.0>>

	* uni2087 (U+2087): L<<534.0,-1.0>--<26.0,0.0>>

	* uni2088 (U+2088): L<<189.0,716.0>--<451.0,715.0>>

	* uni2088 (U+2088): L<<431.0,-8.0>--<209.0,-7.0>>

	* uni2089 (U+2089): L<<24.0,180.0>--<25.0,470.0>>

	* uni2089 (U+2089): L<<399.0,-7.0>--<213.0,-6.0>>

	* uni2089 (U+2089): L<<589.0,550.0>--<588.0,179.0>>

	* uni20AA (U+20AA): L<<179.0,-2.0>--<29.0,-3.0>>

	* uni20AA (U+20AA): L<<237.0,574.0>--<387.0,573.0>>

	* uni20AA (U+20AA): L<<29.0,719.0>--<444.0,717.0>>

	* uni20AA (U+20AA): L<<595.0,142.0>--<445.0,143.0>>

	* uni20AA (U+20AA): L<<653.0,718.0>--<803.0,719.0>>

	* uni20AA (U+20AA): L<<803.0,-3.0>--<388.0,-1.0>>

	* uni20BA (U+20BA): L<<238.0,-1.0>--<42.0,0.0>>

	* uni20BA (U+20BA): L<<42.0,0.0>--<43.0,434.0>>

	* uni20BC (U+20BC): L<<701.0,-2.0>--<394.0,-1.0>>

	* uni2126 (U+2126): L<<329.0,439.0>--<330.0,0.0>>

	* uni2126 (U+2126): L<<388.0,0.0>--<387.0,439.0>>

	* uni2196 (U+2196): L<<35.0,637.0>--<416.0,636.0>>

	* uni2197 (U+2197): L<<482.0,629.0>--<481.0,248.0>>

	* uni2198 (U+2198): L<<466.0,174.0>--<85.0,175.0>>

	* uni2199 (U+2199): L<<22.0,210.0>--<23.0,591.0>>

	* uni25B3 (U+25B3): L<<154.0,205.0>--<604.0,204.0>>

	* uni25B3 (U+25B3): L<<733.0,132.0>--<29.0,135.0>>

	* uni25B4 (U+25B4): L<<377.0,143.0>--<19.0,144.0>>

	* uni25B5 (U+25B5): L<<377.0,143.0>--<19.0,144.0>>

	* uni25B6 (U+25B6): L<<29.0,3.0>--<32.0,707.0>>

	* uni25B8 (U+25B8): L<<29.0,68.0>--<30.0,426.0>>

	* uni25B9 (U+25B9): L<<29.0,68.0>--<30.0,426.0>>

	* uni25BD (U+25BD): L<<29.0,728.0>--<733.0,725.0>>

	* uni25BD (U+25BD): L<<608.0,655.0>--<158.0,656.0>>

	* uni25BE (U+25BE): L<<10.0,434.0>--<368.0,433.0>>

	* uni25BF (U+25BF): L<<19.0,434.0>--<377.0,433.0>>

	* uni25C0 (U+25C0): L<<601.0,707.0>--<604.0,3.0>>

	* uni25C1 (U+25C1): L<<531.0,228.0>--<532.0,678.0>>

	* uni25C1 (U+25C1): L<<604.0,807.0>--<601.0,103.0>>

	* uni25C2 (U+25C2): L<<320.0,426.0>--<321.0,68.0>>

	* uni25C3 (U+25C3): L<<321.0,429.0>--<320.0,71.0>>

	* uniA78D (U+A78D): L<<642.0,0.0>--<330.0,-1.0>> [code: found-semi-vertical]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><br></div></details>

### Summary

| 💔 ERROR | ☠ FATAL | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 0 | 30 | 32 | 395 | 19 | 253 |
| 0% | 0% | 4% | 4% | 54% | 3% | 35% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
