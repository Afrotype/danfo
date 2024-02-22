## FontBakery report

fontbakery version: 0.11.2

<h2>Experimental checks</h2><p>These won't break the CI job for now, but will become effective after some time if nobody raises any concern.</p><details><summary><b>[1] Danfo-Regular[ELSH].ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Ensure the font supports case swapping for all its glyphs. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/case_mapping">com.google.fonts/check/case_mapping</a>)</summary><div>


* 🔥 **FAIL** The following glyphs lack their case-swapping counterparts:

| Glyph present in the font | Missing case-swapping counterpart |
| :--- | :--- |
| U+03BB: GREEK SMALL LETTER LAMDA | U+039B: GREEK CAPITAL LETTER LAMDA |
| U+03C7: GREEK SMALL LETTER CHI | U+03A7: GREEK CAPITAL LETTER CHI |

 [code: missing-case-counterparts]
</div></details><br></div></details><h2>All other checks</h2><details><summary><b>[1] Family checks</b></summary><div><details><summary>ℹ <b>INFO:</b> Check axis ordering on the STAT table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/STAT/axis_order">com.google.fonts/check/STAT/axis_order</a>)</summary><div>


* ℹ **INFO** None of the fonts lack a STAT table.

	And these are the most common STAT axis orderings:
	('ELSH', 1) [code: summary]
</div></details><br></div></details><details><summary><b>[20] Danfo-Regular[ELSH].ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking file is named canonically. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename">com.google.fonts/check/canonical_filename</a>)</summary><div>


* 🔥 **FAIL** Expected "Danfo[ELSH].ttf. Got Danfo-Regular[ELSH].ttf. [code: bad-filename]
</div></details><details><summary>🔥 <b>FAIL:</b> Shapes languages in all GF glyphsets. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyphsets/shape_languages">com.google.fonts/check/glyphsets/shape_languages</a>)</summary><div>


* 🔥 **FAIL** GF_Latin_African glyphset:

