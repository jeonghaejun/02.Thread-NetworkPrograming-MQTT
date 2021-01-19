import json

dic = {
    'file_name': 'C:/Users/wjdgo/iot_workspace/02.Thread,NetworkPrograming,MQTT/02.NetworkPrograming/ShopDB.sql',
    'file_size': 172
}

l = [dic, dic]
list_msg = json.dumps(l)
print(type(list_msg))
print(list_msg)

l2 = json.loads(list_msg)
print(type(l2))
print(l2)
