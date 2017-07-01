# py2_spider
scrapy

## 项目简介
  本项目是基于python2.7，利用scrapy框架来开发的爬虫项目。其中dangdang是对当当网某一类商品进行翻页爬取，sohunews是利用scrapy框架中的CrawlSpider模板自动爬取搜狐新闻网站中的新闻，baike是爬取某一关键词在百度百科进行全站搜索的数据，jingdong是对京东某一类商品进行爬取。

## 项目环境搭建
  项目开发操作系统为64位win7。由于执行命令`pip install scrapy`安装scrapy出现错误，故采用了`conda install scrapy`安装。conda可通过[清华镜像源](https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/)选择Miniconda2-latest-Windows-x86.exe来安装。通过以下两条指令修改conda下载源
  > conda config --add channels 'https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/'
  
  > conda config --set show_channel_urls yes
  
  * baike和jingdong项目所需的随机客户端安装参考：<https://github.com/SaberAlexander/scrapy-useragent>
  
  * jingdong项目所需的splash安装参考：<https://github.com/scrapinghub/splash>
      * 由于操作系统为64位win7，splash安装所需的容器可通过[阿里云](http://mirrors.aliyun.com/docker-toolbox/windows/docker-toolbox/)选择DockerToolbox-17.05.0-ce.exe下载。在Docker中安装splash，启动Docker Quickstart Terminal执行命令：`docker pull scrapinghub/splash`，由于docker images源在国外，下载的时候非常慢，可通过VPN或镜像仓库。本项目是通过DaoCloud镜像仓库来下载，详细步骤见网址：<http://guide.daocloud.io/dcs/daocloud-9153151.html#docker-toolbox>。通过Docker Quickstart Terminal执行命令：`docker run -p 5023:5023 -p 8050:8050 -p 8051:8051 scrapinghub/splash`来启动splash服务，运行jingdong爬虫的过程中要一直开启该服务。（Docker的终端不支持windows下的复制、粘贴的快捷键，防止命令输错，可通过在程序窗口最上方右键，选择”编辑”，可看到粘贴选项）

## 项目操作
* dangdang
    * 在当前项目目录的终端中执行命令：`scrapy crawl dangdangspd`，爬取成功后数据会保存在当前目录`mydata.json`文件中。
* sohunews
    * 在当前项目目录的终端中执行命令：`scrapy crawl sohunewsspd`，爬取成功后数据会保存在当前目录`mydata.json`文件中。
* baike
    * 在当前项目目录的终端中执行命令：`scrapy crawl baikespd`，根据spiders/baikespd.py中变量keyword的值在百度百科进行全站搜索，爬取成功后数据会保存在当前目录`mydata.json`文件中。
    * 在当前项目目录的终端中执行命令：`scrapy crawl baikespd -a search=xxx`，可在百度百科对关键词`xxx`进行全站搜索，爬取成功后数据会保存在当前目录`mydata.json`文件中。
* jingdong
    * 在当前项目目录/myproject/的终端中执行命令：`scrapy crawl jditems`，爬取成功后数据会保存在当前目录`JD_items.json`文件和`JD_items.jl`中。jingdong/JD_comments/JD_comments/spiders/ JD_comments.py为爬虫项目评价详情的爬虫文件，主要提取`JD_items.json`文件中商品的评价详情，生成`JD_ comments.json`文件和`JD_ comments.jl`文件；jingdong/ JD_summarys/ JD_summarys/spiders/ JD_summary.py为爬虫项目评价总结的爬虫文件，主要提取`JD_items.json`文件中商品的评价总结，生成`JD_summarys.json`文件和`JD_summarys.jl`文件。
