# swagger-client
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CartsApi(swagger_client.ApiClient(configuration))
body = swagger_client.BatchChangeCartSelectedReq() # BatchChangeCartSelectedReq | 

try:
    # 批量设置购物车商品选中状态
    api_response = api_instance.batch_change_cart_selected(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->batch_change_cart_selected: %s\n" % e)

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CartsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ChangeCartSelectedReq() # ChangeCartSelectedReq | 
id = 'id_example' # str | 

try:
    # 设置购物车商品选中状态
    api_response = api_instance.change_cart_selected(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->change_cart_selected: %s\n" % e)

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CartsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateCartsReq() # CreateCartsReq | 

try:
    # 添加到商品购物车
    api_response = api_instance.create_carts(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->create_carts: %s\n" % e)

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CartsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # 获取购物车商品详情
    api_response = api_instance.get_cart(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->get_cart: %s\n" % e)

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CartsApi(swagger_client.ApiClient(configuration))
page = 789 # int |  当前页码
page_size = 15 # int |  展示数量 (optional) (default to 15)
orderby = 'cart_id' # str |  排序字段,默认 cart_id (optional) (default to cart_id)
sort = 'desc' # str |  排序方式(asc,desc), 默认 desc (optional) (default to desc)

try:
    # 购物车商品列表
    api_response = api_instance.list_carts(page, page_size=page_size, orderby=orderby, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->list_carts: %s\n" % e)

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CartsApi(swagger_client.ApiClient(configuration))
body = swagger_client.MergeCartsReq() # MergeCartsReq | 

try:
    # 合并本地购物车商品
    api_response = api_instance.merge_carts(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->merge_carts: %s\n" % e)

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CartsApi(swagger_client.ApiClient(configuration))
body = swagger_client.RemoveCartReq() # RemoveCartReq | 

try:
    # 删除购物车商品
    api_response = api_instance.remove_cart(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->remove_cart: %s\n" % e)

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CartsApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateCartReq() # UpdateCartReq | 
id = 'id_example' # str | 

try:
    # 修改购物车商品
    api_response = api_instance.update_cart(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->update_cart: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://127.0.0.1:9060/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CartsApi* | [**batch_change_cart_selected**](docs/CartsApi.md#batch_change_cart_selected) | **POST** /carts/selected | 批量设置购物车商品选中状态
*CartsApi* | [**change_cart_selected**](docs/CartsApi.md#change_cart_selected) | **POST** /cart/{id} | 设置购物车商品选中状态
*CartsApi* | [**create_carts**](docs/CartsApi.md#create_carts) | **POST** /carts | 添加到商品购物车
*CartsApi* | [**get_cart**](docs/CartsApi.md#get_cart) | **GET** /cart/{id} | 获取购物车商品详情
*CartsApi* | [**list_carts**](docs/CartsApi.md#list_carts) | **GET** /carts | 购物车商品列表
*CartsApi* | [**merge_carts**](docs/CartsApi.md#merge_carts) | **POST** /carts/merge | 合并本地购物车商品
*CartsApi* | [**remove_cart**](docs/CartsApi.md#remove_cart) | **POST** /carts/del | 删除购物车商品
*CartsApi* | [**update_cart**](docs/CartsApi.md#update_cart) | **PUT** /cart/{id} | 修改购物车商品
*CategoryApi* | [**categories**](docs/CategoryApi.md#categories) | **GET** /d/categories | 获取类别树形列表
*CategoryApi* | [**create_category**](docs/CategoryApi.md#create_category) | **POST** /d/categories | 创建类别
*CategoryApi* | [**get_category**](docs/CategoryApi.md#get_category) | **GET** /d/categories/{id} | 获取单个类别信息
*CategoryApi* | [**get_popular_categories**](docs/CategoryApi.md#get_popular_categories) | **GET** /d/categories/popular | 获取热门类别列表
*CategoryApi* | [**update_popular_categories**](docs/CategoryApi.md#update_popular_categories) | **PATCH** /d/categories/popular | 更新热门类别列表
*ProductApi* | [**brands**](docs/ProductApi.md#brands) | **GET** /d/brands | 获取品牌列表
*ProductApi* | [**create_brand**](docs/ProductApi.md#create_brand) | **POST** /d/brands | 创建品牌
*ProductApi* | [**get_brand**](docs/ProductApi.md#get_brand) | **GET** /d/brands/{id} | 获取单个品牌信息
*ProductApi* | [**get_brand_tree**](docs/ProductApi.md#get_brand_tree) | **GET** /d/tree-brands | 获取品牌列表树形结构
*ProductApi* | [**get_popular_brands**](docs/ProductApi.md#get_popular_brands) | **GET** /d/popular-brands | 获取热门品牌列表
*ProductApi* | [**get_product**](docs/ProductApi.md#get_product) | **GET** /d/products/{id} | 
*ProductApi* | [**update_brand_order**](docs/ProductApi.md#update_brand_order) | **PATCH** /d/popular-brands | 更新热门品牌列表
*SkuApi* | [**get_item_info**](docs/SkuApi.md#get_item_info) | **GET** /d/itemInfo/{id} | 获取商品详情
*SpuApi* | [**get_spu_items**](docs/SpuApi.md#get_spu_items) | **GET** /d/items | 获取商品列表
*UserApi* | [**add_address**](docs/UserApi.md#add_address) | **POST** /address | 添加地址
*UserApi* | [**address_detail**](docs/UserApi.md#address_detail) | **GET** /address/{id} | 根据id获取地址信息
*UserApi* | [**address_list**](docs/UserApi.md#address_list) | **GET** /address | 获取地址簿列表
*UserApi* | [**get_user_info**](docs/UserApi.md#get_user_info) | **GET** /user/info | 获取用户基本信息
*UserApi* | [**remove_address**](docs/UserApi.md#remove_address) | **DELETE** /address/{id} | 删除地址
*UserApi* | [**update_address**](docs/UserApi.md#update_address) | **PUT** /address/{id} | 编辑地址
*UserApi* | [**update_avatar**](docs/UserApi.md#update_avatar) | **PUT** /user/avatar | 更新用户头像地址

## Documentation For Models

 - [AddAddressReq](docs/AddAddressReq.md)
 - [AddAddressRsep](docs/AddAddressRsep.md)
 - [AddSpu](docs/AddSpu.md)
 - [AddWishListReq](docs/AddWishListReq.md)
 - [AddWishListResp](docs/AddWishListResp.md)
 - [AddressListItem](docs/AddressListItem.md)
 - [AddressListReq](docs/AddressListReq.md)
 - [AddressListResp](docs/AddressListResp.md)
 - [Attr](docs/Attr.md)
 - [BatchChangeCartSelectedReq](docs/BatchChangeCartSelectedReq.md)
 - [BatchChangeCartSelectedResp](docs/BatchChangeCartSelectedResp.md)
 - [Brand](docs/Brand.md)
 - [BrandOrder](docs/BrandOrder.md)
 - [Brands](docs/Brands.md)
 - [Cart](docs/Cart.md)
 - [CartInfo](docs/CartInfo.md)
 - [Categories](docs/Categories.md)
 - [Category](docs/Category.md)
 - [CategoryOrder](docs/CategoryOrder.md)
 - [ChangeCartSelectedReq](docs/ChangeCartSelectedReq.md)
 - [CreateBrand](docs/CreateBrand.md)
 - [CreateCartsReq](docs/CreateCartsReq.md)
 - [CreateCategory](docs/CreateCategory.md)
 - [DeleteAddressReq](docs/DeleteAddressReq.md)
 - [EmptyUser](docs/EmptyUser.md)
 - [GetAddressByIdReq](docs/GetAddressByIdReq.md)
 - [GetCartReq](docs/GetCartReq.md)
 - [GetUserReq](docs/GetUserReq.md)
 - [IdOrder](docs/IdOrder.md)
 - [ListCartsReq](docs/ListCartsReq.md)
 - [ListCartsResp](docs/ListCartsResp.md)
 - [MergeCartsReq](docs/MergeCartsReq.md)
 - [MergeCartsResp](docs/MergeCartsResp.md)
 - [OptionalSku](docs/OptionalSku.md)
 - [PopularBrand](docs/PopularBrand.md)
 - [PopularBrands](docs/PopularBrands.md)
 - [PopularCategories](docs/PopularCategories.md)
 - [PopularCategory](docs/PopularCategory.md)
 - [ProductReply](docs/ProductReply.md)
 - [ProductReq](docs/ProductReq.md)
 - [RemoveCartReq](docs/RemoveCartReq.md)
 - [RemoveCartResp](docs/RemoveCartResp.md)
 - [RemoveWishListReq](docs/RemoveWishListReq.md)
 - [RemoveWishListResp](docs/RemoveWishListResp.md)
 - [SkuInfoReq](docs/SkuInfoReq.md)
 - [SkuInfoRes](docs/SkuInfoRes.md)
 - [SpuItem](docs/SpuItem.md)
 - [SpuListReq](docs/SpuListReq.md)
 - [SpuListRes](docs/SpuListRes.md)
 - [UpdateAddressReq](docs/UpdateAddressReq.md)
 - [UpdateAvatarReq](docs/UpdateAvatarReq.md)
 - [UpdateCartReq](docs/UpdateCartReq.md)
 - [User](docs/User.md)
 - [WishListReq](docs/WishListReq.md)
 - [WishListResp](docs/WishListResp.md)
 - [WishListRespItem](docs/WishListRespItem.md)

## Documentation For Authorization


## apiKey

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author


