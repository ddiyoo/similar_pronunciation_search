import pandas as pd
import kiprisplus_api.functions as kf

similar_df = pd.DataFrame(columns=['applicationNumber', 'TrademarkHangeulName', 'TrademarkEnglishsentenceName','rejectionContentDetail','registrationNumber','sim_applicationNumber','sim_TrademarkHangeulName','sim_TrademarkEnglishsentenceName'])
date =pd.read_csv('date.csv')

for d in range(len(date)):
    startdate = date['start'][d]
    enddate = date['end'][d]

    readfilename = f'pre_{startdate}_{enddate}_0.csv'
    writefilename = f'sim_{startdate}_{enddate}.csv'

    raw = pd.read_csv(f'./output/{readfilename}', engine='python')  ##rejectionContentDetail
    sim_index = raw.query('칭호 ==1').index.tolist()

    for nn, s in enumerate(sim_index):
        processpoint = (int(nn) / int(len(sim_index))) * 100

        print('\033[31m' + str(startdate) + '_' + str(enddate) + ':' + "%0.1f%%" % processpoint + '\033[0m')
        applicationNumber = raw['patent_id'][s]
        TrademarkHangeulName = raw['korean'][s]
        TrademarkEnglishsentenceName = raw['english'][s]
        rejectionContentDetail = str(raw['rejectionContentDetail'][s])
        numbers = kf.extract_regiNum(rejectionContentDetail)
        sim_number = [x for x in numbers if x >= 10000 and x < 1000000]
        if sim_number != 0:
            for sn in sim_number:
                registrationNum = kf.making_registrationNumber(str(sn))

                for num in registrationNum:

                    try:
                        sim_applicationNumber = kf.collect_appliNum(num)
                        print(f'registrationNumber:{num}, applicationNumber:{sim_applicationNumber}')
                        sim_TrademarkHangeulName = kf.collect_tradName(sim_applicationNumber)[0]
                        sim_TrademarkEnglishsentenceName = kf.collect_tradName(sim_applicationNumber)[1]
                        sim_df = sim_df.append(
                            pd.DataFrame([[applicationNumber, TrademarkHangeulName, TrademarkEnglishsentenceName, rejectionContentDetail,
                                           num, sim_applicationNumber, sim_TrademarkHangeulName, sim_TrademarkEnglishsentenceName]],
                                         columns=['applicationNumber', 'trademarkHangeulName', 'trademarkEnglishsentenceName',
                                                  'rejectionContentDetail', 'registrationNumber',
                                                  'sim_applicationNumber',
                                                  'sim_trademarkHangeulName', 'sim_trademarkEnglishsentenceName']), ignore_index=True)
                        sim_df.to_csv(writefilename, header=True, index=False, encoding='euc-kr')
                    except:
                        print(f'None_registrationNumber:{num}')

