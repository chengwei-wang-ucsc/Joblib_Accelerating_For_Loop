import pandas as pd
import talib

def get_factors(index,opening,closing,highest,lowest,volume,rolling=30,normalization=True, drop=False):

    tmp = pd.DataFrame()
    tmp['AD'] = talib.AD(highest, lowest, closing, volume)
    tmp['ADOSC'] = talib.ADOSC(highest, lowest, closing, volume, fastperiod=3, slowperiod=10)
    tmp['ADX_5'] = talib.ADX(highest, lowest, closing, timeperiod=5)
    tmp['ADX_13'] = talib.ADX(highest, lowest, closing, timeperiod=13)
    tmp['APO'] = talib.APO(closing, fastperiod=12, slowperiod=26)
    tmp['AROONDown_5'], tmp['AROONUp_5'] = talib.AROON(highest, lowest, timeperiod=5)
    tmp['AROONDown_13'], tmp['AROONUp_13'] = talib.AROON(highest, lowest, timeperiod=13)
    
    tmp['AROONOSC_5'] = talib.AROONOSC(highest, lowest, timeperiod=5)
    tmp['AROONOSC_13'] = talib.AROONOSC(highest, lowest, timeperiod=13)
    tmp['ATR5'] = talib.ATR(highest, lowest, closing, timeperiod=5)
    tmp['ATR13'] = talib.ATR(highest, lowest, closing, timeperiod=13)
    tmp['TSF5'] = talib.TSF(closing, timeperiod=5)
    tmp['TSF13'] = talib.TSF(closing, timeperiod=13)
    tmp['WILLR5'] = talib.WILLR(highest, lowest, closing, timeperiod=5)
    tmp['WILLR13'] = talib.WILLR(highest, lowest, closing, timeperiod=13)
    tmp['WCLPRICE'] = talib.WCLPRICE(highest, lowest, closing)
    tmp['HT_DCPERIOD'] = talib.HT_DCPERIOD(closing)
    tmp['HT_DCPHASE'] = talib.HT_DCPHASE(closing)
    tmp['inphase'], tmp['quadrature'] = talib.HT_PHASOR(closing)
    tmp['sine'], tmp['leadsine'] = talib.HT_SINE(closing)
    
    tmp['close'] = closing
    tmp['high'] = highest
    tmp['low'] = lowest
    tmp['open'] = opening
    tmp['volume'] = volume

    if normalization:
        factors_list = tmp.columns.tolist()[1:]
        for i in factors_list:
            tmp[i] = (tmp[i]-tmp[i].rolling(window=rolling,center=False).mean())/tmp[i].rolling(window=rolling,center=False).std()
    if drop:
        tmp.dropna(inplace=True)
    return tmp