## FontBakery report

fontbakery version: 0.10.8

<details><summary><b>[12] Danfo-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 288, but got 250 instead [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current FontBakery version is 0.10.8, while a newer 0.10.9 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* 🔥 **FAIL** The following glyphs have no contours even though they were expected to have some:

	- Glyph name: lambda	Expected: 1

	- Glyph name: lambda	Expected: 1
 [code: no-contour]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: b	Contours detected: 3	Expected: 2

	- Glyph name: e	Contours detected: 1	Expected: 2

	- Glyph name: g	Contours detected: 1	Expected: 2 or 3

	- Glyph name: i	Contours detected: 1	Expected: 2

	- Glyph name: j	Contours detected: 1	Expected: 2

	- Glyph name: r	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: ae	Contours detected: 2	Expected: 3

	- Glyph name: egrave	Contours detected: 2	Expected: 3

	- Glyph name: eacute	Contours detected: 2	Expected: 3

	- Glyph name: edieresis	Contours detected: 3	Expected: 4

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: emacron	Contours detected: 2	Expected: 3

	- Glyph name: edotaccent	Contours detected: 2	Expected: 3

	- Glyph name: ecaron	Contours detected: 2	Expected: 3

	- Glyph name: gcircumflex	Contours detected: 2	Expected: 3 or 4

	- Glyph name: gbreve	Contours detected: 2	Expected: 3 or 4

	- Glyph name: gdotaccent	Contours detected: 2	Expected: 3 or 4

	- Glyph name: uni0123	Contours detected: 2	Expected: 3 or 4

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: ij	Contours detected: 2	Expected: 3 or 4

	- Glyph name: oe	Contours detected: 2	Expected: 3

	- Glyph name: racute	Contours detected: 3	Expected: 2

	- Glyph name: uni0157	Contours detected: 3	Expected: 2

	- Glyph name: rcaron	Contours detected: 3	Expected: 2

	- Glyph name: uni0180	Contours detected: 3	Expected: 2

	- Glyph name: uni0181	Contours detected: 4	Expected: 3

	- Glyph name: uni0187	Contours detected: 2	Expected: 1

	- Glyph name: uni0188	Contours detected: 2	Expected: 1

	- Glyph name: uni018A	Contours detected: 3	Expected: 2

	- Glyph name: uni0191	Contours detected: 2	Expected: 1

	- Glyph name: uni0197	Contours detected: 2	Expected: 1

	- Glyph name: uni0198	Contours detected: 2	Expected: 1

	- Glyph name: uni0199	Contours detected: 2	Expected: 1

	- Glyph name: uni019A	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: uni01A4	Contours detected: 3	Expected: 2

	- Glyph name: uni01A5	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01B3	Contours detected: 2	Expected: 1

	- Glyph name: uni01B4	Contours detected: 2	Expected: 1

	- Glyph name: uni01DD	Contours detected: 1	Expected: 2

	- Glyph name: uni01E3	Contours detected: 3	Expected: 4

	- Glyph name: uni01E5	Contours detected: 1	Expected: 2

	- Glyph name: gcaron	Contours detected: 2	Expected: 3 or 4

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni01F5	Contours detected: 2	Expected: 3

	- Glyph name: Oslashacute	Contours detected: 3	Expected: 4

	- Glyph name: oslashacute	Contours detected: 3	Expected: 4

	- Glyph name: uni0205	Contours detected: 3	Expected: 4

	- Glyph name: uni0207	Contours detected: 2	Expected: 3

	- Glyph name: uni0211	Contours detected: 4	Expected: 3

	- Glyph name: uni0213	Contours detected: 3	Expected: 2

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni023A	Contours detected: 2	Expected: 3

	- Glyph name: uni023B	Contours detected: 1	Expected: 2

	- Glyph name: uni023C	Contours detected: 1	Expected: 2

	- Glyph name: uni023D	Contours detected: 2	Expected: 1

	- Glyph name: uni023E	Contours detected: 1	Expected: 2

	- Glyph name: uni0246	Contours detected: 1	Expected: 3

	- Glyph name: uni0247	Contours detected: 1	Expected: 4

	- Glyph name: uni0248	Contours detected: 2	Expected: 1

	- Glyph name: uni024D	Contours detected: 2	Expected: 1

	- Glyph name: uni024E	Contours detected: 1	Expected: 2

	- Glyph name: uni024F	Contours detected: 1	Expected: 2

	- Glyph name: uni1E03	Contours detected: 4	Expected: 3

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E15	Contours detected: 3	Expected: 4

	- Glyph name: uni1E17	Contours detected: 3	Expected: 4

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E21	Contours detected: 2	Expected: 3 or 4

	- Glyph name: uni1E5B	Contours detected: 3	Expected: 2

	- Glyph name: uni1E5D	Contours detected: 4	Expected: 3

	- Glyph name: rmacronbelow	Contours detected: 3	Expected: 2

	- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

	- Glyph name: uni1EBB	Contours detected: 2	Expected: 3

	- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

	- Glyph name: uni1EBF	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC1	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC3	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC5	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC7	Contours detected: 3	Expected: 4

	- Glyph name: uni1ECB	Contours detected: 2	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: Oslashacute	Contours detected: 3	Expected: 4

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: ae	Contours detected: 2	Expected: 3

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: b	Contours detected: 3	Expected: 2

	- Glyph name: e	Contours detected: 1	Expected: 2

	- Glyph name: eacute	Contours detected: 2	Expected: 3

	- Glyph name: ecaron	Contours detected: 2	Expected: 3

	- Glyph name: edieresis	Contours detected: 3	Expected: 4

	- Glyph name: edotaccent	Contours detected: 2	Expected: 3

	- Glyph name: egrave	Contours detected: 2	Expected: 3

	- Glyph name: emacron	Contours detected: 2	Expected: 3

	- Glyph name: g	Contours detected: 1	Expected: 2 or 3

	- Glyph name: gbreve	Contours detected: 2	Expected: 3 or 4

	- Glyph name: gcaron	Contours detected: 2	Expected: 3 or 4

	- Glyph name: gcircumflex	Contours detected: 2	Expected: 3 or 4

	- Glyph name: gdotaccent	Contours detected: 2	Expected: 3 or 4

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: i	Contours detected: 1	Expected: 2

	- Glyph name: ij	Contours detected: 2	Expected: 3 or 4

	- Glyph name: j	Contours detected: 1	Expected: 2

	- Glyph name: oe	Contours detected: 2	Expected: 3

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: oslash	Contours detected: 2	Expected: 3

	- Glyph name: oslashacute	Contours detected: 3	Expected: 4

	- Glyph name: r	Contours detected: 2	Expected: 1

	- Glyph name: racute	Contours detected: 3	Expected: 2

	- Glyph name: rcaron	Contours detected: 3	Expected: 2

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni0123	Contours detected: 2	Expected: 3 or 4

	- Glyph name: uni0157	Contours detected: 3	Expected: 2

	- Glyph name: uni0180	Contours detected: 3	Expected: 2

	- Glyph name: uni0181	Contours detected: 4	Expected: 3

	- Glyph name: uni0187	Contours detected: 2	Expected: 1

	- Glyph name: uni0188	Contours detected: 2	Expected: 1

	- Glyph name: uni018A	Contours detected: 3	Expected: 2

	- Glyph name: uni0191	Contours detected: 2	Expected: 1

	- Glyph name: uni0197	Contours detected: 2	Expected: 1

	- Glyph name: uni0198	Contours detected: 2	Expected: 1

	- Glyph name: uni0199	Contours detected: 2	Expected: 1

	- Glyph name: uni019A	Contours detected: 2	Expected: 1

	- Glyph name: uni01A4	Contours detected: 3	Expected: 2

	- Glyph name: uni01A5	Contours detected: 3	Expected: 2

	- Glyph name: uni01B3	Contours detected: 2	Expected: 1

	- Glyph name: uni01B4	Contours detected: 2	Expected: 1

	- Glyph name: uni01DD	Contours detected: 1	Expected: 2

	- Glyph name: uni01E3	Contours detected: 3	Expected: 4

	- Glyph name: uni01E5	Contours detected: 1	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni023A	Contours detected: 2	Expected: 3

	- Glyph name: uni023B	Contours detected: 1	Expected: 2

	- Glyph name: uni023C	Contours detected: 1	Expected: 2

	- Glyph name: uni023D	Contours detected: 2	Expected: 1

	- Glyph name: uni023E	Contours detected: 1	Expected: 2

	- Glyph name: uni0246	Contours detected: 1	Expected: 3

	- Glyph name: uni0247	Contours detected: 1	Expected: 4

	- Glyph name: uni0248	Contours detected: 2	Expected: 1

	- Glyph name: uni024D	Contours detected: 2	Expected: 1

	- Glyph name: uni024E	Contours detected: 1	Expected: 2

	- Glyph name: uni024F	Contours detected: 1	Expected: 2

	- Glyph name: uni1E03	Contours detected: 4	Expected: 3

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E15	Contours detected: 3	Expected: 4

	- Glyph name: uni1E17	Contours detected: 3	Expected: 4

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E21	Contours detected: 2	Expected: 3 or 4

	- Glyph name: uni1E5B	Contours detected: 3	Expected: 2

	- Glyph name: uni1E5D	Contours detected: 4	Expected: 3

	- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

	- Glyph name: uni1EBB	Contours detected: 2	Expected: 3

	- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

	- Glyph name: uni1EBF	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC1	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC3	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC5	Contours detected: 3	Expected: 4

	- Glyph name: uni1EC7	Contours detected: 3	Expected: 4

	- Glyph name: uni1ECB	Contours detected: 2	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2
 [code: contour-count]
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
 * U+02B8 MODIFIER LETTER SMALL Y: not included in any glyphset definition
 * U+02B9 MODIFIER LETTER PRIME: not included in any glyphset definition
 * U+02BE MODIFIER LETTER RIGHT HALF RING: not included in any glyphset definition
 * U+02BF MODIFIER LETTER LEFT HALF RING: not included in any glyphset definition
 * U+02C0 MODIFIER LETTER GLOTTAL STOP: not included in any glyphset definition
 * U+02C7 CARON: try adding one of: canadian-aboriginal, tifinagh, yi
 * U+02C8 MODIFIER LETTER VERTICAL LINE: not included in any glyphset definition
 * U+02CA MODIFIER LETTER ACUTE ACCENT: not included in any glyphset definition
 * U+02CB MODIFIER LETTER GRAVE ACCENT: not included in any glyphset definition
 * U+02D7 MODIFIER LETTER MINUS SIGN: not included in any glyphset definition
 * U+02D8 BREVE: try adding one of: canadian-aboriginal, yi
 * U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi
 * U+02DB OGONEK: try adding one of: canadian-aboriginal, yi
 * U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition
 * U+02EE MODIFIER LETTER DOUBLE APOSTROPHE: not included in any glyphset definition
 * U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, cherokee, tifinagh, math
 * U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh
 * U+0307 COMBINING DOT ABOVE: try adding one of: malayalam, coptic, syriac, old-permic, tifinagh, canadian-aboriginal, tai-le, math
 * U+030A COMBINING RING ABOVE: try adding syriac
 * U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage
 * U+030C COMBINING CARON: try adding one of: cherokee, tai-le
 * U+030D COMBINING VERTICAL LINE ABOVE: not included in any glyphset definition
 * U+030F COMBINING DOUBLE GRAVE ACCENT: not included in any glyphset definition
 * U+0310 COMBINING CANDRABINDU: not included in any glyphset definition
 * U+0311 COMBINING INVERTED BREVE: try adding coptic
 * U+0312 COMBINING TURNED COMMA ABOVE: not included in any glyphset definition
 * U+0313 COMBINING COMMA ABOVE: try adding old-permic
 * U+0315 COMBINING COMMA ABOVE RIGHT: not included in any glyphset definition
 * U+031B COMBINING HORN: not included in any glyphset definition
 * U+0324 COMBINING DIAERESIS BELOW: try adding one of: cherokee, syriac
 * U+0325 COMBINING RING BELOW: try adding syriac
 * U+0326 COMBINING COMMA BELOW: not included in any glyphset definition
 * U+0327 COMBINING CEDILLA: not included in any glyphset definition
 * U+0328 COMBINING OGONEK: not included in any glyphset definition
 * U+032D COMBINING CIRCUMFLEX ACCENT BELOW: try adding syriac
 * U+032E COMBINING BREVE BELOW: try adding syriac
 * U+032F COMBINING INVERTED BREVE BELOW: not included in any glyphset definition
 * U+0330 COMBINING TILDE BELOW: try adding one of: cherokee, syriac, math
 * U+0331 COMBINING MACRON BELOW: try adding one of: cherokee, gothic, caucasian-albanian, syriac, tifinagh
 * U+0332 COMBINING LOW LINE: not included in any glyphset definition
 * U+0334 COMBINING TILDE OVERLAY: not included in any glyphset definition
 * U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition
 * U+0358 COMBINING DOT ABOVE RIGHT: try adding osage
 * U+03BB GREEK SMALL LETTER LAMDA: try adding one of: greek, math
 * U+03C0 GREEK SMALL LETTER PI: try adding one of: yi, greek, math
 * U+03C7 GREEK SMALL LETTER CHI: try adding one of: greek, math
 * U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai
 * U+1D58 MODIFIER LETTER SMALL U: not included in any glyphset definition
 * U+1D5B MODIFIER LETTER SMALL V: not included in any glyphset definition
 * U+1D7D LATIN SMALL LETTER P WITH STROKE: not included in any glyphset definition
 * U+1DBB MODIFIER LETTER SMALL Z: not included in any glyphset definition
 * U+1DBF MODIFIER LETTER SMALL THETA: not included in any glyphset definition
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
 * U+207F SUPERSCRIPT LATIN SMALL LETTER N: not included in any glyphset definition
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
 * U+2144 TURNED SANS-SERIF CAPITAL Y: not included in any glyphset definition
 * U+2153 VULGAR FRACTION ONE THIRD: not included in any glyphset definition
 * U+2154 VULGAR FRACTION TWO THIRDS: not included in any glyphset definition
 * U+2190 LEFTWARDS ARROW: try adding one of: symbols, math
 * U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math
 * U+2194 LEFT RIGHT ARROW: try adding one of: emoji, symbols, math
 * U+2195 UP DOWN ARROW: try adding one of: emoji, symbols, math
 * U+2196 NORTH WEST ARROW: try adding one of: emoji, symbols, math
 * U+2197 NORTH EAST ARROW: try adding one of: emoji, symbols, math
 * U+2198 SOUTH EAST ARROW: try adding one of: emoji, symbols, math
 * U+2199 SOUTH WEST ARROW: try adding one of: emoji, symbols, math
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
 * U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: symbols, math
 * U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols
 * U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols
 * U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding one of: emoji, symbols
 * U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: symbols, math
 * U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols
 * U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols
 * U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols
 * U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: symbols, math
 * U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols
 * U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols
 * U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding one of: emoji, symbols
 * U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: symbols, math
 * U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols
 * U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols
 * U+25C6 BLACK DIAMOND: try adding symbols
 * U+25C7 WHITE DIAMOND: try adding symbols
 * U+25CA LOZENGE: try adding one of: symbols, math
 * U+25CB WHITE CIRCLE: try adding symbols
 * U+25CF BLACK CIRCLE: try adding symbols
 * U+25E6 WHITE BULLET: try adding symbols
 * U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math
 * U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math
 * U+3008 LEFT ANGLE BRACKET: try adding one of: chinese-simplified, japanese, phags-pa, chinese-hongkong, yi, chinese-traditional, tai-le
 * U+3009 RIGHT ANGLE BRACKET: try adding one of: chinese-simplified, japanese, phags-pa, chinese-hongkong, yi, chinese-traditional, tai-le
 * U+AB53 LATIN SMALL LETTER CHI: not included in any glyphset definition
 * U+FF0D FULLWIDTH HYPHEN-MINUS: try adding chinese-simplified

Or you can add the above codepoints to one of the subsets supported by the font: `cyrillic-ext`, `latin`, `latin-ext`, `vietnamese` [code: unreachable-subsetting]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- _part.cut

	- dotlessi_ogonek

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
greaterequal, lessequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Euro (U+20AC): L<<231.0,550.0>--<231.0,547.0>> -> L<<231.0,547.0>--<231.0,519.0>>

	* paragraph (U+00B6): L<<182.0,715.0>--<491.0,716.0>> -> L<<491.0,716.0>--<648.0,716.0>>

	* section (U+00A7): L<<268.0,464.0>--<326.0,459.0>> -> L<<326.0,459.0>--<344.0,457.0>>

	* uni024E (U+024E): L<<421.0,491.0>--<110.0,517.0>> -> L<<110.0,517.0>--<27.0,517.0>>

	* uni024F (U+024F): L<<421.0,491.0>--<110.0,517.0>> -> L<<110.0,517.0>--<27.0,517.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* Euro (U+20AC): L<<218.0,722.0>--<426.0,721.0>>

	* Ohungarumlaut (U+0150): L<<393.0,877.0>--<511.0,878.0>>

	* Uhungarumlaut (U+0170): L<<423.0,877.0>--<541.0,878.0>>

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

	* bracketleft (U+005B): L<<30.0,-125.0>--<33.0,837.0>>

	* bracketright (U+005D): L<<322.0,842.0>--<319.0,-120.0>>

	* eight (U+0038): L<<189.0,716.0>--<451.0,715.0>>

	* eight (U+0038): L<<431.0,-8.0>--<209.0,-7.0>>

	* five (U+0035): L<<27.0,179.0>--<28.0,470.0>>

	* five (U+0035): L<<592.0,410.0>--<591.0,178.0>>

	* florin (U+0192): L<<29.0,0.0>--<30.0,434.0>>

	* four (U+0034): L<<581.0,-1.0>--<31.0,-3.0>>

	* hungarumlaut (U+02DD): L<<202.0,768.0>--<320.0,769.0>>

	* nine (U+0039): L<<24.0,180.0>--<25.0,470.0>>

	* nine (U+0039): L<<399.0,-7.0>--<213.0,-6.0>>

	* nine (U+0039): L<<589.0,550.0>--<588.0,179.0>>

	* ohungarumlaut (U+0151): L<<393.0,877.0>--<511.0,878.0>>

	* one (U+0031): L<<210.0,715.0>--<397.0,716.0>>

	* one (U+0031): L<<397.0,716.0>--<398.0,495.0>>

	* onequarter (U+00BC): L<<298.0,0.0>--<59.0,-1.0>>

	* paragraph (U+00B6): L<<182.0,715.0>--<491.0,716.0>>

	* percent (U+0025): L<<481.0,722.0>--<599.0,721.0>>

	* perthousand (U+2030): L<<481.0,722.0>--<599.0,721.0>>

	* radical (U+221A): L<<376.0,-101.0>--<181.0,-100.0>>

	* radical (U+221A): L<<512.0,899.0>--<636.0,898.0>>

	* seven (U+0037): L<<26.0,0.0>--<27.0,434.0>>

	* seven (U+0037): L<<27.0,716.0>--<534.0,714.0>>

	* seven (U+0037): L<<534.0,-1.0>--<26.0,0.0>>

	* six (U+0036): L<<430.0,-6.0>--<216.0,-5.0>>

	* sterling (U+00A3): L<<564.0,589.0>--<393.0,590.0>>

	* threequarters (U+00BE): L<<298.0,0.0>--<59.0,-1.0>>

	* triagdn (U+25BC): L<<29.0,731.0>--<733.0,728.0>>

	* triagup (U+25B2): L<<733.0,141.0>--<29.0,144.0>>

	* uhungarumlaut (U+0171): L<<423.0,877.0>--<541.0,878.0>>

	* uni00B9 (U+00B9): L<<210.0,715.0>--<397.0,716.0>>

	* uni00B9 (U+00B9): L<<397.0,716.0>--<398.0,495.0>>

	* uni030B (U+030B): L<<202.0,768.0>--<320.0,769.0>>

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

	* uni25C3 (U+25C3): L<<321.0,429.0>--<320.0,71.0>> [code: found-semi-vertical]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><br></div></details>

### Summary

| 💔 ERROR | ☠ FATAL | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 0 | 3 | 9 | 125 | 7 | 111 |
| 0% | 0% | 1% | 4% | 49% | 3% | 44% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