| Language | FAIL messages |
| :--- | :--- |
| bqv_Latn (Koro Wachi) | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
| ddn_Latn (Dendi) | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach uni0304 to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach uni0304 to uni0190 |
| nus_Latn (Nuer) | Shaper didn't attach uni0331 to uni025B |
|  ^  | Shaper didn't attach uni0331 to uni0190 |
|  ^  | Shaper didn't attach uni0308 to uni0331 |
|  ^  | Shaper didn't attach uni0331 to uni025B |
|  ^  | Shaper didn't attach uni0308 to uni0331 |
|  ^  | Shaper didn't attach uni0308 to uni0190 |
|  ^  | Shaper didn't attach uni0331 to uni0190 |
|  ^  | Shaper didn't attach uni0308 to uni025B |
|  ^  | Shaper didn't attach uni0308 to uni025B |
|  ^  | Shaper didn't attach uni0308 to uni0190 |
|  ^  | Shaper didn't attach uni0331 to uni025B |
|  ^  | Shaper didn't attach uni0331 to uni0190 |
|  ^  | Shaper didn't attach uni0331 to uni025B |
|  ^  | Shaper didn't attach uni0308 to uni0331 |
|  ^  | Shaper didn't attach uni0331 to uni025B |
|  ^  | Shaper didn't attach uni0308 to uni0331 |
|  ^  | Shaper didn't attach uni0331 to uni0190 |
|  ^  | Shaper didn't attach uni0308 to uni0331 |
|  ^  | Shaper didn't attach uni0331 to uni0190 |
|  ^  | Shaper didn't attach uni0308 to uni0331 |
| kdh_Latn (Tem) | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to Upsilonlatin |
| kpe_Latn (Kpelle) | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| pnz_Latn (Pana (Central African Republic)) | Shaper didn't attach uni0327 to uni0190 |
|  ^  | Shaper didn't attach uni0327 to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0327 |
|  ^  | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach uni0327 to uni025B |
|  ^  | Shaper didn't attach uni0327 to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni0327 |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach uni0327 to uni0190 |
|  ^  | Shaper didn't attach uni0302 to uni0327 |
|  ^  | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach uni0327 to uni025B |
|  ^  | Shaper didn't attach uni0302 to uni0327 |
| lu_Latn (Luba-Katanga) | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
| lob_Latn (Lobi) | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
| dnj_Latn_LR (Dan) | Shaper didn't attach uni0302 to uniA78D |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0265 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni0265 |
|  ^  | Shaper didn't attach acutecomb to uniA78D |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uniA78D |
|  ^  | Shaper didn't attach tildecomb to uni0265 |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach uni0302 to uni0265 |
|  ^  | Shaper didn't attach gravecomb to uniA78D |
| bfd_Latn (Bafut) | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni025B |
| nnw_Latn (Southern Nuni) | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| byv_Latn (Medumba) | Shaper didn't attach uni0302 to uni2C6D |
|  ^  | Shaper didn't attach uni0302 to uni0251 |
|  ^  | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni2C6D |
|  ^  | Shaper didn't attach uni030C to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0251 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach uni030C to uni0251 |
|  ^  | Shaper didn't attach uni030C to uni2C6D |
| nmg_Latn (Kwasio) | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach uni030C to uni025B |
|  ^  | Shaper didn't attach uni0304 to uni025B |
|  ^  | Shaper didn't attach uni0304 to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni025B |
|  ^  | Shaper didn't attach uni030C to uni0190 |
|  ^  | Shaper didn't attach uni0304 to uni025B |
|  ^  | Shaper didn't attach uni0304 to uni0190 |
| bqp_Latn (Bisã) | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| grb_Latn (Grebo) | Shaper didn't attach uni0308 to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni025B |
|  ^  | Shaper didn't attach uni0308 to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni025B |
| ewo_Latn (Ewondo) | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni025B |
|  ^  | Shaper didn't attach uni030C to uni0190 |
| nyb_Latn (Nyangbo) | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| gna_Latn (Kaansa) | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach uni030C to uni025B |
| lol_Latn (Mongo) | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| ife_Latn (Ifè) | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
| mcp_Latn (Makaa) | Shaper didn't attach uni0327 to uni0190 |
|  ^  | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach uni0327 to uni025B |
|  ^  | Shaper didn't attach uni030C to uni0327 |
|  ^  | Shaper didn't attach uni0327 to uni025B |
|  ^  | Shaper didn't attach uni0327 to uni0190 |
|  ^  | Shaper didn't attach uni0302 to uni0327 |
|  ^  | Shaper didn't attach uni030C to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach uni0327 to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni0327 |
|  ^  | Shaper didn't attach uni0327 to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0327 |
|  ^  | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach uni030C to uni025B |
|  ^  | Shaper didn't attach uni0327 to uni025B |
|  ^  | Shaper didn't attach uni0302 to uni0327 |
|  ^  | Shaper didn't attach uni0327 to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni0327 |
| ajg_Latn (Aja) | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
| kst_Latn (Winyé) | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| etx_Latn (Iten) | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| dya_Latn (Dyan) | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
| mev_Latn (Mano) | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
| pkb_Latn (Pokomo) | Shaper didn't attach uni032F to t |
|  ^  | Shaper didn't attach uni032F to d |
|  ^  | Shaper didn't attach uni032F to D |
|  ^  | Shaper didn't attach uni032F to T |
| gkp_Latn (Kpelle, Guinea) | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| vai_Latn (Vai (Latin)) | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
| goa_Latn (Guro) | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni025B |
| dip_Latn (Dinka, Northeastern) | Shaper didn't attach uni0308 to uni0190 |
|  ^  | Shaper didn't attach uni0308 to uni025B |
| lnl_Latn (South Central Banda) | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach uni0308 to uni0190 |
|  ^  | Shaper didn't attach uni0308 to uni025B |
| mdt_Latn (Mbere) | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| tuz_Latn (Turka) | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
| bfo_Latn (Malba Birifor) | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
| fmp_Latn (Fe’fe’) | Shaper didn't attach acutecomb to uni0251 |
|  ^  | Shaper didn't attach uni0304 to uni2C6D |
|  ^  | Shaper didn't attach gravecomb to uni2C6D |
|  ^  | Shaper didn't attach uni0304 to uni0251 |
|  ^  | Shaper didn't attach acutecomb to uni2C6D |
|  ^  | Shaper didn't attach gravecomb to uni0251 |
|  ^  | Shaper didn't attach uni030C to uni0251 |
|  ^  | Shaper didn't attach uni030C to uni2C6D |
| rub_Latn (Gungu) | Shaper didn't attach uni032F to b |
|  ^  | Shaper didn't attach uni032F to B |
| kkj_Latn (Kako) | Shaper didn't attach uni0327 to uni0190 |
|  ^  | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach uni0327 to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach uni0327 to uni025B |
| emk_Latn (Maninkakan, Eastern) | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| agq_Latn (Aghem) | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni025B |
|  ^  | Shaper didn't attach uni0304 to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach uni0304 to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni025B |
|  ^  | Shaper didn't attach uni030C to uni0190 |
|  ^  | Shaper didn't attach uni0304 to uni025B |
|  ^  | Shaper didn't attach uni0304 to uni0190 |
| neb_Latn (Toura) | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| ksp_Latn (Kabba) | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach uni0302 to uni0190 |
| teo_Latn (Teso) | Some base glyphs were missing: ᵃ, ᵉ, ᵋ, ᵒ, ᵓ, ᶤ, ᶶ, ⁱ |
|  ^  | Shaper produced a .notdef |
| bom_Latn (Berom) | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| apd_Latn (Sudanese Arabic) | Some mark glyphs were missing: ◌͟ |
| mge_Latn (Mango) | Shaper didn't attach uni0330 to uni025B |
|  ^  | Shaper didn't attach uni0330 to uni0190 |
| tcd_Latn (Tafi) | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| tik_Latn (Tikar) | Shaper didn't attach gravecomb to Eng |
|  ^  | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni025B |
|  ^  | Shaper didn't attach gravecomb to eng |
|  ^  | Shaper didn't attach gravecomb to uni025B |
| sld_Latn (Sissala) | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| dua_Latn (Duala) | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| udu_Latn (Uduk) | Some base glyphs were missing: T͟H, t͟h |
|  ^  | Some mark glyphs were missing: ◌͟ |
|  ^  | Shaper produced a .notdef |
| nnh_Latn (Ngiemboon) | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni025B |
|  ^  | Shaper didn't attach uni030C to uni0190 |
| gvl_Latn (Gulay) | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| bas_Latn (Basaa) | Shaper didn't attach uni1DC6 to uni025B |
|  ^  | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni0190 |
|  ^  | Shaper didn't attach uni1DC7 to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach uni1DC7 to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni025B |
|  ^  | Shaper didn't attach uni0304 to uni025B |
|  ^  | Shaper didn't attach uni0304 to uni0190 |
|  ^  | Shaper didn't attach uni1DC6 to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni025B |
|  ^  | Shaper didn't attach uni030C to uni0190 |
|  ^  | Shaper didn't attach uni0304 to uni025B |
|  ^  | Shaper didn't attach uni0304 to uni0190 |
|  ^  | Shaper didn't attach uni1DC6 to uni025B |
|  ^  | Shaper didn't attach uni1DC7 to uni025B |
|  ^  | Shaper didn't attach uni1DC6 to uni0190 |
|  ^  | Shaper didn't attach uni1DC7 to uni0190 |
| tbz_Latn (Ditammari) | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| box_Latn (Buamu) | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| pug_Latn (Phuie) | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
| bwj_Latn (Láá Láá Bwamu) | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
| bbj_Latn (Ghomala) | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni025B |
| wwa_Latn (Waama) | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni025B |
| blo_Latn (Anii) | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach uni0302 to Upsilonlatin |
|  ^  | Shaper didn't attach gravecomb to Upsilonlatin |
|  ^  | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to Upsilonlatin |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| dgi_Latn (Northern Dagara) | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| gur_Latn (Frafra) | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
| dnj_Latn (Dan) | Some base glyphs were missing: ɤ, ɤ̀, ɤ́, ɤ̂, ɤ̄, ɤ̋, ɤ̏, Ɤ, Ɤ̀, Ɤ́, Ɤ̂, Ɤ̄, Ɤ̋, Ɤ̏ |
|  ^  | Shaper didn't attach gravecomb to uni028C |
|  ^  | Shaper produced a .notdef |
| yba_Latn (Yala) | Shaper didn't attach uni030D to uni0190 |
|  ^  | Shaper didn't attach uni030D to uni025B |
|  ^  | Shaper didn't attach uni0304 to uni025B |
|  ^  | Shaper didn't attach uni0304 to uni0190 |
| kzc_Latn (Bondoukou Kulango) | Shaper didn't attach tildecomb to uniA7B7 |
|  ^  | Shaper didn't attach tildecomb to uni026A |
|  ^  | Shaper didn't attach tildecomb to uniA7B6 |
|  ^  | Shaper didn't attach tildecomb to uniA7AE |
| bqc_Latn (Boko) | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| myk_Latn (Mamara Senoufo) | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| yav_Latn (Yangben) | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
| ozm_Latn (Koonzime) | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach uni030C to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| bsq_Latn (Bassa) | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
| din_Latn (Dinka) | Shaper didn't attach uni0308 to uni025B |
|  ^  | Shaper didn't attach uni0308 to uni0190 |
| biv_Latn (Birifor, Southern) | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to Upsilonlatin |
|  ^  | Shaper didn't attach tildecomb to uni025B |
| bax_Latn (Bamun, Latin) | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni025B |
| nga_Latn (Ngbaka) | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| nmz_Latn (Nawdm) | Shaper didn't attach uni0308 to eng |
|  ^  | Shaper didn't attach uni0308 to Eng |
| ntm_Latn (Nateni) | Shaper didn't attach uni0330 to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0330 |
|  ^  | Shaper didn't attach uni0330 to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni0330 |
|  ^  | Shaper didn't attach uni0330 to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni0330 |
|  ^  | Shaper didn't attach uni0330 to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach uni0330 to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach uni0330 to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0330 |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| bba_Latn (Baatonum) | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
| lee_Latn (Lyélé) | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
| soy_Latn (Miyobe) | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| tvu_Latn (Tunen) | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| ksf_Latn (Bafia) | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| gov_Latn (Goo) | Some base glyphs were missing: ɤ, ɤ̀, ɤ́, ɤ̂, Ɤ, Ɤ̀, Ɤ́, Ɤ̂ |
|  ^  | Shaper didn't attach gravecomb to uni028C |
|  ^  | Shaper didn't attach uni0302 to eng |
|  ^  | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper produced a .notdef |
| loq_Latn (Lobala) | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| mor_Latn (Moro) | Some base glyphs were missing: Ꟈ, ꟈ |
|  ^  | Shaper produced a .notdef |
| sbd_Latn (Southern Samo) | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach uni0308 to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni025B |
|  ^  | Shaper didn't attach uni0308 to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
| ee_Latn (Ewe) | Shaper didn't attach tildecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach tildecomb to uni025B |
|  ^  | Shaper didn't attach tildecomb to uni0190 |
| ln_Latn (Lingala) | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach uni030C to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni025B |
|  ^  | Shaper didn't attach uni030C to uni0190 |
| jgo_Latn (Ngomba) | Shaper didn't attach gravecomb to Eng |
|  ^  | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach acutecomb to Eng |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni025B |
|  ^  | Shaper didn't attach uni0304 to uni025B |
|  ^  | Shaper didn't attach gravecomb to eng |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach uni0304 to eng |
|  ^  | Shaper didn't attach acutecomb to eng |
|  ^  | Shaper didn't attach uni0304 to uni0190 |
|  ^  | Shaper didn't attach uni0304 to Eng |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach acutecomb to uni025B |
|  ^  | Shaper didn't attach acutecomb to uni0190 |
|  ^  | Shaper didn't attach gravecomb to uni025B |
|  ^  | Shaper didn't attach gravecomb to uni0190 |
|  ^  | Shaper didn't attach uni0302 to uni025B |
|  ^  | Shaper didn't attach uni0302 to uni0190 |
|  ^  | Shaper didn't attach uni030C to uni025B |
|  ^  | Shaper didn't attach uni030C to uni0190 |
|  ^  | Shaper didn't attach uni0304 to uni025B |
|  ^  | Shaper didn't attach uni0304 to uni0190 |
|  ^  | Shaper didn't attach acutecomb to eng |
|  ^  | Shaper didn't attach acutecomb to Eng |
|  ^  | Shaper didn't attach gravecomb to eng |
|  ^  | Shaper didn't attach gravecomb to Eng |
|  ^  | Shaper didn't attach uni0304 to eng |
|  ^  | Shaper didn't attach uni0304 to Eng |

 [code: failed-language-shaping]
