def long_grain(text):
    if '茉莉香米' in text or '頂級香米' in text or '茉莉銀絲香米'in text or '絲苗米' in text:
        return '101'
    else:
        return '199'
def short_grain(text):
    if '珍珠米' in text or '短身米' in text or '珍珠白米' in text:
        return '101'
    else:
        return '199'
def spaghetti(text):
    if '扁意粉' in text or '扁意大利粉' in text or '意大利' in text or '意大利意粉' in text or '扁身意粉' in text or '意粉' in text:
        return '101'
    else:
        return '199'
def macaroni(text):
    if '螺絲粉' in text or '直通粉' in text or '通心粉' in text or '通粉' in text or '蜆殼粉' in text or '扭扭粉' in text:
        return '101'
    else:
        return '199'
def noodle(text):
    if '蝦子麵' in text or '關廟麵' in text or '刀削麵' in text or '瑤柱麵' in text or '養生麵條' in text or '彈牙麵' in text or '有機麵線' in text or '有機紅藜麥麵' in text or '擔仔麵' in text or '全蛋麵' in text or '菠菜麵' in text or '蒟蒻麵' in text:
        return '101'
    else:
        return"199"
def instant_noodles(text):
    if '印尼撈麵' in text or '麻油麵' in text or '麻油味麵' in text or '麻油' in text or '豬骨湯麵' in text or '豬骨' in text or '拌麵' in text or '牛骨湯麵' in text or '芝士拉麵' in text or '麻醬拌麵' in text:
        return '101'
    elif '蝦子麵' in text or '關廟麵' in text or '刀削麵' in text or '瑤柱麵' in text or '養生麵條' in text or '彈牙麵' in text or '有機麵線' in text or '有機紅藜麥麵' in text or '擔仔麵' in text or '全蛋麵' in text or '菠菜麵' in text or '蒟蒻麵' in text:
        return '299'
    elif '麵' in text:
        return '199'
    else:
        return""
def oats_and_cereals(text):
    if '燕麥片' in text or '燕麥方脆'in text or '營養麥' in text or '麥片' in text or '燕麥糠' in text or '麥米片' in text or '玉米片' in text or '粟米片' in text or '美祿可可' in text or '蜂蜜星星' in text or '可可脆片' in text:
        return '101'
    else:
        return '199'
def flour_and_pancake_mix(text):
    if '高筋麵粉' in text or '高筋' in text or '低筋麵粉' in text or '低筋' in text or '小麥麵粉' in text or '小麥' in text or '法國全麥麵粉' in text or '法國麵粉' in text or '全麥' in text or '中筋' in text or '中筋麵粉' in text:
        return '101'
    else:
        return '199'
def fish_sashimi(text):
    if '急凍日本油甘魚鮫' in text or '挪威三文魚柳' in text or '日本醋鯖魚(急凍)' in text or '丹麥頂級三文魚180克 ' in text or '煎焗' in text or '氣炸' in text or '連皮' in text or '有皮' in text or '魚扒' in text or '浦燒' in text or '煙三文魚' in text or '三文魚骨' in text or '煙' in text or '三文魚腩邊' in text or '鹽漬三文魚' in text or '三文魚塊' in text or '急凍挪威鯖魚' in text or '急凍豬扒' in text or '三文魚頭' in text:
        return '199'
    elif '魚柳刺身' in text or '刺身' in text or '左口魚' in text or '鯛魚柳' in text or '吞拿魚' in text or '希靈魚' in text or '鯛魚' in text or '鯖魚' in text or '三文魚' in text or '油甘魚' in text:
        return '101'
    else:
        return '199'
def frozen_fish(text):
    if '急凍日本油甘魚鮫' in text or '魚柳' in text or '日本醋鯖魚(急凍)' in text or '丹麥頂級三文魚180克 ' in text or '連皮' in text or '魚扒' in text or '浦燒' in text or '煙三文魚' in text or '三文魚骨' in text or '煙' in text or '三文魚腩邊' in text or '鹽漬三文魚' in text or '三文魚塊' in text or '急凍挪威鯖魚' in text or '三文魚頭' in text or '直切比目魚' in text or '烏頭' in text or '冷藏魚' in text or '多春魚' in text or '龍脷柳' in text:
        return '101'
    elif '魚柳刺身' in text or '刺身' in text or '左口魚' in text or '鯛魚柳' in text or '吞拿魚' in text or '希靈魚' in text or '鯛魚' in text or '鯖魚' in text or '三文魚' in text or '油甘魚' in text:
        return '199'
    else:
        return '199'
