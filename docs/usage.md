# Faiss向量数据库使用指南





# 一、商品链接



[Faiss向量数据库](https://marketplace.huaweicloud.com/hidden/contents/c989ab37-9b79-40d6-9489-1de3ac8d8fe8#productid=OFFI1146359658505064448)

# 二、商品说明



Faiss 是由Facebook AI Reasearch团队开发的一个用于高效相似性搜索和密集向量聚类的库，能够快速处理大规模数据，并且支持在高维空间中进行向量相似性搜索。 本商品通过鲲鹏服务器+EulerOS2.0进行安装部署

# 三、商品购买



您可以在云商店搜索 **Faiss向量数据库**。

其中，地域、规格、推荐配置使用默认，购买方式根据您的需求选择按需/按月/按年，短期使用推荐按需，长期使用推荐按月/按年，确认配置后点击“立即购买”。

## 3.1 使用 RFS 模板直接部署



![img.png](images/img1.png) 
必填项填写后，点击 下一步
![img.png](images/img2.png)
![img.png](images/img3.png)
创建直接计划后，点击 确定
![img.png](images/img4.png)
![img.png](images/img5.png)
点击部署，执行计划
![img.png](images/img6.png)
如下图“Apply required resource success. ”即为资源创建完成
![img.png](images/img7.png)

# 3.2ECS 控制台配置



### 准备工作



在使用ECS控制台配置前，需要您提前配置好 **安全组规则**。

> **安全组规则的配置如下：**
>
> - 入方向规则放通 CloudShell 连接实例使用的端口 `22`，以便在控制台登录调试
> - 出方向规则一键放通

### 创建ECS



前提工作准备好后，选择 ECS 控制台配置跳转到[购买ECS](https://support.huaweicloud.com/qs-ecs/ecs_01_0103.html) 页面，ECS 资源的配置如下图所示：

选择CPU架构 
![img.png](images/img8.png)
选择服务器规格 ![img.png](images/img9.png)
选择镜像 ![img.png](images/img10.png)
其他参数根据实际请客进行填写，填写完成之后，点击立即购买即可 
![img.png](images/img11.png)

> **值得注意的是：**
>
> - VPC 您可以自行创建
> - 安全组选择 [**准备工作**](#准备工作) 中配置的安全组；
> - 弹性公网IP选择现在购买，推荐选择“按流量计费”，带宽大小可设置为5Mbit/s；
> - 高级配置需要在高级选项支持注入自定义数据，所以登录凭证不能选择“密码”，选择创建后设置；
> - 其余默认或按规则填写即可。

# 商品使用



## Faiss使用

运行
```
conda activate faiss 

cd /home/faiss/demos 

python demo.py
```

Faiss向量检索：加载SIFT数据集，训练索引、构建分片索引、并行搜索并合并结果，计算检索准确率。

![img.png](images/img_2.png)

### 参考文档



[Faiss官方文档](https://github.com/facebookresearch/faiss)

