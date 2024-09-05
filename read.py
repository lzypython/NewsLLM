import os
import json
# import demjson
import ast
def addjson(directory,file):
    path = os.path.join(directory,file)
    with open(path, 'r') as f:  
        data = f.readlines()
    b_data = []  
    for item in data:
        # 解析 JSON 对象 
        try:
            json_line = json.loads(item.strip())  
            # 过滤
            if(json_line["source"]=="111新浪微博"):
                pass
            else:
                 conversation = {  
            # "system": "",  # 可以根据需要修改  
            # "input": "",  # A格式的title  
            "text": json_line["content"]  # A格式的content  
                 }  
                 b_data.append(conversation) 
        except Exception as e:
            pass
        # 保存为JSONL文件  
    with open('dataText.json', 'a', encoding='utf-8') as f:  
        # for entry in b_data:
            # print(entry)
            # f.write(json.dumps(entry, ensure_ascii=False, indent=4) +'\n')  
            # print("1")
        json.dump(b_data, f, ensure_ascii=False,indent=4)  # indent=4 使输出更美观
        
def data2json(directory):
       try:  
        files = os.listdir(directory)  
        # 过滤出文件（排除文件夹）  
        files = [f for f in files if os.path.isfile(os.path.join(directory, f))]  
        first_files = files  
        # 打印文件名  
        for file in first_files:  
            addjson(directory,file)  
       except Exception as e:  
           print(f"发生错误: {e}")  

data2json("../NewsLLM")
print("OK")