def sea_shrimp(text):
    if '天婦羅' in text or '蝦手指' in text or '雲吞' in text or '丸' in text or '黃金蝦卷' in text or '炸' in text:
        return '199'
    elif '蝦仁' in text or '蝦肉' in text or '蝦' in text:
        return '101'
    else:
        return '199'
def canned_abalone(text):
    if '南北行 - 澳洲天然原色鮑魚(2隻)' in text or '信玄 - 鮮味一口鮑魚<5粒裝>' in text or '萬順昌 - 秘製慢煮吉品鮑魚 (6頭/430g)' in text or '信玄 - 日本醬油鮑魚 50克' in text or 'ANH - 新西蘭野生黑鮑魚' in text or '平到家 - 足金鮑 南非鮑魚(一罐8隻)' in text or '上湯鮑魚' in text or '海螺' in text or '頂級澳洲鮑魚6-8頭' in text or '清湯' in text or '醬皇' in text or '溏心' in text or '乾鮑魚' in text or '皇后牌頂級南非8頭鮑魚' in text or '蟲草' in text or '鮑魚汁' in text or '小食' in text or '鮑魚麵' in text or '金湯頂級鮑魚' in text or '木耳' in text or '禮盒' in text or '濃湯鮑魚' in text or '佛跳墻' in text or '清湯鮑魚' in text or '阿一原味鮑魚' in text or '黃金吉品鮑魚8隻盒裝' in text or '仿玉鮑' in text or '極品南非鮑魚' in text or '信玄 - 醬油珍珠鮑魚' in text or '渡邊水產 - 原隻鮑魚仔(熟)' in text or '燒汁' in text or '五福臨門' in text or '響螺' in text or '元貝' in text or '麻辣' in text or '罐頭鮑魚' in text or 'XO醬' in text or '花膠' in text or '福袋' in text or '盆菜' in text or '紅燒' in text or '即食' in text or '極品鮑魚' in text or '干貝' in text or '溏心鮑魚' in text or '鮑汁鮑魚' in text or '素' in text or '蠔皇' in text or '鮑魚佛跳牆' in text or '鮑魚丸子' in text:
        return '299'
    elif '青邊鮑魚' in text or '鮮鮑' in text or '吉品鮑' in text or '半熟鮑魚' in text or '磯煮鮑魚' in text or '澳洲鮑魚' in text or '帶殼鮑魚' in text or '翡翠鮑魚' in text or '鮑魚' in text:
        return '101'
    elif '鮑' in text:
        return '199'
    else:
        return '299'
def frozen_scallop(text):
    if '帶子套裝' in text or '素帶子' in text or '無激素雞翼' in text:
        return '199'
    elif '帶子' in text:
        return '101'
    else:
        return '199'
def other_frozen_seafood(text):
    if '火鍋赤貝' in text or '八爪魚粒' in text or '青口' in text or '蠔' in text or '花膠' in text or '扇貝' in text or '海參' in text or '蜆' in text or '魷魚' in text or '蟹腳' in text:
        return '101'
    else:
        return '199'
def cuttlefish_ball(text):
    if '墨魚丸' in text or '墨魚味魚丸' in text or '墨丸' in text:
        return '101'
    elif '丸' in text:
        return '199'
    else:
        return '299'
def frozen_shrimp_and_lobster_balls(text):
    if '鮮蝦丸' in text or '蝦丸' in text or '龍蝦丸' in text or '龍蝦沙拉味丸' in text or '龍蝦沙拉丸' in text or '蝦堡丸' in text or '蝦墨丸' in text:
        return '101'
    elif '丸' in text:
        return '199'
    else:
        return '299'
def other_fish_preparations(text):
    if '蟹柳' in text or '假帶子' in text or '魚手指' in text or '炸魚條' in text or '魚卷' in text or '脆炸魚柳' in text or '蟹肉棒' in text or '魚肉春卷' in text:
        return '101'
    elif '蟹' in text or '魚' in text:
        return '199'
    else:
        return '299'
