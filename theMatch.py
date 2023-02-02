import math
def letsMatchIt(posList1, posList2):
  c4list = 0
  firstVectyXY = []
  secondVectyXY = []
  for element in range(len(posList1)):
      if c4list < 2:
          firstVectyXY.append(posList1[element])
          secondVectyXY.append(posList2[element])
      if c4list < 3:
          c4list += 1
      else: 
          c4list = 0
  firstVectyConfidence = posList1[3::4]
  firstVectyConfidenceSum = sum(firstVectyConfidence)
  # Part1
  part1 = 1 / firstVectyConfidenceSum

  # Part2
  part2 = 0

  for i in range(len(firstVectyXY)):
    tempConf = math.floor(i/2)
    tempSum = firstVectyConfidence[tempConf] * abs(firstVectyXY[i] - secondVectyXY[i])
    part2 = part2 + tempSum

  return part1 * part2


listy1 = [0.347261518239975,0.4843164086341858,-0.23210866749286652,0.9999871253967285,0.35102683305740356,0.4788701832294464,-0.2126317024230957,0.9999710321426392,0.3543102443218231,0.47871336340904236,-0.21268761157989502,0.9999645948410034,0.3570552468299866,0.4785827100276947,-0.21273377537727356,0.999963641166687,0.3418729901313782,0.47881656885147095,-0.217511847615242,0.9999712705612183,0.3380359709262848,0.47862836718559265,-0.21750889718532562,0.999962568283081,0.33437222242355347,0.4783868193626404,-0.21748721599578857,0.9999667406082153,0.3620467185974121,0.47953179478645325,-0.0868787169456482,0.9999117851257324,0.32782164216041565,0.4791349172592163,-0.11042875796556473,0.9999527931213379,0.3527122437953949,0.48911789059638977,-0.18376915156841278,0.9999921321868896,0.3416127860546112,0.48901668190956116,-0.19038721919059753,0.9999921321868896,0.38992708921432495,0.5047857761383057,-0.007412638980895281,0.9999947547912598,0.29735055565834045,0.5082522630691528,-0.03438572585582733,0.9999629259109497,0.42616578936576843,0.5273947715759277,-0.02739701233804226,0.9864827990531921,0.2684498429298401,0.5421058535575867,-0.05451956391334534,0.9952638149261475,0.4334675073623657,0.5525950193405151,-0.2383180856704712,0.9791157841682434,0.27920234203338623,0.562523603439331,-0.22907817363739014,0.9904621243476868,0.4367920756340027,0.5602589249610901,-0.28591272234916687,0.9661985039710999,0.2858732342720032,0.5707036256790161,-0.2723466157913208,0.9791356921195984,0.4312777817249298,0.5584313869476318,-0.31252455711364746,0.9693078398704529,0.2920549511909485,0.566948413848877,-0.2938956916332245,0.9800779819488525,0.42847830057144165,0.5561414361000061,-0.2533511221408844,0.9593402147293091,0.2917978763580322,0.5640013813972473,-0.23996341228485107,0.972527265548706,0.3734802305698395,0.5840979218482971,0.0023243941832333803,0.9999771118164062,0.3219791650772095,0.586273193359375,-0.0021254110615700483,0.9998205304145813,0.3758563995361328,0.6399040222167969,-0.12351880222558975,0.9864138960838318,0.3391142189502716,0.6452522277832031,0.005254446528851986,0.8966791033744812,0.36084091663360596,0.6963038444519043,-0.03426128625869751,0.9665547609329224,0.34701773524284363,0.6512172818183899,0.36034905910491943,0.27152541279792786,0.35740938782691956,0.7039043307304382,-0.029712099581956863,0.7962834239006042,0.3501755893230438,0.6502758264541626,0.39401161670684814,0.20336918532848358,0.3629675507545471,0.7118914127349854,-0.14348722994327545,0.9562666416168213,0.3499341607093811,0.6657222509384155,0.3499314785003662,0.3670654296875]
listy2 = [0.3855326473712921,0.4222719073295593,-0.23525835573673248,0.9999863505363464,0.390018492937088,0.4183308482170105,-0.22191660106182098,0.9999643564224243,0.3929460346698761,0.41836801171302795,-0.22195518016815186,0.9999586939811707,0.3948371708393097,0.4184041917324066,-0.22198544442653656,0.9999557733535767,0.3815249800682068,0.4180811643600464,-0.21877886354923248,0.9999653100967407,0.37886521220207214,0.4179566502571106,-0.21876661479473114,0.9999566078186035,0.3764101266860962,0.41786932945251465,-0.21876220405101776,0.999961256980896,0.39845311641693115,0.41978955268859863,-0.1276596039533615,0.9999107718467712,0.3732537627220154,0.4191862940788269,-0.11565694212913513,0.9999423027038574,0.3903805911540985,0.42683762311935425,-0.1990421563386917,0.9999909996986389,0.38034188747406006,0.42686381936073303,-0.19563820958137512,0.9999908804893494,0.4242350459098816,0.4426209330558777,-0.08214055001735687,0.9999943375587463,0.3515015244483948,0.44239094853401184,-0.011764207854866982,0.9999656677246094,0.4524746835231781,0.4641138017177582,-0.0818365067243576,0.9877631664276123,0.3304654061794281,0.4589373469352722,0.07381250709295273,0.9948551654815674,0.43955889344215393,0.4786101281642914,-0.1877511888742447,0.9809611439704895,0.32081878185272217,0.47729599475860596,0.019573351368308067,0.9906250238418579,0.43406617641448975,0.48379188776016235,-0.21517090499401093,0.9684047698974609,0.3187955319881439,0.4846574068069458,0.006007519084960222,0.9791461825370789,0.4292486011981964,0.480294793844223,-0.23035316169261932,0.9712202548980713,0.32254937291145325,0.4841000735759735,-0.01475286204367876,0.9802612066268921,0.42992180585861206,0.4779840409755707,-0.19441743195056915,0.9615073204040527,0.32474997639656067,0.4823371171951294,0.010941192507743835,0.9730949401855469,0.4159476161003113,0.5017317533493042,-0.022806478664278984,0.9999558925628662,0.37379562854766846,0.504276692867279,0.022784840315580368,0.9998378753662109,0.4233677089214325,0.5430079698562622,0.0065089683048427105,0.9830061197280884,0.35898521542549133,0.5466307401657104,-0.11460345983505249,0.9061127305030823,0.4219336211681366,0.5358014702796936,0.37410032749176025,0.8949908018112183,0.3923592269420624,0.5894510746002197,-0.014757068827748299,0.3425562083721161,0.41995447874069214,0.5365116596221924,0.4103618264198303,0.739534318447113,0.405523419380188,0.595429003238678,-0.009853128343820572,0.27634528279304504,0.4156576693058014,0.5466049313545227,0.3868098855018616,0.9020872712135315,0.3684108853340149,0.6046980619430542,-0.09510830789804459,0.4279663562774658]
listy3 = [0.3536307215690613,0.4287536144256592,-0.3091026246547699,0.9999876618385315,0.35908201336860657,0.4238418638706207,-0.28978821635246277,0.9999676942825317,0.36266279220581055,0.423747718334198,-0.28979235887527466,0.9999624490737915,0.3656448423862457,0.4237179160118103,-0.2898447513580322,0.9999596476554871,0.34840142726898193,0.4238761365413666,-0.29192596673965454,0.9999686479568481,0.34499871730804443,0.4237958490848541,-0.29194995760917664,0.9999607801437378,0.3419742286205292,0.4239223897457123,-0.2920099198818207,0.9999650120735168,0.36982813477516174,0.4253716468811035,-0.16641421616077423,0.9999192953109741,0.33938902616500854,0.42561373114585876,-0.17907395958900452,0.9999479055404663,0.36010605096817017,0.4342721104621887,-0.26197123527526855,0.9999918341636658,0.3484356701374054,0.43432390689849854,-0.2659897804260254,0.999991774559021,0.3994809091091156,0.45340484380722046,-0.07733222097158432,0.999994158744812,0.306582510471344,0.4594133198261261,-0.09781806170940399,0.9999681115150452,0.4338446259498596,0.4739052951335907,0.0044896965846419334,0.9884443283081055,0.27058494091033936,0.49294450879096985,-0.19026991724967957,0.9950541257858276,0.4388846457004547,0.5015502572059631,-0.05129430443048477,0.9816620349884033,0.2772805094718933,0.4952792227268219,-0.4375104308128357,0.9912750124931335,0.4383769929409027,0.5109411478042603,-0.06406135112047195,0.9686600565910339,0.27888739109039307,0.49550023674964905,-0.4833138585090637,0.9805840849876404,0.43177860975265503,0.5097629427909851,-0.08581624180078506,0.9712027311325073,0.2864750921726227,0.4905785322189331,-0.4918835759162903,0.9816088676452637,0.4303715229034424,0.5067523717880249,-0.05797543004155159,0.9614257216453552,0.28839555382728577,0.49005600810050964,-0.4443773925304413,0.9747243523597717,0.3891851305961609,0.5282992720603943,-0.005547757726162672,0.9999573826789856,0.33950087428092957,0.5315786004066467,0.0053201173432171345,0.9998530745506287,0.3983156979084015,0.5860679149627686,-0.047177791595458984,0.9840158820152283,0.3351157009601593,0.5896380543708801,-0.08210749179124832,0.9128792881965637,0.39600157737731934,0.5980051159858704,0.3652576506137848,0.8836714625358582,0.3680824637413025,0.6272726058959961,0.15800635516643524,0.4049026072025299,0.3924150764942169,0.5964193344116211,0.404354989528656,0.7221361398696899,0.3715342879295349,0.6270831227302551,0.1782689243555069,0.32814767956733704,0.4028203785419464,0.6244328022003174,0.3527149260044098,0.8943436145782471,0.3684029281139374,0.6517199873924255,0.06994113326072693,0.4799171984195709]
listy4 = [0.39289528131484985,0.4120579659938812,-0.10331958532333374,0.9997755289077759,0.3957519233226776,0.40665531158447266,-0.10047335922718048,0.9996299743652344,0.39702168107032776,0.40664684772491455,-0.10055456310510635,0.9996519684791565,0.3982306122779846,0.4066632390022278,-0.10057264566421509,0.9996582865715027,0.3913979232311249,0.4063427150249481,-0.10755311697721481,0.9995631575584412,0.38890719413757324,0.406145840883255,-0.10760094970464706,0.9995120763778687,0.385981947183609,0.4060114026069641,-0.10766241699457169,0.9994927644729614,0.3974921703338623,0.4083915054798126,-0.062476251274347305,0.9995133280754089,0.3804776966571808,0.4091527760028839,-0.09709683060646057,0.9991025328636169,0.3942529559135437,0.41740715503692627,-0.086009681224823,0.9996962547302246,0.38843703269958496,0.4171909987926483,-0.09622761607170105,0.9996094107627869,0.34636756777763367,0.4534178376197815,-0.056383196264505386,0.9998971223831177,0.3555562496185303,0.4372048079967499,-0.06925950199365616,0.9941811561584473,0.3777840733528137,0.4750227630138397,-0.06416193395853043,0.9784053564071655,0.3233259916305542,0.46059226989746094,-0.3923892080783844,0.9326543807983398,0.36192888021469116,0.490408718585968,-0.11902688443660736,0.9563747048377991,0.3110058009624481,0.47411900758743286,-0.43443211913108826,0.9539254903793335,0.3289329707622528,0.4867643117904663,-0.13580891489982605,0.9273493885993958,0.30834734439849854,0.4847143590450287,-0.4872989058494568,0.9416768550872803,0.32851019501686096,0.484901487827301,-0.14514584839344025,0.9284653067588806,0.31523188948631287,0.4834452271461487,-0.399762898683548,0.942269504070282,0.3319636881351471,0.48191601037979126,-0.1228461042046547,0.9214394092559814,0.31853750348091125,0.4808213412761688,-0.4197591543197632,0.93072110414505,0.33633607625961304,0.528580367565155,0.0036134852562099695,0.9995384216308594,0.3360186219215393,0.5293545722961426,-0.0036420943215489388,0.999688446521759,0.3638574182987213,0.5437889099121094,0.094340480864048,0.9438280463218689,0.35760045051574707,0.5402606129646301,-0.07678582519292831,0.8654518723487854,0.40704837441444397,0.5850648283958435,0.15194876492023468,0.7818995118141174,0.4094955623149872,0.5754538178443909,-0.09418656677007675,0.437228798866272,0.41051802039146423,0.5979817509651184,0.12043142318725586,0.6538931727409363,0.41062262654304504,0.5860453844070435,-0.11316022276878357,0.38304391503334045,0.40741196274757385,0.5949534177780151,0.017582973465323448,0.8149229288101196,0.4037313163280487,0.5915915369987488,-0.15178945660591125,0.517521858215332]
# print(len(listy1))
# print(len(listy2))
theMatch = letsMatchIt(listy1,listy3)

print(theMatch)