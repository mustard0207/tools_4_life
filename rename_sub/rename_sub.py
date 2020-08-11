#rename.py
import os
import re
import time

work_path = 'Y:\\电视剧\\绝命毒师\\Breaking Bad Season 5  (2160p x265 10bit Joy)' #工作目录

def set_Work_Path():
    #设置工作文件夹路径
    return work_path


def get_File_List(work_path):
    #获取文件夹的所有文件列表
    file_list = os.listdir(work_path)
    return file_list

def get_Video_List(file_list):
    video_list = []
    for file_name in file_list:
        #匹配mkv视频
        if re.match('.*\.mkv$', file_name, re.I):
            video_list.append(file_name)
            # print(video_list)

    return video_list

def get_Sub_List(file_list):
    sub_list = []
    for file_name in file_list:
        #匹配ass或srt字幕
        if re.match('.*\.[as][sr][st]$', file_name, re.I):
            sub_list.append(file_name)

    return sub_list

def change_filename(origin_name, new_name):
    #修改文件名
    os.rename(origin_name, new_name)
    print( origin_name + ' -------> ' + new_name + ' done !')
    #增加文件修改记录
    f = open('History_Filename.txt','a')
    f.write(origin_name + ',' + new_name + ',' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '\n')
    f.close()

def mode_Subtile(video_list, sub_list):
    #开始匹配视频对应的字幕并修改文件名
    for file_video in video_list:
        #根据剧集号来匹配 ex；S01E01
        match_video_file = re.match('^(\w.*)([s]\d\d[e]\d\d).*\.mkv$', file_video, re.I)
        if match_video_file:
            # print('匹配到视频文件: ' + file_video)
            
            name_file = match_video_file.group()
            name_video = match_video_file.group(1)
            num_video = match_video_file.group(2)
            # print(name_video)
            # print(num_video)

            #匹配字幕文件
            for file_sub in sub_list:
                match_sub_file = re.match('^(\w.*)([s]\d\d[e]\d\d).*\.([as][sr][st])$', file_sub, re.I)
                if match_sub_file:
                    if name_video == match_sub_file.group(1) and num_video == match_sub_file.group(2):
                        #找到对应的字幕文件
                        # print('视频文件: ' + match_video_file.group() + ' 的字幕已找到!')
                        # print('对应字幕文件为: ' + match_sub_file.group() + ' !')
                        
                        head_video_file = name_file[:-3]
                        orgin_name_sub = match_sub_file.group()
                        end_orgin_name_sub = orgin_name_sub[-3:]
                        new_name_sub = head_video_file + end_orgin_name_sub
 
                        #可以开始对该字幕文件名进行修改
                        change_filename(orgin_name_sub, new_name_sub)
                        #顺便从字幕列表中删掉该文件
                        sub_list.remove(file_sub)


        else:
            print('文件: ' + file_video + ' 没有匹配到剧集名及剧集号!')


def rename_sub():
    print('The Program is Staring !\n')
    up_time = time.time()

    file_list = get_File_List(work_path)
    #修改指定目录为当前工作目录
    os.chdir(work_path)
    print('当前工作目录为: ' + str(os.getcwd()) + '\n')
    video_list = get_Video_List(file_list)
    sub_list = get_Sub_List(file_list)

    mode_Subtile(video_list, sub_list)

    end_time = time.time()
    print('\nThe Program was end!')
    print('We cost ' + str(end_time - up_time))


def main():
    rename_sub()
        
if __name__ == '__main__':
    main()