def pork_fillet(text):
    if '扒' in text or '有骨豬扒' in text or '無骨豬扒' in text or '梅頭扒' in text:
        return '299'
    elif '腩肉火鍋片' in text or '豬肉丁' in text or '豬腩片' in text or '免治豬肉' in text or '梅肉火鍋片' in text or '豬梅肉' in text or '豬梅片' in text or '豬梅頭肉' in text or '免治豬梅肉' in text or '煙肉片' in text or '豬梅肉片' in text or '豬柳' in text or '無骨肉' in text or '免冶豬肉' in text or '豬腩條' in text:
        return '101'
    elif '豬' in text:
        return '199'
    else:
        return '299'
def pork_steak(text):
    if '豬扒' in text or '有骨豬扒' in text or '無骨豬扒' in text or '梅頭扒' in text or '豬梅肉扒' in text or '豬斧頭扒' in text:
        return '101'
    elif '豬' in text:
        return '199'
    else:
        return '299'
def beef_fillet(text):
    if '牛肉粒' in text or '牛肩肉' in text or '牛上肩切片' in text or '牛柳' in text or '牛柳粒' in text or '肥牛' in text or '牛粒' in text or '牛片' in text:
        return '101'
    elif '牛' in text:
        return '199'
    else:
        return '299'
def beef_steak(text):
    if '牛扒' in text or '牛西冷' in text or '牛肋條' in text or '牛小排' in text or '牛扒' in text or '肉眼' in text or 'T骨' in text or '牛仔骨' in text:
        return '101'
    elif '牛' in text:
        return '199'
    else:
        return '299'

def whole_chicken(text):
    keyword = '全雞','春雞','龍江雞','鳳崗雞','西班牙黃春'
    not_be_keyword = '雞下髀','歐洲雞全餐'
    category = '雞'
    if any(i in text for i in not_be_keyword):
        return '199'
    elif any(i in text for i in keyword):
        return '101'
    elif any(i in text for i in category):
        return '199'
    else:
        return '299'
def chicken_leg_and_steak(text):
    keyword = '雞槌','雞下髀','雞下肶','帶皮雞扒','雞下脾','雞髀扒','雞上脾','雞扒','雞上脾扒'
    not_be_keyword = ''
    category = '雞'
    if any(i in text for i in not_be_keyword):
        return '199'
    elif any(i in text for i in keyword):
        return '101'
    elif any(i in text for i in category):
        return '199'
    else:
        return '299'
def chicken_breast_and_fillet(text):
    keyword = '雞柳','雞胸','雞小胸'
    not_be_keyword = ''
    category = '雞'
    if any(i in text for i in not_be_keyword):
        return '199'
    elif any(i in text for i in keyword):
        return '101'
    elif any(i in text for i in category):
        return '199'
    else:
        return '299'
def frozen_chicken_other(text):
    keyword = '雞塊','雞軟骨','雞腳'
    not_be_keyword = ''
    category = '雞'
    if any(i in text for i in not_be_keyword):
        return '199'
    elif any(i in text for i in keyword):
        return '101'
    elif any(i in text for i in category):
        return '199'
    else:
        return '299'
def frozen_sausages(text):
    keyword = '雞肉腸','香腸','紅腸','芝士腸','黑毛豬莎樂美腸','脆皮腸','黑豚腸','豬肉香腸','高級雞肉腸','豬肉腸','燒烤腸','鷄肉腸'
    not_be_keyword = ''
    category = '腸'
    if any(i in text for i in not_be_keyword):
        return '199'
    elif any(i in text for i in keyword):
        return '101'
    elif any(i in text for i in category):
        return '199'
    else:
        return '299'
def frozen_mutton(text):
    keyword = '羊架','羊卷肉','羊肉片','羊扒','羊腩粒','羊捲肉','羊脾粒','羊仔膝','羊肩扒'
    not_be_keyword = ''
    category = '羊'
    if any(i in text for i in not_be_keyword):
        return '199'
    elif any(i in text for i in keyword):
        return '101'
    elif any(i in text for i in category):
        return '199'
    else:
        return '299'
def canned_luncheon_meat(text):
    keyword = '午餐肉', '火腿豬肉', '午餐豬肉'
    not_be_keyword = ''
    category = '午餐肉'
    if any(i in text for i in not_be_keyword):
        return '199'
    elif any(i in text for i in keyword):
        return '101'
    elif any(i in text for i in category):
        return '199'
    else:
        return '299'
def canned_spiced_pork_cubes(text):
    if '五香肉丁' in text:
        return '101'
    elif '肉' in text:
        return '199'
    else:
        return '299'
