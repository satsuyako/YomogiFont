from fontmake import __main__
from fontTools.ttLib import TTFont, newTable
import shutil
import subprocess
from glyphsLib.cli import main
import ufoLib2
import ufo2ft
import os

print ("Converting to UFO")
main(("glyphs2ufo", "sources/Yomogi.glyphs"))

exportFont = ufoLib2.Font.open("sources/Yomogi-Regular.ufo")

exportFont.lib['com.github.googlei18n.ufo2ft.filters'] = [{
    "name": "flattenComponents",
    "pre": 1,
}]

print ("[Yomogi] Compiling")
static_ttf = ufo2ft.compileTTF(exportFont, removeOverlaps=True)

print ("[Yomogi] Adding bits")
static_ttf["DSIG"] = newTable("DSIG")
static_ttf["DSIG"].ulVersion = 1
static_ttf["DSIG"].usFlag = 0
static_ttf["DSIG"].usNumSigs = 0
static_ttf["DSIG"].signatureRecords = []
static_ttf["head"].flags |= 1 << 3        #sets flag to always round PPEM to integer

print ("[Yomogi] Saving")
static_ttf.save("fonts/ttf/Yomogi-Regular.ttf")

shutil.rmtree("sources/Yomogi-Regular.ufo")
os.remove("sources/Yomogi.designspace")

subprocess.check_call(
        [
            "ttfautohint",
            "--stem-width",
            "nsn",
            "fonts/ttf/Yomogi-Regular.ttf",
            "fonts/ttf/Yomogi-Regular-hinted.ttf",
        ]
    )
shutil.move("fonts/ttf/Yomogi-Regular-hinted.ttf", "fonts/ttf/Yomogi-Regular.ttf")