import sys
# sys.path.append('/data/bwj/project/model-serve/novelty')
# sys.path.append('/data/bwj/project/model-serve/models')
# sys.path.append('/data/bwj/project/model-serve/services')
from novelty.compare import novelty_compare
from services.search_service import search_by_patent

def test_novelty_compare():
    sovereign_content_1 = '根据权利要求1-4任一项所述的炸药，其特征在于，所述纳米玄武岩粉的粒径为10-100nm。'
    sovereign_content_2 = '一种含某型硝酸铵的粘性炸药,其特征在于：所述粘性炸药由下述重量百分比的原料组成：多孔粒状硝酸铵50～75％,某型硝酸铵10～33％,粘结剂3～11％,轻柴油1.5～4.5％,敏化剂4～5％；所述粘结剂由下述重量份的原料组成：某型硝酸铵30～60份,聚丙烯酰胺5～6份,水30～35份；所述含某型硝酸铵的粘性炸药的制备方法包括以下步骤：(1)制备粘结剂：取30～60重量份的某型硝酸铵和5～6重量份的聚丙烯酰胺粉末溶于30～35重量份的水中混合均匀,温度控制在30～80℃；(2)制备粘性炸药：先取重量百分比为50～75％的多孔粒状/硝酸铵某型硝酸铵10～33％和1.5～4.5％的轻柴油加入混拌机中,混拌均匀；然后取重量百分比4～5％的敏化剂加入混拌机中,混拌均匀；最后取重量百分比3～11％的步骤(1)中的粘结剂,加入混拌机中,混拌均匀,形成粘性炸药。'

    start = time.time()
    review_opinion, words_info = novelty_compare(sovereign_content_2, sovereign_content_1)
    end = time.time()
    print(f"\nwords_info:\n{words_info}")
    print(f"\nreview_opinion:\n{review_opinion}")
    print("总时间：", end-start)


def compare_class_precise(classA,classB):
    # 用于对比两个专利的分数
    # classA、classB:[[main_class],[other_class_list]]
    score = 0
    # 主类对有6分，分类每有1对相似的+2分
    if classA[0][0] == classB[0][0]:
        score += 6

    for i in classA[1]:
        for j in classB[1]:
            if i == j:
                score += 2
            break
    return score

def eval_search_recall(filename):
    # 用于宏观地评价检索效果,test_search_by_patent
    scores = 0
    count = 0
    with open(filename,"r",encoding="utf-8") as f:
        rawdata = f.readlines()
        for i in range(0,len(rawdata),2):
            id_info = get_class_by_id(int(rawdata[i].rstrip("\n")))
            idlist = list(map(int,(rawdata[i+1].rstrip("\n")).split(" ")))
            for now_id in idlist:
                now_info = get_class_by_id(now_id)
                scores += compare_class_precise(id_info,now_info)
                count += 1
    print("平均检测分数：{}".format(scores/count))