def canned_double_cooked_sork_slices(text):
    if '回鍋肉' in text:
        return '101'
    elif '肉' in text:
        return '199'
    else:
        return '299'
def mushroom(text):
    keyword = '菇'
    not_be_keyword = ''
    category = ''
    if any(i in text for i in not_be_keyword):
        return '199'
    elif any(i in text for i in keyword):
        return '101'
    elif any(i in text for i in category):
        return '199'
    else:
        return '299'
def canned_corn(text):
    if '粟米粒' in text or '粟米罐頭' in text or '多蔬 - 粟米 340g' in text or '超甜粟米' in text:
        return '101'
    elif '粟米' in text:
        return '199'
    else:
        return '299'
def frozen_green_peas(text):
    if '雜菜' in text or '雜豆' in text or '青豆' in text:
        return '101'
    elif '' in text:
        return '199'
    else:
        return '299'
def canned_fruit(text):
    if '去皮切碎蕃茄' in text or '菠蘿片' in text or '什果' in text or '切邊黃桃' in text or '薄切白桃' in text or '菠蘿粒 (大罐)' in text or '去皮蕃茄' in text:
        return '101'
    elif '罐' in text:
        return '199'
    else:
        return '299'
def milk_powder(text):
    if '奶粉' in text or '惠氏 - 惠氏S-26 Progress Ultima' in text or '成長配方' in text or '雅培 - 低糖加營素' in text or '金裝加營素' in text:
        return '101'
    elif '奶' in text:
        return '199'
    else:
        return '299'
def evaporated_milk(text):
    if '淡奶' in text:
        return '101'
    elif '奶' in text:
        return '199'
    else:
        return '299'
def flavoured_milk(text):
    if '燕麥奶' in text or '香蕉味牛奶'in text or '朱古力牛奶' in text or '木瓜奶' in text or '朱古力奶' in text or '益力多' in text or '美樂多' in text or '香蕉奶' in text:
        return '101'
    elif '奶' in text:
        return '199'
    else:
        return '299'
def corn_oil(text):
    if '粟米油' in text or '玉米油' in text:
        return '101'
    elif '油' in text:
        return '199'
    else:
        return '299'
def olive_oil(text):
    if '欖油' in text or '橄欖果渣油' in text or '橄欖油' in text:
        return '101'
    elif '油' in text:
        return '199'
    else:
        return '299'
def carbonated_drinks(text):
    if '蘇打水' in text or '梳打' in text or '汽水' in text or '可口可樂' in text:
        return '101'
    elif '汽' in text:
        return '199'
    else:
        return '299'
def coffee(text):
    if '咖啡' in text or '濃香焙煎' in text:
        return '101'
    elif '即溶' in text:
        return '199'
    else:
        return '299'
def tea_and_leaf(text):
    if '茶包' in text:
        return '199'
    elif '特級烏龍' in text or '普洱' in text or '鐵觀音' in text or '茶餅' in text or '玫瑰' in text or '香六安' in text or '茶葉' in text or '人參烏龍' in text or '香片' in text or '荔枝紅茶' in text:
        return '101'
    else:
        return '299'
def tea_bag(text):
    if '茶包' in text or '黑烏龍茶 40袋' in text or '立頓茉莉花茶' in text:
        return '101'
    elif '茶' in text:
        return '199'
    else:
        return '299'
def lemon_tea(text):
    if '檸檬茶' in text:
        return '101'
    elif '檸檬' in text:
        return '199'
    else:
        return '299'
def other_tea_drinks(text):
    if '烏龍茶' in text or '菊花茶' in text or '解茶' in text or '普洱茶' in text or '香片茶' in text or '冬瓜茶' in text:
        return '101'
    elif '茶' in text:
        return '199'
    else:
        return '299'
def fresh_fruit_juice(text):
    if '100%椰青水' in text or '100%' in text or '純椰子水' in text or '純正番茄汁' in text or '純正' in text or '100 %蘋果汁' in text:
        return '101'
    elif '果汁' in text or '水' in text:
        return '199'
    else:
        return '299'
def pure_juice_and_cordial(text):
    if '100%' in text or '100 %' in text or '純' in text:
        return '199'
    elif '果汁' in text or '石榴汁' in text or '橙汁' in text or '紅莓汁' in text:
        return '101'
    else:
        return '299'
