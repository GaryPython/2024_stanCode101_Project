"""
File:my_drawing
Name: Dennis
----------------------
TODO:
"""

from campy.graphics.gobjects import GRect, GLabel
from campy.graphics.gwindow import GWindow


def main():
    label = GLabel("Dogcoin\n to $1?", x=500, y=350)
    label.font = "-80"
    window = GWindow(height=800, width=800, title="dooggy coin")
    window.add(label)
    window.add(darkgoldenrod(), x=300, y=300)
    window.add(gold(), x=313, y=300)
    window.add(darkgoldenrod(), x=456, y=300)
    window.add(goldenrod(), x=469, y=300)
    window.add(darkgoldenrod(), x=469, y=287)
    window.add(darkgoldenrod(), x=482, y=287)
    window.add(gold(), x=482, y=300)
    # first line
    window.add(darkgoldenrod(), x=300, y=313)
    window.add(moccasin(), x=313, y=313)
    window.add(gold(), x=326, y=313)
    window.add(darkgoldenrod(), x=443, y=313)
    window.add(goldenrod(), x=456, y=313)
    window.add(darkgoldenrod(), x=469, y=313)
    window.add(gold(), x=482, y=313)
    # second line
    window.add(darkgoldenrod(), x=300, y=326)
    window.add(moccasin(), x=313, y=326)
    window.add(moccasin(), x=326, y=326)
    window.add(gold(), x=339, y=326)
    window.add(darkgoldenrod(), x=352, y=326)

    window.add(darkgoldenrod(), x=430, y=326)
    window.add(goldenrod(), x=443, y=326)
    window.add(darkgoldenrod(), x=456, y=326)
    window.add(darkgoldenrod(), x=469, y=326)
    window.add(gold(), x=482, y=326)
    # third line
    window.add(darkgoldenrod(), x=287, y=339)
    window.add(moccasin(), x=300, y=339)
    window.add(moccasin(), x=313, y=339)
    window.add(darkgoldenrod(), x=326, y=339)
    window.add(darkgoldenrod(), x=339, y=339)
    window.add(gold(), x=352, y=339)
    window.add(darkgoldenrod(), x=365, y=339)
    window.add(darkgoldenrod(), x=378, y=339)
    window.add(goldenrod(), x=391, y=339)
    window.add(goldenrod(), x=404, y=339)
    window.add(goldenrod(), x=417, y=339)
    window.add(goldenrod(), x=417, y=339)
    window.add(goldenrod(), x=430, y=339)
    window.add(darkgoldenrod(), x=443, y=339)
    window.add(goldenrod(), x=456, y=339)
    window.add(goldenrod(), x=469, y=339)
    window.add(goldenrod(), x=482, y=339)
    # forth line
    window.add(darkgoldenrod(), x=287, y=352)
    window.add(moccasin(), x=300, y=352)
    window.add(darkgoldenrod(), x=313, y=352)
    window.add(darkgoldenrod(), x=326, y=352)
    window.add(goldenrod(), x=339, y=352)
    window.add(moccasin(), x=352, y=352)
    window.add(goldenrod(), x=365, y=352)
    window.add(goldenrod(), x=378, y=352)
    window.add(goldenrod(), x=391, y=352)
    window.add(goldenrod(), x=404, y=352)
    window.add(goldenrod(), x=417, y=352)
    window.add(goldenrod(), x=417, y=352)
    window.add(goldenrod(), x=430, y=352)
    window.add(goldenrod(), x=443, y=352)
    window.add(goldenrod(), x=456, y=352)
    window.add(moccasin(), x=469, y=352)
    window.add(moccasin(), x=482, y=352)
    window.add(goldenrod(), x=495, y=352)
    window.add(goldenrod(), x=508, y=352)

    # forth line
    window.add(darkgoldenrod(), x=287, y=365)
    window.add(goldenrod(), x=300, y=365)
    window.add(darkgoldenrod(), x=313, y=365)
    window.add(goldenrod(), x=326, y=365)
    window.add(goldenrod(), x=339, y=365)
    window.add(goldenrod(), x=352, y=365)
    window.add(goldenrod(), x=365, y=365)
    window.add(goldenrod(), x=378, y=365)
    window.add(goldenrod(), x=391, y=365)
    window.add(goldenrod(), x=404, y=365)
    window.add(goldenrod(), x=417, y=365)
    window.add(goldenrod(), x=417, y=365)
    window.add(goldenrod(), x=430, y=365)
    window.add(goldenrod(), x=443, y=365)
    window.add(moccasin(), x=456, y=365)
    window.add(moccasin(), x=469, y=365)
    window.add(moccasin(), x=482, y=365)
    window.add(moccasin(), x=495, y=365)
    window.add(goldenrod(), x=508, y=365)
    window.add(goldenrod(), x=521, y=365)
    # sixth line
    window.add(darkgoldenrod(), x=287, y=378)
    window.add(goldenrod(), x=300, y=378)
    window.add(goldenrod(), x=313, y=378)
    window.add(goldenrod(), x=326, y=378)
    window.add(goldenrod(), x=339, y=378)
    window.add(goldenrod(), x=352, y=378)
    window.add(goldenrod(), x=365, y=378)
    window.add(goldenrod(), x=378, y=378)
    window.add(goldenrod(), x=391, y=378)
    window.add(goldenrod(), x=404, y=378)
    window.add(papayawhip(), x=417, y=378)
    window.add(papayawhip(), x=430, y=378)
    window.add(moccasin(), x=443, y=378)
    window.add(moccasin(), x=456, y=378)
    window.add(papayawhip(), x=469, y=378)
    window.add(papayawhip(), x=482, y=378)
    window.add(moccasin(), x=495, y=378)
    window.add(moccasin(), x=508, y=378)
    window.add(goldenrod(), x=521, y=378)
    # seventh line
    window.add(moccasin(), x=287, y=391)
    window.add(goldenrod(), x=300, y=391)
    window.add(goldenrod(), x=313, y=391)
    window.add(goldenrod(), x=326, y=391)
    window.add(goldenrod(), x=339, y=391)
    window.add(goldenrod(), x=352, y=391)
    window.add(goldenrod(), x=365, y=391)
    window.add(goldenrod(), x=378, y=391)
    window.add(papayawhip(), x=391, y=391)
    window.add(papayawhip(), x=404, y=391)
    window.add(papayawhip(), x=417, y=391)
    window.add(papayawhip(), x=430, y=391)
    window.add(moccasin(), x=443, y=391)
    window.add(papayawhip(), x=456, y=391)
    window.add(papayawhip(), x=469, y=391)
    window.add(papayawhip(), x=482, y=391)
    window.add(papayawhip(), x=495, y=391)
    window.add(moccasin(), x=508, y=391)
    window.add(goldenrod(), x=521, y=391)
    window.add(goldenrod(), x=534, y=391)
    # eighth line
    window.add(moccasin(), x=287, y=404)
    window.add(goldenrod(), x=300, y=404)
    window.add(goldenrod(), x=313, y=404)
    window.add(papayawhip(), x=326, y=404)
    window.add(goldenrod(), x=339, y=404)
    window.add(goldenrod(), x=352, y=404)
    window.add(goldenrod(), x=365, y=404)
    window.add(goldenrod(), x=378, y=404)
    window.add(black(), x=391, y=404)
    window.add(black(), x=404, y=404)
    window.add(moccasin(), x=443, y=404)
    window.add(black(), x=456, y=404)
    window.add(black(), x=469, y=404)
    window.add(moccasin(), x=508, y=404)
    window.add(moccasin(), x=521, y=404)
    window.add(goldenrod(), x=534, y=404)
    window.add(goldenrod(), x=547, y=404)
    # ninth line
    window.add(moccasin(), x=287, y=417)
    window.add(goldenrod(), x=300, y=417)
    window.add(wheat(), x=313, y=417)
    window.add(wheat(), x=326, y=417)
    window.add(goldenrod(), x=339, y=417)
    window.add(goldenrod(), x=352, y=417)
    window.add(goldenrod(), x=365, y=417)
    window.add(goldenrod(), x=378, y=417)
    window.add(black(), x=391, y=417)
    window.add(black(), x=404, y=417)
    window.add(moccasin(), x=443, y=417)
    window.add(black(), x=456, y=417)
    window.add(black(), x=469, y=417)
    window.add(moccasin(), x=508, y=417)
    window.add(moccasin(), x=521, y=417)
    window.add(goldenrod(), x=534, y=417)
    window.add(goldenrod(), x=547, y=417)
    # tenth line
    window.add(moccasin(), x=274, y=430)
    window.add(moccasin(), x=287, y=430)
    window.add(goldenrod(), x=300, y=430)
    window.add(wheat(), x=313, y=430)
    window.add(wheat(), x=326, y=430)
    window.add(wheat(), x=339, y=430)
    window.add(goldenrod(), x=352, y=430)
    window.add(goldenrod(), x=365, y=430)
    window.add(pink(), x=378, y=430)
    window.add(black(), x=391, y=430)
    window.add(black(), x=404, y=430)
    window.add(moccasin(), x=443, y=430)
    window.add(black(), x=456, y=430)
    window.add(black(), x=469, y=430)
    window.add(pink(), x=508, y=430)
    window.add(moccasin(), x=521, y=430)
    window.add(moccasin(), x=534, y=430)
    window.add(goldenrod(), x=547, y=430)
    # eleven line
    window.add(moccasin(), x=261, y=443)
    window.add(moccasin(), x=274, y=443)
    window.add(moccasin(), x=287, y=443)
    window.add(goldenrod(), x=300, y=443)
    window.add(wheat(), x=313, y=443)
    window.add(wheat(), x=326, y=443)
    window.add(wheat(), x=339, y=443)
    window.add(wheat(), x=352, y=443)
    window.add(goldenrod(), x=365, y=443)
    window.add(pink(), x=378, y=443)
    window.add(pink(), x=378, y=443)
    window.add(pink(), x=391, y=443)
    window.add(pink(), x=404, y=443)
    window.add(goldenrod(), x=417, y=443)
    window.add(goldenrod(), x=430, y=443)
    window.add(goldenrod(), x=443, y=443)
    window.add(goldenrod(), x=456, y=443)
    window.add(goldenrod(), x=469, y=443)
    window.add(pink(), x=482, y=443)
    window.add(pink(), x=495, y=443)
    window.add(pink(), x=508, y=443)
    window.add(moccasin(), x=521, y=443)
    window.add(wheat(), x=534, y=443)
    window.add(goldenrod(), x=547, y=443)
    # twelve line
    window.add(moccasin(), x=261, y=456)
    window.add(goldenrod(), x=274, y=456)
    window.add(moccasin(), x=287, y=456)
    window.add(moccasin(), x=300, y=456)
    window.add(gainsboro(), x=313, y=456)
    window.add(wheat(), x=326, y=456)
    window.add(wheat(), x=339, y=456)
    window.add(papayawhip(), x=352, y=456)
    window.add(wheat(), x=365, y=456)
    window.add(papayawhip(), x=378, y=456)
    window.add(goldenrod(), x=391, y=456)
    window.add(goldenrod(), x=404, y=456)
    window.add(goldenrod(), x=417, y=456)
    window.add(goldenrod(), x=430, y=456)
    window.add(black(), x=443, y=456)
    window.add(black(), x=456, y=456)
    window.add(black(), x=469, y=456)
    window.add(black(), x=482, y=456)
    window.add(goldenrod(), x=495, y=456)
    window.add(wheat(), x=508, y=456)
    window.add(wheat(), x=521, y=456)
    window.add(wheat(), x=534, y=456)
    window.add(gainsboro(), x=547, y=456)
    # thirteen line
    window.add(moccasin(), x=261, y=469)
    window.add(goldenrod(), x=274, y=469)
    window.add(moccasin(), x=287, y=469)
    window.add(moccasin(), x=300, y=469)
    window.add(moccasin(), x=313, y=469)
    window.add(gainsboro(), x=326, y=469)
    window.add(wheat(), x=339, y=469)
    window.add(wheat(), x=352, y=469)
    window.add(wheat(), x=365, y=469)
    window.add(wheat(), x=378, y=469)
    window.add(wheat(), x=391, y=469)
    window.add(wheat(), x=404, y=469)
    window.add(papayawhip(), x=417, y=469)
    window.add(wheat(), x=430, y=469)
    window.add(black(), x=443, y=469)
    window.add(black(), x=456, y=469)
    window.add(black(), x=469, y=469)
    window.add(black(), x=482, y=469)
    window.add(wheat(), x=495, y=469)
    window.add(papayawhip(), x=508, y=469)
    window.add(wheat(), x=521, y=469)
    window.add(wheat(), x=534, y=469)
    window.add(gainsboro(), x=547, y=469)
    # forthteen line
    window.add(goldenrod(), x=248, y=482)
    window.add(goldenrod(), x=261, y=482)
    window.add(goldenrod(), x=274, y=482)
    window.add(goldenrod(), x=287, y=482)
    window.add(goldenrod(), x=300, y=482)
    window.add(moccasin(), x=313, y=482)
    window.add(moccasin(), x=326, y=482)
    window.add(gainsboro(), x=339, y=482)
    window.add(wheat(), x=352, y=482)
    window.add(papayawhip(), x=365, y=482)
    window.add(wheat(), x=378, y=482)
    window.add(papayawhip(), x=391, y=482)
    window.add(wheat(), x=404, y=482)
    window.add(wheat(), x=417, y=482)
    window.add(wheat(), x=430, y=482)
    window.add(wheat(), x=443, y=482)
    window.add(black(), x=456, y=482)
    window.add(black(), x=469, y=482)
    window.add(wheat(), x=482, y=482)
    window.add(papayawhip(), x=495, y=482)
    window.add(wheat(), x=508, y=482)
    window.add(wheat(), x=521, y=482)
    window.add(gainsboro(), x=534, y=482)
    # fifteen line
    window.add(moccasin(), x=235, y=495)
    window.add(goldenrod(), x=248, y=495)
    window.add(goldenrod(), x=261, y=495)
    window.add(goldenrod(), x=274, y=495)
    window.add(goldenrod(), x=287, y=495)
    window.add(darkgoldenrod(), x=300, y=495)
    window.add(goldenrod(), x=313, y=495)
    window.add(moccasin(), x=326, y=495)
    window.add(moccasin(), x=339, y=495)
    window.add(gainsboro(), x=352, y=495)
    window.add(gainsboro(), x=365, y=495)
    window.add(wheat(), x=378, y=495)
    window.add(wheat(), x=391, y=495)
    window.add(wheat(), x=404, y=495)
    window.add(wheat(), x=417, y=495)
    window.add(wheat(), x=430, y=495)
    window.add(black(), x=443, y=495)
    window.add(wheat(), x=456, y=495)
    window.add(black(), x=469, y=495)
    window.add(wheat(), x=482, y=495)
    window.add(wheat(), x=495, y=495)
    window.add(wheat(), x=508, y=495)
    window.add(gainsboro(), x=521, y=495)
    # sixteen line
    window.add(moccasin(), x=235, y=508)
    window.add(goldenrod(), x=248, y=508)
    window.add(goldenrod(), x=261, y=508)
    window.add(goldenrod(), x=274, y=508)
    window.add(goldenrod(), x=287, y=508)
    window.add(goldenrod(), x=300, y=508)
    window.add(darkgoldenrod(), x=313, y=508)
    window.add(darkgoldenrod(), x=326, y=508)
    window.add(darkgoldenrod(), x=339, y=508)
    window.add(gainsboro(), x=352, y=508)
    window.add(gainsboro(), x=365, y=508)
    window.add(gainsboro(), x=378, y=508)
    window.add(gainsboro(), x=391, y=508)
    window.add(gainsboro(), x=404, y=508)
    window.add(gainsboro(), x=417, y=508)
    window.add(wheat(), x=430, y=508)
    window.add(wheat(), x=443, y=508)
    window.add(wheat(), x=456, y=508)
    window.add(wheat(), x=469, y=508)
    window.add(wheat(), x=482, y=508)
    window.add(wheat(), x=495, y=508)
    window.add(gainsboro(), x=508, y=508)
    window.add(wheat(), x=521, y=508)
    # seventeen line
    window.add(moccasin(), x=235, y=521)
    window.add(goldenrod(), x=248, y=521)
    window.add(goldenrod(), x=261, y=521)
    window.add(goldenrod(), x=274, y=521)
    window.add(goldenrod(), x=287, y=521)
    window.add(goldenrod(), x=300, y=521)
    window.add(goldenrod(), x=313, y=521)
    window.add(goldenrod(), x=326, y=521)
    window.add(darkgoldenrod(), x=339, y=521)
    window.add(darkgoldenrod(), x=352, y=521)
    window.add(darkgoldenrod(), x=365, y=521)
    window.add(gainsboro(), x=378, y=521)
    window.add(gainsboro(), x=391, y=521)
    window.add(gainsboro(), x=404, y=521)
    window.add(gainsboro(), x=417, y=521)
    window.add(gainsboro(), x=430, y=521)
    window.add(gainsboro(), x=443, y=521)
    window.add(gainsboro(), x=456, y=521)
    window.add(gainsboro(), x=469, y=521)
    window.add(gainsboro(), x=482, y=521)
    window.add(gainsboro(), x=495, y=521)
    window.add(wheat(), x=508, y=521)
    window.add(wheat(), x=521, y=521)
    # eighteen line
    window.add(moccasin(), x=235, y=534)
    window.add(goldenrod(), x=248, y=534)
    window.add(goldenrod(), x=261, y=534)
    window.add(goldenrod(), x=274, y=534)
    window.add(goldenrod(), x=287, y=534)
    window.add(goldenrod(), x=300, y=534)
    window.add(goldenrod(), x=313, y=534)
    window.add(goldenrod(), x=326, y=534)
    window.add(goldenrod(), x=339, y=534)
    window.add(goldenrod(), x=352, y=534)
    window.add(darkgoldenrod(), x=365, y=534)
    window.add(darkgoldenrod(), x=378, y=534)
    window.add(darkgoldenrod(), x=391, y=534)
    window.add(darkgoldenrod(), x=404, y=534)
    window.add(darkgoldenrod(), x=417, y=534)
    window.add(darkgoldenrod(), x=430, y=534)
    window.add(darkgoldenrod(), x=443, y=534)
    window.add(darkgoldenrod(), x=456, y=534)
    window.add(goldenrod(), x=469, y=534)
    window.add(goldenrod(), x=482, y=534)
    window.add(wheat(), x=495, y=534)
    window.add(wheat(), x=508, y=534)
    window.add(wheat(), x=521, y=534)
    # coin
    window.add(khaki(), x=235, y=547)
    window.add(gold(), x=248, y=547)
    window.add(goldenrod(), x=261, y=547)
    window.add(goldenrod(), x=274, y=547)
    window.add(goldenrod(), x=287, y=547)
    window.add(goldenrod(), x=300, y=547)
    window.add(goldenrod(), x=313, y=547)
    window.add(gainsboro(), x=326, y=547)
    # window.add(goldenrod(), x=339, y=547)
    # window.add(gainsboro(), x=352, y=547)
    # window.add(darkgoldenrod(), x=365, y=547)
    # window.add(darkgoldenrod(), x=378, y=547)
    # window.add(darkgoldenrod(), x=391, y=547)
    window.add(darkgoldenrod(), x=404, y=547)
    window.add(darkgoldenrod(), x=417, y=547)
    window.add(darkgoldenrod(), x=430, y=547)
    window.add(darkgoldenrod(), x=443, y=547)
    window.add(goldenrod(), x=456, y=547)
    window.add(goldenrod(), x=469, y=547)
    window.add(wheat(), x=482, y=547)
    window.add(wheat(), x=495, y=547)
    window.add(wheat(), x=508, y=547)
    window.add(goldenrod(), x=521, y=547)
    # coin 2
    window.add(khaki(), x=222, y=560)
    window.add(gold(), x=235, y=560)
    window.add(yellow(), x=248, y=560)
    window.add(yellow(), x=261, y=560)
    window.add(yellow(), x=274, y=560)
    window.add(black(), x=287, y=560)
    window.add(black(), x=300, y=560)
    window.add(black(), x=313, y=560)
    window.add(black(), x=326, y=560)
    window.add(gainsboro(), x=339, y=560)
    window.add(wheat(), x=352, y=560)
    window.add(wheat(), x=365, y=560)
    window.add(wheat(), x=378, y=560)
    window.add(wheat(), x=391, y=560)
    # window.add(darkgoldenrod(), x=404, y=560)
    window.add(darkgoldenrod(), x=417, y=560)
    window.add(darkgoldenrod(), x=430, y=560)
    window.add(goldenrod(), x=443, y=560)
    window.add(goldenrod(), x=456, y=560)
    window.add(wheat(), x=469, y=560)
    window.add(wheat(), x=482, y=560)
    window.add(wheat(), x=495, y=560)
    window.add(goldenrod(), x=508, y=560)
    window.add(goldenrod(), x=521, y=560)
    # coin 3
    window.add(khaki(), x=222, y=573)
    window.add(gold(), x=235, y=573)
    window.add(yellow(), x=248, y=573)
    window.add(yellow(), x=261, y=573)
    window.add(yellow(), x=274, y=573)
    window.add(yellow(), x=287, y=573)
    window.add(black(), x=300, y=573)
    window.add(yellow(), x=313, y=573)
    window.add(yellow(), x=326, y=573)
    window.add(black(), x=339, y=573)
    window.add(gainsboro(), x=352, y=573)
    window.add(gainsboro(), x=365, y=573)
    window.add(gainsboro(), x=378, y=573)
    window.add(gainsboro(), x=391, y=573)
    window.add(gainsboro(), x=404, y=573)
    window.add(darkgoldenrod(), x=417, y=573)
    window.add(goldenrod(), x=430, y=573)
    window.add(goldenrod(), x=443, y=573)
    window.add(wheat(), x=456, y=573)
    window.add(wheat(), x=469, y=573)
    window.add(wheat(), x=482, y=573)
    window.add(goldenrod(), x=495, y=573)
    window.add(goldenrod(), x=508, y=573)
    window.add(goldenrod(), x=521, y=573)
    # coin 4
    window.add(khaki(), x=222, y=586)
    window.add(gold(), x=235, y=586)
    window.add(yellow(), x=248, y=586)
    window.add(yellow(), x=261, y=586)
    window.add(yellow(), x=274, y=586)
    window.add(yellow(), x=287, y=586)
    window.add(black(), x=300, y=586)
    window.add(yellow(), x=313, y=586)
    window.add(yellow(), x=326, y=586)
    window.add(black(), x=339, y=586)
    window.add(yellow(), x=352, y=586)
    window.add(yellow(), x=365, y=586)
    window.add(yellow(), x=378, y=586)
    window.add(yellow(), x=391, y=586)
    window.add(gold(), x=404, y=586)

    window.add(khaki(), x=222, y=599)
    window.add(gold(), x=235, y=599)
    window.add(yellow(), x=248, y=599)
    window.add(yellow(), x=261, y=599)
    window.add(yellow(), x=274, y=599)
    window.add(yellow(), x=287, y=599)
    window.add(black(), x=300, y=599)
    window.add(yellow(), x=313, y=599)
    window.add(yellow(), x=326, y=599)
    window.add(black(), x=339, y=599)
    window.add(yellow(), x=352, y=599)
    window.add(yellow(), x=365, y=599)
    window.add(yellow(), x=378, y=599)
    window.add(yellow(), x=391, y=599)
    window.add(gold(), x=404, y=599)

    window.add(khaki(), x=222, y=612)
    window.add(gold(), x=235, y=612)
    window.add(yellow(), x=248, y=612)
    window.add(yellow(), x=261, y=612)
    window.add(yellow(), x=274, y=612)
    window.add(yellow(), x=287, y=612)
    window.add(black(), x=300, y=612)
    window.add(yellow(), x=313, y=612)
    window.add(yellow(), x=326, y=612)
    window.add(black(), x=339, y=612)
    window.add(yellow(), x=352, y=612)
    window.add(yellow(), x=365, y=612)
    window.add(yellow(), x=378, y=612)
    window.add(yellow(), x=391, y=612)
    window.add(gold(), x=404, y=612)

    window.add(khaki(), x=222, y=625)
    window.add(gold(), x=235, y=625)
    window.add(yellow(), x=248, y=625)
    window.add(yellow(), x=261, y=625)
    window.add(yellow(), x=274, y=625)
    window.add(black(), x=287, y=625)
    window.add(black(), x=300, y=625)
    window.add(black(), x=313, y=625)
    window.add(black(), x=326, y=625)
    window.add(yellow(), x=339, y=625)
    window.add(yellow(), x=352, y=625)
    window.add(yellow(), x=365, y=625)
    window.add(yellow(), x=378, y=625)
    window.add(yellow(), x=391, y=625)
    window.add(gold(), x=404, y=625)

    window.add(khaki(), x=235, y=638)
    window.add(gold(), x=248, y=638)
    window.add(yellow(), x=261, y=638)
    window.add(yellow(), x=274, y=638)
    window.add(yellow(), x=287, y=638)
    window.add(yellow(), x=300, y=638)
    window.add(yellow(), x=313, y=638)
    window.add(yellow(), x=326, y=638)
    window.add(yellow(), x=339, y=638)
    window.add(yellow(), x=352, y=638)
    window.add(yellow(), x=365, y=638)
    window.add(yellow(), x=378, y=638)
    window.add(gold(), x=391, y=638)

    window.add(khaki(), x=248, y=651)
    window.add(gold(), x=261, y=651)
    window.add(yellow(), x=274, y=651)
    window.add(yellow(), x=287, y=651)
    window.add(yellow(), x=300, y=651)
    window.add(yellow(), x=313, y=651)
    window.add(yellow(), x=326, y=651)
    window.add(yellow(), x=339, y=651)
    window.add(yellow(), x=352, y=651)
    window.add(yellow(), x=365, y=651)
    window.add(gold(), x=378, y=651)

    window.add(khaki(), x=261, y=664)
    window.add(khaki(), x=274, y=664)
    window.add(khaki(), x=287, y=664)
    window.add(khaki(), x=300, y=664)
    window.add(khaki(), x=313, y=664)
    window.add(khaki(), x=326, y=664)
    window.add(khaki(), x=339, y=664)
    window.add(khaki(), x=352, y=664)
    window.add(khaki(), x=365, y=664)


