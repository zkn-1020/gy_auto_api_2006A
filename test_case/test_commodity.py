
'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''

from tools.api import request_tool


# 增加产品
def test_addProd(pub_data):
    pub_data["productCode"] = "自动生成 字符串 4 数字 geli"
    method = "POST"  #请求方法，全部大写
    feature = "第一条用例"  # allure报告中一级分类
    story = '增加产品'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    headers = {"token": pub_data["token"]} #取token
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "brand": "格力",
  "colors": [
    "白色",
    "黑色",
    "金色"
  ],
  "price": 3000,
  "productCode": "${productCode}",
  "productName": "格力君越",
  "sizes": [
    "1匹",
    "2匹",
    "3匹"
  ],
  "type": "家用电器"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)


#根据产品编码查商品
def test_getSkuByProdCode(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "第一条用例"  # allure报告中一级分类
    story = '根据产品编码查商品'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/getSkuByProdCode"  # 接口地址
    headers = {"token": pub_data["token"]}  # 取token
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    params={'prodCode': '${productCode}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)


#下架
def test_soldOut(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "第一条用例"  # allure报告中一级分类
    story = '下架'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/soldOut"  # 接口地址
    headers = {"token": pub_data["token"]}  #取token
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'productCode': '${productCode}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)


#预售
def test_toPreSale(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "第一条用例"  # allure报告中一级分类
    story = '预售'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/toPreSale"  # 接口地址
    headers = {"token": pub_data["token"]}  #取token
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'productCode': '${productCode}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)
#
# #第一条结束**********************************************************************************************************************************************************************

# 增加产品
from tools.api import request_tool


def test_addProd3(pub_data):
    pub_data["productCode"] = "自动生成 字符串 4 数字 geli"
    method = "POST"  #请求方法，全部大写
    feature = "第二条用例"  # allure报告中一级分类
    story = '增加产品'  # allure报告中二级分类
    title = "全字段正常流_2"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    headers = {"token": pub_data["token"]} #取token
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "brand": "格力",
  "colors": [
    "白色",
    "黑色",
    "金色"
  ],
  "price": 3000,
  "productCode": "${productCode}",
  "productName": "格力君越",
  "sizes": [
    "1匹",
    "2匹",
    "3匹"
  ],
  "type": "家用电器"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)


#根据产品编码查商品
def test_getSkuByProdCode3(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "第二条用例"  # allure报告中一级分类
    story = '根据产品编码查商品'  # allure报告中二级分类
    title = "全字段正常流_2"  # allure报告中用例名字
    uri = "/product/getSkuByProdCode"  # 接口地址
    headers = {"token": pub_data["token"]}  # 取token
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    params={'prodCode': '${productCode}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)


#修改产品价格
def test_changePriceByProdCode(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "第二条用例"  # allure报告中一级分类
    story = '修改产品价格'  # allure报告中二级分类
    title = "全字段正常流_2"  # allure报告中用例名字
    uri = "/product/changePriceByProdCode"  # 接口地址
    headers = {"token": pub_data["token"]}  # 取token
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'price': '2888', 'prodCode': '${productCode}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)

#根据产品编码查商品
def test_getSkuByProdCode4(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "第二条用例"  # allure报告中一级分类
    story = '根据产品编码查商品'  # allure报告中二级分类
    title = "全字段正常流_2"  # allure报告中用例名字
    uri = "/product/getSkuByProdCode"  # 接口地址
    headers = {"token": pub_data["token"]}  # 取token
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    params={'prodCode': '${productCode}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)

# #第二条结束**********************************************************************************************************************************************************************

# 增加产品
from tools.api import request_tool


def test_addProd6(pub_data):
    pub_data["productCode"] = "自动生成 字符串 4 数字 geli"
    method = "POST"  #请求方法，全部大写
    feature = "第三条用例"  # allure报告中一级分类
    story = '增加产品'  # allure报告中二级分类
    title = "全字段正常流_3"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    headers = {"token": pub_data["token"]} #取token
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "brand": "格力",
  "colors": [
    "白色",
    "黑色",
    "金色"
  ],
  "price": 3000,
  "productCode": "${productCode}",
  "productName": "格力君越",
  "sizes": [
    "1匹",
    "2匹",
    "3匹"
  ],
  "type": "家用电器"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)


#根据产品编码查商品
def test_getSkuByProdCode6(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "第三条用例"  # allure报告中一级分类
    story = '根据产品编码查商品'  # allure报告中二级分类
    title = "全字段正常流_3"  # allure报告中用例名字
    uri = "/product/getSkuByProdCode"  # 接口地址
    headers = {"token": pub_data["token"]}  # 取token
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    params={'prodCode': '${productCode}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)

#修改商品价格
def test_changePrice(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "第三条用例"  # allure报告中一级分类
    story = '修改商品价格'  # allure报告中二级分类
    title = "全字段正常流_3"  # allure报告中用例名字
    uri = "/product/changePrice"  # 接口地址
    headers = {"token": pub_data["token"]}  # 取token
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'SKU': 'geli7160_白色_1匹', 'price': '3000'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)


#查询单个商品
def test_getSKU(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "第三条用例"  # allure报告中一级分类
    story = '查询单个商品'  # allure报告中二级分类
    title = "全字段正常流_3"  # allure报告中用例名字
    uri = "/product/getSKU"  # 接口地址
    headers = {"token": pub_data["token"]}  # 取token
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    params={'SKU': 'geli7160_白色_1匹'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)


# #第三条结束**********************************************************************************************************************************************************************

# 增加产品
from tools.api import request_tool


def test_addProd7(pub_data):
    pub_data["productCode"] = "自动生成 字符串 4 数字 geli"
    method = "POST"  #请求方法，全部大写
    feature = "第四条用例"  # allure报告中一级分类
    story = '增加产品'  # allure报告中二级分类
    title = "全字段正常流_4"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    headers = {"token": pub_data["token"]} #取token
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "brand": "格力",
  "colors": [
    "白色",
    "黑色",
    "金色"
  ],
  "price": 3000,
  "productCode": "${productCode}",
  "productName": "格力君越",
  "sizes": [
    "1匹",
    "2匹",
    "3匹"
  ],
  "type": "家用电器"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)


#根据产品编码查商品
def test_getSkuByProdCode7(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "第四条用例"  # allure报告中一级分类
    story = '根据产品编码查商品'  # allure报告中二级分类
    title = "全字段正常流_4"  # allure报告中用例名字
    uri = "/product/getSkuByProdCode"  # 接口地址
    headers = {"token": pub_data["token"]}  # 取token
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    params={'prodCode': '${productCode}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)

# 全量调整单个商品库存
def test_fullSku(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "第四条用例"  # allure报告中一级分类
    story = '全量调整单个商品库存'  # allure报告中二级分类
    title = "全字段正常流_4"  # allure报告中用例名字
    uri = "/product/fullSku"  # 接口地址
    headers = {"token": pub_data["token"]}  # 取token
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'qty': '100', 'skuCode': 'geli7160_白色_1匹'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)

#增量调整单个商品库存
def test_incrementSku(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "第四条用例"  # allure报告中一级分类
    story = '增量调整单个商品库存'  # allure报告中二级分类
    title = "全字段正常流_4"  # allure报告中用例名字
    uri = "/product/incrementSku"  # 接口地址
    headers = {"token": pub_data["token"]}  # 取token
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'qty': '150', 'skuCode': 'geli7160_白色_1匹'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)

#查询单个库存
def test_getSkuRepertory(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "第四条用例"  # allure报告中一级分类
    story = '查询单个库存'  # allure报告中二级分类
    title = "全字段正常流_4"  # allure报告中用例名字
    uri = "/product/getSkuRepertory"  # 接口地址
    headers = {"token": pub_data["token"]}  # 取token
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    params={'skuCode': 'geli7160_白色_1匹'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)

# #第四条结束**********************************************************************************************************************************************************************

# 增加产品
from tools.api import request_tool


def test_addProd9(pub_data):
    pub_data["productCode"] = "自动生成 字符串 4 数字 geli"
    method = "POST"  #请求方法，全部大写
    feature = "第五条用例"  # allure报告中一级分类
    story = '增加产品'  # allure报告中二级分类
    title = "全字段正常流_5"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    headers = {"token": pub_data["token"]} #取token
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "brand": "格力",
  "colors": [
    "白色",
    "黑色",
    "金色"
  ],
  "price": 3000,
  "productCode": "${productCode}",
  "productName": "格力君越",
  "sizes": [
    "1匹",
    "2匹",
    "3匹"
  ],
  "type": "家用电器"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)


#根据产品编码查商品
def test_getSkuByProdCode9(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "第五条用例"  # allure报告中一级分类
    story = '根据产品编码查商品'  # allure报告中二级分类
    title = "全字段正常流_5"  # allure报告中用例名字
    uri = "/product/getSkuByProdCode"  # 接口地址
    headers = {"token": pub_data["token"]}  # 取token
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    params={'prodCode': '${productCode}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)


#下载某产品的库存信息
def test_downProdRepertory(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "第五条用例"  # allure报告中一级分类
    story = '下载某产品的库存信息'  # allure报告中二级分类
    title = "全字段正常流_5"  # allure报告中用例名字
    uri = "/product/downProdRepertory"  # 接口地址
    headers = {"token": pub_data["token"]}  # 取token
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    params={'pridCode': 'geli7132'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)