def flavoured_drinks(text):
    if '朝米水' in text or '奧樂蜜C' in text or '荔枝玉露' in text or 'Grape 碳酸飲品' in text or '玉露' in text or '巨峰提子' in text or '日本櫻花蘋果汁' in text or '荔枝蘆薈' in text or '馬蹄果汁' in text or '雪梨果汁' in text or '青蘋果汁' in text or '白葡萄桃味果汁' in text or '蒟蒻飲品' in text:
        return '101'
    elif '果汁' in text:
        return '199'
    else:
        return '299'
def soya_bean_milk(text):
    if '豆奶' in text or '大豆' in text or '豆漿' in text or'豆乳' in text:
        return '101'
    elif '豆' in text:
        return '199'
    else:
        return '299'
def essence_of_chicken(text):
    if '禮券' in text or '配方' in text:
        return '199'
    elif '雞精' in text:
        return '101'
    else:
        return '299'
def isoltonic_drinks(text):
    if '強身健體飲品' in text or '營養素飲品' in text or '運動飲品' in text or '黑麥汁' in text or '醋' in text or '能量飲品' in text or '維他命' in text or '蜂蜜' in text or '健康飲料' in text:
        return '101'
    elif '飲品' in text:
        return '199'
    else:
        return '299'
def mineral_water_and_distilled_water(text):
    if '礦泉水' in text or '蒸餾水' in text or '礦物質水' in text:
        return '101'
    elif '水' in text:
        return '199'
    else:
        return '299'
def honey(text):
    if '菊花' in text or '柚子茶' in text or '茶' in text:
        return '199'
    elif '蜂蜜' in text or '花蜜' in text:
        return '101'
    else:
        return '299'
def oyster_sauce(text):
    if '豉油' in text or '優惠裝' in text or '生抽' in text or '白醋' in text or 'XO醬' in text:
        return '199'
    elif '蠔油' in text:
        return '101'
    else:
        return '299'
def chili_sauce(text):
    if '辣椒' in text or '香辣' in text or '麻辣四川口水雞醬' in text or '辣豆瓣醬' in text or '麻辣鮮露' in text or '花椒辣油' in text or '麻辣醬' in text:
        return '101'
    elif '辣' in text:
        return '199'
    else:
        return '299'
def xo_sauce(text):
    if '舊庄特級蠔油' in text or '禮盒' in text:
        return '199'
    elif 'XO醬' in text or 'XO辣椒醬' in text:
        return '101'
    elif '醬' in text:
        return '199'
    else:
        return '299'
def curry_flavourings(text):
    if '椰漿套裝優惠2罐' in text:
        return '199'
    elif '咖喱' in text or '咖哩' in text :
        return '101'
    elif '' in text:
        return '199'
    else:
        return '299'
def vinegar(text):
    not_keyword = ['蘋果','舊庄特級蠔油','果','葡萄']
    keyword = ['醋']
    unrelated_keyword_same_category = ['']
    if not_keyword != '':
        if any(i in text for i in not_keyword):
            return '199'
        elif any(i in text for i in keyword):
            return '101'
        elif any(i in text for i in unrelated_keyword_same_category):
            return '199'
        else:
            return '299'
    else:
        if any(i in text for i in keyword):
            return '101'
        elif any(i in text for i in unrelated_keyword_same_category):
            return '199'
        else:
            return '299'
def soup_and_broth(text):
    not_keyword = ['現金券']
    keyword = ['湯', '燉']
    unrelated_keyword_same_category = ['']
    if not_keyword != '':
        if any(i in text for i in not_keyword):
            return '199'
        elif any(i in text for i in keyword):
            return '101'
        elif any(i in text for i in unrelated_keyword_same_category):
            return '199'
        else:
            return '299'
    else:
        if any(i in text for i in keyword):
            return '101'
        elif any(i in text for i in unrelated_keyword_same_category):
            return '199'
        else:
            return '299'
def vegetarian_food(text):
    if '素' in text or '植物雞塊' in text or '新豬肉' in text or '齋' in text:
        return '101'
    else:
        return '199'
def dried_seafood_and_tonics(text):
    if '雲耳' in text or '牛肝菌' in text or '雪耳' in text or '羊肚菌' in text or '竹笙' in text or '木耳' in text or '黃耳' in text:
        return '101'
    else:
        return '199'