def yellow():
    rect = GRect(12, 12)
    rect.filled = True
    rect.fill_color = "yellow"
    rect.color = "yellow"
    return rect


def khaki():
    rect = GRect(12, 12)
    rect.filled = True
    rect.fill_color = "khaki"
    rect.color = "khaki"
    return rect


def gainsboro():
    rect = GRect(12, 12)
    rect.filled = True
    rect.fill_color = "gainsboro"
    rect.color = "gainsboro"
    return rect


def pink():
    rect = GRect(12, 12)
    rect.filled = True
    rect.fill_color = "pink"
    rect.color = "pink"
    return rect


def wheat():
    rect = GRect(12, 12)
    rect.filled = True
    rect.fill_color = "wheat"
    rect.color = "wheat"
    return rect


def black():
    rect = GRect(12, 12)
    rect.filled = True
    return rect


def papayawhip():
    rect = GRect(12, 12)
    rect.filled = True
    rect.fill_color = "papayawhip"
    rect.color = "papayawhip"
    return rect


def tan():
    rect = GRect(12, 12)
    rect.filled = True
    rect.fill_color = "tan"
    rect.color = "tan"
    return rect


def moccasin():
    rect = GRect(12, 12)
    rect.filled = True
    rect.fill_color = "moccasin"
    rect.color = "moccasin"
    return rect


def darkorange():
    rect = GRect(12, 12)
    rect.filled = True
    rect.fill_color = "darkorange"
    rect.color = "darkorange"
    return rect


def goldenrod():
    rect = GRect(12, 12)
    rect.filled = True
    rect.fill_color = "goldenrod"
    rect.color = "goldenrod"
    return rect


def darkgoldenrod():
    rect = GRect(12, 12)
    rect.filled = True
    rect.fill_color = "darkgoldenrod"
    rect.color = "darkgoldenrod"
    return rect


def gold():
    rect = GRect(12, 12)
    rect.filled = True
    rect.fill_color = "gold"
    rect.color = "gold"
    return rect


if __name__ == '__main__':
    main()
