from random import randrange

def randMessage(senderName):
    index = randrange(0, len(images))
    return (subject(index), body(index, senderName), html(index, senderName))

def subject(index):
    return subjects[0]

def body(index, senderName):
    return bodies[0] % senderName

def html(index, senderName):
    return htmls[0] % (senderName, images[randrange(0, len(images))])

subjects = [
"I'm getting HANGRY"
]

bodies = [
"""
This is an urgent message from %s.  Don't let them get hangry!

This message brought to you by http://dontletmegethangry.com
"""
]

htmls = [
"""
<html><head></head><body>
<p>This is an urgent message from %s.  Don't let them get hangry!</p>
<img src = %s>
<p>This message brought to you with love by dontletmegethangry.com</p>
</body></html>
"""
]

images = [
"http://rs1img.memecdn.com/a-potato-is-fine-too_c_607571.webp",
"http://rs1img.memecdn.com/but-dad-im-hungry_o_796340.gif",
"http://rs1img.memecdn.com/food_o_1204761.webp",
"http://rs1img.memecdn.com/hungry-cat_o_1708127.webp",
"http://rs1img.memecdn.com/he-must-be-hungry_o_230227.webp",
"http://rs1img.memecdn.com/just-a-regular-reaction-and-you-know-it-amp-039-s-true_o_4310587.webp",
"http://rs1img.memecdn.com/kim-jong-un_c_1137669.webp",
"http://rs1img.memecdn.com/moreee_c_110719.webp",
"http://rs1img.memecdn.com/om-nom-nom-nom_c_880714.webp",
"http://rs1img.memecdn.com/pug-decisions_c_2781035.webp",
"http://rs1img.memecdn.com/the-leader-is-hungry_c_1141256.webp",
"http://rs1img.memecdn.com/when-my-cats-are-hungry_c_1004053.webp",
"http://s.quickmeme.com/img/cb/cb14bd3376a0b1bc0366a2128939d56ec4960fb05a085683020455ad2b4697b3.jpg",
"http://www.quickmeme.com/img/d1/d1a2b6a3f1779bc2cc9e279140fd3d2f4acf59e609ba45e391b1bf6617ad2371.jpg",
"http://www.quickmeme.com/img/f7/f7f56079d4db1965bdc0cd86e757b4e90c3101943b0ee90a42489cbb5439c520.jpg",
"https://i.chzbgr.com/maxW500/4779354368/hD41CC126/",
"https://i.chzbgr.com/maxW500/5081082880/h5B051851/",
"https://i.chzbgr.com/maxW500/8204975104/h520D419A/",
"http://weknowmemes.com/wp-content/uploads/2011/10/come-on-baby-dont-be-like-that-i-brought-you-some-toast.jpg",
"http://33.media.tumblr.com/tumblr_m9xbrrj1wV1qf8btso1_500.gif",
"http://s3-ec.buzzfed.com/static/2014-03/enhanced/webdr08/14/23/anigif_enhanced-3456-1394853903-7.gif",
"http://s3-ec.buzzfed.com/static/2014-03/enhanced/webdr08/14/23/anigif_enhanced-3485-1394854020-2.gif",
"http://s3-ec.buzzfed.com/static/2014-03/enhanced/webdr02/14/23/anigif_enhanced-4532-1394855064-10.gif",
"http://s3-ec.buzzfed.com/static/2014-11/27/9/tmp/webdr11/anigif_mobile_2c83bc2e8202e74fe772baaabfc670e5-7.gif",
"http://i.imgur.com/p0D7HVZ.gif",
"http://i.imgur.com/MPV0tV8.gif",
"http://media.giphy.com/media/2CUlgdaAwzQME/giphy.gif"
]