def fried_shrimp_paste(text):
    if '蝦條' in text or '龍蝦片' in text or '脆片' in text or '蝦片' in text or '蝦餅' in text:
        return '101'
    elif '蝦' in text:
        return '199'
    else:
        return '299'
def cooked_nuts(text):
    if '花生醬' in text:
        return '299'
    elif '花生' in text or '杏仁' in text or '合桃' in text or '腰果' in text or '開心果' in text or '果仁' in text or '核桃'in text:
        return '101'
    else:
        return '299'
def preserved_fruit(text):
    if '乾' in text or '梅片' in text or '八仙果' in text or '山楂條' in text or '話梅' in text or '薑片' in text or '檸檬' in text or '酸梅' in text or '乾榴蓮' in text or '提子乾' in text:
        return '101'
    else:
        return '299'
def jelly(text):
    if '啫喱' in text or '蒟蒻' in text or '蒟篛' in text or '果凍' in text:
        return '101'
    else:
        return '299'
def instant_seaweed(text):
    if '紫菜' in text or '海苔' in text:
        return '101'
    else:
        return '299'
def seasoned_squid_and_cuttlefish(text):
    if '魷魚' in text:
        return '101'
    else:
        return '299'
def sweet_corn(text):
    if '粟米片' in text or '粟一燒' in text or '栗米條' in text or '粟米卷' in text or '粟米筒日燒' in text:
        return '101'
    else:
        return '299'
def baby_food(text):
    if '有機全穀無糖米餅' in text or 'Pigeon - 蘋果汁' in text or '低鈉紫菜' in text or '士多啤梨脆片' in text or '胚芽米' in text or '嬰幼兒' in text or '12個月+BB' in text or '適合12個月以上' in text:
        return '101'
    else:
        return '299'
#def fresh_ingredient_pack(text):

def redwine(text):
    if '紅酒' in text or '司堡酒莊 - Castillo De Soldepenas, 2019, 西班牙' in text or 'Doudet Naudin - [勃根地直送] Pinot Noir 2019' in text or 'Chateau De Ribebon - 銳碧莊園 波爾多 高品紅葡萄酒 2016 (JS 91)' in text:
        return '101'
    elif '酒' in text:
        return '199'
    else:
        return '299'
def whitewine(text):
    if '白酒' in text or 'Blue Nun - 德國 Riesling 2019/2020 (全新包裝)' in text or 'Blue Nun - 德國精選瓊瑤漿 Gewurztraminer 2018/2019' in text or 'Blue Nun - 德國 Rivaner 2020' in text or 'Sileni Estates - Cellar Selection Sauvignon Blanc Marlborough 2021 (全新年份，新鮮到港)' in text:
        return '101'
    elif '酒' in text:
        return '199'
    else:
        return '299'
def sake(text):
    if '清酒' in text or '梅酒' in text or '養命酒' in text or '日本' in text or '飛驛高山' in text or '山崎' in text or '沖繩' in text or '大吟釀' in text or '山梨縣' in text or '小野酒造' in text or '奧武藏' in text:
        return '101'
    elif '酒' in text:
        return '199'
    else:
        return '299'
def beer(text):
    if '啤酒' in text:
        return '101'
    elif '酒' in text:
        return '199'
    else:
        return '299'
def mens_coats(text):
    if '女' in text:
        return '299'
    elif '羽絨'in text:
        return '101'
    elif '外套' in text:
        return '199'
    else:
        return '299'
def mens_jackets(text):
    if '女' in text or '暗花' in text or '中性' in text or '小童' in text:
        return '299'
    elif '羽絨'in text:
        return '199'
    elif '長褸' in text or '外套' in text:
        return '101'
    else:
        return '299'
def mens_t_shirt(text):
    if '長袖' in text or  '女' in text or '暗花' in text or '中性' in text or '小童' in text or'VIVIESTA SPORT - 簡約親膚柔軟排汗舒適跑步運動T恤' in text or '運動' in text:
        return '299'
    elif 'T-shirt' in text or 'Tee' in text or 'T恤' in text:
        return '101'
    elif '男' in text:
        return '199'
    else:
        return '299'
def mens_jeans(text):
    if '女' in text:
        return '299'
    elif '牛仔褲' in text:
        return '101'
    elif '男' in text:
        return '199'
    else:
        return '299'
