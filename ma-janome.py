# coding:utf-8

from janome.tokenizer import Tokenizer

t = Tokenizer()
malist = t.tokenize(u"太郎は5月18日の朝9時に花子に会いに行った。")

for n in malist:
	print(n)