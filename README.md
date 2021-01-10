# appgallery-download-info
Get download info of specific app in AppGallery

# usage

1. Create a csv file with AppID of apps to be scraped, named as `input.csv`

e.g.
| appID |  |
|  ----  | --- |
C101451473
C101451474
C101451475
C102670299
C100180977
C101707381
C101257589

2. Execute 
`python3 main.py input.csv`

3. Result will be stored in `output.csv`

# result preview
|appID|appName|versionNumber|packageName|downloads|appUrl|iconUrl|
| - | - |- |- |- |- |- |
|C101451473|DualSpace|3.2.6|com.ludashi.dualspace|"1,513 万次安装"|https://appgallery.cloud.huawei.com/ag/n/app/C101451473?locale=zh_CN&source=appshare&subsource=C101451473|https://appimg2.dbankcdn.com/application/icon144/c11c9d61ff214596bcc95f9355421085.png|
|C101451474|App not exists|||||
|C101451475|App not exists|||||
|C102670299|"Plex: Stream Free Movies, Shows, Live TV & more"|8.11.0.22186|com.plexapp.android|46 万次安装|https://appgallery.cloud.huawei.com/ag/n/app/C102670299?locale=zh_CN&source=appshare&subsource=C102670299|https://appimg2.dbankcdn.com/application/icon144/65/f593a411e1504b8c8ddf80ece147db8f.png
|C100180977|Snaptube|5.06.0.5065510|com.snaptube.premium|"5,066 万次安装"|https://appgallery.cloud.huawei.com/ag/n/app/C100180977?locale=zh_CN&source=appshare&subsource=C100180977|https://appimg2.dbankcdn.com/application/icon144/fe44ceca1df6454aa9cc62da2af4fae6.png
|C101707381|Banca Móvil BAC Credomatic|5.8.0|net.bac.sbe.android|144 万次安装|https://appgallery.cloud.huawei.com/ag/n/app/C101707381?locale=zh_CN&source=appshare&subsource=C101707381|https://appimg2.dbankcdn.com/application/icon144/10119/e24a6bf441d1456a96c256affb65dc1d.png
|C101257589|Hugo - Lo mejor de tu ciudad en minutos|2.81.3|com.hugoapp.client|31 万次安装|https://appgallery.cloud.huawei.com/ag/n/app/C101257589?locale=zh_CN&source=appshare&subsource=C101257589|https://appimg2.dbankcdn.com/application/icon144/10119/6787414d998b4d4c88b46dfa78374dea.png
