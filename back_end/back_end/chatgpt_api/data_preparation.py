import os
import pandas as pd
import json


def prepare_dataset():
    def transform_json_dict(json_dict):
        contents={}
        for name,content in json_dict.items():
            if name in ['title','abstract']:
                contents[name]=content
            elif name=='text':
                for text_dict in content:
                    for subname,subcontent in text_dict.items():
                        if subname=='section':
                            section=subcontent
                        if subname=='strings':
                            text=subcontent
                            # 0523 should delete
                    # if section == 'Introduction':
                    contents[section]=text
    
        return contents

    def findAllFile(base):
        for root, ds, fs in os.walk(base):
            for f in fs:
                #if f.endswith('.json'):
                num=f.split(".")[0]
                fullname = os.path.join(root, f)
                yield num, fullname


    json_base = './DATASET/json/'
    targets_base = './DATASET/targets/'

    json_names=[]
    json_path_names=[]
    targets_names=[]
    targets_path_names=[]

    for num, path in findAllFile(json_base):
        json_names.append(num)
        json_path_names.append(path)
    for num, path in findAllFile(targets_base):
        targets_names.append(num)
        targets_path_names.append(path)

    assert len(json_names)==len(set(json_names)),"有重名文件"
    assert len(targets_names)==len(set(targets_names)),"有重名文件"
    assert set(json_names) == set(targets_names),"json 和 targets没有一一对应"

    data={
        "source":[],
        "target":[],
    }


    for num ,json_path,targets_path in zip(json_names, json_path_names,targets_path_names):

        json_file = json.load(open(json_path))
        targets_file = open(targets_path,encoding='utf-8')
        json_content = transform_json_dict(json_file)
        targets_content  = targets_file.read()
        data['source'].append(json_content)
        data['target'].append(targets_content)
        

    return data

# from .utils.chatgpt_utils import num_tokens_from_messages
from chat_model import ChatModel
if __name__ == '__main__':
    chat_model = ChatModel()


    data = prepare_dataset()
    # source里面有13段
    print(data['source'][0].keys())
    # target里面有7段
    print(len(data['target'][0].split('\n')))
    print(data['target'][0].split('\n')[-1])

    
    chat_model.add_system_message("TL;DR")
    chat_model.add_example_question(data['source'][0]['Introduction'])
    
    print(chat_model.num_tokens)
    chat_model.add_example_answer(data['target'][0].split('\n')[0])

    print(chat_model.num_tokens)

    # chat_model.add_user_question(data['source'[0]])