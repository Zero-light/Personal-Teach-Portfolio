#串口数据：
raw_serial=(
    b"Test1:Voltage=3.3V,Current=0.5A\r\n"
    b"Test2:Voltage=3.4V,Current=0.6A\r\n"
    b"Test3:Voltage=3.2V,Current=0.4A\r\n"
    b"Test4:Voltage=3.5V,Current=0.7A\r\n"
)
#若为异常数据：
raw_serialB=(
    b"Test3:Voltage=3.2V,Current=0.4A\r\nTest4:Voltage=xxxV,Current=0.7A\r\n"
)

def sensor(raw_serial_data):
    try :
        str_data=raw_serial_data.decode("utf-8")
        lines=str_data.splitlines()
    except UnicodeDecodeError:
        print("数据错误")
        return None
    Usum = 0
    Isum = 0
    time=0
    for line in lines:
        try :
            linea=line.split(",")
            if len(linea)<2 :
                raise ValueError("数据格式错误，没有逗号隔开")
            lineb=linea[0].split("=")
            if len(lineb)<2:
                raise ValueError("电压数据格式错误，没有等于隔开")
            linec=float(lineb[1].replace("V",""))
            lined=linea[1].split("=")
            if len(lined)<2:
                raise  ValueError("电流数据格式错误，没有等于隔开")
            linee=float(lined[1].replace("A",""))
            Usum=Usum+linec
            Isum=Isum+linee
            time+=1
        except (ValueError,IndexError) as e:
            print(f"错误信息：{e},跳过这一行，数据有误")
            continue
    Usump=round(Usum/time,2)
    Isump=round(Isum/time,2)
    chars={
        "平均电压值":Usump,
        "平均电流值":Isump,
    }
    return chars
print(sensor(raw_serialB))
