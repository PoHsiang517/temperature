#溫度轉換(Celsius攝氏轉Fahrenheit華氏)
choice = input("請輸入轉換方式 1.攝氏轉華氏 2.華氏轉攝氏...：")
if choice == "1":
	celisius = input("請輸入攝氏溫度: ")
	fahr = int(celisius) * 9 / 5 + 32 #攝氏轉華氏
	print("攝氏溫度" + str(celisius) +"度=華氏" + str(fahr) + "度")
elif choice == "2":
	fahr = input("請輸入華氏溫度: ")
	celisius = (int(fahr) -32) * 5 / 9 #華氏轉攝氏
	print("華氏溫度" + str(fahr) +"度=攝氏" + str(celisius) + "度")
