## Fontbakery report

Fontbakery version: 0.7.33

<details>
<summary><b>[1] Family checks</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Is the command `ftxvalidator` (Apple Font Tool Suite) available?</summary>

* [com.google.fonts/check/ftxvalidator_is_available](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/ftxvalidator_is_available)
<pre>--- Rationale ---

There&#x27;s no reasonable (and legal) way to run the command `ftxvalidator` of the
Apple Font Tool Suite on a non-macOS machine. I.e. on GNU+Linux or Windows etc.

If Font Bakery is not running on an OSX machine, the machine running Font
Bakery could access `ftxvalidator` on OSX, e.g. via ssh or a remote procedure
call (rpc).

There&#x27;s an ssh example implementation at:
https://github.com/googlefonts/fontbakery/blob/master/prebuilt/workarounds
/ftxvalidator/ssh-implementation/ftxvalidator


</pre>

* ⚠ **WARN** Could not find ftxvalidator.

</details>
<br>
</details>
<details>
<summary><b>[8] YomogiFont-Regular.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: FONT_FAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/familyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/familyname)
<pre>--- Rationale ---

Checks that the family name infered from the font filename matches the string
at nameID 1 (NAMEID_FONT_FAMILY_NAME) if it conforms to RIBBI and otherwise
checks that nameID 1 is the family name + the style name.


</pre>

* 🔥 **FAIL** Entry [FONT_FAMILY_NAME(1):WINDOWS(3)] on the "name" table: Expected "Yomogi Font" but got "YomogiFont". [code: mismatch]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: FULL_FONT_NAME entries.</summary>

* [com.google.fonts/check/name/fullfontname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/fullfontname)

* 🔥 **FAIL** Entry [FULL_FONT_NAME(4):WINDOWS(3)] on the "name" table: Expected "Yomogi Font Regular"  but got "YomogiFont Regular". [code: bad-entry]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata.</summary>

* [com.google.fonts/check/monospace](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/monospace)
<pre>--- Rationale ---

There are various metadata in the OpenType spec to specify if a font is
monospaced or not. If the font is not truly monospaced, then no monospaced
metadata should be set (as sometimes they mistakenly are...)

Requirements for monospace fonts:

* post.isFixedPitch - &quot;Set to 0 if the font is proportionally spaced, non-zero
if the font is not proportionally spaced (monospaced)&quot;
  www.microsoft.com/typography/otspec/post.htm

* hhea.advanceWidthMax must be correct, meaning no glyph&#x27;s width value is
greater.
  www.microsoft.com/typography/otspec/hhea.htm

* OS/2.panose.bProportion must be set to 9 (monospace). Spec says: &quot;The PANOSE
definition contains ten digits each of which currently describes up to sixteen
variations. Windows uses bFamilyType, bSerifStyle and bProportion in the font
mapper to determine family type. It also uses bProportion to determine if the
font is monospaced.&quot;
  www.microsoft.com/typography/otspec/os2.htm#pan
  monotypecom-test.monotype.de/services/pan2

* OS/2.xAvgCharWidth must be set accurately.
  &quot;OS/2.xAvgCharWidth is used when rendering monospaced fonts, at least by
Windows GDI&quot;
  http://typedrawers.com/discussion/comment/15397/#Comment_15397

Also we should report an error for glyphs not of average width.

Please also note:
Thomas Phinney told us that a few years ago (as of December 2019), if you gave
a font a monospace flag in Panose, Microsoft Word would ignore the actual
advance widths and treat it as monospaced. Source:
https://typedrawers.com/discussion/comment/45140/#Comment_45140


</pre>

