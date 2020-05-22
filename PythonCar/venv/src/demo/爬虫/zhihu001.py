# -*- coding: UTF-8 -*-
import os,requests,json,re
import util

mainUrl='https://www.zhihu.com/api/v4/questions/37787176/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset={}&platform=desktop&sort_by=default'
dirPath = 'zhihu001/'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                  'AppleWebKit/537.36 (KHTML, '
                  'like Gecko) Chrome/67.0.3396.99 '
                  'Safari/537.36',
    'Host': "www.zhihu.com",
    'Referer': "https://www.zhihu.com/question/37787176"
}

# 请求图片时使用的header
header1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                  'AppleWebKit/537.36 (KHTML, '
                  'like Gecko) Chrome/67.0.3396.99 '
                  'Safari/537.36',
    'Referer': "https://www.zhihu.com/question/37787176"
}



def answer(url_):
    r = requests.get(url_, headers=header)
    data = r.text
    jsonobj = json.loads(data)
    return jsonobj


#  下载网页html内容
def download_page(url):
    r = requests.get(url,header)
    r.encoding = 'utf-8'
    return r.text

def main():
    util.create_pic_dir(dirPath)

    # 获取回答总数
    res = answer(mainUrl.format('0'))
    answer_total = int(res['paging']['totals'])
    print('共{}个回答'.format(answer_total))
    offset = 0
    while offset < answer_total:
        offsetStr = str(offset)
        url2 = mainUrl.format(offsetStr)
        res = answer(url2)
        offset += 500
        data = res['data']
        for index,data2 in enumerate(data):
            answerContent = data2['content']
            imagelinks = re.findall('src=\"(https://.*?)"',answerContent)
            for link in imagelinks:
                imageName = link.split('/')[-1]
                r = requests.get(link, headers=header1)
                imagePath = dirPath + imageName
                with open(imagePath,'wb') as f:
                    f.write(r.content)

    print('爬取结束')
if __name__ == '__main__':
    main()