def test_search_by_patent():
    patent_id_1 = 9531
    # patent_signory_list_1 = ["1.一种带粘合剂层的偏振膜，具备：偏振片与配置于该偏振片的至少单侧的粘合剂层； 该偏振片与该粘合剂层的距离为25μm以下； 该粘合剂层在580nm～610nm范围的波段具有吸收峰，且 该粘合剂层包含下述通式(I)或通式(II)所示化合物X：    S-CH3…(b) 式(I)中，R1、R2、R3、R4、R5、R6、R7及R8分别独立为氢原子、卤素原子、碳数1以上且20以下的取代或未取代的烷基、式(a)所示取代基或式(b)所示取代基；或 R1与R2形成由5或6个碳原子所构成的饱和环状骨架，且R3、R4、R5、R6、R7及R8分别独立为氢原子、卤素原子(优选为Cl)、碳数1以上且20以下的取代或未取代的烷基、式(a)所示取代基或式(b)所示取代基；或 R2与R3形成由5～7个碳原子所构成的饱和环状骨架，且R1、R4、R5、R6、R7及R8分别独立为氢原子、卤素原子(优选为Cl)、碳数1以上且20以下的取代或未取代的烷基、式(a)所示取代基或式(b)所示取代基；或 R5与R6形成由5或6个碳原子所构成的饱和环状骨架，且R1、R2、R3、R4、R7及R8分别独立为氢原子、卤素原子(优选为Cl)、碳数1以上且20以下的取代或未取代的烷基、式(a)所示取代基或式(b)所示取代基；或 R6与R7形成由5～7个碳原子所构成的饱和环状骨架，且R1、R2、R3、R4、R5及R8分别独立为氢原子、卤素原子(优选为Cl)、碳数1以上且20以下的取代或未取代的烷基、式(a)所示取代基或式(b)所示取代基；或 R1与R2形成由5或6个碳原子所构成的饱和环状骨架，R5与R6形成由5或6个碳原子所构成的饱和环状骨架，且R3、R4、R7及R8分别独立为氢原子、卤素原子(优选为Cl)、碳数1以上且20以下的取代或未取代的烷基、式(a)所示取代基或式(b)所示取代基；或者， R2与R3形成由5～7个碳原子所构成的饱和环状骨架，R6与R7形成由5～7个碳原子所构成的饱和环状骨架，且R1、R4、R5及R8分别独立为氢原子、卤素原子(优选为Cl)、碳数1以上且20以下的取代或未取代的烷基、式(a)所示取代基或式(b)所示取代基； 式(II)中，R4及R8分别独立为氢原子或碳数1以上且20以下的取代或未取代的烷基。","2.根据权利要求1所述的带粘合剂层的偏振膜，其中，所述偏振片为聚乙烯醇系偏振片。","3.根据权利要求1所述的带粘合剂层的偏振膜，其中，所述偏振片与所述粘合剂层直接层叠。","4.根据权利要求1所述的带粘合剂层的偏振膜，其中，所述偏振片的氧气透过率为1[cm3/(m2·24h·atm)]以下。","5.根据权利要求1所述的带粘合剂层的偏振膜，其中，所述粘合剂层的厚度为25μm以下。","6.一种图像显示设备，具备权利要求1所述的带粘合剂层的偏振膜。"]
    patent_signory_list_1 = [
        "1.一种带粘合剂层的偏振膜，具备：偏振片与配置于该偏振片的至少单侧的粘合剂层； 该偏振片与该粘合剂层的距离为25μm以下； 该粘合剂层在580nm～610nm范围的波段具有吸收峰，且 该粘合剂层包含下述通式(I)或通式(II)所示化合物X：    S-CH3…(b) 式(I)中，R1、R2、R3、R4、R5、R6、R7及R8分别独立为氢原子、卤素原子、碳数1以上且20以下的取代或未取代的烷基、",
        "2.根据权利要求1所述的带粘合剂层的偏振膜，其中，所述偏振片为聚乙烯醇系偏振片。",
        "3.根据权利要求1所述的带粘合剂层的偏振膜，其中，所述偏振片与所述粘合剂层直接层叠。",
        "4.根据权利要求1所述的带粘合剂层的偏振膜，其中，所述偏振片的氧气透过率为1[cm3/(m2·24h·atm)]以下。",
        "5.根据权利要求1所述的带粘合剂层的偏振膜，其中，所述粘合剂层的厚度为25μm以下。",
        "6.一种图像显示设备，具备权利要求1所述的带粘合剂层的偏振膜。"]
    
    # patent_id_2 = 562
    # patent_signory_list_2 = ["1、一种烟花鞭炮火药彩光氧化剂，其特征在于由下列重量份额的原料混合制成：高氯酸钾30-80、硝酸钡10-40、阻燃剂10-30。"]
    idlist_1 = search_by_patent(patent_signory_list_1)
    print("origin_id:{},search_top3_id:{}".format(patent_id_1,idlist_1[0:3]))


if __name__ == '__main__':
    # load_model()
    # test_get_sig_by_id()
    #  models.init_app()
    # test_signory_item_analysis()
    # test_novelty_compare()
    test_search_by_patent()
    # test_mysql()