* ⚠ **WARN** GF_Latin_African glyphset:

| Language | FAIL messages |
| :--- | :--- |
| mua_Latn (Mundang) | No variant glyphs were found for Eng |
| gng_Latn (Ngangam) | No variant glyphs were found for Eng |
| kyf_Latn (Kouya) | No variant glyphs were found for Eng |
| bsc_Latn (Bassari) | No variant glyphs were found for Eng |
| hna_Latn (Mina) | No exemplar glyphs were defined for language Mina |
| amo_Latn (Amo) | No exemplar glyphs were defined for language Amo |
| lmp_Latn (Limbum) | No variant glyphs were found for Eng |
| nhu_Latn (Noone) | No variant glyphs were found for Eng |
| dop_Latn (Lukpa) | No variant glyphs were found for Eng |
| nus_Latn (Nuer) | No variant glyphs were found for Eng |
| bcw_Latn (Bana) | No variant glyphs were found for Eng |
| sxw_Latn (Saxwe Gbe) | No variant glyphs were found for Eng |
| toq_Latn (Toposa) | No variant glyphs were found for Eng |
| kdh_Latn (Tem) | No variant glyphs were found for Eng |
| ahs_Latn (Ashe) | No variant glyphs were found for Eng |
| ekm_Latn (Elip) | No variant glyphs were found for Eng |
| ffm_Latn (Maasina Fulfulde) | No variant glyphs were found for Eng |
| tpm_Latn (Tampulma) | No variant glyphs were found for Eng |
| wan_Latn (Wan) | No variant glyphs were found for Eng |
| moa_Latn (Mwan) | No variant glyphs were found for Eng |
| mgo_Latn (Metaʼ) | No variant glyphs were found for Eng |
| dyo_Latn (Jola-Fonyi) | No variant glyphs were found for Eng |
| kvf_Latn (Kabalai) | No variant glyphs were found for Eng |
| tuq_Latn (Tedaga) | No variant glyphs were found for Eng |
| dow_Latn (Doyayo) | No variant glyphs were found for Eng |
| tem_Latn (Timne) | No variant glyphs were found for Eng |
| fuh_Latn (Fulfulde, Western Niger) | No variant glyphs were found for Eng |
| lok_Latn (Loko) | No variant glyphs were found for Eng |
| adj_Latn (Adioukrou) | No variant glyphs were found for Eng |
| nnw_Latn (Southern Nuni) | No variant glyphs were found for Eng |
| tnr_Latn (Ménik) | No variant glyphs were found for Eng |
| mhi_Latn (Ma’di) | No variant glyphs were found for Eng |
| ikx_Latn (Ik) | No variant glyphs were found for Eng |
| nmg_Latn (Kwasio) | No variant glyphs were found for Eng |
| lig_Latn (Ligbi) | No variant glyphs were found for Eng |
| ewo_Latn (Ewondo) | No variant glyphs were found for Eng |
| god_Latn (Godié) | No variant glyphs were found for Eng |
| ted_Latn (Krumen, Tepo) | No variant glyphs were found for Eng |
| bib_Latn (Bissa) | No variant glyphs were found for Eng |
| mmu_Latn (Mmaala) | No variant glyphs were found for Eng |
| dyi_Latn (Sénoufo, Djimini) | No variant glyphs were found for Eng |
| anv_Latn (Denya) | No variant glyphs were found for Eng |
| gaa_Latn (Ga) | No variant glyphs were found for uni01B7 |
| bim_Latn (Bimoba) | No variant glyphs were found for Eng |
| sok_Latn (Sokoro) | No variant glyphs were found for Eng |
| dts_Latn (Dogon, Toro So) | No variant glyphs were found for Eng |
| bza_Latn (Bandi) | No variant glyphs were found for Eng |
| nym_Latn (Nyamwezi) | No variant glyphs were found for Eng |
| dje_Latn (Zarma) | No variant glyphs were found for Eng |
| mcp_Latn (Makaa) | No variant glyphs were found for Eng |
| mbu_Latn (Mbula-Bwazza) | No variant glyphs were found for Eng |
| hag_Latn (Hanga) | No variant glyphs were found for Eng |
| xrb_Latn (Karaboro, Eastern) | No variant glyphs were found for Eng |
| sig_Latn (Paasaal) | No variant glyphs were found for Eng |
| acd_Latn (Gikyode) | No variant glyphs were found for Eng |
| spp_Latn (Sénoufo, Supyire) | No variant glyphs were found for Eng |
| gud_Latn (Dida, Yocoboué) | No variant glyphs were found for Eng |
| naw_Latn (Nawuri) | No variant glyphs were found for Eng |
| ade_Latn (Adele) | No variant glyphs were found for Eng |
| yam_Latn (Yamba) | No variant glyphs were found for Eng |
| krs_Latn (Gbaya (Sudan)) | No variant glyphs were found for Eng |
| knp_Latn (Kwanja) | No variant glyphs were found for Eng |
| xon_Latn (Konkomba) | No variant glyphs were found for Eng |
| ken_Latn (Kenyang) | No variant glyphs were found for Eng |
| csk_Latn (Jola-Kasa) | No variant glyphs were found for Eng |
| pbi_Latn (Parkwa) | No variant glyphs were found for Eng |
| mgc_Latn (Morokodo) | No variant glyphs were found for Eng |
| bud_Latn (Ntcham) | No variant glyphs were found for Eng |
| fue_Latn (Fulfulde, Borgu) | No variant glyphs were found for Eng |
| avn_Latn (Avatime) | No variant glyphs were found for Eng |
| bex_Latn (Jur Modo) | No variant glyphs were found for Eng |
| vai_Latn (Vai (Latin)) | No variant glyphs were found for Eng |
| gnd_Latn (Zulgo-Gemzek) | No variant glyphs were found for Eng |
| kye_Latn (Krache) | No variant glyphs were found for Eng |
| mcu_Latn (Mambila, Cameroon) | No variant glyphs were found for Eng |
| etu_Latn (Ejagham) | No variant glyphs were found for Eng |
| ntr_Latn (Delo) | No variant glyphs were found for Eng |
| meq_Latn (Merey) | No variant glyphs were found for Eng |
| lgg_Latn (Lugbara) | No variant glyphs were found for Eng |
| fub_Latn (Fulfulde, Adamawa) | No variant glyphs were found for Eng |
| mfi_Latn (Wandala) | No variant glyphs were found for Eng |
| fmp_Latn (Fe’fe’) | No variant glyphs were found for Eng |
| rub_Latn (Gungu) | No variant glyphs were found for Eng |
| kzr_Latn (Karang) | No variant glyphs were found for Eng |
| mnf_Latn (Mundani) | No variant glyphs were found for Eng |
| agq_Latn (Aghem) | No variant glyphs were found for Eng |
| nfr_Latn (Nafaanra) | No variant glyphs were found for Eng |
| fod_Latn (Foodo) | No variant glyphs were found for Eng |
| vag_Latn (Vagla) | No variant glyphs were found for Eng |
| xuo_Latn (Kuo) | No variant glyphs were found for Eng |
| nuv_Latn (Nuni, Northern) | No variant glyphs were found for Eng |
| nko_Latn (Nkonya) | No variant glyphs were found for Eng |
| log_Latn (Logo) | No variant glyphs were found for Eng |
| kpo_Latn (Ikposo) | No variant glyphs were found for Eng |
| ggn_Latn (Eastern Gurung, Latin) | No exemplar glyphs were defined for language Eastern Gurung, Latin |
| sil_Latn (Sisaala, Tumulung) | No variant glyphs were found for Eng |
| ses_Latn (Koyraboro Senni) | No variant glyphs were found for Eng |
| kus_Latn (Kusaal) | No variant glyphs were found for Eng |
| ncu_Latn (Chumburung) | No variant glyphs were found for Eng |
| tik_Latn (Tikar) | No variant glyphs were found for Eng |
| ktj_Latn (Krumen, Plapo) | No variant glyphs were found for Eng |
| srr_Latn (Serer) | No variant glyphs were found for Eng |
| sld_Latn (Sissala) | No variant glyphs were found for Eng |
| sav_Latn (Saafi-Saafi) | No variant glyphs were found for Eng |
| dua_Latn (Duala) | No variant glyphs were found for Eng |
| ny_Latn (Nyanja) | No variant glyphs were found for Eng |
| mgy_Latn (Mbunga) | No exemplar glyphs were defined for language Mbunga |
| nnh_Latn (Ngiemboon) | No variant glyphs were found for Eng |
| gde_Latn (Gude) | No variant glyphs were found for Eng |
| bas_Latn (Basaa) | No variant glyphs were found for Eng |
| mzw_Latn (Deg) | No variant glyphs were found for Eng |
| avu_Latn (Avokaya) | No variant glyphs were found for Eng |
| muy_Latn (Muyang) | No variant glyphs were found for Eng |
| kqp_Latn (Kimré) | No variant glyphs were found for Eng |
| ndz_Latn (Ndogo) | No variant glyphs were found for Eng |
| yat_Latn (Yambeta) | No variant glyphs were found for Eng |
| pil_Latn (Yom) | No variant glyphs were found for Eng |
| blo_Latn (Anii) | No variant glyphs were found for Eng |
| bzw_Latn (Basa) | No variant glyphs were found for Eng |
| mas_Latn (Masai) | No variant glyphs were found for Eng |
| wo_Latn (Wolof) | No variant glyphs were found for Eng |
| nhb_Latn (Beng) | No variant glyphs were found for Eng |
| yas_Latn (Nugunu) | No variant glyphs were found for Eng |
| dgi_Latn (Northern Dagara) | No variant glyphs were found for Eng |
| agc_Latn (Agatu) | No variant glyphs were found for Eng |
| fuq_Latn (Central-Eastern Niger Fulfulde) | No variant glyphs were found for Eng |
| dzg_Latn (Dazaga) | No variant glyphs were found for Eng |
| dnj_Latn (Dan) | No variant glyphs were found for uni0181 |
| ahl_Latn (Igo) | No variant glyphs were found for Eng |
| kyq_Latn (Kenga) | No variant glyphs were found for Eng |
| gux_Latn (Gourmanchéma) | No variant glyphs were found for Eng |
| cko_Latn (Anufo) | No variant glyphs were found for Eng |
| tod_Latn (Toma) | No variant glyphs were found for uni01B2 |
| wci_Latn (Gbe, Waci) | No variant glyphs were found for Eng |
| lg_Latn (Ganda) | No variant glyphs were found for Eng |
| bm_Latn (Bambara) | No variant glyphs were found for Eng |
| myk_Latn (Mamara Senoufo) | No variant glyphs were found for Eng |
| dyu_Latn (Dyula) | No variant glyphs were found for Eng |
| twq_Latn (Tasawaq) | No variant glyphs were found for Eng |
| yav_Latn (Yangben) | No variant glyphs were found for Eng |
| kfo_Latn (Koro) | No exemplar glyphs were defined for language Koro |
| ozm_Latn (Koonzime) | No variant glyphs were found for Eng |
| gmm_Latn (Gbaya-Mbodomo) | No variant glyphs were found for Eng |
| boz_Latn (Tiéyaxo Bozo) | No variant glyphs were found for Eng |
| xed_Latn (Hdi) | No variant glyphs were found for Eng |
| kmy_Latn (Koma) | No variant glyphs were found for Eng |
| biv_Latn (Birifor, Southern) | No variant glyphs were found for Eng |
| xwe_Latn (Gbe, Xwela) | No variant glyphs were found for Eng |
| mdj_Latn (Mangbetu) | No variant glyphs were found for Eng |
| vut_Latn (Vute) | No variant glyphs were found for Eng |
| mbo_Latn (Mbo) | No variant glyphs were found for Eng |
| gej_Latn (Gen) | No variant glyphs were found for Eng |
| bsp_Latn (Baga Sitemu) | No variant glyphs were found for Eng |
| mur_Latn (Murle) | No variant glyphs were found for Eng |
| cme_Latn (Cerma) | No variant glyphs were found for Eng |
| nmz_Latn (Nawdm) | No variant glyphs were found for Eng |
| daa_Latn (Dangaléat) | No variant glyphs were found for Eng |
| lem_Latn (Nomaande) | No variant glyphs were found for Eng |
| syi_Latn (Seki) | No exemplar glyphs were defined for language Seki |
| mfv_Latn (Mandjak) | No variant glyphs were found for Eng |
| lee_Latn (Lyélé) | No variant glyphs were found for Eng |
| soy_Latn (Miyobe) | No variant glyphs were found for Eng |
| tvu_Latn (Tunen) | No variant glyphs were found for Eng |
| maw_Latn (Mampruli) | No variant glyphs were found for Eng |
| ksf_Latn (Bafia) | No variant glyphs were found for Eng |
| loq_Latn (Lobala) | No variant glyphs were found for Eng |
| cch_Latn (Atsam) | No exemplar glyphs were defined for language Atsam |
| bav_Latn (Vengo) | No variant glyphs were found for Eng |
| ee_Latn (Ewe) | No variant glyphs were found for Eng |
| las_Latn (Lama (Togo)) | No variant glyphs were found for Eng |
| jgo_Latn (Ngomba) | No variant glyphs were found for Eng |
| bqj_Latn (Bandial) | No variant glyphs were found for Eng |

 [code: warning-language-shaping]