* 🔥 **FAIL** On monospaced fonts, the value of post.isFixedPitch must be set to a non-zero value (meaning 'fixed width monospaced'), but got 0 instead. [code: mono-bad-post-isFixedPitch]
* 🔥 **FAIL** On monospaced fonts, the value of OS/2.panose.bProportion must be set to 9 (proportion: monospaced), but got 0 instead. [code: mono-bad-panose-proportion]
* ⚠ **WARN** Font is monospaced but 597 glyphs (7.171171171171172%) have a different width. You should check the widths of: ['A', 'Aacute', 'Abreve', 'uni1EAE', 'uni1EB6', 'uni1EB0', 'uni1EB2', 'uni1EB4', 'Acircumflex', 'uni1EA4', 'uni1EAC', 'uni1EA6', 'uni1EA8', 'uni1EAA', 'uni0200', 'Adieresis', 'uni1EA0', 'Agrave', 'uni1EA2', 'uni0202', 'Amacron', 'Aogonek', 'Aring', 'Aringacute', 'Atilde', 'AE', 'AEacute', 'B', 'C', 'Cacute', 'Ccaron', 'Ccedilla', 'Ccircumflex', 'Cdotaccent', 'D', 'Eth', 'Dcaron', 'Dcroat', 'E', 'Eacute', 'Ebreve', 'Ecaron', 'Ecircumflex', 'uni1EBE', 'uni1EC6', 'uni1EC0', 'uni1EC2', 'uni1EC4', 'uni0204', 'Edieresis', 'Edotaccent', 'uni1EB8', 'Egrave', 'uni1EBA', 'uni0206', 'Emacron', 'Eogonek', 'uni1EBC', 'F', 'G', 'Gbreve', 'Gcaron', 'Gcircumflex', 'uni0122', 'Gdotaccent', 'H', 'Hbar', 'Hcircumflex', 'I', 'Iacute', 'Ibreve', 'Icircumflex', 'uni0208', 'Idieresis', 'Idotaccent', 'uni1ECA', 'Igrave', 'uni1EC8', 'uni020A', 'Imacron', 'Iogonek', 'Itilde', 'J', 'Jcircumflex', 'K', 'uni0136', 'L', 'Lacute', 'Lcaron', 'uni013B', 'Ldot', 'Lslash', 'M', 'N', 'Nacute', 'Ncaron', 'uni0145', 'Eng', 'Ntilde', 'O', 'Oacute', 'Obreve', 'Ocircumflex', 'uni1ED0', 'uni1ED8', 'uni1ED2', 'uni1ED4', 'uni1ED6', 'uni020C', 'Odieresis', 'uni022A', 'uni0230', 'uni1ECC', 'Ograve', 'uni1ECE', 'Ohorn', 'uni1EDA', 'uni1EE2', 'uni1EDC', 'uni1EDE', 'uni1EE0', 'Ohungarumlaut', 'uni020E', 'Omacron', 'uni01EA', 'Oslash', 'Oslashacute', 'Otilde', 'uni022C', 'OE', 'P', 'Thorn', 'Q', 'R', 'Racute', 'Rcaron', 'uni0156', 'uni0210', 'uni0212', 'S', 'Sacute', 'Scaron', 'Scedilla', 'Scircumflex', 'uni0218', 'uni018F', 'T', 'Tbar', 'Tcaron', 'uni0162', 'uni021A', 'U', 'Uacute', 'Ubreve', 'Ucircumflex', 'uni0214', 'Udieresis', 'uni1EE4', 'Ugrave', 'uni1EE6', 'Uhorn', 'uni1EE8', 'uni1EF0', 'uni1EEA', 'uni1EEC', 'uni1EEE', 'Uhungarumlaut', 'uni0216', 'Umacron', 'Uogonek', 'Uring', 'Utilde', 'V', 'W', 'Wacute', 'Wcircumflex', 'Wdieresis', 'Wgrave', 'X', 'Y', 'Yacute', 'Ycircumflex', 'Ydieresis', 'uni1EF4', 'Ygrave', 'uni1EF6', 'uni0232', 'uni1EF8', 'Z', 'Zacute', 'Zcaron', 'Zdotaccent', 'OE.rotat', 'a', 'aacute', 'abreve', 'uni1EAF', 'uni1EB7', 'uni1EB1', 'uni1EB3', 'uni1EB5', 'acircumflex', 'uni1EA5', 'uni1EAD', 'uni1EA7', 'uni1EA9', 'uni1EAB', 'uni0201', 'adieresis', 'uni1EA1', 'agrave', 'uni1EA3', 'uni0203', 'amacron', 'aogonek', 'aring', 'aringacute', 'atilde', 'ae', 'aeacute', 'b', 'c', 'cacute', 'ccaron', 'ccedilla', 'ccircumflex', 'cdotaccent', 'd', 'eth', 'dcaron', 'dcroat', 'e', 'eacute', 'ebreve', 'ecaron', 'ecircumflex', 'uni1EBF', 'uni1EC7', 'uni1EC1', 'uni1EC3', 'uni1EC5', 'uni0205', 'edieresis', 'edotaccent', 'uni1EB9', 'egrave', 'uni1EBB', 'uni0207', 'emacron', 'eogonek', 'uni1EBD', 'uni0259', 'f', 'g', 'gbreve', 'gcaron', 'gcircumflex', 'uni0123', 'gdotaccent', 'h', 'hbar', 'hcircumflex', 'i', 'dotlessi', 'iacute', 'ibreve', 'icircumflex', 'uni0209', 'idieresis', 'i.loclTRK', 'uni1ECB', 'igrave', 'uni1EC9', 'uni020B', 'imacron', 'iogonek', 'itilde', 'j', 'uni0237', 'jcircumflex', 'k', 'uni0137', 'kgreenlandic', 'l', 'lacute', 'lcaron', 'uni013C', 'ldot', 'lslash', 'm', 'n', 'nacute', 'ncaron', 'uni0146', 'eng', 'ntilde', 'o', 'oacute', 'obreve', 'ocircumflex', 'uni1ED1', 'uni1ED9', 'uni1ED3', 'uni1ED5', 'uni1ED7', 'uni020D', 'odieresis', 'uni022B', 'uni0231', 'uni1ECD', 'ograve', 'uni1ECF', 'ohorn', 'uni1EDB', 'uni1EE3', 'uni1EDD', 'uni1EDF', 'uni1EE1', 'ohungarumlaut', 'uni020F', 'omacron', 'uni01EB', 'oslash', 'oslashacute', 'otilde', 'uni022D', 'oe', 'p', 'thorn', 'q', 'r', 'racute', 'rcaron', 'uni0157', 'uni0211', 'uni0213', 's', 'sacute', 'scaron', 'scedilla', 'scircumflex', 'uni0219', 'germandbls', 't', 'tbar', 'tcaron', 'uni0163', 'uni021B', 'u', 'uacute', 'ubreve', 'ucircumflex', 'uni0215', 'udieresis', 'uni1EE5', 'ugrave', 'uni1EE7', 'uhorn', 'uni1EE9', 'uni1EF1', 'uni1EEB', 'uni1EED', 'uni1EEF', 'uhungarumlaut', 'uni0217', 'umacron', 'uogonek', 'uring', 'utilde', 'v', 'w', 'wacute', 'wcircumflex', 'wdieresis', 'wgrave', 'x', 'y', 'yacute', 'ycircumflex', 'ydieresis', 'uni1EF5', 'ygrave', 'uni1EF7', 'uni0233', 'uni1EF9', 'z', 'zacute', 'zcaron', 'zdotaccent', 'ordfeminine', 'ordmasculine', 'uniFF71', 'uniFF67', 'uniFF72', 'uniFF68', 'uniFF73', 'uniFF69', 'uniFF74', 'uniFF6A', 'uniFF75', 'uniFF6B', 'uniFF76', 'uniFF77', 'uniFF78', 'uniFF79', 'uniFF7A', 'uniFF7B', 'uniFF7C', 'uniFF7D', 'uniFF7E', 'uniFF7F', 'uniFF80', 'uniFF81', 'uniFF82', 'uniFF6F', 'uniFF83', 'uniFF84', 'uniFF85', 'uniFF86', 'uniFF87', 'uniFF88', 'uniFF89', 'uniFF8A', 'uniFF8B', 'uniFF8C', 'uniFF8D', 'uniFF8E', 'uniFF8F', 'uniFF90', 'uniFF91', 'uniFF92', 'uniFF93', 'uniFF94', 'uniFF6C', 'uniFF95', 'uniFF6D', 'uniFF96', 'uniFF6E', 'uniFF97', 'uniFF98', 'uniFF99', 'uniFF9A', 'uniFF9B', 'uniFF9C', 'uniFF66', 'uniFF9D', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero.zero', 'zero.lf', 'one.lf', 'two.lf', 'three.lf', 'four.lf', 'five.lf', 'six.lf', 'seven.lf', 'eight.lf', 'nine.lf', 'uni00B9', 'uni00B2', 'uni00B3', 'uni2074', 'fraction', 'onehalf', 'onequarter', 'threequarters', 'uni2164', 'period', 'comma', 'colon', 'semicolon', 'exclam', 'exclamdown', 'question', 'questiondown', 'periodcentered', 'bullet', 'asterisk', 'numbersign', 'slash', 'backslash', 'uniFF02', 'uniFF07', 'periodcentered.loclCAT.case', 'backslash.half', 'periodcentered.loclCAT', 'parenleft', 'parenright', 'braceleft', 'braceright', 'bracketleft', 'bracketright', 'uniFF62', 'uniFF63', 'hyphen', 'uni00AD', 'endash', 'emdash', 'underscore', 'quotesinglbase', 'quotedblbase', 'quotedblleft', 'quotedblright', 'quoteleft', 'quoteright', 'guillemotleft', 'guillemotright', 'guilsinglleft', 'guilsinglright', 'quotedbl', 'quotesingle', 'uniFF65', 'uniFF64', 'uniFF61', 'uni2002', 'space', 'uni00A0', 'CR', 'uni20B5', 'cent', 'colonmonetary', 'currency', 'dollar', 'dong', 'Euro', 'florin', 'franc', 'uni20B2', 'uni20AD', 'lira', 'uni20BA', 'uni20BC', 'uni20A6', 'peseta', 'uni20B1', 'uni20BD', 'uni20B9', 'sterling', 'uni20A9', 'yen', 'uni2219', 'uni2215', 'plus', 'minus', 'multiply', 'divide', 'equal', 'notequal', 'greater', 'less', 'greaterequal', 'lessequal', 'plusminus', 'approxequal', 'asciitilde', 'logicalnot', 'asciicircum', 'uni00B5', 'percent', 'uniFFE2', 'at', 'ampersand', 'paragraph', 'section', 'registered', 'degree', 'bar', 'brokenbar', 'uni02BC', 'uni02C9', 'dieresis', 'dotaccent', 'grave', 'acute', 'hungarumlaut', 'circumflex', 'caron', 'breve', 'ring', 'tilde', 'macron', 'cedilla', 'ogonek', 'uniFF9E', 'uniFF9F', 'uniFF70', 'cid00002', 'cid00003'] [code: mono-outliers]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---

Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will
only differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.

However, a quotedbl should have 2 contours, unless the font belongs to a
display family.

This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.


</pre>

* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: Eng	Contours detected: 2	Expected: 1
Glyph name: oe	Contours detected: 4	Expected: 3
Glyph name: Uogonek	Contours detected: 2	Expected: 1
Glyph name: uogonek	Contours detected: 2	Expected: 1
Glyph name: ohorn	Contours detected: 3	Expected: 2
Glyph name: uhorn	Contours detected: 2	Expected: 1
Glyph name: uni01EA	Contours detected: 3	Expected: 2
Glyph name: uni01EB	Contours detected: 3	Expected: 2
Glyph name: Oslashacute	Contours detected: 3	Expected: 4
Glyph name: oslashacute	Contours detected: 3	Expected: 4
Glyph name: uni1E9E	Contours detected: 2	Expected: 1
Glyph name: uni1EDB	Contours detected: 4	Expected: 3
Glyph name: uni1EDD	Contours detected: 4	Expected: 3
Glyph name: uni1EDF	Contours detected: 4	Expected: 3
Glyph name: uni1EE1	Contours detected: 4	Expected: 3
Glyph name: uni1EE3	Contours detected: 4	Expected: 3
Glyph name: uni1EE9	Contours detected: 3	Expected: 2
Glyph name: uni1EEB	Contours detected: 3	Expected: 2
Glyph name: uni1EED	Contours detected: 3	Expected: 2
Glyph name: uni1EEF	Contours detected: 3	Expected: 2
Glyph name: uni1EF1	Contours detected: 3	Expected: 2
Glyph name: uni2500	Contours detected: 2	Expected: 1
Glyph name: uni2502	Contours detected: 4	Expected: 1
Glyph name: uni250C	Contours detected: 4	Expected: 1
Glyph name: uni2510	Contours detected: 4	Expected: 1
Glyph name: uni2514	Contours detected: 7	Expected: 1
Glyph name: uni2518	Contours detected: 4	Expected: 1
Glyph name: uni251C	Contours detected: 2	Expected: 1
Glyph name: uni2524	Contours detected: 9	Expected: 1
Glyph name: uni252C	Contours detected: 3	Expected: 1
Glyph name: uni2534	Contours detected: 2	Expected: 1
Glyph name: uni253C	Contours detected: 7	Expected: 1
Glyph name: Eng	Contours detected: 2	Expected: 1
Glyph name: Oslashacute	Contours detected: 3	Expected: 4
Glyph name: Uogonek	Contours detected: 2	Expected: 1
Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: oe	Contours detected: 4	Expected: 3
Glyph name: ohorn	Contours detected: 3	Expected: 2
Glyph name: oslashacute	Contours detected: 3	Expected: 4
Glyph name: uhorn	Contours detected: 2	Expected: 1
Glyph name: uni1E9E	Contours detected: 2	Expected: 1
Glyph name: uni1EDB	Contours detected: 4	Expected: 3
Glyph name: uni1EDD	Contours detected: 4	Expected: 3
Glyph name: uni1EDF	Contours detected: 4	Expected: 3
Glyph name: uni1EE1	Contours detected: 4	Expected: 3
Glyph name: uni1EE3	Contours detected: 4	Expected: 3
Glyph name: uni1EE9	Contours detected: 3	Expected: 2
Glyph name: uni1EEB	Contours detected: 3	Expected: 2
Glyph name: uni1EED	Contours detected: 3	Expected: 2
Glyph name: uni1EEF	Contours detected: 3	Expected: 2
Glyph name: uni1EF1	Contours detected: 3	Expected: 2
Glyph name: uogonek	Contours detected: 2	Expected: 1 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---

All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.

If using GlyphsApp, ligature carets can be set directly on canvas by accessing
the `Glyph -&gt; Set Anchors` menu option or by pressing the `Cmd+U` keyboard
shortcut.

If designing with UFOs, (as of Oct 2020) ligature carets are not yet compiled
by ufo2ft, and therefore will not build via FontMake. See
googlefonts/ufo2ft/issues/329


</pre>

* ⚠ **WARN** GDEF table is missing, but it is mandatory to declare it on fonts that provide ligature glyphs because the caret (text cursor) positioning for each ligature must be provided in this table. [code: GDEF-missing]

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)

* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary>

* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)
<pre>--- Rationale ---

This test heuristically detects outline segments which form a particularly
small angle, indicative of an outline error. This may cause false positives in
cases such as extreme ink traps, so should be regarded as advisory and backed
up by manual inspection.


</pre>

* ⚠ **WARN** The following glyphs have jaggy segments:
	* M.rotat: B<<477.5,457.0>-<611.0,455.0>-<727.0,447.0>>/B<<727.0,447.0>-<315.0,575.0>-<302.0,588.0>> = 13.313768063866487
	* M: B<<402.5,336.5>-<405.0,470.0>-<412.0,586.0>>/B<<412.0,586.0>-<284.0,174.0>-<271.0,161.0>> = 13.80563804237296
	* OE.rotat: B<<224.0,611.5>-<248.0,611.0>-<286.0,610.0>>/B<<286.0,610.0>-<149.0,639.0>-<149.0,703.0>> = 10.444439371249782
	* OE.rotat: B<<867.0,703.0>-<867.0,640.0>-<746.0,611.0>>/B<<746.0,611.0>-<765.0,611.0>-<784.5,611.0>> = 13.477822753241302
	* OE: B<<156.0,726.0>-<219.0,726.0>-<248.0,605.0>>/B<<248.0,605.0>-<248.0,624.0>-<248.0,643.5>> = 13.477822753241302
	* OE: B<<247.5,83.0>-<248.0,107.0>-<249.0,145.0>>/B<<249.0,145.0>-<220.0,8.0>-<156.0,8.0>> = 10.444439371249782
	* eng: L<<126.0,470.0>--<126.0,332.0>>/B<<126.0,332.0>-<142.0,400.0>-<179.0,437.0>> = 13.240519915187184
	* eta: B<<351.0,359.0>-<348.0,338.0>-<348.0,324.0>>/B<<348.0,324.0>-<358.0,367.0>-<376.5,407.5>> = 13.091893064346833
	* gamma: B<<374.0,325.0>-<370.0,261.0>-<356.0,198.0>>/B<<356.0,198.0>-<381.0,257.0>-<415.0,314.0>> = 10.434965350703013
	* m.rotat: L<<616.0,780.0>--<489.0,779.0>>/B<<489.0,779.0>-<536.0,770.0>-<565.0,745.0>> = 11.291444001117814 and 182 more. [code: found-jaggy-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines?</summary>

* [com.google.fonts/check/outline_semi_vertical](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical)
<pre>--- Rationale ---

This test detects line segments which are nearly, but not quite, exactly
horizontal or vertical. Sometimes such lines are created by design, but often
they are indicative of a design error.

This test is disabled for italic styles, which often contain nearly-upright
lines.


</pre>

* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
	* .notdef: L<<128.0,771.0>--<873.0,773.0>>
	* .notdef: L<<160.0,-12.0>--<844.0,-7.0>>
	* .notdef: L<<851.0,730.0>--<150.0,727.0>>
	* .notdef: L<<866.0,-51.0>--<138.0,-56.0>>
	* A.rotat: L<<433.0,695.0>--<432.0,527.0>>
	* A: L<<164.0,292.0>--<332.0,291.0>>
	* Aacute: L<<164.0,292.0>--<332.0,291.0>>
	* Abreve: L<<164.0,292.0>--<332.0,291.0>>
	* Acircumflex: L<<164.0,292.0>--<332.0,291.0>>
	* Adieresis: L<<164.0,292.0>--<332.0,291.0>> and 20158 more. [code: found-semi-vertical]

</details>
<br>
</details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 3 | 6 | 95 | 7 | 83 | 0 |
| 0% | 2% | 3% | 49% | 4% | 43% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
