# -*- coding: utf-8 -*-
'''
Stage: "真希の家"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def be_victim(w: World):
    maki = w.get('maki')
    dad = w.get('dad')
    return w.scene('被害者面',
            w.symbol("　　　　◆"),
            "貧しさがわかる狭さと物、あと$makiが苦労して生活を支えていることなど",
            "壁にはセーラー服が掛けてある",
            maki.be(),
            dad.come(),
            dad.talk("全く、お前は自分が女だってこと忘れてんじゃねえか？",
                "知らない男の家に入り浸ってただピアノ弾かせてもらってたなんて警察が信じると思うのかよ"),
            maki.do("父親に引き取られてアパートに戻ってきた$Sだったが、",
                "警察の事情聴取に疲れ果てていてとても酔っぱらいの戯言に付き合う気分にはなれなかった"),
            dad.talk("おい何だ？", "何か言うことはないのか？",
                "あいつが死ななかったらお前は酷い目に遭ってたかもしれんのだぞ？",
                "お前はラッキーだったんだよ",
                "ただでさえそんな頭してまともに思われてないんだから、これを機にもうちょっと真面目に学校に行ってだな"),
            maki.talk("うっさい！　しね！"),
            dad.talk("おい！　何だよ！", "$meの何が悪いってんだよ！"),
            "父親の怒鳴り声が、まだ耳がしっかり聞こえていた頃にいつまでも鳴り止まない雑音だったことを思い出す",
            maki.do("父親の脛を蹴飛ばし、$Sはそのまま家に上がらずに外へと駆け出した"),
            maki.do("アスファルトが雨で濡れている中、それでも構わずに無我夢中で走った",
                "気がつくと商店街のアーケードまで来ていたが、既にほとんどの店が閉まり、電灯も半分は切れて暗くなってしまっている"),
            maki.talk("あ……"),
            maki.do("電気屋のショウウインドーに飾られたテレビに映ったニュースでは、女子高生を連れ去った元作曲家の$full_sakaiが脳梗塞で亡くなったと報じられていた"),
            outline="家に連れ戻された$makiは、世間では$sakaiに監禁されていたことになっていた")