</div></details><details><summary>🔥 <b>FAIL:</b> Check a font's STAT table contains compulsory Axis Values. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/STAT">com.google.fonts/check/STAT</a>)</summary><div>


* 🔥 **FAIL** Compulsory STAT Axis Values are incorrect:

 | Name | Axis | Current Value | Current Flags | Current LinkedValue | Expected Value | Expected Flags | Expected LinkedValue |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Regular | wght | N/A | N/A | N/A | 400.0 | 0 | 700.0 |
 [code: bad-axis-values]
</div></details><details><summary>🔥 <b>FAIL:</b> Check variable font instances (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fvar_instances">com.google.fonts/check/fvar_instances</a>)</summary><div>


* 🔥 **FAIL** fvar instances are incorrect:
- Delete additional instances

| Name | current | expected |
| :--- | :--- | :--- |
| Regular | ELSH=0.0 | ELSH=0.0 |
| Comb | ELSH=50.0 | N/A |
| Claw | ELSH=100.0 | N/A | [code: bad-fvar-instances]
</div></details><details><summary>🔥 <b>FAIL:</b> Validate STAT particle names and values match the fallback names in GFAxisRegistry. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/STAT/gf_axisregistry">com.google.fonts/check/STAT/gf_axisregistry</a>)</summary><div>


* 🔥 **FAIL** On the font variation axis 'ELSH', the name 'Regular' is not among the expected ones (Default) according to the Google Fonts Axis Registry. [code: invalid-name]
* 🔥 **FAIL** On the font variation axis 'ELSH', the name 'Comb' is not among the expected ones (Default) according to the Google Fonts Axis Registry. [code: invalid-name]
* 🔥 **FAIL** On the font variation axis 'ELSH', the name 'Claw' is not among the expected ones (Default) according to the Google Fonts Axis Registry. [code: invalid-name]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1068, but got 1050 instead [code: ascent]
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
121 more.

Use -F or --full-lists to disable shortening of long lists.

Or you can add the above codepoints to one of the subsets supported by the font: `cyrillic-ext`, `greek-ext`, `latin`, `latin-ext`, `vietnamese` [code: unreachable-subsetting]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure variable fonts include an avar table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/mandatory_avar_table">com.google.fonts/check/mandatory_avar_table</a>)</summary><div>


* ⚠ **WARN** This variable font does not have an avar table. [code: missing-avar]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- _part.cut

	- dotlessi_ogonek

	- hook.part

	- hookleft.part

	- hookright.part

	- rightHorn.part
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 298 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 279:
greater, less

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
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/Shaping Checks.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>ℹ <b>INFO:</b> Show hinting filesize impact. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/hinting_impact">com.google.fonts/check/hinting_impact</a>)</summary><div>


* ℹ **INFO** Hinting filesize impact:

 |               | Danfo-Regular[ELSH].ttf          |
 |:------------- | ---------------:|
 | Dehinted Size | 142.5kb |
 | Hinted Size   | 142.5kb   |
 | Increase      | 24 bytes      |
 | Change        | 0.0 %  |
 [code: size-impact]
</div></details><details><summary>ℹ <b>INFO:</b> Font has old ttfautohint applied? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint">com.google.fonts/check/old_ttfautohint</a>)</summary><div>


* ℹ **INFO** Could not detect which version of ttfautohint was used in this font. It is typically specified as a comment in the font version entries of the 'name' table. Such font version strings are currently: ['Version 1.000'] [code: version-not-detected]
</div></details><details><summary>ℹ <b>INFO:</b> EPAR table present in font? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/epar">com.google.fonts/check/epar</a>)</summary><div>


* ℹ **INFO** EPAR table not present in font. To learn more see https://github.com/fonttools/fontbakery/issues/818 [code: lacks-EPAR]
</div></details><details><summary>ℹ <b>INFO:</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/gasp">com.google.fonts/check/gasp</a>)</summary><div>


* ℹ **INFO** These are the ppm ranges declared on the gasp table:

PPM <= 65535:
	flag = 0x0F
	- Use grid-fitting
	- Use grayscale rendering
	- Use gridfitting with ClearType symmetric smoothing
	- Use smoothing along multiple axes with ClearType®
 [code: ranges]
</div></details><details><summary>ℹ <b>INFO:</b> Check for font-v versioning. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fontv">com.google.fonts/check/fontv</a>)</summary><div>


* ℹ **INFO** Version string is: "Version 1.000"
The version string must ideally include a git commit hash and either a "dev" or a "release" suffix such as in the example below:
"Version 1.3; git-0d08353-release" [code: bad-format]
</div></details><details><summary>ℹ <b>INFO:</b> Font contains all required tables? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/required_tables">com.google.fonts/check/required_tables</a>)</summary><div>


* ℹ **INFO** This font contains the following optional tables:

	- loca

	- prep

	- GPOS

	- GSUB

	- gasp [code: optional-tables]
</div></details><details><summary>ℹ <b>INFO:</b> List all superfamily filepaths (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/superfamily/list">com.google.fonts/check/superfamily/list</a>)</summary><div>


* ℹ **INFO** . [code: family-path]
</div></details><br></div></details>

### Summary

| 💔 ERROR | ☠ FATAL | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| 0 | 0 | 7 | 7 | 111 | 8 | 127 | 0 |
| 0% | 0% | 3% | 3% | 43% | 3% | 49% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **PASS**
* **DEBUG**
