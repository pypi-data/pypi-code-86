class pyezxl_color:
	def __init__(self,aa):
		# 사용가능한 색깔을 보다 쉽게 표현하기위해 만들었다
		# 색은 3가지로 구분 : 테이블등을 만들때 사용하면 좋은 색 : ez1~15번까지
		# 12가지의 색을 기본, 약간 옅은 테이블색칠용, 파스텔톤의 3가지로 구분
		# 각 3종류는 7개의 형태로 구분하여 +, -의 형태로 표현을 하도록 하였다
		aa = "www.halmoney.com"
		self.color_nono = {
			"ez1" : 6384127,
			"ez2" : 4699135,
			"ez3" : 9895421,
			"ez4" : 7855479,}


	def color(self):
		color_no = {
			"ez1" : 6384127,
			"ez2" : 4699135,
			"ez3" : 9895421,
			"ez4" : 7855479,
			"ez5" : 13616814,
			"ez6" : 11902643,
			"ez7" : 12566463,
			"ez8" : 12419407,
			"ez9" : 5066944,
			"ez10" : 5880731,
			"ez11" : 10642560,
			"ez12" : 13020235,
			"ez13" : 4626167,
			"ez14" : 65535,
			"ez15" : 13566071,
			"white---" : 15790320,
			"white--" : 16119285,
			"white-" : 16448250,
			"white" : 16777215,
			"white+" : 16777215,
			"white++" : 16777215,
			"white+++" : 16777215,
			"white_t---" : 15790320,
			"white_t--" : 16119285,
			"white_t-" : 16448250,
			"white_t" : 16777215,
			"white_t+" : 16777215,
			"white_t++" : 16777215,
			"white_t+++" : 16777215,
			"white_p---" : 15790320,
			"white_p--" : 16119285,
			"white_p-" : 16448250,
			"white_p" : 16777215,
			"white_p+" : 16777215,
			"white_p++" : 16777215,
			"white_p+++" : 16777215,
			"black---" : 0,
			"black--" : 0,
			"black-" : 0,
			"black" : 0,
			"black+" : 1052688,
			"black++" : 2171169,
			"black+++" : 3289650,
			"black_t---" : 0,
			"black_t--" : 0,
			"black_t-" : 0,
			"black_t" : 0,
			"black_t+" : 1052688,
			"black_t++" : 2171169,
			"black_t+++" : 3289650,
			"black_p---" : 0,
			"black_p--" : 1052688,
			"black_p-" : 2171169,
			"black_p" : 3289650,
			"black_p+" : 4342338,
			"black_p++" : 5460819,
			"black_p+++" : 6579300,
			"gray---" : 5855577,
			"gray--" : 6710886,
			"gray-" : 7566195,
			"gray" : 8421504,
			"gray+" : 9211020,
			"gray++" : 10066329,
			"gray+++" : 10921638,
			"gray_t---" : 8355711,
			"gray_t--" : 9605778,
			"gray_t-" : 10855845,
			"gray_t" : 12105912,
			"gray_t+" : 13355979,
			"gray_t++" : 14606046,
			"gray_t+++" : 15921906,
			"gray_p---" : 13355979,
			"gray_p--" : 13750737,
			"gray_p-" : 14211288,
			"gray_p" : 14606046,
			"gray_p+" : 15066597,
			"gray_p++" : 15461355,
			"gray_p+++" : 15921906,
			"red---" : 179,
			"red--" : 204,
			"red-" : 230,
			"red" : 255,
			"red+" : 1710847,
			"red++" : 3355647,
			"red+++" : 5066239,
			"red_t---" : 2303075,
			"red_t--" : 4276858,
			"red_t-" : 6316434,
			"red_t" : 8356010,
			"red_t+" : 10329794,
			"red_t++" : 12369370,
			"red_t+++" : 14408946,
			"red_p---" : 1384703,
			"red_p--" : 3029503,
			"red_p-" : 4739583,
			"red_p" : 6384127,
			"red_p+" : 8094207,
			"red_p++" : 9738751,
			"red_p+++" : 11449087,
			"orange---" : 29875,
			"orange--" : 33996,
			"orange-" : 38374,
			"orange" : 42495,
			"orange+" : 1748735,
			"orange++" : 3389439,
			"orange+++" : 5095679,
			"orange_t---" : 411799,
			"orange_t--" : 2712488,
			"orange_t-" : 5013177,
			"orange_t" : 7379402,
			"orange_t+" : 9680091,
			"orange_t++" : 11980780,
			"orange_t+++" : 14347005,
			"orange_p---" : 37626,
			"orange_p--" : 1351423,
			"orange_p-" : 3057919,
			"orange_p" : 4699135,
			"orange_p+" : 6405887,
			"orange_p++" : 8046847,
			"orange_p+++" : 9753599,
			"yellow---" : 46003,
			"yellow--" : 52428,
			"yellow-" : 59110,
			"yellow" : 65535,
			"yellow+" : 1769471,
			"yellow++" : 3407871,
			"yellow+++" : 5111807,
			"yellow_t---" : 47292,
			"yellow_t--" : 115655,
			"yellow_t-" : 249810,
			"yellow_t" : 383965,
			"yellow_t+" : 452584,
			"yellow_t++" : 586739,
			"yellow_t+++" : 720895,
			"yellow_p---" : 4979964,
			"yellow_p--" : 6618364,
			"yellow_p-" : 8257021,
			"yellow_p" : 9895421,
			"yellow_p+" : 11533821,
			"yellow_p++" : 13172478,
			"yellow_p+++" : 14810878,
			"green---" : 13312,
			"green--" : 19712,
			"green-" : 26368,
			"green" : 32768,
			"green+" : 39424,
			"green++" : 45824,
			"green+++" : 52480,
			"green_t---" : 2646351,
			"green_t--" : 4618601,
			"green_t-" : 6590851,
			"green_t" : 8563101,
			"green_t+" : 10535351,
			"green_t++" : 12507601,
			"green_t+++" : 14545387,
			"green_p---" : 3853882,
			"green_p--" : 5165902,
			"green_p-" : 6543459,
			"green_p" : 7855479,
			"green_p+" : 9167499,
			"green_p++" : 10545056,
			"green_p+++" : 11857076,
			"blue---" : 11730944,
			"blue--" : 13369344,
			"blue-" : 15073280,
			"blue" : 16711680,
			"blue+" : 16718362,
			"blue++" : 16724787,
			"blue+++" : 16731469,
			"blue_t---" : 6772768,
			"blue_t--" : 8286527,
			"blue_t-" : 9800286,
			"blue_t" : 11379581,
			"blue_t+" : 12893340,
			"blue_t++" : 14407099,
			"blue_t+++" : 15986395,
			"blue_p---" : 11773054,
			"blue_p--" : 12365710,
			"blue_p-" : 13024158,
			"blue_p" : 13616814,
			"blue_p+" : 14209470,
			"blue_p++" : 14867918,
			"blue_p+++" : 15460574,
			"indigo---" : 3538975,
			"indigo--" : 5177390,
			"indigo-" : 6881340,
			"indigo" : 8519755,
			"indigo+" : 10223706,
			"indigo++" : 11862120,
			"indigo+++" : 13566071,
			"indigo_t---" : 6373412,
			"indigo_t--" : 7953218,
			"indigo_t-" : 9533281,
			"indigo_t" : 11113087,
			"indigo_t+" : 12693150,
			"indigo_t++" : 14272956,
			"indigo_t+++" : 15853019,
			"indigo_p---" : 3538975,
			"indigo_p--" : 5177390,
			"indigo_p-" : 6881340,
			"indigo_p" : 8519755,
			"indigo_p+" : 10223706,
			"indigo_p++" : 11862120,
			"indigo_p+++" : 13566071,
			"purple---" : 3407924,
			"purple--" : 5046349,
			"purple-" : 6750311,
			"purple" : 8388736,
			"purple+" : 10092698,
			"purple++" : 11731123,
			"purple+++" : 13435085,
			"purple_t---" : 5321023,
			"purple_t--" : 6966874,
			"purple_t-" : 8678262,
			"purple_t" : 10389650,
			"purple_t+" : 12101037,
			"purple_t++" : 13812425,
			"purple_t+++" : 15524069,
			"purple_p---" : 9728913,
			"purple_p--" : 10453404,
			"purple_p-" : 11178152,
			"purple_p" : 11902643,
			"purple_p+" : 12627134,
			"purple_p++" : 13351882,
			"purple_p+++" : 14076373,
			"pink---" : 4656639,
			"pink--" : 6435327,
			"pink-" : 8214015,
			"pink" : 10058239,
			"pink+" : 11836927,
			"pink++" : 13615615,
			"pink+++" : 15459839,
			"pink_t---" : 8543231,
			"pink_t--" : 9201919,
			"pink_t-" : 9860607,
			"pink_t" : 10519295,
			"pink_t+" : 11177983,
			"pink_t++" : 11836671,
			"pink_t+++" : 12495615,
			"pink_p---" : 10651135,
			"pink_p--" : 11441919,
			"pink_p-" : 12298239,
			"pink_p" : 13154559,
			"pink_p+" : 14010879,
			"pink_p++" : 14867199,
			"pink_p+++" : 15723519,
			"brown---" : 4478571,
			"brown--" : 4807795,
			"brown-" : 5137019,
			"brown" : 5466499,
			"brown+" : 5795723,
			"brown++" : 6124947,
			"brown+++" : 6454427,
			"brown_t---" : 7243428,
			"brown_t--" : 7769256,
			"brown_t-" : 8295341,
			"brown_t" : 8821426,
			"brown_t+" : 9347255,
			"brown_t++" : 9873340,
			"brown_t+++" : 10399425,
			"brown_p---" : 11977425,
			"brown_p--" : 12634839,
			"brown_p-" : 13292253,
			"brown_p" : 13949924,
			"brown_p+" : 14607338,
			"brown_p++" : 15264752,
			"brown_p+++" : 15922423,
			1 : 0,
			2 : 16777215,
			3 : 255,
			4 : 65280,
			5 : 16711680,
			6 : 65535,
			7 : 16711935,
			8 : 16776960,
			9 : 128,
			10 : 32768,
			11 : 8388608,
			12 : 32896,
			13 : 8388736,
			14 : 8421376,
			15 : 12632256,
			16 : 8421504,
			17 : 16751001,
			18 : 6697881,
			19 : 13434879,
			20 : 16777164,
			21 : 6684774,
			22 : 8421631,
			23 : 13395456,
			24 : 16764108,
			25 : 8388608,
			26 : 16711935,
			27 : 65535,
			28 : 16776960,
			29 : 8388736,
			30 : 128,
			31 : 8421376,
			32 : 16711680,
			33 : 16763904,
			34 : 16777164,
			35 : 13434828,
			36 : 10092543,
			37 : 16764057,
			38 : 13408767,
			39 : 16751052,
			40 : 10079487,
			41 : 16737843,
			42 : 13421619,
			43 : 52377,
			44 : 52479,
			45 : 39423,
			46 : 26367,
			47 : 10053222,
			48 : 9868950,
			49 : 6697728,
			50 : 6723891,
			51 : 13056,
			52 : 13107,
			53 : 13209,
			54 : 6697881,
			55 : 10040115,
			56 : 3355443,
		}
		return color_no