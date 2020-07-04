import json
import os
import linecache

def read_whitelist():
    nono = 0
    try:
        os.mkdir("Snap")
    except:
        pass

    json_filename = 'Server_Download\whitelist.json'
    txt_filename = 'Snap\whitelist.txt'
    file=open(txt_filename,'w')
    with open(json_filename) as check:
        check2 = check.read()
        if check2 =='[]\n':
            return False
        check.close()
    with open(json_filename) as f:
        pop_data = json.load(f)
        last_whitelist = pop_data[len(pop_data)-1]
        del pop_data[len(pop_data)-1]
        print(type(last_whitelist))
        for pop_dict in pop_data:
            ignoresPlayerLimit_id = pop_dict['ignoresPlayerLimit']
            name_id = pop_dict['name']
            xuid_id = pop_dict['xuid']
            temp = str(name_id) + ';' + str(xuid_id) + ';' + str(ignoresPlayerLimit_id)
            file.write(temp + '\n')  
        ignoresPlayerLimit_id = last_whitelist['ignoresPlayerLimit']
        name_id = last_whitelist['name']
        xuid_id = last_whitelist['xuid']
        temp = str(name_id) + ';' + str(xuid_id) + ';' + str(ignoresPlayerLimit_id)
        file.write(temp)       
        file.close()
        return True

def write_whitelist():
    #temp_dict = {}
    result = []
    submit = 'Snap\\whitelist.json'
    
    try:
        os.mkdir("Snap")
    except:
        pass
    for line in open('Snap\whitelist.txt'):
        temp_dict = {}
        line = line.replace('\n', '').replace('\r', '')
        if line.endswith("False"):
            line = line.replace('False', 'false')
        elif line.endswith("True"):
            line = line.replace('True', 'true')
        xuid = ''
        white_name = line.partition(';')[0]
        ignoresPlayerLimit_id = line.rpartition(';')[2]
        del_name_id = line.find(';')
        del_ignore_id = line.rfind(';')
        for i in range(0,len(line)):
             if i > del_name_id and i < del_ignore_id:
                 xuid = xuid + line[i]
        temp_dict['ignoresPlayerLimit'] = ignoresPlayerLimit_id
        temp_dict['name'] = white_name
        temp_dict['xuid'] = xuid
        result.append(temp_dict)
        #print(result)

    with open(submit, 'w') as f:
        json.dump(result, f)
    with open(submit, 'r+') as f:
        f = f.read().replace(r' "false"', 'false').replace(r' "true"', 'true')
        with open(submit, 'w') as d:
            d.write(f)

def add_whitelist(name, ignore='false', xuid=' '):
    name = str(name)
    xuid = str(xuid)
    ignore = str(ignore)
    try:
        os.mkdir("Snap")
    except:
        pass
    with open('Snap/whitelist.txt', 'a') as f:
        f.write('\n' + name + ';' + xuid + ';' + ignore)

def del_whitelist(name):
    name = str(name)
    with open('Snap\whitelist.txt','r') as r:
        lines=r.readlines()
    with open('Snap\whitelist.txt','w') as w:
        for l in lines:
            if name not in l:
                w.write(l)
    # 删除空行
    count = len(open('Snap\whitelist.txt', 'r').readlines())
    print(count)
    file1 = open('Snap\whitelist.txt', 'r', encoding='utf-8') 
    file2 = open('Snap\whitelist2.txt', 'w', encoding='utf-8')
    try:
        for line in file1.readlines():
            if line == '\n':
                line = line.strip("\n")
            file2.write(line)
    finally:
        file1.close()
        file2.close()
        os.remove('Snap\whitelist.txt')
        os.rename('Snap\whitelist2.txt','Snap\whitelist.txt')

if __name__ == "__main__":
    pass
    #del_whitelist('Dameng23333')
    #write_whitelist()
    #read_whitelist()
    #add_whitelist('Eltrac')
    #if read_whitelist() == False:
    #    print('空列表')
    #else:
    #    pass