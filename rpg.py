def in_the_zoo():
	print("你的小隊裡有一個小男生看起來悶悶不樂地坐在位置上，請選擇：")
	print("(1)關心他")
	print("(2)不理他")
	while True:
		move = input("> ")
		if move == "1":
			print("你獲得了小男孩的全然信任")
			win()
			break;
		if move == "2":
			print("說好的有愛心呢，忘記人設了嗎？")
			dead()
			break;
		else:
			print("輸入錯誤，請重新輸入")

def dead(why):
	print("你死於「%s」" % why)
	quit()

def win():
	print("你成功收編了一位十歲小男孩")
	quit()

def start():
	print("你是一個很有愛心的大學生，參加了學校舉辦的偏鄉關懷計劃。")
	print("某天，偏鄉中心的助理邀請你辦理偏鄉孩子們北上出遊的活動。")
	print("請問你決定拒絕助理還是答應參加？")
	while True:
		move = input("> ")
		if move == "拒絕助理":
			print("你怎麼這麼沒愛心，維持好人設好嗎。")
			dead("設計者的譴責")
		elif move == "答應參加":
			in_the_zoo()
		else:
			print("輸入錯誤，請重新輸入拒絕助理或答應參加。")

start()