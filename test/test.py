import sys
# sys.path.append('/data/bwj/project/model-serve/novelty')
# sys.path.append('/data/bwj/project/model-serve/models')
# sys.path.append('/data/bwj/project/model-serve/services')
from novelty.compare import novelty_compare
from services.search_service import search_by_patent

def test_novelty_compare():
    sovereign_content_1 = '一种炸药，其特征在于，所述炸药包括如下重量百分比的组分：'
    sovereign_content_2 = '一种陶化剂，其特征在于，该陶化剂由下列重量比例成份组成。'
    # sovereign_content_1 = '该装置由螺钉构成。'
    # sovereign_content_2 = '螺栓构成了该装置。'
    print(novelty_compare(sovereign_content_2, sovereign_content_1))

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
