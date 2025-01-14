# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
import random
import asyncio
import os
from pyppeteer import launch
 
def initPractice1(num):
    list = []
    plusOrminus = ['+','-']
    for i in range(num):
        val1 = random.randint(100,999)
        val2 = random.randint(100,999)
        randomSymbol = plusOrminus[random.randint(0,1)]
        str = f'<li>{val1} &nbsp;{randomSymbol} &nbsp;{val2} &nbsp;=</li>'
        list.append(str)
    return list;

def initPractice2(num):
    list = []
    plusOrminus = ['+','-']
    for i in range(num):
        val1 = random.randint(0,9)
        val2 = random.randint(0,9)
        val3 = random.randint(0,9)
        val4 = random.randint(0,9)
        val5 = random.randint(0,9)
        val6 = random.randint(0,9)
        randomSymbol = plusOrminus[random.randint(0,1)] 
        str = f'''<li>
                <div class="top">
                    {val1}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{val2}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{val3}
                </div>
                <div class="middle">
                    <span>{randomSymbol}</span
                    >{val4}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{val5}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{val6}
                </div>
                <div class="down clearfix">
                    <div></div>
                    <div></div>
                    <div></div>
                </div>
                </li>'''
        list.append(str)
    return list


def generate_html(practice1,practice2):
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template('template.html')     
    with open("result.html",'w',encoding="utf-8") as fout:   
        html_content = template.render(practice1=practice1,practice2=practice2)
        fout.write(html_content)
 

async def html2pdf(fileName):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(os.path.join(os.getcwd(),"result.html"))
    await page.pdf({
        "path": "output/"+fileName+".pdf", "format": 'A4'})
    await browser.close()


if __name__ == "__main__":
    count = int(input("输入生成多少张试卷："))
    practice1Num = int(input("每张试卷 口算练习 题目数量："))
    practice2Num = int(input("每张试卷 竖式计算 题目数量："))
    for i in range(count):
        print(f"正在生成第{i+1}张试卷......")
        practice1 = initPractice1(practice1Num)
        practice2 = initPractice2(practice2Num)   
        generate_html(practice1,practice2)     
        asyncio.get_event_loop().run_until_complete(html2pdf(str(i+1)))
    print("全部生成完毕！按任意键退出程序")
    os.system('pause')