def sports_jackets_and_trousers(text):
    if '女裝' in text or '內褲' in text or '臂套' in text or '眼鏡' in text or '襪' in text or '背囊' in text or '護膝' in text or '波鞋' in text or '護理噴劑' in text or '墊' in text or '噴霧' in text or '鞋' in text:
        return '299'
    elif '運動' in text or '防水' in text or '快乾' in text:
        return '101'
    elif '男' in text:
        return '199'
    else:
        return '299'
def men_sports_shirts(text):
    if 'Secret Face' in text or 'Baleno' in text or 'NATIONAL GEOGRAPHIC' in text:
        return '299'
    elif '背心' in text or '裇衫' in text or 'T恤' in text:
        return '101'
    elif '運動' in text:
        return '199'
    else:
        return '299'
def men_sports_shorts(text):
    if '運動短褲' in text or '緊身短褲'in text:
        return '101'
    elif '運動' in text:
        return '199'
    else:
        return '299'
def men_windbreaker(text):
    if '女裝' in text or '女子' in text:
        return '299'
    elif '連帽風褸' in text or '帽輕薄風衣外套' in text or '防風外套' in text or '風褸' in text or '套頭風衣' in text:
        return '101'
    elif '風' in text:
        return '199'
    else:
        return '299'
def women_suits_summer(text):
    if '背心哺乳裙' in text or '背心裙' in text or '裙套裝' in text or '哺裙套裝' in text or '哺乳套裝' in text:
        return '101'
    elif '乳' in text or'裙' in text:
        return '199'
    else:
        return '299'
def women_blouse_and_shirt_summer(text):
    if '男' in text or '運動' in text:
        return '299'
    elif '條子恤衫' in text or '長袖針織衫' in text or '長袖恤衫' in text or '襯衫' in text or '上衣' in text or '裇衫' in text or '無袖上衣' in text or '雪紡' in text:
        return '101'
    else:
        return '299'
def women_frocks_and_skirts_summer(text):
    if '連衣裙' in text or '連身裙' in text or '西裙' in text or '背心裙' in text:
        return '101'
    elif '裙' in text:
        return '199'
    else:
        return '299'
def women_trousers_summer(text):
    if '男' in text or '運動長褲' in text:
        return '299'
    elif '梳織長褲' in text or '修身褲' in text or '修身長褲' in text or '直腳西褲' in text or '九分褲' in text or '女裝Basic短褲' in text or '麻棉短褲' in text or '休閑長褲' in text or '腰圍托腹長褲' in text:
        return '101'
    elif '褲' in text:
        return '199'
    else:
        return '299'
def pregnant_clothing(text):
    if '哺乳套裝' in text or '哺乳裙' in text or '孕裝' in text or 'Sakura 櫻花 - 日本直送和服' in text or '露臍套裝' in text or '二件式透氣襯衫&吊帶背心' in text or '工人裙連襯衫' in text:
        return '101'
    elif '孕' in text:
        return '199'
    else:
        return '299'
def women_blouse_and_shirt_winter(text):
    if '男' in text or '運動' in text:
        return '299'
    elif '寛鬆恤衫' in text or '條子恤衫' in text or '長袖針織衫' in text or '長袖恤衫' in text or '襯衫' in text or '上衣' in text or '裇衫' in text or '上衣' in text or '雪紡' in text:
        return '101'
    elif '恤衫' in text:
        return '199'
    else:
        return '299'
def women_frocks_and_skirts_winter(text):
    if '連衣裙' in text or '連身裙' in text or '西裙' in text or '背心裙' in text or '哺乳長裙' in text:
        return '101'
    elif '裙' in text:
        return '199'
    else:
        return '299'
def women_trousers_winter(text):
    if '男' in text or '運動長褲' in text:
        return '299'
    elif '九分褲' in text or '針織長褲' in text or '裙褲' in text or '束腳褲' in text or '梳織長褲' in text or '修身褲' in text or '修身長褲' in text or '直腳西褲' in text or '七分褲' in text or'寬褲' in text or '休閑長褲' in text or '腰圍托腹長褲' in text:
        return '101'
    elif '褲' in text:
        return '199'
    else:
        return '299'
def women_coat(text):
    if '男' in text or '輕薄' in text or '運動'in text or '牛仔' in text or '風褸' in text or '棒球' in text or '背心' in text:
        return '299'
    elif '外套' in text or '短款西裝外套' in text:
        return '101'
