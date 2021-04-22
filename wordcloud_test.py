import MeCab
from wordcloud import WordCloud, ImageColorGenerator
from matplotlib import pyplot as plt
from imageio import imread


with open("kumono_ito.txt", encoding="utf-8")as f:
    read_data = f.read()

tagger = MeCab.Tagger()
tagger.parse("")
node = tagger.parseToNode(read_data)

# 名詞を取り出す
word_list = []
while node:
    word_type = node.feature.split(',')[0]
    if word_type == '名詞':
        word_list.append(node.surface)
    node = node.next

# リストを文字列に変換
word_chain = ' '.join(word_list)

back_coloring = imread("lotus_pic3.png")
image_colors_byImg = ImageColorGenerator(back_coloring)

word_cloud = WordCloud(font_path='C:\Windows\Fonts\yumin.ttf', background_color="white",
                       width=800, height=500).generate(word_chain)
plt.imshow(word_cloud.recolor(color_func=image_colors_byImg))
plt.axis("off")
plt.show()